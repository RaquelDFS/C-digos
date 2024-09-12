#Suponha, agora, que você, ainda trabalhando no cinema do estudo de caso da aula passada, precise verificar a aceitação de cinco filmes exibidos no mês.
#Para tanto, será necessário criar um algoritmo que seja capaz de classificar os filmes de 1 a 5 estrelas. Como posso utilizar estruturas de repetição e controle de repetição para elaborar esse algoritmo?

#Mostrar o filme um e atribuir uma nota e assim sucessivamente

filmes = [1,2,3,4,5]


for filme in filmes:
        nota = int(input(f"Voce gostou do filme {filme}?"))