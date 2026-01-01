from celle import Celle
from random import randint

class Rutenett:
    def __init__(self, ant_rader, ant_kolonner):
        self._ant_rader = ant_rader
        self._ant_kolonner = ant_kolonner
        self._rutenett = self._lag_tomt_rutenett() 


    def _lag_tom_rad(self):
        lst = []
        for i in range((self._ant_kolonner)):
            lst.append(None)
        return lst


    def _lag_tomt_rutenett(self):
        rutenett = []
        for _ in range(self._ant_rader):  # Itererer ant_rader ganger
            rutenett.append(self._lag_tom_rad())  # Legger til en tom rad
        return rutenett
    

    def  lag_celle(self):
        a = Celle()
        if randint(0,2) == 0:
            a.sett_levende()
        return a


    def fyll_med_tilfeldige_celler(self):
        for rad in range(len(self._rutenett)):
            for kol in range(len(self._rutenett[rad])):
                #print(rad,kol)
                self._rutenett[rad][kol] = self.lag_celle()

    def hent_celle(self, rad, kol):
        # Sjekk at rad og kol ligger innenfor gyldige grenser
        if 0 <= rad < self._ant_rader and 0 <= kol < self._ant_kolonner:
            return self._rutenett[rad][kol]
        return None


    def tegn_rutenett(self):
 
        for rad in range(len(self._rutenett)):
            print()
            for kol in range(len(self._rutenett[rad])):
                print(self._rutenett[rad][kol].hent_status_tegn(), end="")
        for i in range(10):
            print()


    def _sett_naboer(self,rad,kol):
        naboer = []
        for r in range(rad - 1, rad + 2):  # Gå gjennom rader fra rad-1 til rad+1
            for k in range(kol - 1, kol + 2):  # Gå gjennom kolonner fra kol-1 til kol+1
                if r == rad and k == kol:
                    continue  # Ikke legg til cellen selv som nabo
                nabo = self.hent_celle(r, k)  # Hent cellen ved (r, k)
                if nabo is not None:  # Sjekk at naboen eksisterer
                    naboer.append(nabo)
        # Sett naboer for cellen
        celle = self.hent_celle(rad, kol)
        if celle is not None:
            for nabo in naboer:
                celle.legg_til_nabo(nabo) # Antatt metode for å sette naboer

        

        
    def koble_celler(self):
        for rad in range(len(self._rutenett)):
            for kol in range(len(self._rutenett[rad])):
                self._sett_naboer(rad, kol)

    
    def hent_alle_celler(self):
        lst = []
        for rad in range(len(self._rutenett)):
            for kol in range(len(self._rutenett[rad])):
                lst.append(self.hent_celle(rad,kol))

        return lst
    
    def antall_levende(self):
        teller = 0
        for celle in self.hent_alle_celler():
            if celle.er_levende():
                teller += 1

        return teller





