

# Mi Version 1.0
print("\n Bienvenido al Generador de Series Fibonacci \n\n")
# Ingreso del Limite de la Serie
Limite = int( input( "Ingrese el Limite :"))
Elemento = 1
Inicio = 0
Paso = 1
print ' 0, 1', 

while ( Inicio + Paso < Limite ):
	Elemento = Inicio + Paso
	Inicio = Paso
	Paso = Elemento
	print ', ', Elemento ,


print '.'
print Elemento , ' < ' , Limite 

