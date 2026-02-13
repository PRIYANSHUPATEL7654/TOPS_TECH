class Book:

    def __init__(self):
        self.books = {}
    
    def input_books_data(self):
        no_of_books = int(input("How many books data do you want to enter : "))
        for i in range(no_of_books):
            print(f"BOOK {i+1}")
            self.title = input("Enter book name : ")
            self.author = input("Enter author name : ")
            self.price = int(input("Enter price of the book : "))
            self.no_of_pg = int(input("Enter the number of pages in the book : "))
            self.books[self.title] = {"author" : self.author, "price" : self.price, "num_of_pages" : self.no_of_pg}

    def display_books_data(self):
        if not self.books:
            print("No books data available")
        else:
            for title,details in self.books.items():
                print(f"Title : {title}")
                print(f"\tAuthor : {details["author"]}")
                print(f"\tPrice: {details['price']}")
                print(f"\tPages: {details['num_of_pages']}\n")

obj = Book()

while True:
    choice = int(input("1) Input book data\n2) Show book data\n3) Exit\nEnter your choice from above options : "))
    if choice == 1:
        obj.input_books_data()
    elif choice == 2:
        obj.display_books_data()
    else:
        break