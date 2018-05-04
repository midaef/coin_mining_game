
import random
from ezprint import p
import os


m = 30
g = 1

def cls():
	os.system('cls')


def dolor1():
	m1 = '┌──┐\n│1$│\n└──┘'
	p(m1)

def dolor2():
	m2 = '┌──┐\n│1☼│\n└──┘'
	p(m2)

def dolor3():
	m3 = '┌┐\n││\n└┘'
	p(m3)


def menu():
	global m 
	cls()
	p('===GAME FOR WINDOWS===')
	p('======COIN_FARME======')
	p('=========MENU=========')
	p('===YOUR BALANCE: ' + str(m) + '====')
	p('====1-START MINING====')
	p('====2-MARKETPLACE=====')
	p('====3-EXIT============')
	v = input('>>>')
	if v == '1':
		main() 
	elif v == '2':
		market()
	elif v == '3':
		exit()
	else:
		p('Incorrect choose!')

def market():
	global m
	global g
	cls()
	p('1-To buy for 30 coins: +2 coins for mining')
	v = input('>>>')
	if v == '1':
		if m >=30:
			g = g + 1
			m = m - 30
			menu()
		else:
			p('Not enough money')
	else:
		p('Incorrect choose!')


def main():
	global m 
	global g
	cls()
	while True:
		p('Your balance: ' + str(m) + ' coin')
		p('=======================================')
		r = random.randint(1,100)
		if r < 50:
			dolor2()
		elif r > 50:
			dolor1()
		else:
			dolor3()
			m = m + g
			p('That is fine! You have found got 1 coin')
		p('========================================')
		p('Commands: "exit"- exit to menu')
		v = input('Click to Enter(continue): ')
		cls()
		if v == 'exit':
			menu()

if __name__ == '__main__':
	menu()
	main()



