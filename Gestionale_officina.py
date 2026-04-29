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
        return f"{self.get_marca()}, {self.get_modello()} è un {type(Elettrodomestico)} del {self.get_anno_acquisto()}, ha un guasto{self.get_guasto()}"
     
    # metodo astratto:
    @abstractmethod
    def stima_costo_base(self):
        pass
            
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
    
    def __init__(self, marca: str, modello:str, anno_acquisto:int, guasto:str):
        