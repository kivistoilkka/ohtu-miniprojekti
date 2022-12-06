
class StubUI:
    def __init__(self, app, ref_service) -> None:
        self.app = app
        self.reference_service = ref_service
        self.outputs = []

    def sort_data(self, data, sort_key, order):
        if sort_key == "1":
            if order == "1":
                data.sort(key=lambda ref: ref.year, reverse=False)
            if order == "2":
                data.sort(key=lambda ref: ref.year, reverse=True)

        elif sort_key == "2":
            if order == "2":
                data.reverse()
        return data

    def view_ref(self, sort_key, order):

        data = self.reference_service.get_all_references()
        data = self.sort_data(data, sort_key, order)

        for ref in data:
            author = ref.author
            title = ref.title
            publisher = ref.publisher

            if len(author) > 15:
                author = author[:11] + "..."
            if len(title) > 15:
                title = title[:11] + "..."
            if len(publisher) > 15:
                publisher = publisher[:11] + "..."

            self.outputs.append(f"Author: {author:15} | Title: {title:15} | Year: {ref.year:4} \
                | Publisher: {publisher:15} | Key: {ref.bib_key} \n"
                                )

    def add_ref(self, ref_list):
        self.reference_service.add_reference(ref_list)
