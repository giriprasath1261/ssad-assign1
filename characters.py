import random
import os
from board import *
from globalvar import *

class Object:
	hegiht=1
	width=1
	grid=[]

class Charecter:
	position=1
	grid=[]

class Hero(Charecter):
	def __init__(self):
		self.__x = 8
		self.__y = 9
		self._grid=[
		"    _    ",
		"   (|)   ",
		"  /|||\  ",
		"_/ ||| \_",
		"   |||   ",
		"  /   \  ",
		" |     | ",
		"==     =="
		]
		self._shootgrid=[
		" _       ",
		"(|)      ",
		"|||\__====",
		"|||___||`",
		"|||      ",
		"|  \     ",
		"|   \    ",
		"==   ==  "
		]
		self._supersaiyangrid=[
		"_  |||  _",
		" \ (|) / ",
		"  \|||/  ",
		"   |||   ",
		"   |||   ",
		"  /   \  ",
		" |     | ",
		"==     =="
		]
		self.__yesgrid=["yes"]
		# self.shape='A'
		self.__position=1
		self.__height=0

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

	def Print(self,ccol = 1,crow = 40,shield=False):
		column = ccol
		row = crow
		temp = column

		for r in range(8):
			column = temp
			for block in range(len(player._grid[r])):
				if(shield==False):
					if(r==0 or r==1):
						board.matrix[row][column+block] = '\033[37;46m'+ player._grid[r][block] +'\033[0m'
					if(r==2 or r==3):
						board.matrix[row][column+block] = '\033[31;46m'+ player._grid[r][block] +'\033[0m'
					if(r==4 or r==5 or r==6):
						board.matrix[row][column+block] = '\033[35;46m'+ player._grid[r][block] +'\033[0m'
					if(r==7):
						board.matrix[row][column+block] = '\033[30;46m'+ player._grid[r][block] +'\033[0m'
				else:
					if(r==0):
						board.matrix[row][column+block] = '\033[33;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
					if(r==1):
						board.matrix[row][column+block] = '\033[37;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
					if(r==2 or r==3):
						board.matrix[row][column+block] = '\033[31;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
					if(r==4):
						board.matrix[row][column+block] = '\033[35;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
					if(r==5 or r==6):
						board.matrix[row][column+block] = '\033[31;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
					if(r==7):
						board.matrix[row][column+block] = '\033[35;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
				# board.matrix[row-1][column+block]=" "
			row = row +1


	def Delete(self,ccol = 1,crow = 40):
		column = ccol
		row = crow
		temp = column

		for r in range(8):
			column = temp
			for block in range(len(player._grid[r])):
				board.matrix[row][column+block] = '\033[30;46m'+' '+'\033[0m'
				# board.matrix[row-1][column+block]=" "
			row = row +1

	def Gravity(self,ccol = 1,crow = 40,step = 1,shield=False):
		column = ccol
		row = crow
		temp = column

		self.Delete(column,row)
		self.Print(column,row+step,shield)

	def yes(self,ccol,crow):
		column = ccol
		row = crow
		temp = column
		for block in range(len(player.__yesgrid)):
			board.matrix[row][column+block] = '\033[37;46m'+ player.__yesgrid[block] +'\033[0m'




class Shooter(Hero):
	def __init__(self):
		self.__x = 8
		self.__y = 9

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

	def Print(self,ccol = 1,crow = 40):
		column = ccol
		row = crow
		temp = column

		for r in range(8):
			column = temp
			for block in range(len(player._grid[r])):
				if(r==0 or r==1):
					board.matrix[row][column+block] = '\033[37;46m'+ player._shootgrid[r][block] +'\033[0m'
				if(r==2 or r==3):
					board.matrix[row][column+block] = '\033[31;46m'+ player._shootgrid[r][block] +'\033[0m'
				if(r==4 or r==5 or r==6):
					board.matrix[row][column+block] = '\033[35;46m'+ player._shootgrid[r][block] +'\033[0m'
				if(r==7):
					board.matrix[row][column+block] = '\033[30;46m'+ player._shootgrid[r][block] +'\033[0m'
				# board.matrix[row][column+block] = '\033[37;46m'+player._shootgrid[r][block] +'\033[0m'
				# board.matrix[row-1][column+block]=" "
			row = row +1

	def Delete(self,ccol = 1,crow = 40):
		column = ccol
		row = crow
		temp = column

		for r in range(8):
			column = temp
			for block in range(len(player._grid[r])):
				board.matrix[row][column+block] = '\033[37;46m'+' '+'\033[0m'
				# board.matrix[row-1][column+block]=" "
			row = row +1



