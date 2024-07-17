fichero = open("data/generos.csv", "r")


" print (fichero.read(8))  # el 8 para traer los 8 primeros caracteres del ficheros "

" print (fichero. readline()) "

# se puede iterar por los ficheros:

for linea in fichero:
    print(linea)
    
# imprime esto

""" 
1;Accion

2;Animacion

3;Aventura

4;Comedia

5;Crimen

6;Drama

7;Familiar

8;Fantasia

9;Musical

10;Romantica

11;Terror

12;Thriller

13;Western
""" 

