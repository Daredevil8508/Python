#Variables
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

#Concatenación
print(my_string_variable, my_int_variable, my_bool_variable)

#Imprimir tipo de variable
print(type(print(my_string_variable, my_int_variable, my_bool_variable)))
print("Este es el valor de:", my_bool_variable)

#Funciones del sistema
print(len(my_string_variable))

#Variables en una misma linea
name, surname, alias, age = "Andres", "Abella", "Daredev", 39
print(name, surname, alias, age)

#Input
'''
name = input('Cual es tu nombre: ')
age = input('Cual es tu edad: ')
'''

#Cambiar tipo
name = 39
age = "Andres"
print(name)
print(age)

#Forzar el tipo
address: str = "Mi dirección"
address = 39
print(type(address))
