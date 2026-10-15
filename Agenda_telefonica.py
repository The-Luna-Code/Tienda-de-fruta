#La idea sería crear un diccionario donde cada nombre sea la clave, y el valor sea su número de teléfono, como una pequeña 
#agenda de contactos guardada en el programa.Después armas una función que reciba un nombre, busque ese nombre dentro del 
#diccionario, y te devuelva o muestre el número de teléfono correspondiente,
#si el nombre no está en la agenda, que te diga que no lo encontró.

agenda = {"Juan": "123-456-7890", "María": "098-765-4321", "Pedro": "555-555-5555", "Ana": "111-222-3333", "Luis": "444-555-6666"}

def buscar_telefono(nombre):
    if nombre in agenda:
        return agenda[nombre]
    else:
        return "Nombre no registrado en la agenda."

# Solicita al usuario que ingrese el nombre de la persona que desea buscar su numero de teléfono
nombre_a_buscar = input("Ingrese el nombre de la persona que desea buscar su número de teléfono: ")

# verifica si el nombre existe en la agenda y muestra el resultado
if nombre_a_buscar.title() in agenda:
    print(f"El numero de telefono de {nombre_a_buscar.title()} es: {agenda[nombre_a_buscar.title()]}")
else:
    print(f"{nombre_a_buscar.title()} no esta registrado en la agenda.")
