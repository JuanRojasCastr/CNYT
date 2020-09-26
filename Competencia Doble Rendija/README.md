## Competencia de la doble rendija.

El experimento de la doble rendija nos permite empezar a entender el mundo cuantico y como la fisica antigua se queda eatras para explicar algunas cosas de nuestro universo.

Primero se listaran los materiales y las condiciones del experimento, luego como se hizo y los resultados obtenidos, por ultimos se dará la explicacion de como sucede y una pequeña muestra del calculo de probabilidades mediante la libreria creada.

#### Materiales:

- Cinta aislante (negra).
- Tijeras.
- Hilo (en este caso dental).
- Un anillo o tubo.
- Carton y pegamento (opcional).

![Materiales](https://cdn.discordapp.com/attachments/584593411567517710/759475885895319582/20200926_130510.jpg)

#### Condicones:

- Tener una separacion considerable entre la doble rendija y la pared o superficie donde impacta la luz.
- Estar en un lugar con poca luz.
- Tener una camara en lo posbile con buena definicion y que permita controlar los niveles de luz que entra a la camara (abrir o cerrar opturacion)

#### Proceso de creacion y montaje.

1. Lo primero sera cortar un hilo y ponerlo de tal forma que divida en dos el hueco por donde pasa el dedo.
2. Recrotar pedazos de cinta aislante para sujetar el hilo, luego seguir cortando y pegando para crear la doble rendija. (es importante ir probando que sea suficientemente pequeña la rendija)
3. De manera opcional se puede pegar un pedazo de carton en la parte de abajo del anillo para poder ponerlo en una superficie sin que se ruede o incline.

*Imagen rendija*

#### Resultados:

Antes de proceder a mostrar los resultados obtenidos recuerde que este es un experimento y por ende se necesita de paciencia, en mi caso mostrare partes del proceso, es decir pequeñas muestras de cada toma hasta llegar a la ultima prueba donde considero que es la mejor. 
Tambien el registrar el experimento debido al enfoque de la camara.

![Priemra foto](https://cdn.discordapp.com/attachments/584593411567517710/759478484430094376/unknown.png)

En esta primera toma del experimento no habia considerado ni la luz ni la distancia con lo cual era dificl evidenciar el patron.

![Segunda Foto](https://cdn.discordapp.com/attachments/584593411567517710/759478544559505458/unknown.png)

Aqui logre el patron pero debido a la distancia y la luz todavia no lograba hacer que se viera con mejor definicion.

![Tercera Foto](https://cdn.discordapp.com/attachments/584593411567517710/759478602676174878/unknown.png)

Aqui el patros se podia ver mejor pero el problema era ajustar para que la camara lo lograra captar.

![Cuarta Foto](https://cdn.discordapp.com/attachments/584593411567517710/759478675715522600/unknown.png)

Este fue el mejor de mis intentos y uno de los ultimos, la camara logro captar "bien" el patron.

Aclaro que todas las fotos son extractos de videos que fui tomando que cada toma.

#### Explicacion:

Primero hay que dejar claro que la luz no es un "rayo", sino una onda, segundo que el movimiento de los fotones de luz se explican atravez de la funcion de onda, y mediante la ecuacion de Schrödinger, estas pueden tener la forma de onas estacionarias
que se traducen a probabilidades de estar en un estado, hablando de manera coloquial, al funcionanar como ondas estacinarias, estas al llegar a la rendija se solapan unas a otras, es decir hay lugares en que las funciones de onda de cada rendija oscilen a la vez
y esto nos muestra que en el centro es la mayor probabilidad de de impactar, y existen otros lugares donde las ondas se cancelan, creando estos "huecos" del patron:

![Foto con indicaciones](https://cdn.discordapp.com/attachments/584593411567517710/759478818867773520/unknown.png)

*Para mostrar que las probabilidades si cambian utilizamos nuestra liberia*:

#### Uso de libreria:

Es imporante recalcar que utilizaremos las librerias de este repositorio. 

Primero mostramos un ejemplo del sistema si usaramos el sisitema cuantico:

~~~


		# Por comodidad en la escritura definimos los numeros complejos como c1, c2, c3:
        c1 = (-1 / (6 ** 0.5), 1 / (6 ** 0.5))
		c2 = (-1 / (6 ** 0.5), -1 / (6 ** 0.5))
		c3 = (1 / (6 ** 0.5), -1 / (6 ** 0.5))
        
        # Ahora llamamos a la funcion que calcula las probabilidades de un sistema cuantico.
        
        print(rendijas_cuantico([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]], [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]], 2))
        
        # Es importante que para ver los resultados del sistema se tiene que usar de dos ticks para adelante.

~~~

Para ver de manera grafica lo que hicimos, es decir ver nuestro vector inicial, la matriz y el resultado:

![Imagen Referencia](https://cdn.discordapp.com/attachments/584593411567517710/759485728483704883/unknown.png)

*Recuerde que es solo un ejemplo y no se consideran todas las posibles opciones, por esto nos dan probabilidades diferentes a la realidad*

Ahora mostraremos el procedimiento con un sistema probabilistico clasico:

~~~

		
        # Llamamos la funcion que calcula las probabilidades de forma clasica:
        
        print(rendijas_clasico([[0, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0], [0, 1/3, 0, 1, 0, 0, 0, 0], [0, 1/3, 0, 0, 1, 0, 0, 0], [0, 1/3, 1/3, 0, 0, 1, 0, 0], [0, 0, 1/3, 0, 0, 0, 1, 0], [0, 0, 1/3, 0, 0, 0, 0, 1]], [[1], [0], [0], [0], [0], [0], [0], [0]], 2))

		# Con esto sería sufuciente
~~~

De forma grafia tendriamos:

![Imagen Referencia 2](https://cdn.discordapp.com/attachments/584593411567517710/759491041195196416/unknown.png)

## Autor

Juan Camilo Rojas Castro.
