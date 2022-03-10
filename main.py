variations = {
    '0': ['0','8'],
    '1': ['1','2', '4'],
    '2': ['2','1','5','3'],
    '3': ['3','2', '6'],
    '4': ['4','1','5','7'],
    '5': ['5','2','4','6','8'],
    '6': ['6','3','5','9'],
    '7': ['7','4','8'],
    '8': ['8','5','7','0','9'],
    '9': ['9','8','6'],
}

def get_possible_pins(pin):
    return variations[pin]

def get_pins(observed):
    # Apareamiento de arrays
    
    # mi idea es obtener un array de pins posibles, por cada pin leido.
    # Teniendo ese array, puedo mapearlo para tener n arrays, siendo n la cantidad de pins vistos
    # Luego tendria que hacer combinatoria, con todas las variaciones posibles
    
    arr_of_adjacents_pins = []
    for i in range(len(observed)):
        possible_pins = get_possible_pins(observed[i])
        arr_of_adjacents_pins.append(possible_pins)
    # arr_of_adjacents_pins es un array que contiene, por cada pin observado, una lista
    # de todos los posibles pins. Es decir, es un array de arrays.
    
    # Por teoria de combinatoria, se que si tengo un conjunto de elementos K, con k-cantidad de elementos,
    # y n lugares disponibles, las combinaciones posibles que tengo con repeticion es de k ** n
    # siendo que puedo meter en cada lugar, a un elemento del conjunto K
    
    # En este ejercicio, tengo diferentes conjuntos, que son mis arrays de adyacencias
    # Por lo tanto, la formula sera k1*k2*k3*...*kn, siendo n la cantidad de pins observados
    # Como la cantidad de arrays a aparear son potencialmente infinitas, necesito adaptarme a esa dinamica
    # Aprovechando que la multiplicacion es asociativa, puedo hacer ((k1*k2)*k3) e ir resolviendo asi.
    # Por lo tanto, a la hora de hacer las combinaciones, voy tomando un array de posibles pins, los combino con un 
    # array de combinaciones de la iteracion anterior llamado combinations_arr y los resultados los meto en un array 
    # final_array. Esto lo hago para no ir iterando y manmipulando el mismo array y evitar inconsistencias.
    
    # En la primera iteracion, combinations_arr va a ser igual al primer array de pins adyacentes, debido a que no hay nada para combinar
    # pero a partir de la siguiente iteracion, ahi voy a ir mezclando lo que tenga en combinations_arr con cada elemento del nuevo array
    # arr_of_adjacents_pins[i], y el resultado del apareamiento lo inserto en final_array
    # Final_array se resetea en cada iteracion, debido a que la longitud de cada combinacion debe ser igual a len(observed).
    
    i = 0
    combinations_arr = [] # aca voy a tener las combinaciones parciales
    final_array = [] # en cada iteracion, voy a poner el resultado final aca
    print("Pin observer ",observed)
    while i<len(observed):
        if i == 0:
            combinations_arr += arr_of_adjacents_pins[i]
            final_array = combinations_arr
        else:
            # Combino los que ya existen con los nuevos
            final_array = []
            for pin in combinations_arr:
                for another_pin in arr_of_adjacents_pins[i]:
                    # mezclo una combinacion parcial con un nuevo pin
                    final_array.append(pin+another_pin)
        i +=1
        combinations_arr = final_array
        # Esto lo hago para que combinations_arr contenga los resultados hasta el momento, por si es necesario
        # otra iteracion. Si no hay mas iteraciones, se retorna final_array. Si hay mas iteraciones
        # utilizo el array de combinaciones, para calcular las nuevas e ir insertandolas en un nuevo array.
    
    print("Final array")
    print(final_array)
    return sorted(final_array)
