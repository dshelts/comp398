#HW1 Web App Linked list
#Andrew Shelton
#pre-style guide
class Node:
	def __init__(self, cargo = None, next = None, prev = None):
		self.car = cargo
		self.next = next
		self.prev = prev

	def getData(self):
		return str(self.car)
	
	def setNext(self, next):
		self.next = next
	
	def getNext(self): 
		return self.next

	def setPrev(self, prev):
		self.prev = prev


class List:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def isEmpty(self):
		return self.head == None

	def append(self, cargo):

		temp = Node(cargo)
		
		if self.head == None:
			self.head = temp
			self.tail = temp
		
		else:
			temp.setPrev(self.tail) # tail <-prev-(TEMP)-next->None
			self.tail.setNext(temp) #(Node)<-prev-(Tail)-next->(temp)
			self.tail = temp #(temp) == (tail)

	def populate(self, fileName): #assuming a newline seperated
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
		if data == lowItem:
			print "Found, " + temp.getData()
		else:
			print str(item) + ", Not Found"

	def __str__(self):
		strBuffer = "["
		temp = self.head
		count = 0

		while temp.getNext() != None:
			#print temp.getData()
			strBuffer += temp.getData() + ", "
			count += 1
			if count%20 ==0:
				strBuffer = strBuffer[:-1] + '\n'  
			temp = temp.getNext()
		
		strBuffer += (temp.getData() + ']') #off by one fix
			
		return strBuffer

