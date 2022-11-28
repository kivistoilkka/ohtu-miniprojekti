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
        print(data)
    
    def add_ref(self):
        selection = input("Haluatko luoda uuden tietokannan (kyllä/ei)? ")
        if selection == "kyllä":
            self.app.db.create_tables(self.app.connection)
        
        ref_list = self.app.reference_reader.ref_reader()

        self.app.book_reference_repo.add_to_table(self.app.connection,ref_list)
