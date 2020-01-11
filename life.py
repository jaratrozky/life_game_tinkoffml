# Без ооп тк я не очень хорошо знаю ооп
# 0 - пусто
# 1 - рыба
# 2 - креветка
# 3 - скала
# я даже пытался соблюдать pep8 

import argparse
from random import choice as ch
import time
import os


# не требует комментариев
def show_board(board):
	s = ''
	for i in board:
		for j in i:
			s += str(j)
		s += '\n'
	return s


def check_alive(board):
	l = len(board)
	n_board = []
	for i in range(l):
		n_board.append([])
		for j in range(l):
			cf = 0 # кол-во рыб вокруг данной клетки
			cs = 0 # то же, но креветки
			# костыли сплошные, но я это делаю в 2 часа ночи
			try:
				# проверяю не выходит ли [i][j] за массив тк мне лень было писать if
				temp = board[i][j]

				# скала остаётся скалой, таков путь
				if board[i][j] == 3:
					n_board[i].append(3)

				# если рыба, то идём по квадрату 3x3 вокруг рыбы с проверкой на наличие рыб
				elif board[i][j] == 1:
					for x in range(i - 1, i + 2):
						for y in range(j - 1, j + 2):
							if x < l and y < l and x > -1 and y > -1 and [x, y] != [i, j]:
								if board[x][y] == 1:
									cf += 1 
					# рыба живёт или умирает
					if cf in [2, 3]:
						n_board[i].append(1)
					else:
						n_board[i].append(0)

				# то же, но для креветок
				elif board[i][j] == 2:
					for x in range(i - 1, i + 2):
						for y in range(j - 1, j + 2):
							if x < l and y < l and x > -1 and y > -1 and [x, y] != [i, j]:
								if board[x][y] == 2:
									cf += 1
					if cf in [2, 3]:
						n_board[i].append(2)
					else:
						n_board[i].append(0)

				# если у нас пустой океан, то считаем всех рыб и креветок вокруг
				elif board[i][j] == 0:
					for x in range(i - 1, i + 2):
						for y in range(j - 1, j + 2):
							if x < l and y < l and x > -1 and y > -1:
								if board[x][y] == 2:
									cs += 1
								elif board[x][y] == 1:
									cf +=1

					# насколько я понял условие, сначала 
					# надо проверить наличие ровно трёх рыб,
					# а затем уже проверять креветок
					if cf == 3:
						n_board[i].append(1)
					elif cs == 3:
						n_board[i].append(2)
					else:
						n_board[i].append(0)
			except:
				pass
	return n_board


#создаю консольные аргументы для программы
parser = argparse.ArgumentParser(description='Get size of the board.')
parser.add_argument('-s', action='store', dest='s', help='Size of board', default = 8)
parser.add_argument('-d', action='store', dest='d', help='Duration of one generation', default = 500)
parser.add_argument('-m', action='store', dest='m', help='Amount of generations', default = 20)

args = parser.parse_args()
size = int(args.s)
dur = int(args.d) / 1000
moves = int(args.m)

board = []

for i in range(size):
	board.append([])
	for j in range(size):
		board[i].append(ch([0,1,2,3]))

os.system('clear') #костыль тк я не смог завести человеческий модуль для TUI
				   #и под виндой не работает ещё, ага
print(show_board(board))

for i in range(moves):
	board = check_alive(board)
	s = show_board(board)
	time.sleep(dur)
	os.system('clear')
	print(s)
