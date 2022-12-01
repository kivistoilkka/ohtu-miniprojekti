
class StubUI:
    def __init__(self, app, ref_service) -> None:
        self.app = app
        self.reference_service = ref_service
    
    def run(self):
        pass
    
    def add_ref(self, reference:list):
        pass

    def view_ref(self):
        for ref in self.database:
            pass