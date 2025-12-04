# Parte 1
#### Función A: 
- Pura
- Ya que el valor de retorno depende de sus argumentos de entrada 
- No necesita conversion 

#### Función B: 
- Impura
- Depende de la existencia de una variable externa y al volver a llamar la funcion no devolvera el mismo resultado a pesar de que esta no recibe parametros
- Para convertirla eliminaria la dependencia global     

#### Función C: 
- Impura
- Modifica el arreglo con una variable no definida por el usuario
- La convertiria pasando la fecha como un parametro y retornaria una copia del arreglo con el cambio para no modificar el original
#### Función D: 
- Pura
- Ya que genera la lista, no la modifica
- No necesita conversion
#### Función E: `mezclar_lista`
- Impura
- Modifica la lista original
- La converitiria en pura devolviendo una copia de la lista modificada

# Parte 4

1. ¿Qué significa que una función sea "pura"?
Significa que siempre dara el mismo resultado y no modifica ni utiliza registros fuera de su procedimiento lo cual pueda provocar que el resultado varie a pesar de tener los mismos datos de entrada, como ejemplo podemos utilizar un libro, si vas a la pagina 20, siempre tendrá el mismo contenido, no cambia ni se transforma, siempre estan las mismas palabras

2. En la Parte 3, ¿por qué crear_transformador retorna una función en lugar de aplicar directamente la transformación? ¿Qué ventaja ofrece este diseño?
En lugar de procesar los datos inmediatamente, el código simplemente "prepara" la operación específica que queremos realizar y la deja lista para usarse más tarde, su ventaja es la reutilizacion de codigo 

3. ¿Qué dificultades encontraste al convertir el código imperativo a funcional en la Parte 2? ¿Qué parte fue más difícil y cómo la resolviste?
El saber cuantas funciones usar y el decifrar como hacerlas lo más puras posibles, investigue en internet para resolverlo

4. Si tuvieras que explicar la diferencia entre programación imperativa y funcional a alguien que no programa, ¿qué analogía usarías?
Usaría la analogia del sandwich, ya que es distinto el decirle a alguien como realizarun sandwich de jamon y queso paso a paso, a decirle, "quiero un sandwich de jamon y queso" 