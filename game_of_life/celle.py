class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0

    
    def sett_doed(self):
        self._status = "doed"

    def sett_levende(self):
        self._status = "levende"

    def er_levende(self):
        if self._status == "levende":
            return True
        else:
            return False

    def hent_status_tegn(self):
        if self.er_levende():
            return "O"
        else:
            return "."

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)


    def tell_levende_naboer(self):
        antall = 0
        for nabo in self._naboer:
            if nabo.er_levende():
                antall += 1
        self._ant_levende_naboer = antall



    def oppdater_status(self):
        if self.er_levende():
            if self._ant_levende_naboer < 2 or self._ant_levende_naboer > 3 :
                self._status = "doed"
        else: 
            if self._ant_levende_naboer == 3:
                self._status = "levende"
          
            