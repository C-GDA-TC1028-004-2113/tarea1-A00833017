def main():
    #escribe tu código abajo de esta línea
    nm =int(input("Dame el número de mensajes: "))
    nm2 = float(input("Dame el número de megas: "))
    nm3= int(input("Dame el número de minutos: "))
    ct = (nm+nm2+nm3)*.8
    print("El costo mensual es:", ct)




if __name__ == '__main__':
    main()
