from datetime import date 
import re
import os 


class Mail:

    def __init__(self):
        pass
        

    def get_oggetto(self):
        mese, anno = (date.today().strftime(marzullo) for marzullo in ["%m", "%Y"])
        return f"Consuntivo Geco {mese}-{anno}"


    def get_corpo(self):
        return "\nIn allegato il consuntivo cliente.\n\nA presto\n\n(Questo e' un auto-messaggio)" 
    

    def get_msg(self):
        return self.get_oggetto() + "\n\n" + self.get_corpo()
    

    def get_file_path(self):  
        return "iOS.pdf"