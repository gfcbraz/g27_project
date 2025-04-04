# -*- coding: utf-8 -*-
"""
@author: António Furtado
#objective: Teste da classe Studies
"""
# Importa a classe 'Studis' que se encontra na pasta 'classes'
from classes.studies import Studies

# Lê os dados da classe Studies
Studies.read("data/Research.db")

# Percorre os objetos do primeiro ao último
print("\nprimeiro->último:")
p1 = Studies.first()
while p1 != None:
    print(p1)
    p1 = Studies.nextrec()

# Percorre os objetos do último ao primeiro
print("\núltimo->primeiro:")
p1 = Studies.last()
while p1 != None:
    print(p1)
    p1 = Studies.previous()

# Cria um novo objeto Studies
print("\nStudy com o código 850 criada:")
p1 = Studies(850, 'ComportamentosAditivos', 'Gym', '14/03/2006', 17)
print(p1)

# Percorre os objetos usando as variáveis de classe 'obj' e 'lst'
print("\nVariáveis de classe 'obj' e 'lst'")
for codigo in Studies.lst:
    p1 = Studies.obj[codigo]
    print(p1)

# Acede ao objeto cujo código é 850
print("\nStudy com o código 850:")
p1 = Studies.obj[850]
print(p1)

# Apaga a o objeto studies com o código '555'
print("\nStudy com o código 850 removida")
Studies.remove(850)

# Percorre os objetos usando a variável de classe 'obj'
print("\nVariável de classe 'obj':")
for p1 in Studies.obj.values():
    print(p1)

# Escreve os dados da classe Studies
Studies.write("data/Research.db")