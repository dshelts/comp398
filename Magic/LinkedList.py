#HW1 Web App Linked list
#Andrew Shelton
"""Using google's style guide"""

class List:
	"""Contructs a Linked List an empty List.

	Contains a private Node class to be used by the List class.

	Args:
		None.
	Returns:
		Nothing.

	"""
	
	class Node:
	
		def __init__(self, cardName = None, cost = None, next = None, prev = None, ):
			""" Contructs a basic node class.

				Args:
					Cargo = data, next = next, prev = previous
				returns:
					None
			"""
			self.car = cardName
			self.cost = cost
			self.next = next
			self.prev = prev

		def getData(self):
			""" Gets the data from the node.
				
				Args:
					self also access within its own object
				Returns:
					The cargo and cost from the node as a string
			"""
			return str(self.car) 
		def getCost(self):
			return str(self.cost)

		def setNext(self, next):
			""" Sets the next link for the node.

				Args:
					next an instance of a node class.
				Returns:
					Nothing.
			"""
			self.next = next

		def getNext(self): 
			""" Returns the node asigned to next.

				Args:
					self allows access its own object
				Returns:
					the node objected assigned to next
			"""
			return self.next

		def getPrev(self):
			""" Sets the prev link for the node.

				Args:
					prev an instance of a node class.
				Returns:
					Nothing.
				Currently unused.
			"""
			return self.prev

		def setPrev(self, prev):
			""" Sets the prev link for the node.

				Args:
					prev an instance of a node class.
				Returns:
					Nothing.
			"""
			self.prev = prev

	def __init__(self):
		""" Contrusts an empty list.

			Args: 
				head = Null until populated, tail = Null until populated
			Returns:
				Nothing. 
		"""
		self.head = None
		self.tail = None

	def append(self, cargo, cost):
		""" Creates and appends a node to the List.

			Args: 
				self allows access to the List as Node class methods,  cargo data for the node
			Returns:
				Nothing. 
		"""
		temp = self.Node(cargo, cost)
		
		if self.head == None:
			#if list is empty
			self.head = temp
			self.tail = temp
		
		else:
			#set new nodes previous to current tail
			#set current tail's next to new node
			#set the tail of list to new node
			temp.setPrev(self.tail) 
			self.tail.setNext(temp) 
			self.tail = temp 

	def populate(self, fileName): #assuming a newline seperated
		""" Fills the list with information from a File, Assumes new line seperated.

			Args:
				self, and fileName.
			returns:
				nothing.
		"""
		with open(fileName, 'r') as inFile:
			for line in inFile:
				name, cost = line.split() 
				self.append(name.strip(), cost.strip())#strip the \n 

	def search(self, item):
		temp = self.head
		lowItem = item.lower()#uniformitity for comparison

		while temp.getNext() != None:
			data = temp.getData().lower()#uniformitity for comparison
			if data == lowItem:
				break
			temp = temp.getNext()
		data = temp.getData().lower()

		#Fixs off by one error and returns to result of the search
		if data == lowItem:
			print "Found, " + temp.getData() + " " + temp.getCost()
		else:
			print str(item) + ", Not Found"
	
	def allWithColorX(self, color):
		colorList = List()
		color = color[0:]
		temp = self.head
		lowColor = color.lower()
		if temp == None:
			return "List to search is empty, Please run LinkedList.List().populate(<valid file>)"

		while temp.getData() != None :
			cost = temp.getCost().lower()
			length = len(cost)
			for i in xrange (0, length):
				if color == cost[i-1 : i]:
					colorList.append(temp.getData(), temp.getCost())
					break
				else:
					pass
			temp = temp.getNext()
		return colorList

	def __str__(self):
		""" allows the print function to work on this object.

			Args: 
				self
			Returns:
				Nothing. 
		"""
		strBuffer = "[ "
		temp = self.head
		count = 0
		
		while temp.getData() != None:
			#print temp.getData()
			strBuffer += temp.getData() + ", "
			count += 1
			if count % 20 == 0:
				strBuffer = strBuffer[:-1] + '\n'  
			temp = temp.getNext()
		
		strBuffer +=  ' ]'
	
		return strBuffer










		
