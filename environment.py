from random import randint
import os
import time
from board import *
from characters import *
from globalvar import *

def GenerateLasers():
	for i in range(coin.getno()):
		startCol = randint(10,1800)
		startRow = randint(1,47)
		coins.append(CoinList(startCol,startRow))
		coin.create(startRow,startCol)

	for i in range(hlaser.getno()):
		startCol = randint(10,180)*10
		startRow = randint(1,45)
		horiLasers.append(HoriLaserList(startCol,startRow))
		hlaser.create(startRow,startCol)

	for i in range(vlaser.getno()):
		startCol = randint(10,180)*10
		startRow = randint(1,40)
		vertLasers.append(VertLaserList(startCol,startRow))
		vlaser.create(startRow,startCol)

	# for i in range(llaser.getno()):
	# 	startCol = randint(10,130)*13
	# 	startRow = randint(1,40)
	# 	vertLasers.append(LeftLaserList(startCol,startRow))
	# 	llaser.create(startRow,startCol)

	# for i in range(rlaser.getno()):
	# 	startCol = randint(10,130)*13
	# 	startRow = randint(1,40)
	# 	vertLasers.append(RightLaserList(startCol,startRow))
	# 	rlaser.create(startRow,startCol)


	for i in range(4):
		startCol = randint(1,18)* 100
		startRow = randint(1,40)
		magnets.append(MagnetList(startCol,startRow))
		magnet.create(startRow,startCol)

