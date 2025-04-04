# -*- coding: utf-8 -*-
"""
@author: Gonçalo Braz
#objective: Teste da classe Enrollments
"""
# Importa a classe 'Enrollments' que se encontra na pasta 'classes'
from classes.Enrollments import Enrollments

# Lê os dados da classe Enrollments
Enrollments.read("data/Research.db")

# Percorre os objetos do primeiro ao último
print("\nprimeiro->último:")
p1 = Enrollments.first()
while p1 != None:
    print(p1)
    p1 = Enrollments.nextrec()

# Percorre os objetos do último ao primeiro
print("\núltimo->primeiro:")
p1 = Enrollments.last()
while p1 != None:
    print(p1)
    p1 = Enrollments.previous()

# Cria um novo objeto Enrollments
print("\nEnrollment com o código 1555 criada:")
p1 = Enrollments(1555, 200, 27, '12/02/2025', 'Yes', 'Active')
print(p1)

# Percorre os objetos usando as variáveis de classe 'obj' e 'lst'
print("\nVariáveis de classe 'obj' e 'lst'")
for codigo in Enrollments.lst:
    p1 = Enrollments.obj[codigo]
    print(p1)

# Acede ao objeto cujo código é 555
print("\nEnrollment com o código 1555:")
p1 = Enrollments.obj[1555]
print(p1)

# Apaga a o objeto enrollments com o código '1555'
print("\nEnrollment com o código 1555 removida")
Enrollments.remove(1555)

# Percorre os objetos usando a variável de classe 'obj'
print("\nVariável de classe 'obj':")
for p1 in Enrollments.obj.values():
    print(p1)

# Escreve os dados da classe Enrollments
Enrollments.write("data/Research.db")
