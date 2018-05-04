
import random
from ezprint import p
import os


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
	p('===GAME FOR WINDOWS===')
	p('======COIN_FARME======')
	p('=========MENU=========')
	p('====1-START MINING====')
	v = input('>>>')
	if v == '1':
		main() 


def main():
	cls()
	while True:
		r = random.randint(1,100)
		if r < 50:
			dolor2()
		elif r > 50:
			dolor1()
		else:
			dolor3()
		p('===============================')
		p('help:exit')
		v = input('Click to Enter(continue): ')
		cls()
		if v == 'exit':
			menu()

if __name__ == '__main__':
	menu()
	main()



