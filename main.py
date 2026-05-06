class Book:
    def __init__(self, title, author, pages, code):
        self.title = title
        self.author = author
        self._pages = pages
        self.__code = code

    def read(self, pages):
        print(f"Reading {pages} pages")

    def bookmark(self, page):
        print(f"Bookmark at {page}")

    def info(self):
        print(self.title, self.author)
