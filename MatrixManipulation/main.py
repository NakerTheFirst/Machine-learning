import numpy as np
import pandas as pd


def main():
    pass


# noinspection PyPep8Naming
def setList():

    lst_ = []
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    # Take user input for 2D matrix
    for rows in range(0, n):
        tmplst = []
        for cols in range(0, m):
            value = float(input(f"Value of element {rows}x{cols}: "))
            tmplst.append(value)
        lst_.append(tmplst)

    return lst_


if __name__ == '__main__':

    # noinspection PyPep8Naming
    class MetaMat:
        def __init__(self, list_):
            self.list_ = list_
            self.__List = self.list_
            self.__PFrame = pd.DataFrame(list_)
            self.__NMatrix = np.array(list_)

        def get__List(self, __List):
            return self.__List

        def get__PFrame(self, __PFrame):
            return self.__PFrame

        def get__NMatrix(self, __NMatrix):
            return self.__NMatrix

    fruits = [["Apple", "Banana", "Cherry"],
              ["Kiwi", "Orange", "Tomato"],
              ["Berry", "Mango", "Cranberry"]]

    lst = setList()

    t1 = MetaMat(lst)

    print(t1.get__List(lst), end=" \n")
    print(t1.get__PFrame(lst), end=" \n")
    print(t1.get__NMatrix(lst), end=" \n")

