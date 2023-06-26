class vehiculo:
    placa: str = ''
    tipo: str = ''
    hora: int = 0
    minutos: int = 0
    valor_a_pagar: float = 0
    
    def __init__(self, placa, tipo, hora, minutos, valor_a_p):
        self.placa = placa
        self.tipo = tipo
        self.hora = hora
        self.minutos = minutos
        self.valor_a_p = valor_a_p
        
class Parquedero:
    
    def __init__(self):
        
        tipo = input("ingrese el tipo de vehiculo |1 - moto $90| 2 - carro $110 | 3 - camioneta $130|")#leemos el tipo de vehiculo
        while tipo != 1 and tipo != 2 and tipo != 3:
            input("ERROR ingrese el tipo de vehiculo |1 - moto $90| 2 - carro $110 | 3 - camioneta $130|")
        
        tipo_str = ""#tipo no es un entero por eso necesitamos castearlo
        
         
        
        placa = input("ingrese la placa de vehiculo:")
        while placa != "":
            input("ERROR ingrese la placa de vehiculo:")
        horas = int(input("ingrese la hora:"))#esto castea de string a entero
        while horas < 0 :
            int(input("ERROR ingrese la hora:"))
        minutos = int(input("ingrese los minutos:"))
        while minutos < 0 :
            int(input("ERROR ingrese los minutos:"))
            
        vehiculo = vehiculo(placa,horas,minutos)#crear nuestro objeto, es decir el vehiculo

