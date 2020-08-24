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

### New Update!!
The calculator recently have a update that add new awesome functions, all related with Complex Vector Spaces, maybe its a hard concept to understand but am sure that this calculator can help you and make it easy.

The new functions:
- Vector Addition
- Vector Inverse Addition
- Vector Scalar Multiplication
- Matrix Addition
- Matrix Inverse Addition
- Matrix Scalar Multiplication
- Matrix/Vector Transpose
- Matrix/Vector Conjugate
- Matrix/Vector Adjoint
- Matrix Multiplication
- Matrix Action Over a Vector
- Inner Point
- Vector Norm
- Distance Between Vectors
- Unitary Matrix Verification
- Hermitian Matrix Verification
- Matrix Tensor Product

There is a lot of new functions, am sure that will be very useful,


***Important!!:** Every time i update the project the newest this will be ahead and the others will be registered below*

## What do you need to get a copy?
### Prerequisite
- Python (PyCharm or IDLE)
- Git
### Installing
Don't mind about the updates, the installation process is the same. 

In case you know how to use Git just clone the project and omit the following steps. 

First open or create a folder where you want to clone the project, then with right-click select "Git Bash Here" once the console is open write "git clone" and paste the repository link, as the following images:

***1. New Folder:***

![Step1](https://cdn.discordapp.com/attachments/584593411567517710/747548747763941496/unknown.png)

***2. (Git Bash):***

![Step2](https://cdn.discordapp.com/attachments/584593411567517710/747549065453109268/unknown.png)

***3(Console Command):***

![Step3](https://cdn.discordapp.com/attachments/584593411567517710/747549595386642492/unknown.png)

To copy just go upper and select "code" and click on the copy icon as the following image:

![Step4](https://media.discordapp.net/attachments/584593411567517710/741729755992293406/unknown.png)

Now the repository is copied and you are ready to open the project "ComplexCalculator.py" if you want to operate complex numbers or onpen. 
Last i will show you how to run a run a function but is the same method for everyone:
~~~
def add(c1, c2):
    re = c1[0] + c2[0]
    im = c1[1] + c2[1]
    resp = re, im
    return resp  
	
print(add((1, 2), (3, 4)))

~~~
*Remember that we use **tuple's** for the input in all functions*

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
        
     # MATRIX ADD TEST
     
     def test_m_add(self):
        a = [[(6, 5), (2, 1), (4, 3)], [(4, 4), (4, 4), (4, 4)]]
        b = [[(10, 1), (2, 3), (6, 7)], [(3, 2), (8, 2), (7, 5)]]  # Be carefull writing 
        c = [[(-1, 6), (8, -9), (0, 3)], [(0, 0), (8, 5), (-1, -5)]]

        self.assertEqual(ComplexVectorSapces.m_add(a, b), [[(16, 6), (4, 4), (10, 10)], [(7, 6), (12, 6), (11, 9)]])
        self.assertEqual(ComplexVectorSapces.m_add(a, c), [[(5, 11), (10, -8), (4, 6)], [(4, 4), (12, 9), (3, -1)]])
        self.assertEqual(ComplexVectorSapces.m_add(b, c), [[(9, 7), (10, -6), (6, 10)], [(3, 2), (16, 7), (6, 0)]])
        
        #The test for matrix or vectors are the same, just remember to write the complex numbers as tuple's and the reals 
        #as tuple's with the second digit being a 0
     
~~~
*Remember, all test's are equal in structure but change **values** and **function***

## Built With
- [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - Integrated Development Environment
## Authors
- **Juan Camilo Rojas** - *Project creator*
## License
This project was developed under **Python Community Version** - [Terms of Use](https://www.jetbrains.com/company/useterms.html?fromFooter)