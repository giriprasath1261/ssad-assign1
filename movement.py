import random
import os
import time
from board import *
from characters import *
from globalvar import *

def TitlePrint(lives=3,score=0,name="KILLMONGER",shields=3,boost=3,boss=0,time_rem=360):
	print("############################################################################################  JETPACK JOYRIDE   ########################################################################################")
	print()
	if(boss==0):
		print(" Name: "+ name + "                    Score:" + str(score) + "                    Lives: " + str(lives) + "                     Shields: " + str(shields) + "                    RemTime: " + str(time_rem) + "                    Boost: " + str(boost) )
	else:
		print(" Name: "+ name + "                    Score:" + str(score) + "                    Lives: " + str(lives) + "                     Shields: " + str(shields) + "                    RemTime: " + str(time_rem) + "                    Boost: " + str(boost) + "                   BossLives: "+ str(boss))






def BulletRelease(ccol,crow,cpos=0):
	lim=1
	col=ccol
	row=crow
	board.matrix[row+2][col+13]= '\033[37;46m'+ '=' +'\033[0m'
	board.matrix[row+2][col+14]= '\033[37;46m'+ '>' +'\033[0m'
	bullets.append(BulletList(col+14,row+2,col+14))
	board.matrix[row+2][col+13]= '\033[37;46m'+ ' ' +'\033[0m'

	# time.sleep(0.05)
	# board.matrix[row+3][col+13]=' '
	# board.matrix[row+3][col+14]=' '
	# for traj in range(col+14,cpos-2):
	# 	# if traj%lim==0:
	# 	board.matrix[row+3][traj-lim]=' '
	# 	board.matrix[row+3][traj-lim+1]=' '
	# 	board.matrix[row+3][traj]='='
	# 	board.matrix[row+3][traj+1]='>'
	# 	print('\033[0;0H]')
	# 	TitlePrint()
	# 	board.Display(cpos,cpos+200)
	# 	time.sleep(0.03)
	# board.matrix[row+3][cpos + 200 - 2]=' '
	# board.matrix[row+3][cpos + 200 - 3]=' '
	# board.matrix[row+3][cpos + 200 - 4]=' '

def MoveBullet():

	for i in bullets:
		if(i.getx()<1996):
			ttemp = i.getx() + 1
			i.setx(ttemp)
			board.matrix[i.gety()][i.getx()-1]= '\033[37;46m'+ ' ' +'\033[0m'
			board.matrix[i.gety()][i.getx()]= '\033[37;46m'+ '=' +'\033[0m'
			board.matrix[i.gety()][i.getx()+1]= '\033[37;46m'+ '>' +'\033[0m'
			if(i.getx()-i.start>150):
				board.matrix[i.gety()][i.getx()]= '\033[37;46m'+ ' ' +'\033[0m'
				board.matrix[i.gety()][i.getx()+1]= '\033[37;46m'+ ' ' +'\033[0m'
				bullets.remove(i)

		if(i.getx() == 1996):
			board.matrix[i.gety()][i.getx()] = '\033[37;46m'+ ' ' +'\033[0m'
			board.matrix[i.gety()][i.getx()+1] = '\033[37;46m'+ ' ' +'\033[0m'
			bullets.remove(i)


	for i in dragbullets:
		if(i.getx()>1805):
			dragon.deleteIce(i.gety(),i.getx())
			ttemp = i.getx() - 1
			i.setx(ttemp)
			dragon.createIce(i.gety(),i.getx())
		else:
			dragon.deleteIce(i.gety(),i.getx())
			dragbullets.remove(i)

def Attraction(curr_col,curr_row):

	for m in magnets:
		if m.getx() - curr_col < 50 and m.getx() - curr_col > 0:
			player.Delete(curr_col,curr_row)
			curr_col = curr_col + 1
			player.Print(curr_col,curr_row)
		elif curr_col - m.getx() < 50 and curr_col - m.getx() > 0:
			player.Delete(curr_col,curr_row)
			curr_col = curr_col - 1
			player.Print(curr_col,curr_row)

		# if m.y - curr_row < 25 and m.y - curr_row > 0:
		# 	player.Delete(curr_col,curr_row)
		# 	curr_row = curr_row + 1
		# 	player.Print(curr_col,curr_row)
		# elif curr_row - m.y < 50 and curr_row - m.y > 0:
		# 	player.Delete(curr_col,curr_row)
		# 	curr_row = curr_row - 1
		# 	player.Print(curr_col,curr_row)
	return [curr_col,curr_row]

	