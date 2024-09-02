class Calsado:
    def __init__(self,made_in,marca,tipo,nro,suela):
        self.made_in = made_in
        self.marca = marca
        self.tipo = tipo
        self.nro =  nro
        self.suela = suela
        
    def Mostrar_calsado(self):
        print(f" MadeIn: {self.made_in} \n Marca: {self.marca} \n Tipo: {self.tipo} \n Numero: {self.nro} \n Suela: {self.suela} \n")

class Zapatilla(Calsado):
    def __init__(self,made_in,marca,tipo,nro,suela,modelo,materiales,stock):
        super().__init__(made_in,marca,tipo,nro,suela)
        self.modelo = modelo
        self.materiales = materiales
        self.stock = stock
    
    def Mostrar_Calsado(self):
        super().Mostrar_calsado()
        print(f" Modelo: {self.modelo} \n Materiales: {self.materiales} \n Stock: {self.stock} ")

Zapatilla_1 = Zapatilla("Made In Vietnam","Nike","Caña Alta - Deportiva",16,"Goma","Impac 4","Zoom",75)
Zapatilla_2 = Zapatilla("Made In China","Puma","Caña Media - Deportiva",37,"Goma","HyperDunk 2017","Air",25)

Zapatilla_1.Mostrar_calsado()
Zapatilla_2.Mostrar_calsado()