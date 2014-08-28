import LinkedList 

def main():
	myFile = 'CardList.txt'
	
	myList = LinkedList.List()
	myList.populate(myFile)
	
	#test suite
	myList.search("1996 World Champion") #first item in the list
	myList.search("Zzzyxas's Abyss")	#last item in the list 
	myList.search("quacker") #not in list
	print myList
	#test Suite end



if __name__ == '__main__':
	main()