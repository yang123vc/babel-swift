class OCClass:
    def __init__(self, name):
        self.name = name
        self.properties = []


class OCProperty:
    def __init__(self, ocClass, identifier):
        self.ocClass = ocClass
        self.identifier = identifier
