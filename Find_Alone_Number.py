def get_result(socks):
    long=len(socks)
    res = socks[0]
    # Do XOR of all elements and return
    for i in range(1,long):
        res = res ^ socks[i]
        print("Estoy en la posicion", i)
        print("Variable", res)
     
    return res
 
# Creo el Array
socks = [2, 3, 5, 3, 1, 2, 1,5,12] 
print ("El elemento sin compañero es", get_result(socks))