"""
###**Ejercicio 6.3**
Crear una clase de Peliculas:
*   Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
*   Se deben crear 4 metodos en la clase:
    1.  Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion}  
        y fue filmada en {nacionalidad}
    2. Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    3. Cambiar el genero de una pelicula
    4. Modificar puntuacion de la pelicula

El programa debe:
*   Tener un menu con 7 opciones:
    1. Crear una pelicula y guardar su nombre (instancia) en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
    6. Verificar el año de la pelicula
    7  Modificar puntuacion de la pelicula (entre 1 y 10)
    """
import Pelicula as pl
generos = ["comedia","accion","terror"]
peliculas = []
pelicula_1 = pl.Pelicula("abc",1995,"comedia","argentina",10)
pelicula_1.presentar_pelicula()