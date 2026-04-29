class Lavatrice(Elettrodomestico): 
    
    soglia_capacita_alta = 8
    
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str,
                 capacita_kg: int, giri_centrifuga: int):
        
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        # attributi pubblici, niente __ davanti
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga

    def stima_costo_base(self):
        costo = 60.0
        if self.capacita_kg > self.soglia_capacita_alta:  # self.capacita_kg, non self.__capacita_kg
            costo += 20.0
        return costo

    def descrizione(self):
        return (
            super().descrizione() +
            f" | Capacità: {self.capacita_kg} kg"           # stesso
            f" | Centrifuga: {self.giri_centrifuga} giri/min"  # stesso
        )
    
    