class SuperSaiyan(Hero):
	def __init__(self):
		self.__x = 11
		self.__y = 13

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

	def Print(self,ccol = 1,crow = 40):
		column = ccol
		row = crow
		temp = column

		for r in range(8):
			column = temp
			for block in range(len(player._supersaiyangrid[r])):
				if(r==0):
					board.matrix[row][column+block] = '\033[33;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
				if(r==1):
					board.matrix[row][column+block] = '\033[30;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
				if(r==2 or r==3):
					board.matrix[row][column+block] = '\033[30;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
				if(r==4):
					board.matrix[row][column+block] = '\033[30;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
				if(r==5 or r==6):
					board.matrix[row][column+block] = '\033[30;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
				if(r==7):
					board.matrix[row][column+block] = '\033[30;46m'+ player._supersaiyangrid[r][block] +'\033[0m'
				# board.matrix[row][column+block] = '\033[37;46m'+player._supersaiyangrid[r][block] +'\033[0m'
				# board.matrix[row-1][column+block]=" "
			row = row +1

	def Delete(self,ccol = 1,crow = 40):
		column = ccol
		row = crow
		temp = column

		for r in range(8):
			column = temp
			for block in range(len(player._grid[r])):
				board.matrix[row][column+block] = '\033[37;46m'+' '+'\033[0m'
				# board.matrix[row-1][column+block]=" "
			row = row +1


player=Hero()
shooter = Shooter()
saiyan = SuperSaiyan()

class LaserEmitter(Object):
	def __init__(self):
		self._grid = ["whoop"]
		self._xsize=1
		self._ysize=1

	def getxsize(self):
		return self._xsize
	def setxsize(self,xsize):
		self._xsize = xsize

	def getysize(self):
		return self._ysize
	def setysize(self,ysize):
		self._ysize = ysize

	def create(self,pox,poy):
		column = poy
		row = pox
		temp = column
		for i in range(self._ysize):
			column = temp
			for block in range(len(self._grid[i])):
				board.matrix[row][column+block]= '\033[30;43m'+self._grid[i][block] +'\033[0m'
			row=row+1

	def delete(self,pox,poy):
		column=poy
		row = pox
		temp = column
		for i in range(self._ysize):
			column = temp
			for block in range(len(self._grid[i])):
				board.matrix[row][column+block]='\033[33;46m'+' '+'\033[0m'
			row=row+1


class LaserHorizontal(LaserEmitter):
	def __init__(self):
		self._grid = ["||--------------------||","||--------------------||"]
		self._xsize = 24
		self._ysize = 2
		self.__no = 16

	def getxsize(self):
		return self._xsize
	def setxsize(self,xsize):
		self._xsize = xsize

	def getysize(self):
		return self._ysize
	def setysize(self,ysize):
		self._ysize = ysize

	def getno(self):
		return self.__no
	def setno(self,no):
		self.__no=no

class LaserVertical(LaserEmitter):
	def __init__(self):
		self._grid = ["--","||","||","||","||","||","||","--"]
		self._xsize = 2
		self._ysize = 8
		self.__no = 16

	def getxsize(self):
		return self._xsize
	def setxsize(self,xsize):
		self._xsize = xsize

	def getysize(self):
		return self._ysize
	def setysize(self,ysize):
		self._ysize = ysize

	def getno(self):
		return self.__no
	def setno(self,no):
		self.__no=no

