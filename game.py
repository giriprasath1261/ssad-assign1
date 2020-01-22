import random
from globalvar import *
from environment import *
from board import *
from characters import *
import random
import os
import select,sys
import termios,tty,time
from movement import *
import time
import math


#required variables 
lives = 5
score = 0
boss = 10
shields = 1
shield = False
shield_start=0
boost = False
boost_start=0
boosts = 1
store = 0

#starting functions
GenerateLasers()
TitlePrint(lives,score,name,shields)
board.Display(begin,end)
player.Print()


#checking if key is pressed
def keypressed():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

Needed = termios.tcgetattr(sys.stdin)


try:
	tty.setcbreak(sys.stdin.fileno())

	#time variables in the start
	fseconds = time.time() * 3
	ffseconds = time.time() / 2
	fffseconds = time.time() 
	start_time = math.floor(fseconds)
	fstart_time = math.floor(ffseconds)
	ffstart_time = math.floor(fffseconds)
	curr_time=start_time
	fcurr_time=fstart_time
	scurr_time = ffstart_time

	#main loop of the game:
	while GameOver==False:
		temp_time=curr_time
		ftemp_time=fcurr_time

		#switch case according to pressed key
		if keypressed():
			key = sys.stdin.read(1)
			if key=='w':
				shoot=False
				if(shield==True):
					saiyan.Delete(curr_col,curr_row)
				else:
					player.Delete(curr_col,curr_row)
				if(curr_row>2):
					curr_row = curr_row - 1
				if(shield==True):
					saiyan.Print(curr_col,curr_row)
				else:
					player.Print(curr_col,curr_row)
				arr=CollisionLaser(curr_col,curr_row,lives,score,boss,shield)
				lives=arr[0]
				score=arr[1]
				boss=arr[2]
				shield = arr[3]


			if key=='s':
				shoot=False
				if(shield==True):
					saiyan.Delete(curr_col,curr_row)
				else:
					player.Delete(curr_col,curr_row)
				if(curr_row<40):
					curr_row = curr_row +1
				if(shield==True):
					saiyan.Print(curr_col,curr_row)
				else:
					player.Print(curr_col,curr_row)
				arr=CollisionLaser(curr_col,curr_row,lives,score,boss,shield)
				lives=arr[0]
				score=arr[1]
				boss=arr[2]
				shield = arr[3]



			if key=='a':
				shoot=False
				if(shield==True):
					saiyan.Delete(curr_col,curr_row)
				else:
					player.Delete(curr_col,curr_row)
				if(curr_col>curr_pos):
					curr_col = curr_col - 1
				if(shield==True):
					saiyan.Print(curr_col,curr_row)
				else:
					player.Print(curr_col,curr_row)
				arr=CollisionLaser(curr_col,curr_row,lives,score,boss,shield)
				lives=arr[0]
				score=arr[1]
				boss=arr[2]
				shield = arr[3]


			if key=='d':
				shoot=False
				if(shield==True):
					saiyan.Delete(curr_col,curr_row)
				else:
					player.Delete(curr_col,curr_row)
				if(curr_col<curr_pos+190 and curr_col < 1958):
					if(boost==False):
						curr_col = curr_col + 2
					else:
						curr_col = curr_col + 4
				if(shield==True):
					saiyan.Print(curr_col,curr_row)
				else:
					player.Print(curr_col,curr_row)
				arr=CollisionLaser(curr_col,curr_row,lives,score,boss,shield)
				lives=arr[0]
				score=arr[1]
				boss=arr[2]
				shield = arr[3]


			if key=='f':
				if shoot==False:
					if shield == False:
						player.Delete(curr_col,curr_row)
						shooter.Print(curr_col,curr_row)
						BulletRelease(curr_col,curr_row,curr_pos)
						# lives=CollisionLaser()
						shoot=True
					else:
						saiyan.Delete(curr_col,curr_row)
						shooter.Print(curr_col,curr_row)
						BulletRelease(curr_col,curr_row,curr_pos)
						# lives=CollisionLaser()
						shoot=True

				elif shoot==True:
					if shield == False:
						shooter.Delete(curr_col,curr_row)
						player.Print(curr_col,curr_row)
						shoot=False
					else:
						shooter.Delete(curr_col,curr_row)
						saiyan.Print(curr_col,curr_row)
						shoot=False

			if key=='e':
				if shields > 0:
					if shield == False:
						shield= True
						shields = shields -1
						player.Delete(curr_col,curr_row)
						saiyan.Print(curr_col,curr_row)
						saiyan.Delete(curr_col,curr_row)
						curr_row=curr_row
						shield_start = math.floor(time.time())

			if key=='z':
				if boosts > 0:
					if boost == False:
						boosts=boosts-1
						boost = True
						boost_start = math.floor(time.time())

			if key=='q':
				sys.exit()	


		#current time variables
		temp=time.time() * 3
		ftemp=time.time() / 2
		stemp = time.time()
		curr_time=math.floor(temp)
		fcurr_time=math.floor(ftemp)
		scurr_time = math.floor(stemp)
		time_rem = 360 - (scurr_time - ffstart_time)
		
		#gravity
		if(curr_row<40):
			if(curr_time!=temp_time):
				if(curr_row>34):
					if(shield==False):
						player.Delete(curr_col,curr_row)
						player.Print(curr_col,40)
					else:
						saiyan.Delete(curr_col,curr_row)
						saiyan.Print(curr_col,40)
					curr_row=40
				else:
					player.Gravity(curr_col,curr_row,2,shield)
					curr_row=curr_row+2

		#shield timer
		if(scurr_time-shield_start>4):
			shield=False

		if(scurr_time-shield_start>20):
			shields=1

		#boost timer
		if(scurr_time-boost_start>2):
			boost=False

		if(scurr_time-boost_start>20):
			boosts=1
		
		#display mover
		if(boost==True):	
			if curr_time-start_time>3:
				curr_pos = curr_pos +3
			store = curr_pos - (curr_time-start_time)*8
		else:
			curr_pos=(curr_time-start_time)*8 + store						
		# else:
			# curr_pos=(curr_time-start_time)*10			
		
		#stop display moving
		if curr_pos > 1800:
			curr_pos = 1800
		
		#dont let player go out of display
		if(curr_pos-curr_col>1):
			if(shield==False):
				player.Delete(curr_col,curr_row)
				curr_col=curr_pos
				player.Print(curr_col,curr_row)
			else:
				saiyan.Delete(curr_col,curr_row)
				curr_col=curr_pos
				saiyan.Print(curr_col,curr_row)

		#game over lose
		if(lives<=0):
			GameOver=True
		if(time_rem < 1):
			GameOver = True
		
		#magnet
		arr2= Attraction(curr_col,curr_row)
		curr_col=arr2[0]
		# curr_row=arr2[0] 

		print('\033[0;0H]')
		
		#check collision
		arr=CollisionLaser(curr_col,curr_row,lives,score,boss,shield)
		lives=arr[0]
		score=arr[1]
		boss=arr[2]
		shield = arr[3]

		#move all bullets
		MoveBullet()
		
		#boss fight
		if(curr_col==1800):
			if(curr_row < 33):
				dragon.create(curr_row,1960)
			else:
				dragon.create(33,1960)
		elif(curr_col>=1800):
			if(curr_row < 33 ):
				dragon.create(curr_row,1960)
			else:
				dragon.create(33,1960)
			if(fcurr_time!=ftemp_time):
				dragon.shoot(curr_row)
		
		#priting stats
		if(curr_col<1800):
			TitlePrint(lives,score,name,shields,boosts,0,time_rem)
		else:
			TitlePrint(lives,score,name,shields,boosts,boss,time_rem)
		
		#game over win
		if(boss<=0):
			if(curr_col>=1800):
				if(curr_row < 33):
					dragon.delete(curr_row,1960)
				else:
					dragon.delete(33,1960)
			win.printWin()
			yoda.printYoda()
			vader.printVader()
			board.Display(2000,2200)
			sys.exit()
		
		#display function
		board.Display(curr_pos,curr_pos+200)
		
		#delete dragon
		if(curr_col>1800):
			if(curr_row < 33):
				dragon.delete(curr_row,1960)
			else:
				dragon.delete(33,1960)


finally:
	termios.tcsetattr(sys.stdin,termios.TCSADRAIN,Needed)
	print("GAME OVER")

# print(player.shape)