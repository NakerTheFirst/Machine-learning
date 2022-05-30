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
                        lst_[i][j] = 0
                        print("Changing to 0 complete")


if __name__ == '__main__':

    # noinspection PyPep8Naming
    class MetaMat:
        def __init__(self, list_):
            self.__List = list_
            self.__NMatrix = np.array(self.__List)
            self.__PFrame = pd.DataFrame(self.__List)

        # Swapping is zero-indexed
        def swapListRows(self, row1, row2):
            self.__List[row1], self.__List[row2] \
                = self.__List[row2], self.__List[row1]

        def swapMatrixColumns(self, col1, col2):
            tmp = np.copy(self.__NMatrix[:, col1])
            self.__NMatrix[:, col1] = self.__NMatrix[:, col2]
            self.__NMatrix[:, col2] = tmp

        def transposePSquare(self, df_, col1, row1, col2, row2):

            # Check if matrix is square
            if not abs(col1 - col2) == abs(row1 - row2):
                return "Indexes don't form a square matrix"

            # Check if matrix is 1x1 size
            if col1 == col2 and row1 == row2:
                return df_.iloc[row1:row1 + 1, row1:row1 + 1]

            # Row2 and col2 must be higher than row1 and col1
            if row1 > row2:
                row1, row2 = row2, row1

            if col1 > col2:
                col1, col2 = col2, col1

            # Slice submatrix and transpose
            sliced = df_.iloc[row1:row2+1, col1:col2+1]
            sliced = pd.DataFrame.transpose(sliced)

            transposed = sliced

            return transposed

        # Getters
        def get__List(self):
            return self.__List

        def get__PFrame(self):
            return self.__PFrame

        def get__NMatrix(self):
            return self.__NMatrix


    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    lst = setList(n, m)

    checkList(lst)

    t1 = MetaMat(lst)

    # transpose(col1, row1, col2, row2)
    # matrix = [[11, 22, 33, 44], [55, 66, 77, 88],
    #           [99, 111, 122, 133], [144, 155, 166, 177]]

    # df = pd.DataFrame(matrix)

    print("Before slicing:\n", t1.get__PFrame())

    print("After transposing:\n", t1.transposePSquare(t1.get__PFrame(), 0, 0, 2, 2))
