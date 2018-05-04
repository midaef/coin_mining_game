
import random
from ezprint import p
import os


m = 0


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
	v = input('>>>')
	if v == '1':
		main() 


def main():
	global m 
	cls()
	while True:
		p('===============================')
		r = random.randint(1,100)
		if r < 50:
			dolor2()
		elif r > 50:
			dolor1()
		else:
			dolor3()
			m = m + 1
			p('That is fine! You have found got 1 coin')
		p('===============================')
		p('Help: exit')
		v = input('Click to Enter(continue): ')
		cls()
		if v == 'exit':
			menu()

if __name__ == '__main__':
	menu()
	main()



