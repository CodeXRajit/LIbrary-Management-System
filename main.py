import json
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,title,author):
        book=Book(title,author)
        self.books.append(book)
        self.save_books
        
    def list_book(self):
       
       return [f"{book.title}  by  {book.author} "for book in self.books ]
    def remove_book(self,book):
         if book in self.books:
            self.books.remove(book)
         else :
            print("book not found !")
    def save_books(self):
        with open("books.json", "w") as file:
            json.dump([{"title": b.title, "author": b.author, "is_borrowed": b.is_borrowed} for b in self.books], file)



class Book:
   def __init__(self,title,author):
      self.title=title
      self.author= author 
      self.is_borrowed=False
      self.returned=False
   def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return "the book is borrowed"
        return "the book has already been borrowed"
   def return_book(self):
      if not self.returned:
         self.returned=True
         return "the book has been returned"
      return "the book has already been returned"

       

def main():
    library = Library() 

    print("""
        1. Add a book
        2. View available books
        3. Exit
        """)
    while True:
      user_input = input("> ")

      if user_input == "1":
               title = input("Title of the book: ")
               author = input("Author of the book: ")
               library.add_book(title,author)
      elif user_input=="2":
         print (library.list_book())

if __name__=="__main__":
    main()
