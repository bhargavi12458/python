class book:
    def_init_(self,title):
        self.title=title
        def create_book_list():
            return[book("python 101"),book("AI basics"),book("data science")]
        books=create_book_list()
        for b in books:
            print("book title:" b.title)
            
