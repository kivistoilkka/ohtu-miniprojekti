from reference_reader import ReferenceReader
class UI:    
    def __init__(self, app):
        self.app = app
        

    
    def run(self):

        while(True):
            options = int(input("Mitä haluat tehdä?\n Luoda tiedosto, paina 1\n Tarkastella luotuja viitteitä, paina 2\n Lisää uusi viite, paina 3 \n Sulje ohjelma, paina 4\n"))

            if options == 1:
                self.create_file()
        
            elif options == 2:
                self.view_ref()
        
            elif options == 3:
                self.add_ref()
            
            elif options == 4:
                break

        
    def create_file(self):
        pass

    def view_ref(self):
        
        data = self.app.book_reference_repo.get_data(self.app.connection)
        
        for ref in data:
            author = ref[1]
            title = ref[2]
            publisher = ref[4]

            if len(author) > 15:
                author = ref[1][:11] + "..."
            if len(title) > 15:
                title = ref[2][:11] + "..."
            if len(publisher) > 15:
                publisher = ref[4][:11] + "..."

            print(f"Author: {author:15} | Title: {title:15} | Year: {ref[3]:4} | Publisher: {publisher:15} | Key: {ref[5]} \n")
    
    def add_ref(self):
        selection = input("Haluatko luoda uuden tietokannan (kyllä/ei)? ")
        if selection == "kyllä":
            self.app.db.create_tables(self.app.connection)
        
        ref_list = self.app.reference_reader.ref_reader()

        self.app.book_reference_repo.add_to_table(self.app.connection,ref_list)