def CollisionLaser(curr_col,curr_row,lives,score,blives,shield=False):
	flag = 0
	gAmE = "amazeballs"
	pposx = curr_col
	pposy = curr_row
	pwidth = player.gety()
	pheight = player.getx()
	hwidth = hlaser.getxsize()
	hheight = hlaser.getysize()
	vwidth = vlaser.getxsize()
	vheight = vlaser.getysize()
	dwidth = dragon.getxsize()
	dheight = dragon.getysize()
	mwidth = magnet.getxsize()
	mheight = magnet.getysize()
	cwidth = llaser.getxsize()
	cheight = llaser.getysize()

	for i in range(len(horiLasers)):
		if((pposx <= horiLasers[i].getx()+hwidth) and (pposx + pwidth >= horiLasers[i].getx()) and (pposy <= horiLasers[i].gety() + hheight) and (pposy + pheight >= horiLasers[i].gety())):
			hlaser.delete(horiLasers[i].gety(),horiLasers[i].getx())
			player.Print(curr_col,curr_row)
			horiLasers.pop(i)
			if shield==False:
				flag = 1
			break


	for i in range(len(vertLasers)):
		if((pposx <= vertLasers[i].getx()+vwidth) and (pposx + pwidth >= vertLasers[i].getx()) and (pposy <= vertLasers[i].gety() + vheight) and (pposy + pheight >= vertLasers[i].gety())):
			vlaser.delete(vertLasers[i].gety(),vertLasers[i].getx())
			player.Print(curr_col,curr_row)
			vertLasers.pop(i)
			if shield==False:
				flag = 1
			break

	for i in range(len(leftLasers)):
		if((pposx <= leftLasers[i].getx()+cwidth) and (pposx + pwidth >= leftLasers[i].getx()) and (pposy <= leftLasers[i].gety() + cheight) and (pposy + pheight >= leftLasers[i].gety())):
			llaser.delete(leftLasers[i].gety(),leftLasers[i].getx())
			player.Print(curr_col,curr_row)
			leftLasers.pop(i)
			if shield==False:
				flag = 1
			break

	for i in range(len(rightLasers)):
		if((pposx <= rightLasers[i].getx()+cwidth) and (pposx + pwidth >= rightLasers[i].getx()) and (pposy <= rightLasers[i].gety() + cheight) and (pposy + pheight >= rightLasers[i].gety())):
			llaser.delete(rightLasers[i].gety(),rightLasers[i].getx())
			player.Print(curr_col,curr_row)
			rightLasers.pop(i)
			if shield==False:
				flag = 1
			break

	for i in range(len(magnets)):
		if((pposx <= magnets[i].getx()+mwidth) and (pposx + pwidth >= magnets[i].getx()) and (pposy <= magnets[i].gety() + mheight) and (pposy + pheight >= magnets[i].gety())):
			magnet.delete(magnets[i].gety(),magnets[i].getx())
			player.Print(curr_col,curr_row)
			magnets.pop(i)
			if shield==False:
				flag = 1
			break


	for i in range(len(coins)):
		if((pposx <= coins[i].getx()) and (pposx+pwidth >= coins[i].getx()) and (pposy <= coins[i].gety()) and (pposy + pheight >= coins[i].gety())):
			coin.delete(coins[i].gety(),coins[i].getx())
			player.Print(curr_col,curr_row)
			coins.pop(i)
			score=score+1
			break


	for b in bullets:
		for i in range(len(horiLasers)):
			if((b.getx() <= horiLasers[i].getx()+hwidth) and (b.getx() >= horiLasers[i].getx()) and (b.gety() <= horiLasers[i].gety()+hheight) and (b.gety() >= horiLasers[i].gety())):
				hlaser.delete(horiLasers[i].gety(),horiLasers[i].getx())
				horiLasers.pop(i)
				board.matrix[b.gety()][b.getx()]= '\033[37;46m'+ ' ' +'\033[0m'
				board.matrix[b.gety()][b.getx()+1]= '\033[37;46m'+ ' ' +'\033[0m'
				bullets.remove(b)
				score=score+10
				break

		for i in range(len(magnets)):
			if((b.getx() <= magnets[i].getx()+hwidth) and (b.getx() >= magnets[i].getx()) and (b.gety() <= magnets[i].gety()+hheight) and (b.gety() >= magnets[i].gety())):
				magnet.delete(magnets[i].gety(),magnets[i].getx())
				magnets.pop(i)
				board.matrix[b.gety()][b.getx()]= '\033[37;46m'+ ' ' +'\033[0m'
				board.matrix[b.gety()][b.getx()+1]= '\033[37;46m'+ ' ' +'\033[0m'
				bullets.remove(b)
				score=score+100
				break


		for i in range(len(vertLasers)):
			if((b.getx() <= vertLasers[i].getx()+vwidth) and (b.getx() >= vertLasers[i].getx()) and (b.gety() <= vertLasers[i].gety()+vheight) and (b.gety() >= vertLasers[i].gety())):
				vlaser.delete(vertLasers[i].gety(),vertLasers[i].getx())
				vertLasers.pop(i)
				board.matrix[b.gety()][b.getx()]= '\033[37;46m'+ ' ' +'\033[0m'
				board.matrix[b.gety()][b.getx()+1]= '\033[37;46m'+ ' ' +'\033[0m'
				bullets.remove(b)
				score=score+10
				break

		for i in range(len(leftLasers)):
			leftLasers.pop(i)
			if((b.getx() <= leftLasers[i].getx()+cwidth) and (b.getx() >= leftLasers[i].getx()) and (b.gety() <= leftLasers[i].gety()+cheight) and (b.gety() >= leftLasers[i].gety())):
				llaser.delete(leftLasers[i].gety(),leftLasers[i].getx())
				board.matrix[b.gety()][b.getx()]= '\033[37;46m'+ ' ' +'\033[0m'
				board.matrix[b.gety()][b.getx()+1]= '\033[37;46m'+ ' ' +'\033[0m'
				bullets.remove(b)
				score=score+10
				break

		for i in range(len(rightLasers)):
			if((b.getx() <= rightLasers[i].getx()+cwidth) and (b.getx() >= rightLasers[i].getx()) and (b.gety() <= rightLasers[i].gety()+cheight) and (b.gety() >= rightLasers[i].gety())):
				rlaser.delete(rightLasers[i].gety(),rightLasers[i].getx())
				rightLasers.pop(i)
				board.matrix[b.gety()][b.getx()]= '\033[37;46m'+ ' ' +'\033[0m'
				board.matrix[b.gety()][b.getx()+1]= '\033[37;46m'+ ' ' +'\033[0m'
				bullets.remove(b)
				score=score+10
				break


		for i in range(len(coins)):
			if((b.getx()==coins[i].getx()) and (b.gety()==coins[i].gety())):
				coin.delete(coins[i].gety(),coins[i].getx())
				coins.pop(i)
				score=score-5
				break


		if((b.getx() <= dragon.getx() + dwidth) and (b.getx() >= dragon.getx()) and (b.gety() <= dragon.gety() + dheight) and (b.gety() >= dragon.gety())):
			blives=blives-1
			if(blives==0):
				board.matrix[b.gety()][b.getx()]= '\033[37;46m'+ ' ' +'\033[0m'
				board.matrix[b.gety()][b.getx()+1]= '\033[37;46m'+ ' ' +'\033[0m'
				bullets.remove(b)
				score = score + 10000
				break
			else:
				board.matrix[b.gety()][b.getx()]= '\033[37;46m'+ ' ' +'\033[0m'
				board.matrix[b.gety()][b.getx()+1]= '\033[37;46m'+ ' ' +'\033[0m'
				bullets.remove(b)
				score = score + 10000


	for i in dragbullets:
		if((pposx <= i.getx()+5) and (pposx + pwidth >= i.getx()) and (pposy <= i.gety() + 3) and (pposy + pheight >= i.gety())):
			dragon.deleteIce(i.gety(),i.getx())
			player.Print(curr_col,curr_row)
			dragbullets.remove(i)
			if shield == False:
				flag = 1
			else:
				shield = False
			break


	if flag==1:
		return [lives-1,score,blives,shield]
	else:
		return [lives,score,blives,shield]
