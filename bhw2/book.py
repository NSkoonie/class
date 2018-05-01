#bhw2
#Library Class
#Noah Schoonover

class Book(object):
    def __init__(self, title="unknown", year_published=2000, authors=[], edition=1, publisher='unknown'):
        self.__title = title # this is a private instance variable
        self.__year = year_published
        self.__authors = authors
        self.__edition = edition
        self.__publisher = publisher

    #getter methods

    def getTitle(self):
        return self.__title

    def getYear(self):
        return self.__year

    def getAuthors(self):
        return self.__authors

    def getEdition(self):
        return self.__getEdition

    def getPublisher(self):
        return self.__publisher

    #setter methods

    def setTitle(self, title):
        self.__title = title

    def setYear(self, year):
        self.__year = year

    def setAuthors(self, authors):
        self.__authors = authors

    def setEdition(self, edition):
        self.__edition = edition

    def setPublisher(self, publisher):
        self.__publisher = publisher

    #print method

    def __str__(self):
        authors = self.__authors[0]
        for i in range(1, len(self.__authors)):
            authors += " and " + self.__authors[i]

        return (authors.strip() + ", " + self.__title + ", " +  str(self.__year))
