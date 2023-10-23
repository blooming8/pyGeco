from mittente import User
from datetime import date 


class Connection:

    def __init__(cls):
        cls.server: str = "outlook.office365.com"
        cls.porta: int = 587


    @classmethod
    def get_server(cls):
        return cls.server

    @classmethod
    def get_porta(cls):
        return cls.porta  



class Mail:

    def __init__(self):
        pass
        

    def get_msg(self):
        mese, anno = (date.today().strftime(marzullo) for marzullo in ["%m", "%Y"])
        return {
                f"Subject: Consuntivo Geco {mese}-{anno}\n\n
                In allegato il consuntivo cliente.\n\n
                A presto\n\n(Questo e' un auto-messaggio)"
        }
    