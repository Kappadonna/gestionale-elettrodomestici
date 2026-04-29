from abc import ABC, abstractmethod
import datetime

anno = datetime.date.today().year






class Lavatrice(Elettrodomestico): 
    
    
    soglia_capacità_alta = 8
    
    # costruttore: richiama super() per gli attributi comuni, aggiunge quelli specifici
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str,
                 capacita_kg: int, giri_centrifuga: int):
        
        # chiama il costruttore di Elettrodomestico per marca, modello, anno, guasto
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        # attributi privati specifici della lavatrice 
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga

    # getter
    def get_capacita_kg(self):
        return self.__capacita_kg

    def get_giri_centrifuga(self):
        return self.__giri_centrifuga

    # setter
    def set_capacita_kg(self, capacita_kg):
        self.__capacita_kg = capacita_kg

    def set_giri_centrifuga(self, giri):
        self.__giri_centrifuga = giri

    # override di stima_costo_base
    
    def stima_costo_base(self):
        costo = 60.0
    
        if self.__capacita_kg > self.soglia_capacità_alta:
            costo += 20.0
        return costo

    
    def descrizione(self):
        return (
            super().descrizione() +
            f" | Capacità: {self.__capacita_kg} kg"
            f" | Centrifuga: {self.__giri_centrifuga} giri/min"
        )


















