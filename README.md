# Apareamiento-de-arrays

Pequeño challenge de Codewars

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
    
Se tiene ese tablero, donde se ingresa una contraseña.
Alguien observa a otro ingresar, y se fija en los pines ingresados.
Pero esta observacion no es exacta, ya que el pin ingresado pudo haber sido el observado o uno de los adyacentes.
La adyacencia se analiza en forma vertical u horizontal

Por ejemplo. Se observa que se ingreso el pin '1'. Por lo tanto el pin final pudo haber sido '1', '2' o '4'.
Si se observa el pin '11', el pin final ingresado pudo haber sido '11','12,'14, y asi.
En fin, el ejercicio consiste en realizar una combinatoria de una cantidad desconocida de arrays
