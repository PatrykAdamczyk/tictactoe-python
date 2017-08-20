import sys
class Game():
	def __init__(self):
		self.players = [" " ,"X", "O"]
		self.score = {
			self.players[1]: 0,
			self.players[2]: 0
		}
		self.cleangametable()
	def cleangametable(self):
		self.gametable = [
			[self.players[0],self.players[0],self.players[0]],
			[self.players[0],self.players[0],self.players[0]],
			[self.players[0],self.players[0],self.players[0]]
		]
	def run(self):
		self.header()
		player = self.players[0]
		while True:
			while not self.check():
				if player == self.players[0]:
					player = self.players[1]
				elif player == self.players[1]:
					player = self.players[2]
				elif player == self.players[2]:
					player = self.players[1]
				self.show()
				try:
					print("Type choice or 25 to exit")
					choicex = int(input((player + " x: "))) - 1
					choicey = int(input((player + " y: "))) - 1
				except:
					choicex = -1
					choicey = -1
				if choicex is 24 and choicey is 24:
					sys.exit()
				if self.move((choicey,choicex),player) is False:
					continue
			self.cleangametable()
			self.win(player)
			choice = input("Q to Quit or anything to continue")
			if  choice == "Q" or choice == "q":
				sys.exit()
	def show(self):
		for i in range (0,3):
			for j in range(0,3):
				print("[",self.gametable[i][j],"] ", end="")
			print()
	def move(self, cords, player):
		if cords[0] < 0 and cords[1] < 0:
			return False
		try:
			if self.gametable[cords[0]][cords[1]] != self.players[0]:
				print("You can't move here")
				return False
			else:
				self.gametable[cords[0]][cords[1]] = player
		except IndexError:
			return False
		pass
	def win(self, player):
		print("Won ", player)
		self.score[player] += 1
		print("Leadersboard: ")
		print(self.players[1], " : ", self.score[self.players[1]])
		print(self.players[2], " : ", self.score[self.players[2]])
	def tb(self,x,y):
		return self.gametable[y][x]
	def check(self):
		#F1
		if self.tb(0,0) == self.tb(0,1) == self.tb(0,2) != self.players[0]:
			return True
		if self.tb(1,0) == self.tb(1,1) == self.tb(1,2) != self.players[0]:
			return True
		if self.tb(2,0) == self.tb(2,1) == self.tb(2,2) != self.players[0]:
			return True
		#F2
		if self.tb(0,0) == self.tb(1,0) == self.tb(2,0) != self.players[0]:
			return True
		if self.tb(0,1) == self.tb(1,1) == self.tb(2,1) != self.players[0]:
			return True
		if self.tb(0,2) == self.tb(1,2) == self.tb(2,2) != self.players[0]:
			return True
		#F3
		if self.tb(0,0) == self.tb(1,1) == self.tb(2,2) != self.players[0]:
			return True
		#F4
		if self.tb(2,0) == self.tb(1,1) == self.tb(0,2) != self.players[0]:
			return True
		return False
	def test(self):
		#test False
		self.cleangametable()
		self.show()
		assert self.check() == False
		#test False 2
		self.move((0,0), self.players[1])
		self.show()
		print(self.check() == False)
		assert self.check() == False
		#test F1
		self.cleangametable()
		p = self.players[1]
		self.move((0,0),p)
		self.move((0,1),p)
		self.move((0,2),p)
		self.show()
		assert self.check() == True
		#test F2
		self.cleangametable()
		self.move((0,0),p)
		self.move((1,0),p)
		self.move((2,0),p)
		self.show()
		assert self.check() == True
		#test F3
		self.cleangametable()
		self.move((0,0),p)
		self.move((1,1),p)
		self.move((2,2),p)
		self.show()
		assert self.check() == True
		#test F4
		self.cleangametable()
		self.move((0,2),p)
		self.move((1,1),p)
		self.move((2,0),p)
		self.show()
		assert self.check() == True
		print("Tested!!!!")
	def header(self):
		print("PAiP Tic Tac Toe v.1.0.0.0")
		print("Created with Python 3.6")
		print("==========================")

