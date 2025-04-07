from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import DensePassageRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline

# Step 1: Load the Harry Potter text from a local file
with open("harrypotter.txt", "r", encoding="utf-8") as file:
    harry_potter_text = file.readlines()

# Step 2: Preprocess the text
def preprocess_function(texts):
    return [{"text": text.strip()} for text in texts if text.strip()]

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large")
tokenized_dataset = preprocess_function(harry_potter_text)

# Step 3: Fine-tune the model
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large")

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
)

trainer.train()

# Step 4: Set up a RAG system
# Initialize FAISS document store
document_store = FAISSDocumentStore(faiss_index_factory_str="Flat")

# Write Harry Potter text into the document store
docs = [{"content": text} for text in harry_potter_text]
document_store.write_documents(docs)

# Initialize Dense Passage Retriever
retriever = DensePassageRetriever(
    document_store=document_store,
    query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
    passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base",
    use_gpu=True,
)

document_store.update_embeddings(retriever)

# Initialize FARMReader
reader = FARMReader(model_name_or_path="./results", use_gpu=True)

# Create a QA pipeline
pipeline = ExtractiveQAPipeline(reader, retriever)

# Step 5: Ask questions
def ask_question(question):
    prediction = pipeline.run(query=question, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}})
    return prediction

# Example usage
if __name__ == "__main__":
    question = "What is the name of Harry Potter's owl?"
    answer = ask_question(question)
    print(answer)
