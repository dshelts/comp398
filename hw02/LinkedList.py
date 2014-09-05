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
	
		def __init__(self, cargo = None, next = None, prev = None):
			""" Contructs a basic node class.

				Args:
					Cargo = data, next = next, prev = previous
				returns:
					None
			"""
			self.car = cargo
			self.next = next
			self.prev = prev

		def getData(self):
			""" Gets the data from the node.
				
				Args:
					self also access within its own object
				Returns:
					The cargo from the node as a string
			"""
			return str(self.car)

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

	def append(self, cargo):
		""" Creates and appends a node to the List.

			Args: 
				self allows access to the List as Node class methods,  cargo data for the node
			Returns:
				Nothing. 
		"""
		temp = self.Node(cargo)
		
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
				self.append(line.strip())#strip the \n 

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
			print "Found, " + temp.getData()
		else:
			print str(item) + ", Not Found"

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
		
		while temp.getNext() != None:
			#print temp.getData()
			strBuffer += temp.getData() + ", "
			count += 1
			if count % 20 == 0:
				strBuffer = strBuffer[:-1] + '\n'  
			temp = temp.getNext()
		
		strBuffer +=  (temp.getData() + ' ]') #off by one fix
	
		return strBuffer

