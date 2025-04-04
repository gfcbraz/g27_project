# -*- coding: utf-8 -*-
"""
@author: Rui Graça
#objective: Teste da classe Participants
"""
# Importa a classe 'Participants' que se encontra na pasta 'classes'
from classes.participants import Participants

# Lê os dados da classe Participants
Participants.read("data/Research.db")

# Percorre os objetos do primeiro ao último
print("\nprimeiro->último:")
p1 = Participants.first()
while p1 != None:
    print(p1)
    p1 = Participants.nextrec()

# Percorre os objetos do último ao primeiro
print("\núltimo->primeiro:")
p1 = Participants.last()
while p1 != None:
    print(p1)
    p1 = Participants.previous()

# Cria um novo objeto Participant
print("\nParticipant com o código 1020 criada:")
p1 = Participants(1020, 'Joana Fonseca ', 35)
print(p1)

# Percorre os objetos usando as variáveis de classe 'obj' e 'lst'
print("\nVariáveis de classe 'obj' e 'lst'")
for codigo in Participants.lst:
    p1 = Participants.obj[codigo]
    print(p1)

# Acede ao objeto cujo código é 1020
print("\nParticipant com o código 1020:")
p1 = Participants.obj[1020]
print(p1)

# Apaga a o objeto participant com o código 1020
print("\nParticipant com o código 1020 removida")
Participants.remove(1020)

# Percorre os objetos usando a variável de classe 'obj'
print("\nVariável de classe 'obj':")
for p1 in Participants.obj.values():
    print(p1)

# Escreve os dados da classe Participants
Participants.write("data/Research.db")
