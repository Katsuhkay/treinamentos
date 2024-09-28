# 1. Crie três variáveis com três tipos de dados diferentes, respeitando sua sintaxe:

nome = "Jesus"
ano = 2024
valor = 19.99
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 2. Crie um comentário de no máximo uma linha:

# Conhecei a verdade e a verdade voc libertará.

######################################################################################################################################################

# 3. Crie um comentário de mais de uma linha:

'''Efésios 4:30-32 

30 E não entristeçais o Espírito Santo de Deus, no qual estais selados para o dia da redenção.
31 Toda a amargura, e ira, e cólera, e gritaria, e blasfêmia e toda a malícia sejam tiradas dentre vós,
32 Antes sede uns para com os outros benignos, misericordiosos, perdoando-vos uns aos outros, como também Deus vos perdoou em Cristo.'''

######################################################################################################################################################

# 4. Escreva um programa que mostra em tela uma mensagem: Olá Mundo!!

print("Olá Mundo!!\n")
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 5. Crie uma variável nome e atribua para a mesma um nome digitado pelo usuário:

input(str("Qual o seu nome? \n")) # Uso do \n para digitar na linha de baixo
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 6. Exiba em tela o valor e o tipo de dado da variável num1: Sendo num1 = 1987

num_ano = 1987

print(num_ano, '\n')
# Imprime o valor da variável.
print(type(num_ano), '\n')
# Imprime o tipo da variável.
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 7. Peça para que o usuário digite um número, em seguida exiba em tela o número digitado.

ano = input("Em que ano você nasceu?\n")
# Pede para o usuário digitar um valor.
print(ano)
# Imprime o valor da variável ano digitado anteriormente.
# Dá para usar uma variável vazia para pular linha também.
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 8. Peça para que o usuário digite um número, em seguida o converta para float, exibindo em tela tanto o número em si quanto seu tipo.

altura = float(input("Qual a sua altura? "))
# Pede o dado ao usuário do tipo float
print(altura)
# Imprime o dado
print(type(altura), '\n')
#imprime o tipo do dado
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 9. Crie uma lista com o nome de 5 pessoas

list_nome = ['João', 'Paulo', 'José', 'Maria', 'Pedro']
# Listas ficam em [] (Colchetes)
print(list_nome)
# Imprime a lista
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 10. Mostre o tamanho da lista nomes / o número de elementos da lista nomes:
#     Mostre separadamente apenas o terceiro elemento dessa lista:

list2_nome = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']

print(len(list2_nome))
# Usa-se len para mostrar o tamanho da lista
print(list2_nome[3], '\n')
# O valor 3 no colchete pede a variável especifica no quarto local da lista
# Puxa-se o 4 valor pois listas começam pelo 0 e não pelo 1
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 11. Some o valor de duas variáveis num1 e num2: Senso num1=52 e num2=106. Por fim exiba em tela o resultado da soma.

num1 = 52
num2 = 106

print(f"O valor da soma é de ", num1+num2)
# Pode ser feito da seguinte forma também:
# print(num1 + num2)
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 12. Some os valores das variáveis num3 e num4, atribuindo o resultado da soma a uma nova variável homônia. Exiba em tela o conteúdo dessa varável

num3 = 52
num4 = 106

soma = num1 + num2
# Váriável criada para a soma

print(f"O valor da soma é de {soma}")
#Mostrando o valor da variável ao invés de fazer uma soma na função print
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 13. Subtraia os valores de num5 e num6:

num5 = 50
num6 = 106

print(num5-num6)

#ou

subtracao = num5 - num6

print(subtracao)
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 14. Realize as operações de multiplicação e de divisão entre os valores das variáveis num7 e num8:

num7 = 52
num8 = 106

multiplicacao = num7 * num8
#Nova variável para a multiplicação
divisao = num7 / num8
#Nova variável para a divisão

print(multiplicacao)
print(divisao)
#Imprime as duas variáveis
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 15. Eleve o valor de num9 a oitava potência, sendo num9=51:

num9 = 51

print(num9**8)
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 16. Escreva um programa que pede que o usuário dê a entrada em dois valore, em seguida, exiba em tela o resultado da soma, subtração, multiplicação e divisão desses números:

num10 = float(input("Digite o primeiro número: "))
num11 = float(input("Digite o segundo número: "))


soma16 = num10 + num11
subtracao16 = num10 - num11
multiplicacao16 = num10 * num11
divisao16 = num10 / num11

