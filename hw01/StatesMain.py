#StatesMain.py
import LinkedList
#test on a different file

def main():

	myFile = 'States.csv'
	myList = LinkedList.List()
	myList.populate(myFile) 
	
	print myList




if __name__ == '__main__':
	main()