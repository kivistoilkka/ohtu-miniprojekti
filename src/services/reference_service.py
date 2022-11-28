from repositories.book_reference_repo import BookReference

class ReferenceService:
    def __init__(self, repo): #TODO: validator
        self.repo = repo

    def add_reference(
        self,
        author:str,
        title:str,
        year:int,
        publisher:str,
        bib_key:str
    ) -> bool:
        try:
            self.repo.add_to_table([author, title, year, publisher, bib_key])
            return True
        except:
            return False