from entities.reference import Reference

class ReferenceService:
    def __init__(self, book_repo, validator):
        self.book_repo = book_repo
        self.validator = validator

    def add_reference(self, data) -> bool:
        try:
            fixed_data = self.validator.validate(data)
            self.book_repo.add_to_table(fixed_data)
            return True
        except Exception:
            return False

    def _create_reference_object(
        self,
        author: str,
        title: str,
        year: int,
        publisher: str,
        bib_key: str,
        tag: str
    ) -> Reference:
        return Reference(author, title, year, publisher, bib_key, tag)

    def _format_references_data_to_objects(self, data):
        ref_objects = map(
            lambda ref: self._create_reference_object(
                ref[1], ref[2], ref[3], ref[4], ref[5], ref[6]
            ), data
        )
        return list(ref_objects)

    def get_all_references(self):
        data = self.book_repo.get_data()
        return self._format_references_data_to_objects(data)

    def get_references_by_tag(self, tag:str):
        data = self.book_repo.get_data_by_tag(tag)
        return self._format_references_data_to_objects(data)

    def delete_reference(self, key):
        self.book_repo.delete_from_table(key)

    def ref_before_delete(self, key):
        self.book_repo.ref_to_delete(key)
