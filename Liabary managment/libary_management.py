class libary:
    lendDetail = {}
    user = []

    def __init__(self, Books, Name):
        self.books = Books
        self.avalabelBook = self.books[:]
        self.libName = Name

    def DisplayBook(self):
        print("\n\n\t\t  books")
        print("--------------------------------------------")
        for i in range(len(self.books)):
            print("\t\t", i+1, ")", self.books[i])
        print("--------------------------------------------")

    def DisplayAvalabelBook(self):
        print("\n\n\t\t  books")
        print("--------------------------------------------")
        for i in range(len(self.avalabelBook)):
            print("\t\t", i+1, ")", self.avalabelBook[i])
        print("--------------------------------------------")

    def LendBook(self):
        lendBookName = ""
        print("\n\n--------------------------------------------")
        print("\n\n\tEnter Your Name : ", end="")
        lendName = input()
        if lendName in self.user:
            print("\n\tOne user can take only one book")
            return
        print("\n\tEnter Book Name : ", end="")
        lendBookName = input()
        if lendBookName not in self.avalabelBook:
            print("\n\t***** Book is not available *****")
          
            return
        self.user.append(lendName)
        self.avalabelBook.remove(lendBookName)
        self.lendDetail[lendName] = lendBookName
        print(
            f"\nbook '{lendBookName}' is lended by '{lendName}' sucessfully !!")
        print("--------------------------------------------")

    def AddBook(self):
        print("\n--------------------------------------------")
        print("\n\tEnter book name : ", end="")
        a = input()
        self.books.append(a)
        self.avalabelBook.append(a)
        print("\n\tBook added sucessfully !!")
        print("\n\tThank You!!!! For Supporting Us !!")
        print("--------------------------------------------")

    def ReturnBook(self):
        print("\n--------------------------------------------")
        print("\tPlease enter your name :", end="")
        Name = input()
        self.user.remove(Name)
        self.avalabelBook.append(self.lendDetail.get(Name))
        print(
            f"\n\tBook '{self.lendDetail.get(Name)}' return success fully !!")
        del self.lendDetail[Name]
        print("--------------------------------------------")

    def displaylendBook(self):

        print("\n\n\t----------------------------------------")
        print("\t\t{:<18} {:<18}".format('Book Name', 'Lender'))
        print("\t----------------------------------------")

        for key, value in self.lendDetail.items():
            name = value

            print("\t\t{:<18} {:<18}".format(name, key))


if __name__ == '__main__':

    print("\n\n---------------------------------------------------------")
    namelib = input("\n\tEnter your libary name here => ")
    numberOfBook = int(input("\n\tEnter Number of Books : "))
    booksList = []
    print()

    for i in range(numberOfBook):
        print(f"\t\tEnter book number {i+1} for libary : ", end="")
        temp = input()
        booksList.append(temp)
    l1 = libary(booksList, namelib)

    while 1:

        print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n\n")
        print("what you want to do ? kindly Enter option from here\n")
        print("Enter 1 for Display Books ")
        print("Enter 2 for avalabel Book list ")
        print("Enter 3 for Lend Book")
        print("Enter 4 for Return Book")
        print("Enter 5 for Display lend list")
        print("Enter 6 for Add book / Donate Book")

        choice = int(input("\n\tEnter your choice here => "))

        if choice == 1:
            l1.DisplayBook()

        elif choice == 2:
            l1.DisplayAvalabelBook()

        elif choice == 3:
            l1.LendBook()

        elif choice == 4:
            l1.ReturnBook()

        elif choice == 5:
            l1.displaylendBook()

        elif choice == 6:
            l1.AddBook()

        else:
            print("Enter valid choice : ")
