class Reference:
    def __init__(self, author:str, title:str, year:int, publisher:str, bib_key:str):
        self.__author = author
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__bib_key = bib_key

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @property
    def publisher(self):
        return self.__publisher

    @property
    def bib_key(self):
        return self.__bib_key

    def __str__(self) -> str:
        return f"{self.__author}: {self.__title} ({self.__year}), {self.__publisher}. \
            BibTeX key: {self.__bib_key}"
