class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        return self.books[key]

    def by_author(self, author):
        matches = []
        for book in self.books:
            if book.author == author:
                matches.append(book)

        if not matches:
            raise KeyError('Author does not exist')

        return matches

    @property
    def titles(self):
        titles = []
        for book in self.books:
            titles.append(book.title)
        if not titles:
            raise KeyError('Title does not exist')

        return titles

    @property
    def authors(self):
        authors = []
        for book in self.books:
            if book.author not in authors:
                authors.append(book.author)

        return authors

    def union(self, other):
        books = []
        for book in self.books:
            if book not in books:
                books.append(book)

        for book in other.books:
            if book not in books:
                books.append(book)

        return Library(books)
