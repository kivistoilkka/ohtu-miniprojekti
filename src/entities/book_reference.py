class BookReference:
    def __init__(self, author: str, title: str, year: int, publisher: str, bib_key: str, tag: str):
        self.__author = author
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__bib_key = bib_key
        self.__tag = tag

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
    
    def text_to_bold(self, text):
        return "\033[1m" + text + "\033[0m"

    @property
    def tag(self):
        return self.__tag

    def __str__(self) -> str:

        author = self.__author
        title = self.__title
        publisher = self.__publisher

        if len(author) > 15:
                author = author[:11] + "..."
        if len(title) > 15:
                title = title[:11] + "..."
        if len(publisher) > 15:
                publisher = publisher[:11] + "..."

        return f"\n {self.text_to_bold('Author')}: {self.__author:15} | {self.text_to_bold('Title')}: {self.__title:15} | {self.text_to_bold('year')}: {self.__year:4} \
    | {self.text_to_bold('Publisher')}: {self.__publisher:15} | {self.text_to_bold('key')}: {self.__bib_key} | {self.text_to_bold('tag')}: {self.__tag} \n"
                    