class LaserCrossLeft(LaserEmitter):
	def __init__(self):
		self._grid = [
		" _      ",
		"| |     ",
		" \\     ",
		"  \\    ",
		"   \\   ",
		"    \\  ",
		"     \\ ",
		"     |_|"
		]
		self._xsize = 8
		self._ysize = 8
		self.__no = 10

	def getxsize(self):
		return self._xsize
	def setxsize(self,xsize):
		self._xsize = xsize

	def getysize(self):
		return self._ysize
	def setysize(self,ysize):
		self._ysize = ysize

	def getno(self):
		return self.__no
	def setno(self,no):
		self.__no=no

	# def create(self,pox,poy):
	# 	column = poy
	# 	row = pox
	# 	temp = column
	# 	for i in range(8):
	# 		column = temp
	# 		for block in range(8):
	# 			board.matrix[row][column+block]= '\033[30;43m'+self._grid[i][block] +'\033[0m'
	# 		row=row+1
	#
	# def delete(self,pox,poy):
	# 	column=poy
	# 	row = pox
	# 	temp = column
	# 	for i in range(8):
	# 		column = temp
	# 		for block in range(8):
	# 			board.matrix[row][column+block]='\033[33;46m'+' '+'\033[0m'
	# 		row=row+1


class LaserCrossRight(LaserEmitter):
	def __init__(self):
		self._grid = [
		"      _ ",
		"     | |",
		"     // ",
		"    //  ",
		"   //   ",
		"  //    ",
		" //     ",
		"|_|     "
		]
		self._xsize = 8
		self._ysize = 8
		self.__no = 10

	def getxsize(self):
		return self._xsize
	def setxsize(self,xsize):
		self._xsize = xsize

	def getysize(self):
		return self._ysize
	def setysize(self,ysize):
		self._ysize = ysize

	def getno(self):
		return self.__no
	def setno(self,no):
		self.__no=no

	# def create(self,pox,poy):
	# 	column = poy
	# 	row = pox
	# 	temp = column
	# 	for i in range(8):
	# 		column = temp
	# 		for block in range(8):
	# 			board.matrix[row][column+block]= '\033[30;43m'+self._grid[i][block] +'\033[0m'
	# 		row=row+1
	#
	# def delete(self,pox,poy):
	# 	column=poy
	# 	row = pox
	# 	temp = column
	# 	for i in range(8):
	# 		column = temp
	# 		for block in range(8):
	# 			board.matrix[row][column+block]='\033[33;46m'+' '+'\033[0m'
	# 		row=row+1


class Coin():
	def __init__(self):
		self._grid = ["$"]
		self.__xsize = 1
		self.__ysize = 1
		self.__no = 50

	def getxsize(self):
		return self.__xsize
	def setxsize(self,xsize):
		self.__xsize = xsize

	def getysize(self):
		return self.__ysize
	def setysize(self,ysize):
		self.__ysize = ysize

	def getno(self):
		return self.__no
	def setno(self,no):
		self.__no=no

	def create(self,pox,poy):
		column = poy
		row = pox
		board.matrix[row][column] = '\033[30;43m'+self._grid[0][0] + '\033[0m'

	def delete(self,pox,poy):
		column = poy
		row = pox
		board.matrix[row][column] = '\033[30;46m'+" " + '\033[0m'

laser = LaserEmitter()
hlaser = LaserHorizontal()
vlaser = LaserVertical()
llaser = LaserCrossLeft()
rlaser = LaserCrossRight()
coin = Coin()


