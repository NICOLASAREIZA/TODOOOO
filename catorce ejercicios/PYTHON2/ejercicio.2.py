#Leer 3 número distintos y determinar cuál es el menor.

A=int(input("Ingrese primer numero: "))
B=int(input("Ingrese segundo numero: "))
C=int(input("Ingrese tercer numero: "))

if(A == C and A < B  ):
    print("El primer numero y el tercer numero son iguales y son los menores")

elif(B == C and B < A):
    print("El segundo numero y el tercer numero son iguales y son los menores")
    
elif(A == B and A < C):
    print("El primer numero y el segundo numero son los iguales y son los menores")
    
elif(A == C and B == C):
    print("Todos los numeros son iguales...")
    
else:
 if(A < B and A < C):
  print("El primer numero es el menor",A )
 
 elif(B < A and B < C):
  print("El segundo numero es el menor ",B )
 else:
  print("El tercer numero es el menor",C )