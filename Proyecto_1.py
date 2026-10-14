#imagina que un pequeño negocio de ventas necesita un programa que guarde una lista de productos con sus precios, 
#que pueda calcular el total de una compra, y al final le diga al cliente cuánto debe pagar, incluyendo un diez por 
#ciento de descuento si la compra supera los cien soles. ¿Te animas a pensar cómo lo armarías?
#creamos la lista de productos y sus precios
productos = {"mansanas": 3.5, "bananas": 2.0, "naranjas": 4.0, "uvas": 5.0}

#pedimos al usuario que ingrese los productos que desea comprar y sus cantidades
#y tambien si compraran por kilos las frutas cuanto deberian pagar
compra = {}
for producto in productos:
    cantidad = float(input(f"¿Cuántos kilos de {producto} desea comprar? "))
    compra[producto] = cantidad

#calculamos el total de la compra
total = 0
for producto, cantidad in compra.items():
    total += productos[producto] * cantidad

#aplicamos el descuento si la compra supera los cien soles
if total > 100:
    total *= 0.9

print(f"El total de la compra es: {total}")