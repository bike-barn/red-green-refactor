# Red, Green, Refactor

A very simple calculator designed to teach software testing.

## What does Red Green Refactor mean?

**NOTE:** If you want to just dive into code skip to the 
[Quick Start](#quickstart) section. If you want to know why we're doing this
read on. **Don't be afraid to skim and come back.** There's going to be a lot
of information in this workshop.

Red Green Refactor is a concept derived from the Test Driven Development crowd.
The basic idea is that you write a simple test first. You make sure it fails
(just in case you've made a test that will always pass and thus be a false
positive). This is the Red step.

Then you make the test pass (Green Step).

Finally you clean up your code. Potentially you make style changes, rename
variables to make sense, pull things out into functions. The important part is
that the tests don't change and that they all pass by the end of the refactor.

These tests tend to be simple. So simple they can seem really dumb sometimes.
Normally these tests basically boil down to hard coded input, hard coded
expected output, and running a function to make sure it's output matches the
expected output.

The goal of this simplicity is to be fairly confident that
your tests themselves don't have bugs. The more complex your test the less
confidence you can have in them.

The majority of the reference implementaiton is inspired by [Ruslan Spivak]'s
_[Let's Build a Simple Interpreter]_ project.

## Quickstart

### Indentation Style
This repository only uses 4 spaces. Tabs are not included and shouldn't be
used.

### Prerequisites
This tutorial assumes you have the following:
- A UNIX-like operating system (e.g. `Linux`, `OS X`, `FreeBSD`, etc.)
- The [Git] version control system.
- Python 3.4 or greater.
- [`virtualenv`][virtualenv] and [`virtualenvwrapper`][virtualenvwrapper].

### Cloning This Repository
Pick a directory you want to work out of and run
```bash
git clone https://github.com/bike-barn/red-green-refactor.git
```

### Installation
1. Enter the project directory
```bash
cd red-green-refactor
```

2. Make a [virtualenv] using
   ```bash
   mkvirtualenv --python $(which python3) red-green-refactor
   ```
   **NOTE**: If you get an error like
   ```bash
   bash: mkvirtualenv: command not found
   ```
   you may need to make sure [virtualenvwrapper] is installed correctly.

3. Ensure you're using the correct [virtualenv].
   ```bash
   workon red-green-refactor
   ```
   If you are using the correct [virtualenv] your prompt should be modified to
   look something like this
   ```bash
   (red-green-refactor) username@hostname:~/Projects/red-green-refactor $
   ```
   Alternatively, if your prompt doesn't change you can determine whether you're
   in a virtualenv by running
   ```bash
   which python
   ```
   You should see something like
   ```bash
   /home/user/.virtualenvs/red-green-refactor/bin/python
   ```

4. Install the development requirements using `pip`.
   ```bash
   pip install -e .'[develop]'
   ```
   **NOTE**: This must be done from within the project directory.

At this point you should be ready to go! Read on! :grin:

## Terms

### **Hint**
These are suggestions from the authors on directions you should think about
or documentation you should look up. Generally speaking these are meant to be
aids for when you're stuck on a problem.

If we've left a hint it's probably because a student has struggled at this
point previously.

**NOTE:** Hints will always come with an assignment that they're supposed to be
paired with. An example of this would be:

```
Hint Assignment Two:
```

### **Saved by The Test**
Certain sections of this tutorial have been labelled as
```
Saved by The Test
```
These denote places in the code where the presence of tests saved the authors
from undue headache. They have been preserved as a reminder that _everyone_
makes mistakes and that tests are here to help. :wink:

### **Rabbit Hole**
Certain sections of this tutorial have been labelled as
```
Rabbit Hole
```
These denote places in the code where the authors tried to anticipate questions
or concerns that folks who are new to Python might have, but that may not get
covered in detail. Hopefully these comments will elucidate some of the more
confusing parts in this tutorial. If not, feel free to ask questions! :smile:

### **Command To Run All Tests**

**NOTE**: If you run all of the unit tests without implementing any features
you _will_ be assaulted with **angry** test failures.

```bash
pytest tests/*
```

#### Example Unit Test Output

```bash
$ pytest tests/*
====================== test session starts ===========================
platform darwin -- Python 3.5.0, pytest-2.9.2, py-1.4.31, pluggy-0.3.1
rootdir: /Users/alexlord/git/personal/red-green-refactor-rawrgulmuffins, inifile:
plugins: cov-2.4.0
collected 36 items


tests/assignment_four/test_arithmetic.py ................
tests/assignment_one/test_token.py ...
tests/assignment_three/test_consume_whitespace.py .....
tests/assignment_three/test_tokenize_integers.py ...
tests/assignment_two/test_calc.py .........


====================== 36 passed in 0.11 seconds ======================
```

### Coverage.py

There is a python project called `coverage`. It's main job is to tell you what
lines are covered by unit tests and which ones are not. When you ran `pip
install -e .'[develop]'` you installed `pytest-cov` which is a pytest plugin that adds
code coverage to `pytest`. This is one of the nice things about `pytest` that
we like.

### Tests With Code Coverage

```bash
pytest --cov=calc/ --cov-report term-missing tests/*
```

#### Example Output With Coverage

```bash
$ py.test --cov=calc/ --cov-report term-missing tests/*
====================== test session starts ============================
platform darwin -- Python 3.5.0, pytest-2.9.2, py-1.4.31, pluggy-0.3.1
rootdir: /Users/alexlord/git/personal/red-green-refactor-rawrgulmuffins, inifile:
plugins: cov-2.4.0
collected 36 items


tests/assignment_four/test_arithmetic.py ................
tests/assignment_one/test_token.py ...
tests/assignment_three/test_consume_whitespace.py .....
tests/assignment_three/test_tokenize_integers.py ...
tests/assignment_two/test_calc.py .........


---------- coverage: platform darwin, python 3.5.0-final-0 -----------
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
calc/__init__.py       6      0   100%
calc/__main__.py      18     18     0%   1-43
calc/calc.py          92      0   100%
calc/token.py          8      0   100%
------------------------------------------------
TOTAL                124     18    85%




====================== 36 passed in 0.12 seconds ======================
```

## Notes:
- This code has was written and tested against Python 3.4 and 3.5.

[Ruslan Spivak]: https://ruslanspivak.com/
[Let's Build a Simple Interpreter]: https://ruslanspivak.com/lsbasi-part1/
[Git]: https://git-scm.com/
[virtualenv]: https://virtualenv.pypa.io/en/stable/
[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/en/latest/
