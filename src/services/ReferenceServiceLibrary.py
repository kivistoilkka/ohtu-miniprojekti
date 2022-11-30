from reference_service import ReferenceService

class ReferenceServiceLibrary:
    def __init__(self) -> None:
        self.referenceservice = ReferenceService()
    
    def add_reference(self):
        author = "testi author"
        title = "testi title"
        year= 0000
        publ = "testi publisher"
        key = "abc"

        success = self.referenceservice.add_reference(author, title, year, publ, key)
        return success

    def add_existing_reference(self):
        pass

    