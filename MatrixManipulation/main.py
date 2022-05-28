import numpy as np
import pandas as pd

# Main, setList, checkList

def main():
    return 0


# noinspection PyPep8Naming
def setList(n_, m_):

    lst_ = []

    # Take user input for 2D matrix
    for rows in range(0, n_):
        tmplst = []
        for cols in range(0, m_):
            value = input(f"Value of element {rows}x{cols}: ")
            tmplst.append(value)
        lst_.append(tmplst)

    return lst_


# noinspection PyPep8Naming
def checkList(lst_):

    isNum = []
    for i in range(len(lst_)):
        for j in range(len(lst_[i])):
            if not lst_[i][j].isnumeric():
                print(f"\nValue of lst_[{i}][{j}] is not numeric."
                      f"\nWhat do you want to do with it?\n")
                print("1. Replace \n2. Change to 0\n")
                choice = int(input("Enter corresponding number: "))
                match choice:
                    case 1:
                        repl = input("Input replacing number: ")
                        while not repl.isnumeric():
                            repl = input("Value is not numeric. "
                                         "Reenter the value: ")
                            lst_[i][j] = repl
                        print(f"Replacing complete")
                    case 2:
                        lst_[i][j] = 0
                        print("Changing to 0 complete")


if __name__ == '__main__':

    # noinspection PyPep8Naming
    class MetaMat:
        def __init__(self, list_):
            self.list_ = list_
            self.__List = self.list_
            self.__PFrame = pd.DataFrame(list_)
            self.__NMatrix = np.array(list_)

        # Swapping is zero-indexed
        def swapListRows(self, row1, row2):
            self.__List[row1], self.__List[row2] \
                = self.__List[row2], self.__List[row1]

        def swapMatrixColumns(self):
            pass

        def transposePSquare(self):
            pass

        # Getters
        def get__List(self, __List):
            return self.__List

        def get__PFrame(self, __PFrame):
            return self.__PFrame

        def get__NMatrix(self, __NMatrix):
            return self.__NMatrix


    # Main:
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    lst = setList(n, m)

    checkList(lst)

    print(lst)

    t1 = MetaMat(lst)

    # Swapping is zero-indexed
    t1.swapListRows(0, 1)

    print(lst)

    # print(t1.get__List(lst), end=" \n")
    # print(t1.get__PFrame(lst), end=" \n")
    # print(t1.get__NMatrix(lst), end=" \n")
