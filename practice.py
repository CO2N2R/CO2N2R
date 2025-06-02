# import dependencies 
import numpy, pandas, random, argparse    
# pip install _

Date: str = "2025 Jan 29"
number: float = 3.141592
integer: int = 10

def generator(num: int):
    for _ in range(3):
        yield random.randint(num: int, integer: int)

#def user_input():
 #   user_input = input("Please enter integer:")

def sets():
    set_of_fruits ={"apple", "banana", "orange"}
    assert isinstance(set_of_fruits, tuple)

def tuples():
    tuple_of_veggies = ("carrot","cauliflower","lettuce")
    
    print(tuple_of_veggies.count)

function()
# user_input()
print(generator(input))


class ComplexNumberWithConstructor:
        """Example of the class with constructor"""
        def __init__(self, real_part: float, imaginary_part: float):
            self.real = real_part
            self.imaginary = imaginary_part

        def get_real(self):
            """Return real part of complex number."""
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            return self.imaginary

complex_number = ComplexNumberWithConstructor(3.0, -4.5)
assert complex_number.real, complex_number.imaginary == (3.0, -4.5)