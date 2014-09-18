#linkedlist.py
class List:
	class Node:
	
		def __init__(self, feild = None, className = None, next = None, prev = None, ):
			self.feild = feild
			self.className = className
			self.next = next
			self.prev = prev

		def getFeild(self):
			return str(self.feild)
		def getClassName(self):
			return str(self.className) 

		def setNext(self, next):
			self.next = next

		def getNext(self): 
			return self.next

		def getPrev(self):
			return self.prev

		def setPrev(self, prev):
			self.prev = prev

	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, feild, className):
		temp = self.Node(feild, className)
		
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
		with open(fileName, 'r') as inFile:
			for line in inFile:
				feild, className = str(line.split(','))
				self.append(feild, className)

	def search(self, item):
		temp = self.head
		lowItem = item.lower()#uniformitity for comparison

		while temp.getNext() != None:
			data = temp.getClassName().lower()#uniformitity for comparison
			if data == lowItem:
				break
			temp = temp.getNext()
		data = temp.getClassName().lower()

		#Fixs off by one error and returns to result of the search
		if data == lowItem:
			print "Found, " + temp.getClassName()
		else:
			print str(item) + ", Not Found"

	def __str__(self):

		strBuffer = "[ "
		temp = self.head
		count = 0
		
		while temp.getNext() != None:
			#print temp.getClassName()
			strBuffer += temp.getClassName() + ", "
			count += 1
			if count % 20 == 0:
				strBuffer = strBuffer[:-1] + '\n'  
			temp = temp.getNext()
		
		strBuffer +=  (temp.getClassName() + ' ]') #off by one fix
	
		return strBuffer
