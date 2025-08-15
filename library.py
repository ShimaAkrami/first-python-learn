class library():
    def __init__(self):
        self.books=[]
                  
    def add_book(self,title,author):
        self.books.append({"title":title,"auther":auther})
        print(f"{title} book added.") 

    def remove_book(self,title):
        for book in self.books:
            if book["tilte"]==tilte:
                self.books.remove(book)
                print(f"{title} book deleted.")
        print(f"{title} book is not found.")

    def search_book(self,title):
        for book in self.books:
            if book["title"]==title:
                print(f"{title} book who written by {auther} is found.")
        print(f"this {title} book don't exist.")
    
    def show_book(self):
        if not self.books:
            print("there is no book here")
        else:
            print ("book lists:/n")
            for book in self.books:
                print("-{book[title]} book writhen by {book[auther]}")





        