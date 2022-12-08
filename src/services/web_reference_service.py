from entities.web_reference import WebReference


class WebReferenceService:
    def __init__(self, repo, validator):
        self.repo = repo
        self.validator = validator

    def add_reference(self, data) -> bool:
        try:
            fixed_data = self.validator.validate(data)
            self.repo.add_to_table(fixed_data)
            return True
        except Exception:
            return False

    def _create_reference_object(
        self,
        author: str,
        title: str,
        year: int,
        publisher: str,
        bib_key: str
    ) -> WebReference:
        return WebReference(author, title, year, publisher, bib_key)

    def get_all_references(self):
        refs = self.repo.get_data()
        ref_objects = map(
            lambda ref: self._create_reference_object(
                ref[1], ref[2], ref[3], ref[4], ref[5]
            ), refs
        )
        return list(ref_objects)

    def delete_reference(self, key):
        self.repo.delete_from_table(key)

    def ref_before_delete(self, key):
        self.repo.ref_to_delete(key)
