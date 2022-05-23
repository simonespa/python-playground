# Python Playground

Playground repository for Python and its ecosystem.

I wrote the code within the "bbc_training" folder during the "Introduction to Python" BBC Academy course run by [Reindert-Jan Ekker](https://codesensei.nl). The course material was provided by the instructor.

The code in the "exercises" folder are coding puzzles for general practice to keep myself current with Python programming and general algorithm resolution and data structure.
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

If you want to switch projects or otherwise leave your virtual environment

```
deactivate
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

## Requirements file

```
pip freeze > requirements.txt
```

## Useful commands

```
pip list
```

```
pip show requests
```
