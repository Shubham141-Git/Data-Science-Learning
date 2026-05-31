from my_module import test
from my_module import calculator

print(__name__) # when we run this file, it will print __main__ because this file is being run as the main program. But when we import the test module, it will print test because the __name__ variable in the test module will be set to test when it is imported. So the output of this code will be: 
# my_module.test
# __main__

#__name__ is a special variable in Python it has its execution file name in it
# if __name__ is present in the same file u are executing from, then it will be set to  __main__ because it is the main program that is being run. 
# if __name__ is not present in the  current file u are exceting from, then it will be set to the name of the module that is being imported.


#But if __name__ is not present in the current file you are executing from, then it will be set to the name of the module that is being imported. So when we run this file, it will print __main__ because this file is being run as the main program. But when we import the test module, it will print test because the __name__ variable in the test module will be set to test when it is imported. So the output of this code will be: 


if __name__ == "__main__":
    cal = calculator.Calulcator()
    print(cal.add(2, 3))




'''   
__name__ is a special variable in Python that tells:

“How this file is being executed.”
SIMPLE RULE
Situation	__name__ Value
File is directly run	"__main__"
File is imported	module/file name
LET'S UNDERSTAND WITH REAL EXAMPLE
FILE 1 → test.py
print(__name__)
FILE 2 → main.py
from test import *

print(__name__)
CASE 1 → RUN test.py DIRECTLY

Suppose you run:

python test.py

Then inside test.py:

__name__ = "__main__"

Output:

__main__

Because THIS file is the main program being executed.

CASE 2 → RUN main.py

Now run:

python main.py
STEP-BY-STEP WHAT HAPPENS
Step 1

Python imports test.py

During import:

__name__ = "test"

because now it is NOT main file.

It is just a module.

So:

print(__name__)

inside test.py

prints:

test
Step 2

Now main.py executes:

print(__name__)

For main.py:

__name__ = "__main__"

because THIS is the file being run.

So output:

__main__
FINAL OUTPUT WHEN RUNNING main.py
test
__main__
VERY IMPORTANT IDEA

Each file has its OWN __name__.

WHY IS THIS USEFUL?

Used to prevent some code from running during import.

MOST IMPORTANT USE
if __name__ == "__main__":
EXAMPLE
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))
WHEN RUN DIRECTLY
python test.py

Output:

5

because:

__name__ == "__main__"

is TRUE.

WHEN IMPORTED
import test

Now:

__name__ = "test"

Condition becomes FALSE.

So:

print(add(2,3))

will NOT run.

WHY DO WE USE THIS?

Suppose your file contains:

functions
classes
testing code

You want testing code to run ONLY when file is directly executed.

NOT during import.

REAL LIFE ANALOGY

Think:

__main__

means:

👉 “I am the boss file currently running.”

And:

test

means:

👉 “I was imported by another file.”

SIMPLE MEMORY TRICK
Direct Run
python file.py

↓

__name__ = "__main__"
Import
import file

↓

__name__ = "file"

'''