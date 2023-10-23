class Connection:

    def __init__(cls):
        cls.server = "outlook.office365.com"
        cls.porta = 587


    @classmethod
    def get_server(cls):
        return cls.server


    @classmethod
    def get_porta(cls):
        return cls.porta  
