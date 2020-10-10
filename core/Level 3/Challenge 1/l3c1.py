# Inspired by Taha Junaid


class Sports:

	def __init__(self, Sports, Type = ""):
		self.Type = Type
		self.legends = []

	def dispLegends(self):
		print(*legends, sep = "\n")

	def dispDetails(self):
		print(" Game Type: ", self.Type)
		print(" Legends: ", self.legends)

	def addLegends(self):
		name = input(" Player name: ")
		isActive = input(" Is the player active (y/n): ")
		if isActive == "y": isActive = "Active"
		else: isActive = "Retired"
		self.legends.append([name, isActive])
		print("")


class Cricket(Sports):

	def __init__(self, overs, equipment = ['bat', 'ball', 'wickets'], origin = "England", players = 22):
		Sports.__init__(self, Type = "Outdoors")
		#self.name = name
		self.overs = overs
		self.equipment = equipment
		self.origin = origin
		self.players = players

	def dispDetails(self):
		print(" Game type: ", self.Type)
		print(" Country of origin: ", self.origin)
		print(" No. of players: ". self.players)
		print(" Prominent players: ", self.legends)

class T20(Cricket):

	def __init__(overs = 20):
		Cricket.__init__(self, overs, equipment, origin, players)

	def dispDetails(self):
		print(" No. of overs: ", self.overs)

class ODI(Cricket):

	def __init__(overs = 50):
		Cricket.__init__(self, overs, equipment, origin, players)

	def dispDetails(self):
		print(" No. of overs: ", self.overs)


class Chess(Sports):

	def __init__(self, time, equipment = ['board', 'pieces', 'timer'], origin = "India", players = 2):
		Sports.__init__(self, Type = "Indoors")
		self.time = time
		self.equipment = equipment
		self.origin = origin
		self.players = players

	def dispDetails(self):
		print(" Game type: ", self.Type)
		print(" Country of origin: ", self.origin)
		print(" No. of players: ", self.players)
		print(" Prominent players: ", self.legends)

class Blitz(Chess):
	def __init__(time = "15-30 min"):
		Chess.__init__(self, time, equipment, origin, players)

	def dispDetails(self):
		print(" Time: ", self.time)

class Lightning(Chess):
	def __init__(time = "less than 15 min"):
		Chess.__init__(self, time, equipment, origin, players)

	def dispDetails(self):
		print(" Time: ", self.time)



ch = 0
ich = 0
och = 0
while ch != 3:
	print(" 1. Chess \n 2. Cricket \n 3. Exit")
	ch = int(input())
	
	if ch == 1:
		while ich != 4:
			Chess.dispDetails()
			Chess.dispLegends()
			print(" 1. Blitz \n 2. Lightning \n 3. Add Legend \n 4. Exit")
			ich = int(input())
			if ich == 1: Blitz.dispDetails()
			if ich == 2: Lightning.dispDetails()
			if ich == 3: Chess.addLegends()
			if ich == 4: break
				
	if ch == 2:
		while och != 4:
			Cricket.dispDetails()
			Cricket.dispLegends()
			print(" 1. ODI \n 2. T20 \n 3. Add Legend \n 4. Exit")
			och = int(input())
			if och == 1: ODI.dispDetails()
			if och == 2: T20.dispDetails()
			if och == 3: Cricket.addLegends()
			if och == 4: break

	if ch == 3:
		break