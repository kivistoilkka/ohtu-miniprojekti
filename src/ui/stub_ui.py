from services.reference_service import ReferenceType

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

    def view_ref(self, sort_key, order, tag, ref_type):
        if tag != "":
            all_data = self.reference_service.get_references_by_tag(tag)
        else:
            all_data = self.reference_service.get_all_references()
        if ref_type == ReferenceType.Book:
            data = self.sort_data(all_data["book_references"], sort_key, order)
        elif ref_type == ReferenceType.Website:
            data = self.sort_data(all_data["web_references"], sort_key, order)

        for ref in data:
            author = ref.author
            title = ref.title

            if ref_type == ReferenceType.Book:
                publisher_or_url = ref.publisher
            elif ref_type == ReferenceType.Website:
                publisher_or_url = ref.url

            if len(author) > 15:
                author = author[:11] + "..."
            if len(title) > 15:
                title = title[:11] + "..."
            if len(publisher_or_url) > 15:
                publisher_or_url = publisher_or_url[:11] + "..."

            self.outputs.append(f"Author: {author:15} | Title: {title:15} | Year: {ref.year:4} \
                | Publisher: {publisher_or_url:15} | Key: {ref.bib_key} | Tag: {ref.tag}\n"
                                )

    def add_ref(self, ref_list, ref_type_str):
        if ref_type_str == "book_reference":
            self.reference_service.add_reference(ref_list, ReferenceType.Book)
        elif ref_type_str == "web_reference":
            self.reference_service.add_reference(ref_list, ReferenceType.Website)
