

class InputValidator():
    def __init__(self):
        pass

    def validate(self, reference_list):
        if "" in reference_list:
            raise ValueError("Jokin vaadituista tiedoista puuttuu")
        try:
            reference_list[2] = int(reference_list[2])
        except ValueError as exc:
            raise ValueError("Vuosi ei ollut kokonaisluku") from exc
        return reference_list
