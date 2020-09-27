## Competencia de la doble rendija.

El experimento de la doble rendija nos permite empezar a entender el mundo cuántico y como la física antigua se queda atrás para explicar algunas cosas de nuestro universo.

Primero se listarán los materiales y las condiciones del experimento, luego como se hizo y los resultados obtenidos, por últimos se dará la explicación de como sucede y una pequeña muestra del cálculo de probabilidades mediante la librería creada.

#### Materiales:

- Cinta aislante (negra).
- Tijeras.
- Hilo (en este caso dental).
- Un anillo o tubo.
- Cartón y pegamento (opcional).

![Materiales](https://cdn.discordapp.com/attachments/584593411567517710/759475885895319582/20200926_130510.jpg)

#### Condiciones:

- Tener una separación considerable entre la doble rendija y la pared o superficie donde impacta la luz.
- Estar en un lugar con poca luz.
- Tener una cámara en lo posible con buena definición y que permita controlar los niveles de luz que entra a la cámara (abrir o cerrar opturación)

#### Proceso de creación y montaje.

1. Lo primero será cortar un hilo y ponerlo de tal forma que divida en dos el hueco por donde pasa el dedo.
2. Recorta pedazos de cinta aislante para sujetar el hilo, luego seguir cortando y pegando para crear la doble rendija. (es importante ir probando que sea suficientemente pequeña la rendija)
3. De manera opcional se puede pegar un pedazo de cartón en la parte de abajo del anillo para poder ponerlo en una superficie sin que se ruede o incline.

*Imagen rendija*

#### Resultados:

Antes de proceder a mostrar los resultados obtenidos recuerde que este es un experimento y por ende se necesita de paciencia, en mi caso mostrare partes del proceso, es decir pequeñas muestras de cada toma hasta llegar a la última prueba donde considero que es la mejor. 
También el registrar el experimento debido al enfoque de la cámara.

![Primera foto](https://cdn.discordapp.com/attachments/584593411567517710/759478484430094376/unknown.png)

En esta primera toma del experimento no había considerado ni la luz ni la distancia con lo cual era difícil evidenciar el patrón.

![Segunda Foto](https://cdn.discordapp.com/attachments/584593411567517710/759478544559505458/unknown.png)

Aquí logre el patrón, pero debido a la distancia y la luz todavía no lograba hacer que se viera con mejor definición.

![Tercera Foto](https://cdn.discordapp.com/attachments/584593411567517710/759478602676174878/unknown.png)

Aquí el patrón se podía ver mejor pero el problema era ajustar para que la cámara lo lograra captar.

![Cuarta Foto](https://cdn.discordapp.com/attachments/584593411567517710/759478675715522600/unknown.png)

Este fue el mejor de mis intentos y uno de los últimos, la cámara logro captar "bien" el patrón.

Aclaro que todas las fotos son extractos de videos que fui tomando que cada toma.

#### Explicación:

Primero hay que dejar claro que la luz no es un "rayo", sino una onda, segundo que el movimiento de los fotones de luz se explica atreves de la función de onda, y mediante la ecuación de Schrödinger, estas pueden tener la forma de ondas estacionarias
que se traducen a probabilidades de estar en un estado, hablando de manera coloquial, al funcionaran como ondas estacionarias, estas al llegar a la rendija se solapan unas a otras, es decir hay lugares en que las funciones de onda de cada rendija oscilen a la vez
y esto nos muestra que en el centro es la mayor probabilidad de de impactar, y existen otros lugares donde las ondas se cancelan, creando estos "huecos" del patrón:

![Foto con indicaciones](https://cdn.discordapp.com/attachments/584593411567517710/759478818867773520/unknown.png)

*Para mostrar que las probabilidades si cambian utilizamos nuestra Liberia*:

#### Uso de librería:

Es importante recalcar que utilizaremos las librerías de este repositorio. 

Primero mostramos un ejemplo del sistema si usáramos el sistema cuántico:

~~~


		# Por comodidad en la escritura definimos los números complejos como c1, c2, c3:
        c1 = (-1 / (6 ** 0.5), 1 / (6 ** 0.5))
		c2 = (-1 / (6 ** 0.5), -1 / (6 ** 0.5))
		c3 = (1 / (6 ** 0.5), -1 / (6 ** 0.5))
        
        # Ahora llamamos a la función que calcula las probabilidades de un sistema cuántico.
        
        print(rendijas_cuantico([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]], [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]], 2))
        
        # Es importante que para ver los resultados del sistema se tiene que usar de dos ticks para adelante.

~~~

Para ver de manera grafica lo que hicimos, es decir ver nuestro vector inicial, la matriz y el resultado:

![Imagen Referencia](https://cdn.discordapp.com/attachments/584593411567517710/759485728483704883/unknown.png)

*Recuerde que es solo un ejemplo y no se consideran todas las posibles opciones, por esto nos dan probabilidades diferentes a la realidad*

Ahora mostraremos el procedimiento con un sistema probabilístico clásico:

~~~

		
        # Llamamos la función que calcula las probabilidades de forma clásica:
        
        print(rendijas_clasico([[0, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0], [0, 1/3, 0, 1, 0, 0, 0, 0], [0, 1/3, 0, 0, 1, 0, 0, 0], [0, 1/3, 1/3, 0, 0, 1, 0, 0], [0, 0, 1/3, 0, 0, 0, 1, 0], [0, 0, 1/3, 0, 0, 0, 0, 1]], [[1], [0], [0], [0], [0], [0], [0], [0]], 2))

		# Con esto sería suficiente
~~~

De forma gráfica tendríamos:

![Imagen Referencia 2](https://cdn.discordapp.com/attachments/584593411567517710/759491041195196416/unknown.png)

## Autor

Juan Camilo Rojas Castro.
