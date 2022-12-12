from enum import Enum
from entities.book_reference import BookReference
from entities.web_reference import WebReference

class ReferenceType(Enum):
    Book = "book",
    Website = "website"

class ReferenceService:
    def __init__(self, book_repo, web_repo, validator):
        self.book_repo = book_repo
        self.web_repo = web_repo
        self.validator = validator

    def add_reference(self, data, ref_type) -> bool:
        try:
            fixed_data = self.validator.validate(data)
            if ref_type == ReferenceType.Book:
                self.book_repo.add_to_table(fixed_data)
                return True
            elif ref_type == ReferenceType.Website:
                self.web_repo.add_to_table(fixed_data)
                return True
            return False
        except Exception:
            return False

    def _create_book_reference_object(
        self,
        author: str,
        title: str,
        year: int,
        publisher: str,
        bib_key: str,
        tag: str
    ) -> BookReference:
        return BookReference(author, title, year, publisher, bib_key, tag)

    def _create_web_reference_object(
        self,
        author: str,
        title: str,
        year: int,
        url: str,
        bib_key: str,
        tag
    ) -> WebReference:
        return WebReference(author, title, year, url, bib_key, tag)


    def _format_references_data_to_object_lists_in_dict(self, book_data, web_data):
        book_ref_objects = map(
            lambda ref: self._create_book_reference_object(
                ref[1], ref[2], ref[3], ref[4], ref[5], ref[6]
            ), book_data
        )
        web_ref_objects = map(
            lambda ref: self._create_web_reference_object(
                ref[1], ref[2], ref[3], ref[4], ref[5], ref[6]
            ), web_data
        )
        return {
            "book_references": list(book_ref_objects),
            "web_references": list(web_ref_objects)
        }

    def get_all_references(self):
        book_data = self.book_repo.get_data()
        web_data = self.web_repo.get_data()
        return self._format_references_data_to_object_lists_in_dict(book_data, web_data)

    def get_references_by_tag(self, tag:str):
        book_data = self.book_repo.get_data_by_tag(tag)
        web_data = self.web_repo.get_data_by_tag(tag)
        return self._format_references_data_to_object_lists_in_dict(book_data, web_data)

    def delete_reference(self, bib_key, ref_type) -> bool:
        if ref_type == ReferenceType.Book:
            self.book_repo.delete_from_table(bib_key)
            return True
        elif ref_type == ReferenceType.Website:
            self.web_repo.delete_from_table(bib_key)
            return True
        return False

    def get_reference(self, bib_key, ref_type):
        if ref_type == ReferenceType.Book:
            return self.book_repo.get_reference(bib_key)
        elif ref_type == ReferenceType.Website:
            return self.web_repo.get_reference(bib_key)
        raise ValueError("Virheellinen viitteen tyyppi")
