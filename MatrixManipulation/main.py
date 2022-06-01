import numpy as np
import pandas as pd
import time


def main():
    return 0


# noinspection PyPep8Naming
def setList(n_, m_):

    lst_ = []

    # Take user input for 2D matrix
    for rows in range(0, n_):
        tmplst = []
        for cols in range(0, m_):
            if rows == 0 and cols == 0:
                print("\n")
            value = input(f"Value of element {rows}x{cols}: ")
            tmplst.append(value)
        lst_.append(tmplst)

    return lst_


# noinspection PyPep8Naming
def checkList(lst_):

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
                        lst_[i][j] = repl
                        print(f"Replacing complete")
                    case 2:
                        lst_[i][j] = '0'
                        print("Changing to 0 complete")


if __name__ == '__main__':

    # noinspection PyPep8Naming
    class MetaMat:
        def __init__(self, list_):
            self.__List = list_
            self.__NMatrix = np.array(self.__List)
            self.__PFrame = pd.DataFrame(self.__List)
            self.markAction = 0

        # Swapping is zero-indexed
        def swapListRows(self, row1, row2):
            self.__List[row1], self.__List[row2] \
                = self.__List[row2], self.__List[row1]
            self.markAction = 1
            self.update()

        def swapMatrixColumns(self, col1, col2):
            tmp = np.copy(self.__NMatrix[:, col1])
            self.__NMatrix[:, col1] = self.__NMatrix[:, col2]
            self.__NMatrix[:, col2] = tmp
            self.markAction = 2
            self.update()

        def transposePSquare(self, key1, index1, key2, index2):

            df_ = self.get__PFrame()

            # Check if matrix is square
            if not abs(key1 - key2) == abs(index1 - index2):
                return "Indexes don't form a square matrix"

            # Check if matrix is 1x1 size
            if key1 == key2 and index1 == index2:
                return df_.iloc[index1:index1 + 1, index1:index1 + 1]

            # index2 and key2 must be greater than index1 and key1
            if index1 > index2:
                index1, index2 = index2, index1

            if key1 > key2:
                key1, key2 = key2, key1

            # Slice submatrix and transpose
            sliced = df_.iloc[index1:index2+1, key1:key2+1]
            self.__PFrame = pd.DataFrame.transpose(sliced)

            self.markAction = 3
            self.update()

        def update(self):

            match self.markAction:

                case 0:
                    print("Nothing to update")

                case 1:
                    self.__NMatrix = np.array(self.__List)
                    self.__PFrame = pd.DataFrame(self.__List)

                case 2:
                    NMatrixList = self.__NMatrix.tolist()
                    self.__List = NMatrixList
                    self.__PFrame = pd.DataFrame(self.__NMatrix)

                case 3:
                    PFrameList = self.__PFrame.values.tolist()
                    self.__List = PFrameList
                    self.__NMatrix = np.array(self.__PFrame)

            self.markAction = 0

        # Getters
        def get__List(self):
            return self.__List

        def get__PFrame(self):
            return self.__PFrame

        def get__NMatrix(self):
            return self.__NMatrix

    # User manual
    print("\nWelcome! \nThe program provides basic matrix manipulation functionalities in Python.\n")
    print("Please specify a matrix\n")
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    lst = setList(n, m)

    checkList(lst)
    t1 = MetaMat(lst)
    close = False

    while not close:

        print("\nWhat action do you want to take?")
        print("1. Print the matrix")
        print("2. Reenter the matrix")
        print("3. Swap rows in 2D Python list")
        print("4. Swap columns")
        print("5. Transpose the matrix")
        print("6. Update all the matrix representations")
        print("7. Quit")

        action = int(input())

        match action:
            case 1:
                print("\nWhich matrix representation do you wish to see?")
                print("1. 2D Python list\n"
                      "2. Numpy 2D array\n"
                      "3. Pandas dataframe\n"
                      "4. All of the mentioned\n")
                subaction = int(input("Enter a number: "))

                print("\n")

                match subaction:
                    case 1:
                        print("Python list:\n", t1.get__List())
                    case 2:
                        print("Numpy 2D array:\n", t1.get__NMatrix())
                    case 3:
                        print("Pandas dataframe:\n", t1.get__PFrame())
                    case 4:
                        print("Python list:\n", t1.get__List())
                        print("\n")
                        print("Numpy 2D array:\n", t1.get__NMatrix())
                        print("\n")
                        print("Pandas dataframe:\n", t1.get__PFrame())
                        print("\n")

                time.sleep(2.5)

            case 2:
                n = int(input("Enter the number of rows: "))
                m = int(input("Enter the number of columns: "))

                lst = setList(n, m)
                checkList(lst)
                t1 = MetaMat(lst)

            case 3:
                a = int(input("Define the first row to swap: "))
                b = int(input("Define the second row to swap: "))
                t1.swapListRows(a, b)

            case 4:
                a = int(input("Define the first column to swap: "))
                b = int(input("Define the second column to swap: "))
                t1.swapMatrixColumns(a, b)
            case 5:
                a = int(input("Define row of the first submatrix element to transpose: "))
                b = int(input("Define column of the first submatrix element to transpose: "))
                c = int(input("Define row of the second submatrix element to transpose: "))
                d = int(input("Define column of the second submatrix element to transpose: "))
                t1.transposePSquare(a, b, c, d)
            case 6:
                t1.update()
            case 7:
                print("Quitting...")
                close = True
