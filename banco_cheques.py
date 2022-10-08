## El cajero de un banco solo dispone de billetes de $10000, $2000 y monedas de $100. Su función es cambiar los cheques a los clientes, dándoles el menor número posible de billetes. Asumiendo que todos los cheques son múltiples de $100, hacer el diagrama de flujo y el programa en Python que reciba el valor del cheque a cambiar y que le informe al cajero cuántos billetes de cada denominación debe entregar. Como no se sabe cuántos clientes vienen en un día, el programa debe terminar cuando reciba cero como valor del cheque, y al final del día debe informar cuántos billetes de cada denominación se gastaron

print("------------------------")
print("------BANCO-CHEQUE------")
print("------------------------")
print("")

#input


n = 100
# Process & output
n10 = 0
n2 = 0
n1 = 0

while n != 0:
    n = int(input("Digita la cantidad del cheque: "))
    print("")
    if n % 100 == 0:
        cheque = n
        mil_10 = n // 10000
        n10 = n10 + mil_10
        n = n - mil_10 * 10000
        
        mil_2 = n //2000
        n2 = n2 + mil_2
        n = n - mil_2 * 2000
        
        cien = n // 100
        n1 = n1 + cien
        #mil_2 = ((n / 10000) - mil_10)/2000
        print("Para el cheque de",cheque,"se necesitan:")
        print("se necesitan",mil_10,"billetes de $10.000")
        print("se necesitan",mil_2,"billetes de $2.000")
        print("se necesitan",cien,"monedas de $100")
        print("")
    else:
        print("Digitaste un una cantidad que no es multiplo de $100")
    
else:
    print("---------------------")
    print("El programa finalizo.")
    print("Registro de la sesión:")
    print("Se gastaron",n10,"billetes de $10.000 en total")
    print("Se gastaron",n2,"billetes de $2.000 en total")
    print("Se gastaron",n1,"monedas de $100 en total")
    print("---------------------")
    
