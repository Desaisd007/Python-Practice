# here we write class for book details

class BookDetails:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print('\n name of book : ',self.title,'\n','name of author :',self.author,'\n','price : ',self.price)

B1=BookDetails('hemlet','Shakespeare',499)
B1.show_details()