print(f"O resultado da soma dos valores {num10} e {num11} é {soma16}")
print(f"O resultado da subração dos valores de {num10} e {num11} é {subtracao16}")
print(f"O resultado da multiplicação dos valores {num10} e {num11} é de {multiplicacao16}")
print(f"O resultado da divisão dos valores {num10} e {num11} é de {divisao16}")
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 17. Dadas duas variáveis num12 e num13 com valores 100 e 89, respectivamente, verifique se o valor num12 é maior que o de num13, depois se é menor:

num12 = 100
num13 = 89

print(num12 > num13) #Retorna True
print(num12 < num13) #Retorna False
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 18. Verifique se os valores num12 e num13 são iguais:

print(num12 == num13) #Retorna False
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 19. Verifique se num12 e num13 são diferentes:

print(num12 != num13) #Retorna True
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 20. Verifique se o valor de num12 é igual ou menor que 100:

print(num12 <= 100)
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 21. Verifique se os valores de num12 e num13 são iguais ou menores que 100

print(num12 and num13 <= 100) 
#False, pois ambos os valores são verdadeiros.
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 22. Verifique se os valores de num12 e num13 são maiores ou iguais a 100:

print(num12 and num13 >= 100)
#False, pois um dos valores é falso (num13 = 89, que é menor que 100)
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 23. Verifique se o valor de num14 consta nos elementos de lista1. Sendo num14 = 100 e lista1 = [10, 100, 1000, 10000, 100000].

num14 = 100
lista1 = [10, 100, 1000, 10000, 100000]

print(num14 in lista1) #Retorna True, o valor da variável está presente na lista.
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 24. Crie duas variáveis com dois valores numéricos inteiros digitados pelo usuário, caso o valor do primeiro número dor maior que o do segundo, exiba na tela uma mensagem de acordo.
# Caso contrário, exiba um tela uma mensagem dizendo que o primeiro valor é menor que o segundo.

num15 = int(input("Digite o primeito valor:\n"))
num16 = int(input("Digite o segundo valor:\n"))

if num15 > num16:
    print("O primeiro valor é maior que o segundo.")
elif num15 == num16:
    print("O valores são iguais")
else:
    print("O primeiro valor é menor que o segundo.")
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 25. Peça para que o usuário digite um número, em seguida exoba em tela uma mensagem dizendo que tal número é PAR ou se é ÍMPAR:

num17 = int(input("Digite um número para descobrir se é par ou ímpar:\n"))

if num17 % 2 == 0:
    print(f"O número {num17} é par.")
else:
    print(f"O número {num17} é ímpar.")
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 26. Crie uma variável com valor inicial 0, enquanto o valor dessa variável for igual ou menor que 10, exiba em tela o próprio valor da variável.
# A cada execusão a mesma deve ter seu valor atualizado, incrementando em 1 unidade:

var1 = 0

while var1 <= 10:
    print(var1)
    var1 = var1 + 1
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 27. Crie uma estrutura de repetição que percorre a string "Nikola Tesla", exibindo em tela letra por letra desse nome:

for i in "Nikola Tesla":
    print(i)
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 28. Crie uma lista com 8 elementos de uma lista de compras de supermercado,
# por meio de um laço de repetição 'for' liste individualmente cada um dos itens dessa lista:

lista2 = ['Yamaha YZF-R6', 'Kawasaki Ninja ZX-6R', 'Honda CBR 600RR', 'Suzuki GSX-R750', 'Yamaha MT-07', 'Ducati Monster', 'BMW S1000RR', 'Kawasaki Ninja ZX-10R']

for i in lista2:
    print(i)
print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 29. Crie um programa que lê um valor de início de uma valor de fim, exibindo em tela a contagem dos números dentro desse intervalo.

inicio = int(input("Digite o número que irá começar a contagem:\n"))
fim = int(input("Digite onde irá acabar a contagem:\n"))

for i in range(inicio, fim + 1):
    print(i)

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 30. Crie um programa que realize a contagem de 0 a 20, exibindo apenas os valores pares:

for i in range(0, 20):
    if i % 2 == 0:
    #Separando número par
        print(i)
        #Imprime somente os valores pares

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 31. Crie um programa que realiza a Progressão Aritmética de 20 elementos, com primeiro termo e razão definidos pelo usuário:

termo = int(input("Digite o primeiro termo:\n"))
razao = int(input("Digite a razão:\n"))

pa = termo + (20-1) * razao

