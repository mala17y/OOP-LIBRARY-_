class Library:                       
    def __init__(self, book_list, name):
        self.books_list = book_list
        self.name = name
        self.lend_books = {}

    def display_books(self):
        print(f"WE HAVE FOLLOWING BOOKS IN OUR LIBRARY: {self.name}")
        for book in self.books_list:
            print(book)

    def lend_book(self, user, lend_book):                    
        if lend_book not in self.lend_books:
            self.lend_books[lend_book] = user
            print("YOUR LENDER-BOOK DATABASE HAS BEEN UPDATED! YOU CAN TAKE YOUR BOOK NOW!")
        else:
            print(f"BOOK IS ALREADY BEING USED BY: {self.lend_books[lend_book]}")

    def add_book(self, add_book):
        self.books_list.append(add_book)
        print("BOOK HAS BEEN ADDED TO THE BOOK LIST")

    def return_book(self, return_book):
        if return_book in self.lend_books:
            del self.lend_books[return_book]
            print("BOOK HAS BEEN RETURNED")
        else:
            print("THIS BOOK WAS NOT LENT OUT")
        
        if return_book in self.books_list:
            print("BOOK IS ALREADY IN THE LIBRARY")
        else:
            self.books_list.append(return_book)
            print("BOOK HAS BEEN ADDED TO THE BOOK LIST")

if __name__ == '__main__':
    malaika = Library(['Python', 'ML', 'ANN', 'DL', 'Computer Vision'], 'Learn with Malaika') 
    
    while True:
        print(f"WELCOME TO {malaika.name} library. Enter your choices:")
        print("1: Display books")
        print("2: Lend a book")
        print("3: Add a book to the library")
        print("4: Return a book")

        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            malaika.display_books()
        elif user_choice == 2:
            lend_book = input("ENTER THE NAME OF THE BOOK YOU WANT TO LEND: ")
            user = input("ENTER YOUR NAME: ")
            malaika.lend_book(user, lend_book)
        elif user_choice == 3:
            add_book = input("ENTER THE NAME OF THE BOOK YOU WANT TO ADD: ")
            malaika.add_book(add_book)
        elif user_choice == 4:
            return_book = input("ENTER THE NAME OF THE BOOK YOU WANT TO RETURN: ")
            malaika.return_book(return_book)
        else:
            print("ENTER A VALID CHOICE NUMBER")

        user_input = input("PRESS Q TO quit and C to continue: ").lower()
        if user_input == 'q':
            break
        elif user_input == 'c':
            continue
