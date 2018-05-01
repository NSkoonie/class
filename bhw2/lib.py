#bhw2
#Library Class
#Noah Schoonover

import book

class Library(object):
    def __init__(self, books=[]):
        self.__books = books
        self.__numBooks = len(books)

    def add(self, book):
        self.__books.append(book)

    def rm(self, book):
        self.__books.remove(book)

    def getNumBooks(self):
        return self.__numBooks

    def __str__(self):
        books = "\n\t*** Books in your library ***\n"
        for i in  range(len(self.__books)):
            books += self.__books[i].__str__() + "\n"

        books += "\n****************************************\n"
        return (books)
