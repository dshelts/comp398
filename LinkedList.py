#HW1 Web App Linked list
#Andrew Shelton

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
			temp.setPrev(self.tail) # tail <-prev-(NODE)-next->None
			self.tail.setNext(temp) #(Node)<-prev-(Tail)-next->(temp)
			self.tail = temp #temp is now tail

	def populate(self, fileName): #assuming a newline seperated
		with open(fileName, 'r') as inFile:
			for line in inFile:
				self.append(line.strip())



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

