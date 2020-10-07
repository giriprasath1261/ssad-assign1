curr_col = 1
curr_row = 40
curr_pos = 0
name="KILLMONGER"
GameOver=False
shoot=False
start=True
screen = 0
begin=0
end=200
onGround=True

class HoriLaserList:
	def __init__(self,x,y):
		self.__x = x
		self.__y = y

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y
horiLasers = []

class VertLaserList:
	def __init__(self,x,y):
		self.__x = x
		self.__y = y

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

vertLasers = []

class LeftLaserList:
	def __init__(self,x,y):
		self.__x = x
		self.__y = y

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

leftLasers = []

class RightLaserList:
	def __init__(self,x,y):
		self.__x = x
		self.__y = y

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

rightLasers = []

class MagnetList:
	def __init__(self,x,y):
		self.__x = x
		self.__y = y

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

magnets = []
# vertLaseresRow=[]
# vertLasersCol=[]
# coinRow=[]
# coinCol=[]

class CoinList:
	def __init__(self,x,y):
		self.__x = x
		self.__y = y

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

coins=[]


class BulletList:
	def __init__(self,x,y,start):
		self.__x = x
		self.__y = y
		self.start = start

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

	def getstart(self):
		return self.__start
	def sety(self,start):
		self.__start = start

bullets=[]

class DragonBulletList:
	def __init__(self,x,y,start):
		self.__x = x
		self.__y = y
		self.start = start

	def getx(self):
		return self.__x
	def setx(self,x):
		self.__x = x

	def gety(self):
		return self.__y
	def sety(self,y):
		self.__y = y

	def getstart(self):
		return self.__start
	def sety(self,start):
		self.__start = start

dragbullets=[]