for i in range(termo, pa + razao, razao):
    print(i)

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 32. Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuário

tab1 = int(input("Qual tabuada você quer saber?\n"))

for i in range(1, 11):
    print(tab1*i)

# Ou também:

for num in range(1, 11):
    print(f"{tab1} X {num} = {tab1 * num}")

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 33. Crie um programa que realiza a contagem regressiva de 20 SEGUNDOS:

from time import sleep

for i in range(20, -1, -1):
    print(i)
    sleep(1)

print("Contagem terminada!")

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 34. Crie um programa que realiza a contagem de 1 até 100, usando apenas números ímpares, ao final do processo exiba quantos numeros foram encontrados nesse intervalo.
# Assim como a soma dos mesmos.

contador = 0
soma = 0

for i in range (1, 101):
    if i % 3 == 0:
        soma += i
        contador += 1

print(f"Foram encontrados {contador} números ímpares")
print(f"A soma dos números ímpares é {soma}!!")

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 35. Crie um programa que pese ao usuário que o mesmo digite um número qualquer, em seguida retorne se esse número é primo ou não.
# Caso não, retorne também quantas vezes esse número é divisível:

num18 = int(input("Digite um número: "))
divisoes = 0

for i in range(1, num18 + 1):
    if num18 % i == 0:
        divisoes += 1

if divisoes == 2:
    print(f"{num18} é primo!!")
    print(f"{num18} é divisível por 1 ou por {num18}")
else:
    print(f"{num18} não é primo!!")
    print(f"{num18} não é divisível por {divisoes} vezes...")

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 36. Crie um programa que pede ao usuário digite um nome ou frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

frase = str(input("Digite uma plavra ou frase: ")).strip().upper()
# .strip(): Remove espaços extras no início e no fim da string.
# .upper(): Converte todos os caracteres da string para maiúsculas, facilitando a comparação, independentemente de letras maiúsculas ou minúsculas.

palavras = frase.split()
# .split(): Divide a string em palavras, usando os espaços como delimitadores.
caracteres = ''.join(palavras)
# ''.join(palavras): Combina os elementos da lista palavras em uma string contínua.
frase_convertida = ''
# Descrição: Inicializa uma variável vazia frase_convertida, que será usada para armazenar a frase invertida.

for i in range(len(caracteres) -1, -1, -1):
# (len(caracteres) -1, -1, -1): Cria um intervalo que começa no último índice da string e vai até o índice 0 (decrementando 1 em 1)
    frase_convertida += caracteres[i]
    # Adiciona cada caractere (começando do fim) à variável frase_convertida

print(caracteres, frase_convertida)
# Imprime a string original sem espaços e a versão convertida 

if frase_convertida == caracteres:
    print("A frase ou palavra é um palíndromo!")
else:
    print("A frase ou palavra digitada não é um palíndromo!")

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 37. Declare uma variável que por sua vez recebe um nome digitado pelo usuário, em seguida, exiba em tela a mensagem de boas vindas que incorpora o nome anteriormente digitado.
# fazendo uso da f'string

nome = str(input('Digite seu nome: '))

print(f"Bem vindo(a) {nome}, é um prazer te receber em nosso Hotel.")

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 38. Peça para que o usuário digite um número, diretamente dentro da função print() eleve esse número ao quadrado.
# Exiba o resultado incorporado a uma mensagem:

num19 = int(input('Por favor, digite um número: '))

print(f"Você escolheu o númro {num19}, elevado ao quadrado ele resulta em {num19**2}")

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 39. Dada a seguinte lista: ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria'], substitua o terceiro elemento da lista por Jaime:

nomes = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']

nomes[2] = 'Jaime'

print(nomes)

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 40. Adicione o elemento 'Paulo' na lista nomes:

nomes.append('Paulo')

print(nome)

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 41. Adicione o elemento "Eliana" na lista de nomes, esfecificamente na terceira posição:

nomes.insert(2, 'Eliana')

print(nomes)

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 42. Remova o elemento 'Carlos' da lista de nomes:

nomes.remove('Carlos')

print(nomes)

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 43. Mostre o segundo, o terceiro e o quarto elemento da lista de nomes.
# Separadamente, mostre apenas o último elemento da lista de nomes:

print(nomes[1:4])
print(nomes[-1])

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 44. Crie um dicionário via métodos construtor dict(), atribuindo para o mesmo ao menos 5 conjuntos de chaves e valores.
# Utilize objetos e seus valores