class Dragon():
	def __init__(self):
		self._grid = [
		"<>=======()                           ",
		"(/\___   /|\\          ()==========<>_",
		"     \_/ | \\        //|\   ______/ \)",
		"       \_|  \\      // | \_/          ",
		"         \|\/|\_   //  /\/            ",
		"         (oo)\ \_//  /                ",
		"         //_/\_\/ /  |                ",
		"        @@/  |=\  \  |                ",
		"             \_=\_ \ |                ",
		"               \==\ \|\_              ",
		"            __(\===\(  )\             ",
		"           (((~) __(_/   |            ",
		"                (((~) \  /            ",
		"                ______/ /             ",
		"                '------'               "
		]
		self.__ice= [
		" \|/",
		"--+--",
		" /|\ "
		]
		self.__xsize = 38
		self.__ysize = 15
		self.__x = 960
		self.__y = 10

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

	def getxsize(self):
		return self.__xsize
	def setxsize(self,xsize):
		self.__xsize = xsize

	def getysize(self):
		return self.__ysize
	def setysize(self,ysize):
		self.__ysize = ysize

	def create(self,pox=10,poy=1960):
		column = poy
		row = pox
		temp = column
		self.__x = poy
		self.__y = pox
		for i in range(self.__ysize):
			column = temp
			for block in range(len(self._grid[i])):
				board.matrix[row][column+block]= '\033[37;46m'+self._grid[i][block] +'\033[0m'
			row=row+1

	def delete(self,pox=10,poy=1960):
		column = poy
		row = pox
		temp = column
		for i in range(self.__ysize):
			column = temp
			for block in range(len(self._grid[i])):
				board.matrix[row][column+block]= '\033[37;46m'+ ' ' +'\033[0m'
			row=row+1

	def createIce(self,pox,poy=1960):
		column = poy
		row = pox
		temp = column
		#insert bullet
		for i in range(3):
			column = temp
			for block in range(len(self.__ice[i])):
				board.matrix[row][column-6+block]= '\033[37;46m'+self.__ice[i][block] +'\033[0m'
			row=row+1

	def deleteIce(self,pox,poy=1960):
		column = poy
		row = pox
		temp = column
		#insert bullet
		for i in range(3):
			column = temp
			for block in range(len(self.__ice[i])):
				board.matrix[row][column-6+block]= '\033[37;46m'+ " " +'\033[0m'
			row=row+1


	def shoot(self,pox,poy=1960):
		column = poy
		row = pox
		temp = column
		self.createIce(pox,poy)
		dragbullets.append(DragonBulletList(poy-6,pox,poy-6))
		self.deleteIce(pox,poy)

dragon = Dragon()

class Magnet():
	def __init__(self):
		self._grid = [
		"|------",
		"|",
		"|",
		"|------",
		]
		self.__x = 10
		self.__y = 500
		self.__xsize = 7
		self.__ysize = 4

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

	def getxsize(self):
		return self.__xsize
	def setxsize(self,xsize):
		self.__xsize = xsize

	def getysize(self):
		return self.__ysize
	def setysize(self,ysize):
		self.__ysize = ysize

	def create(self,pox=10,poy=1960):
		column = poy
		row = pox
		temp = column
		self.__x = poy
		self.__y = pox
		for i in range(self.__ysize):
			column = temp
			for block in range(len(self._grid[i])):
				if(i==0 or i==1):
					board.matrix[row][column+block]= '\033[31;41m'+self._grid[i][block] +'\033[0m'
				else:
					board.matrix[row][column+block]= '\033[34;44m'+self._grid[i][block] +'\033[0m'
			row=row+1

	def delete(self,pox=10,poy=1960):
		column = poy
		row = pox
		temp = column
		for i in range(self.__ysize):
			column = temp
			for block in range(len(self._grid[i])):
				board.matrix[row][column+block]= '\033[37;46m'+ ' ' +'\033[0m'
			row=row+1

magnet=Magnet()

class Win(LaserEmitter):
	def __init__(self):
		self.xsize=50
		self.ysize=15
		self.grid=[
		"            ___              ___   ___         ___",
		"\        / |    |    |      |   \ |   | |\  | |",
		" \  /\  /  |--  |    |      |   | |   | | \ | |--",
		"  \/  \/   |___ |___ |___   |___/ |___| |  \| |___",
		" ",
		"        	\   /  __",
		"   		 \ /  |  | |  |",
		"   		  |   |__| |__|",
		"             |",
		"  ___   _        __  _",
		"  |__  |_| \  / |_  | \         ___   __    ___",
		"  ___| | |  \/  |__ |_/  \   / |   | |  \  |   |",
		"                          \ /  |   | |   | |___|",
		"                           |   |   | |   | |   |",
		"                           |   |___| |__/  |   |"
		]
	
	def printWin(self,poy=2080,pox=15):
		column = poy
		row = pox
		temp = column
		for i in range(self.ysize):
			column = temp
			for block in range(len(self.grid[i])):
				board.matrix[row][column+block]= '\033[30;46m'+ self.grid[i][block] +'\033[0m'
			row=row+1		

