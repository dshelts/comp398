import LinkedList 

def main():
	myFile = 'CardList.txt'
	
	myList = LinkedList.List()
	myList.populate(myFile)
	
	#test suite
	myList.search("1996 World Champion") #KNOWN first item in the list
	myList.search("Zzzyxas's Abyss")	 #KNOWN last item in the list 
	myList.search("yOu Won'T Find ME!")  #KNOWN not in list
	print myList
	#test Suite end



if __name__ == '__main__':
	main()