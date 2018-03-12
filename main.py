import numpy
import function
def main():
    data=numpy.arange(27).reshape(3,3,3)
    print(function.f1(data))
    print(function.f2(data))