win=Win()

class Yoda(LaserEmitter):
	def __init__(self):
		self.xsize=40
		self.ysize=29
		self.grid=[
		"                    ____",
		"                 _.' :  `._",
		"             .-.'`.  ;   .'`.-.",
		"    __      / : ___\ ;  /___ ; \      __",
		"  ,'_ ----.:__; .-. ;: : .-. :__;.---- _`,",
		"  :' `.t----.. '<@.`;_  ',@>` ..----j.' `;",
		"       `:-.._J '-.-'L__ `-- ' L_..-;'",
		"          -.__ ; \.-    -./  : __.- ",
		"             L    \------/    J",
		"               -.    --    .- ",
		"          __.l -:_JL_;- ;.__",
		"     .-j/ .;  ;   / . \ -.",
		"   .  /:`.  -.:     .-  . ;  `.",
		"     .-   / ;   -.  -..-  .-   :     -.",
		"  .+ -.  : :       -.__.-       ;-._   \ ",
		"  ; \  `.; ;                    : :  +. ;",
		"  :  ;   ; ;                    : ;  : \:",
		" : `. -; ;  ;                  :  ;   ,/;",
		"  ;    -: ;  :                ;  : .-    :",
		"  :\     \  : ;             : \.-       :",
		"   ;`.    \  ; :            ;. _..--  / ;",
		"   :   -.   -:  ;          :/.       .   :",
		"     \       .-`.\        /t-    :-+.   :",
		"      `.  .-     `l    __/ /`. :  ; ; \  ;",
		"        \   .-  .- -.-   .  . j \  /   ;/",
		"         \ / .-    /.     . .  ;_:     ;",
		"          :- -.`./-.      /    `.___. ",
		"                \ `t  ._  / ",
		"                  -.t-._: "
		]
	
	def printYoda(self,poy=2150,pox=10):
		column = poy
		row = pox
		temp = column
		for i in range(self.ysize):
			column = temp
			for block in range(len(self.grid[i])):
				board.matrix[row][column+block]= '\033[30;46m'+ self.grid[i][block] +'\033[0m'
			row=row+1		

yoda=Yoda()

class Vader(LaserEmitter):
	def __init__(self):
		self.xsize=40
		self.ysize=27
		self.grid=[
		"                       .-.",
		"                      |_:_|",
		"                     /(_Y_)\ ",
		".                   ( \/M\/ )",
		"  .               _. -/ - \- ._",
		"    :           _/.-- [[[[] --.\_",
		"      :        /_   : |:: | :   .\ ",
		"        :     //   ./ |OwO| \.   :\ ",
		"          :  _: ..  \_|___|_/ :   :|",
		"            :.  .   |_[___]_|  :. :\ ",
		"            [::\ |  :  | |  :   ; : \ ",
		"              -    \/ .| |.  \  .;.  |",
		"             |\_    \   -    :       |",
		"             |  \    \ .:    :   |   |",
		"             |   \    |  .   :    \  |",
		"             /       \   :. .;       |",
		"            /     |   |  :__/     :   \ ",
		"           |  |   |    \:   | \   |   ||",
		"          /    \  : :  |:   /  |__|   /|",
		"          |     : : :_/_|  / ._\   --|_\ ",
		"          /___.-/_|-    \  \ ",
		"                          -",
		"                                 __.-._",
		"                                  -._ 7",
		"                                  / .-c",
		"                                  |  /T",
		"                                 _)_/LI"
		]
	
	def printVader(self,poy=2010,pox=10):
		column = poy
		row = pox
		temp = column
		for i in range(self.ysize):
			column = temp
			for block in range(len(self.grid[i])):
				board.matrix[row][column+block]= '\033[30;46m'+ self.grid[i][block] +'\033[0m'
			row=row+1		

vader=Vader()