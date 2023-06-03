# Python Playground

Playground repository for Python exercises.

## Getting Started

### Create a virtual environment

Create a virtual environment with `virtualenv`

```
virtualenv .python
```

### Activate the virtual environment

```
source .python/bin/activate
```
or

```
. python/bin/activate
```

### Verify the virtual environment

You can confirm you’re in the virtual environment by checking the location of your Python interpreter

```
which python
```

### Dependencies

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

## Test and code formatting

To test every `*_test.py` module

```
pytest
```

To format every file in the `exercises` folder

```
black src
```

## Requirements file

If you want to generate a new "requirements" file or add/remove dependencies and update the existing one

```
pip freeze > requirements.txt
```

## How to upgrade the dependencies

Replace all `==` symbols in the `requirements.txt` file with `>=`, then run

```
pip install -r requirements.txt --upgrade
```

then run

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