dicionario = dict(Pão = 'R$ 1,99',
                  Açúcar = 'R$ 4,99',
                  Café = 'R$ 3,49',
                  Macarrão = 'R$ 3,99',
                  Carne = 'R$ 16,99')

print(dicionario) 

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 45. A partir da seguinte lista ['C', 'JavaScript', 'Lua', 'Python'] verifique primeiramente e retorne se a linguagem de programação Python consta na lista.
# Retorne uma menságem amigável ao usuário para estas duas situações:

linguagens = ['C', 'JavaScript', 'Lua', 'Python']

for i in linguagens:
    if i == "Python":
        print(f"A linguagem {i} está na lista")
    else:
        pass

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 46. A partir de um simples dicionário composto por três itens, {'Alto Nível': 'Python', 'Médio Nível':'C', 'Baixo Nível':'Assembly'}, Verifique se 'Python' consta no dicionário em questão, utilizando de negação lógica para tal verificação.

d = {'Alto Nívelo': 'Python',
     'Médio Nível': 'C',
     'Baixo Nível': 'Assembly'}

# Usa-se o laço for para percorrer cada item de uma lista, dicionário, tupla ou qualquer coisa do tipo
for i in d.values():
    if not i == 'Python':
        print(f"Python não está na lista")
    else:
        print(f"Python consta na lista")
        break

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 47. Crie um dicionário usando o construtor de dicionários do Python, alimente os valores com os dados de duas listas

itens = ['Caneta', 'Lápis', 'Borrecha', 'Caderno']
valores = ['1,99', '0,99', '0,50', '9,90']

dicionario1 = dict(keys = itens, values = valores)

print(dicionario1)
print(type(dicionario1))

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 48. Cie uma simples estrutura de dados simulando um dastro para uma loja. Nesse cadastro debe conter informações como:
# Nome, idade, sexo, estado civil, nacionalidade, faixa de renda, etc... Exiba em tela tais dados

cadastro = {'Nome': 'Alex',
            'Sexo': 'Masculino',
            'Idade': 26,
            'Nascionalidade': 'Brasileiro',
            'Estado civil': 'Solteiro',
            'Escolaridade': 'Cursando Faculdade',
            'Ocupação': 'Desempregado',
            'Renda': 'Sem renda no momento'}

print(cadastro)

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 49. Cire um programa que recebe dados de um aluno como nome e suas notas em supostos 3 trimestres de aula, retornando um novo dicionário com o nome do aluno e a média de suas notas:

aluno = [{'Nome': 'Francisco', 'Notas': [62, 73, 90]}]

def calculo_media(aluno):
    notas = []
    for media in aluno:
        if len(media['Notas']) > 0:
            temp = round(sum(media['Notas']) / len(media['Notas']))
        else:
            temp = 0
        notas.append({'Nome': media['Nome'], 'Média das notas':temp})
    print(notas)

media_estudante = calculo_media(aluno)

print("******************************************************************************************************************************************************")
print()

######################################################################################################################################################

# 50. Crie um sistema de perguntas e respostas com o usuário, pedindo que o mesmo insira um resposta. Caso a primeira questão esteja correta, exiba em tela uma mensagem de acerto e parta para a próxima pergunta, caso incorreta, exiba uma mensagem de erro e pule para a próxima pergunta:

base = {
    'Pergunta 01': {
        'pergunta': 'Quanto é 4 x 4?',
        'Alternativas': {
            'a': '12',
            'b': '24',
            'c': '16',
            'd': '20'
        },
        'Resposta certa': 'c'
    },
    'Pergunta 02': {
        'pergunta': 'Quanto é 6/3?',
        'Alternativas': {
            'a': '2',
            'b': '1',
            'c': '3',
            'd': '4'
        },
        'Resposta certa': 'a'
    }
}

respostas_certas = 0

for pkeys, pvalues in base.items():
    print(f"{pkeys}: {pvalues['pergunta']}")

    for rkeys, rvalues in pvalues['Alternativas'].items():
        print(f"[{rkeys}]: {rvalues}")

    resposta = input('Escolha uma das alternativas: [a], [b], [c] ou [d]: ')

    if resposta == pvalues['Resposta certa']:
        print("Resposta correta!")
        respostas_certas += 1
    else:
        print("Resposta incorreta!")

if respostas_certas == 0:
    print("Você não acertou nenhuma questão.")
elif respostas_certas == 1:
    print("Você acertou uma de duas questões.")
else:
    print('Você acertou todas as duas questões.')
