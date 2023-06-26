#write a function tht can sum up numbers
def sum_numbers(numbers=None):
    if numbers is None:#es mas apropiado utilizar is que los dos iguales para hacer una comparacion con None
        return sum(range(1, 101))#sumar parametros del 1 al 100
    return sum(numbers)