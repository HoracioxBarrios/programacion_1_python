import re
'''
1.Crear una función llamada es_mayuscula que reciba un string y 
devuelva True en caso de que todas las letras sean mayúsculas 
o False en el caso contrario
'''

texto_ejemplo = "PEPE"

def es_mayuscula(texto : str)-> bool:
    '''
    verifica si una palabra esta compuesta por solo letras mayusculas
    recibe una palabra
    devuelve True en caso de ser todo mayusculas
    '''
    if(re.findall(r"^[A-Z]+$", texto)): # cometi el error de no ponerle "+" para que no sea solo una letra, sino 1 o mas
        return True
    else:
        return False


print(es_mayuscula(texto_ejemplo))



''' uso match para ver si conincide lo uso en un if si hay 
un objeto match seria True, si no devuevulve None'''










# palabra = "PEPE" #True
# # palabra = "Pepe" #False
# # palabra = "pepe" #False
# # palabra = "PepE" #False

# def es_mayuscula(cadena :str)-> bool:
#     '''
#     comprueba si una o mas letras son mayusculas
#     recibe una cadena str
#     devuelve true en caso de ser todas Mayusculas
#     '''
#     es_mayuscula = re.findall(r"^[A-Z]+$", cadena)
#     if(len(es_mayuscula) > 0):
#         return True
#     else:
#         return False
   

# print(es_mayuscula(palabra))

# '''
# r"^[A-Z]+$"   Nota: r es de regular expression. 
# ^ en este caso significa empiza con letras desde A-Z nayusculas, [] estos 
# corchetes significan Conjunto de caracteres 
# + seria Una o más ocurrencias, y $ significa en este caso que termina con mayuscula

# re.findall() retorna una lista
# '''