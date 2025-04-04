# -*- coding: utf-8 -*-
"""
@author: Rui Ferreira
#objective: Teste da classe Center
"""
# Importa a classe 'Center' que se encontra na pasta 'classes'
from classes.Center import Center

# Lê os dados da classe Center
Center.read("data/Research.db")

# Percorre os objetos do primeiro ao último
print("\nprimeiro->último:")
p1 = Center.first()
while p1 != None:
    print(p1)
    p1 = Center.nextrec()

# Percorre os objetos do último ao primeiro
print("\núltimo->primeiro:")
p1 = Center.last()
while p1 != None:
    print(p1)
    p1 = Center.previous()

# Cria um novo objeto Center
print("\nCenter com o código 38 criada:")
p1 = Center(38, 'Centro', 'Póvoa de Varzim')
print(p1)

# Percorre os objetos usando as variáveis de classe 'obj' e 'lst'
print("\nVariáveis de classe 'obj' e 'lst'")
for codigo in Center.lst:
    p1 = Center.obj[codigo]
    print(p1)

# Acede ao objeto cujo código é 38
print("\nCenter com o código 38:")
p1 = Center.obj[38]
print(p1)

# Apaga a o objeto pessoa com o código 38
print("\nCenter com o código 38 removida")
Center.remove(38)

# Percorre os objetos usando a variável de classe 'obj'
print("\nVariável de classe 'obj':")
for p1 in Center.obj.values():
    print(p1)

# Escreve os dados da classe Center
Center.write("data/Research.db")
