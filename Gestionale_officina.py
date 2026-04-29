from abc import ABC, abstractmethod
import datetime

anno = datetime.date.today().year
#print(anno)  # Output: 2026 (o l'anno attuale)

class Elettrodomestico(ABC):
    
    # costruttore con attributi privati
    def __init__(self, marca: str, modello:str, anno_acquisto:int, guasto:str):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
    
    # metodo concreto per ritorna descrizione
    def descrizione(self):
        return (
        f" | Classe: {type(self)}"
        f" | Marca: {self.get_marca()}" +
        f" | Modello:{self.get_modello()}" +
        f" | Anno d'acquisto: {self.get_anno_acquisto()}" +
        f" | Guasto: {self.get_guasto()}"
        )

    def stima_costo_base(self):
        return 50
            
    # metodi getter
    def get_marca(self):
        return self.__marca
    
    def get_modello(self):
        return self.__modello
    
    def get_anno_acquisto(self):
        return self.__anno_acquisto
    
    def get_guasto(self):
        return self.__guasto
    
    # metodi setter
    def set_marca(self, nuova_marca):
        self.__marca = nuova_marca
    
    def set_modello(self, nuovo_modello):
        self.__modello = nuovo_modello
    
    def set_anno_acquisto(self, nuovo_anno_acquisto):
        anno = datetime.date.today().year
        # Check per verificare che l'anno di acquisto non sia nel futuro
        if nuovo_anno_acquisto >= anno:
            self.__anno_acquisto = nuovo_anno_acquisto
        else:
            raise ValueError("L'anno di acquisto non può essere nel futuro")
            
    def set_guasto(self, nuovo_guasto):
        self.__guasto = nuovo_guasto
        
        
class Forno(Elettrodomestico):
    
    def __init__(self, marca: str, modello:str, anno_acquisto:int, guasto:str, tipo_alimentazione: str, ha_ventilato:bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.tipo_alimentazione = tipo_alimentazione
        self.ha_ventilato = ha_ventilato
        
    def stima_costo_base(self):
        if self.tipo_alimentazione == 'elettrico':
            if self.ha_ventilato:
                return super().stima_costo_base() + 25
            else:
                return super().stima_costo_base() + 15
        else:
            if self.ha_ventilato:
                return super().stima_costo_base() + 20
            else:
                return super().stima_costo_base() + 10
            
    def descrizione(self):
        return (
            super().descrizione() +
            f" | Tipo alimentazione: {self.tipo_alimentazione}"
            f" | Ventilato: {self.ha_ventilato}"
        )
                
    
f1 = Forno("samsung", "ab1", "2024", "resistenza", "elettrico", True)

print(f1.descrizione())



f2 = Forno("turi", "cd2", "2021", "resistenza", "elettrico", False)

f3 = Forno("cico", "ef3", "2025", "resistenza", "gas", True)

f4 = Forno("canon", "ab1", "2027", "sportello", "gas", False)



class Frigorifero(Elettrodomestico):
    
    def __init__(self, marca: str, modello:str, anno_acquisto:int, guasto:str, litri:int, ha_freezer:bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.litri = litri
        self.ha_freezer = ha_freezer

    def stima_costo_base(self):
        costo_base = super().stima_costo_base()

        if self.litri > 50:
            return costo_base + 30 + (30 if self.ha_freezer else 0)
        elif self.litri > 25:
            return costo_base + 10 + (30 if self.ha_freezer else 0)
        else:
            return costo_base + (30 if self.ha_freezer else 0)
    
    def descrizione(self):
        return (
            super().descrizione() +
            f" | Capacità: {self.litri} l"
            f" | Freezer: {'V' if self.ha_freezer else 'X'}"
        )

class Lavatrice(Elettrodomestico): 
    
    soglia_capacita_alta = 8
    
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str,
                 capacita_kg: int, giri_centrifuga: int):
        
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        # attributi pubblici, niente __ davanti
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga

    def stima_costo_base(self):
        costo = super().stima_costo_base()
        if self.capacita_kg > self.soglia_capacita_alta:  # self.capacita_kg, non self.__capacita_kg
            costo += 20.0
        return costo

    def descrizione(self):
        return (
            super().descrizione() +
            f" | Capacità: {self.capacita_kg} kg"           # stesso
            f" | Centrifuga: {self.giri_centrifuga} giri/min"  # stesso
        )
    
    

class TicketRiparazione:
    
    ID_TICKET = 0
    
    def __init__(self, elettrodomestico: Elettrodomestico, stato = None, note = None):
        TicketRiparazione.ID_TICKET +=1
        self.__id_ticket = TicketRiparazione.ID_TICKET
        self.__elettrodomestico = elettrodomestico
        self.__stato = stato if stato is not None  else "aperto"
        self.__note = note if note is not None else []
        
    def calcola_preventivo(self, extra1 = None, extra2 = None):
        if extra1 == "commissioni" and extra2 == "iva":
            costo = self.get_elettrodomestico().stima_costo_base() + 10
            print("Commissioni di €10 applicate + iva al 22%")
            return costo * 1.22
        elif extra1 == "commissioni": 
            costo = self.get_elettrodomestico().stima_costo_base() + 10
            print("Commissioni di €10 applicate")
            return costo
        else:
            print("Nessun extra addebbitato")
            return self.get_elettrodomestico().stima_costo_base()
        
        
    # Metodi getter
    
    def get_id(self):
        return self.__id_ticket
    
    def get_elettrodomestico(self):
        return self.__elettrodomestico
    
    def get_stato(self):
        return self.__stato
    
    def get_note(self):
        return self.__note
    
    # Metodi setter
    def set_stato(self, nuovo_stato):
        self.__stato = nuovo_stato
        
    def aggiungi_note(self, nuove_note : str):
        self.__note = self.__note.append(nuove_note)
    
    

    
   

t1 = TicketRiparazione(f1)
t2 = TicketRiparazione(f1)

print(t1.get_id())
print(t1.get_stato())
print(t1.get_note())

print(t2.get_id())
print(t2.get_stato())
print(t2.get_note())

print(t1.calcola_preventivo("commissioni"))
print(t1.calcola_preventivo("commissioni", "iva"))
print(t1.calcola_preventivo())      
        
    
    












    