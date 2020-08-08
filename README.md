# The Easiest Complex Calculator!

This repository contains the easiest complex calculator, it make everything, obviously you can do basic operations but also the calculator includes a coordinates converter all was developed on python and works with easy and intuitive commands.

Here are exactly the things that you can do:
1. Addition
2. Multiplication
3. Subtraction
4. Division
5. Modulus
6. Conjugate
7. Converter:
	- Polar to Cartesian
	- Cartesian to Polar
8. Phase

## What do you need to get a copy?
### Prerequisite
- Python (PyCharm or IDLE)
- Git
### Installing

In case you know how to use Git just clone the project and omit the following steps. 

First open or create a folder where you want to clone the project, then with right-click select "Git Bash Here" once the console is open write "git clone" and paste the repository link, to copy just go upper and select "code" and click on the copy icon as the following image:

![Steps](https://media.discordapp.net/attachments/584593411567517710/741729755992293406/unknown.png)

Now the repository is copied and you are ready to open the project "ComplexCalculator.py". 
Last i will show you how to run a run a function but is the same method for everyone:
~~~
def add(c1, c2):
    re = c1[0] + c2[0]
    im = c1[1] + c2[1]
    resp = re, im
    # return resp  
	print(resp)

add((1, 2), (3, 4))
~~~
*Remember that we use **print** for this but when we gonna test have to use **return** and that for the input we use tuple's*

## Testing
Testing is really simple only have to change few things and run the code!.

For the test open the project "CalculatorTest.py" and follow the next steps:

~~~
import unittest
import ComplexCalculator

class TestComplexCalculator(unittest.TestCase):  "This is the way to start the testing"

    # ADD TEST

    def test_add(self):
        a = (-2, -1)     "Here we declare de value of the tuple"
        b = (0, 3)	     "If you want change it!"
        c = (1, 4)	     "Try to do different combinations between negatives, postives and zero"
        d = (2, 5)

        self.assertEqual(ComplexCalculator.add(a, b), (-2, 2))  "I like to make four test's but if you want do some more"
        self.assertEqual(ComplexCalculator.add(a, c), (-1, 3))  "For other test: "
        self.assertEqual(ComplexCalculator.add(b, d), (2, 8))	"ComplexCalculator.function_you_want_to_try"
        self.assertEqual(ComplexCalculator.add(d, c), (3, 9))
~~~
*Remember, all test's are equal in structure but change **values** and **function***

## Built With
- [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - Integrated Development Environment
## Authors
- **Juan Camilo Rojas** - *Project creator*
## License
This project was developed under **Python Community Version** - [Terms of Use](https://www.jetbrains.com/company/useterms.html?fromFooter)