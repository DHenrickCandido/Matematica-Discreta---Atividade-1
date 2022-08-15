#Leitura do arquivo
f = open("entrada.txt", "r")

operacoes = []
conjunto1 = []
conjunto2 = []

qtdOperacoes = int(f.readline())
for i in range(qtdOperacoes):
  operacoes.append(f.readline().rstrip('\n').upper().strip(' '))
  list = [x.strip(' ') for x in f.readline().rstrip('\n').split(',')]
  conjunto1.append(list)
  list = [x.strip(' ') for x in f.readline().rstrip('\n').split(',')]
  conjunto2.append(list)

#Operacoes
def union(conjunto1,conjunto2):
  ret = conjunto1 + conjunto2
  return ret
  
def intersec(conjunto1,conjunto2):
  ret = []
  for i in range(len(conjunto1)):
    if conjunto1[i] in conjunto2:
        ret.append(conjunto1[i])
  return ret


def diff(conjunto1,conjunto2):
  ret = []
  for i in range(len(conjunto1)):
    if conjunto1[i] not in conjunto2:
        ret.append(conjunto1[i]) 
  return ret

def prod(conjunto1,conjunto2):
  ret = []
  for i in range(len(conjunto1)):
    for j in range(len(conjunto2)):
      ret.append([conjunto1[i],conjunto2[j]])
  return ret

print(operacoes)
#Exercicio
print(f"O código executará {qtdOperacoes} operações.")
for i in range(qtdOperacoes):
  print(f"Operacao {i+1}:")
  if operacoes[i] == 'U':
      print(union(conjunto1[i],conjunto2[i]))
  if operacoes[i] == 'I':
      print(intersec(conjunto1[i],conjunto2[i]))
  if operacoes[i] == 'D':
      print(diff(conjunto1[i],conjunto2[i]))
  if operacoes[i] == 'C':
      print(prod(conjunto1[i],conjunto2[i]))
