# Python Playground

Playground repository for Python and its ecosystem.

The code in `bbc_training` folder is from the "Introduction to Python" BBC Academy course I attended, run by [Reindert-Jan Ekker](https://codesensei.nl). There are lab exercises about Python fundamentals, packaging, testing, file and error handling, plus some intro exercises to Pandas and Jupiter notebooks.

The `exercises` folder contains coding puzzles for general practice to keep myself current with Python programming and general algorithm resolution and data structure.
## Getting Started

Create a virtual environment with `virtualenv`

```
virtualenv .env
```

Activate the virtual environment

```
source .env/bin/activate
```
or

```
. env/bin/activate
```

You can confirm you’re in the virtual environment by checking the location of your Python interpreter

```
which python
```

Install the required dependencies

```
pip install -r requirements.txt
```

## Run the code

Let's say there is an `example.py` module within the `exercises` folder that defines a `hello` function.

Open the Python interpreter

```
python
```

import the function you want to run from its module

```py
from exercises.example import hello
```

execute the function

```py
hello()
```

Modules don't have any "main" execution. If you were to run a file directly, you would need to add the following to it

```py
if __name__ == '__main__':
  hello()
```

and then run

```
python exercises/example.py
```

## Requirements file

If you want to generate a new "requirements" file or add/remove dependencies and update the existing one

```
pip freeze > requirements.txt
```

## PIP useful commands

To list all the installed libraries in `site-packages`

```
pip list
```

To "show" the details of a specific library

```
pip show requests
```

## Deactivate the current virtual environment

If you want to switch to another project or generally speaing leave your current virtual environment

```
deactivate
```
