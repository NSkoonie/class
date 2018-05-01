#bhw2
#Test Library
#Noah Schoonover

import book
import lib

mylib = lib.Library()
book1 = book.Book("Python Programming", 2019, ["John Doe", "Jane Doe"])
book2 = book.Book("C Programming", 2012, ["Jack Jackson"])
book3 = book.Book("Functional Programming", 2012, ["Jack Jackson"])
mylib.add(book1)
mylib.add(book2)
mylib.add(book3)
print(mylib)
