import random


rows=50
columns=2400


class Board:
    def __init__(self):
        self.matrix = [['\033[33;46m'+' '+'\033[0m'] * columns for i in range(rows)]
        for i in range(columns):
            self.matrix[0][i] = '\033[33;43m'+'_'+'\033[0m'
            self.matrix[rows-2][i] = '\033[91;42m'+'L'+'\033[0m'
            self.matrix[rows-1][i] = '\033[91;42m'+'L'+'\033[0m'
        for i in range(rows):
            self.matrix[i][0] = '\033[33m'+'|'+'\033[0m'
            self.matrix[i][columns-1] = '\033[33m'+'|'+'\033[0m'
        self.matrix[0][0] = '\033[33m'+' '+'\033[0m'
        self.matrix[0][columns-1] = '\033[33m'+' '+'\033[0m'
        self.__r=rows
        self.__c=columns

    def Display(self,start=0,stop=200):
        # print('\033[0;0h]')
    	for i in range(rows):
    		for j in range(start,stop):
    			print(self.matrix[i][j],end='')
    		print()
    	print()

board = Board()


# def generateLasers:
