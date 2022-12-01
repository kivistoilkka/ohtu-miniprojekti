from entities.reference import Reference


class ReferenceService:
    def __init__(self, repo):
        self.repo = repo

    def add_reference(self, data) -> bool:
        try:
            self.repo.add_to_table(data)
            return True
        except:
            return False

    def _create_reference_object(
        self,
        author: str,
        title: str,
        year: int,
        publisher: str,
        bib_key: str
    ) -> Reference:
        return Reference(author, title, year, publisher, bib_key)

    def get_all_references(self):
        refs = self.repo.get_data()
        ref_objects = map(
            lambda ref: self._create_reference_object(
                ref[1], ref[2], ref[3], ref[4], ref[5]
            ), refs
        )
        return list(ref_objects)
