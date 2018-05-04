
import random
from ezprint import p


def dolor1():
	m1 = '┌──┐\n│1$│\n└──┘'
	p(m1)

def dolor2():
	m2 = '┌──┐\n│1☼│\n└──┘'
	p(m2)

def dolor3():
	m3 = '┌┐\n││\n└┘'
	p(m3)

def main():
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
		if v == 'exit':
			pass

if __name__ == '__main__':
	main()



