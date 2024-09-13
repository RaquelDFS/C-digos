#Listas 
notas_aluno =[]
bimenstre = ["primeiro","segundo","terceiro","quarto"]

#Função que determina se um aluno está aprovado ou não
def sistema_de_aprovacao():

    #Registra o nome do aluno e varivaies necessárias
    nome_aluno = input("Cadastre o nome do aluno:")
    soma_notas = 0
    situacao = None

    #Função que cadastra as notas do aluno
    for b in range(4):
        while True:
            nota = float(input(f"Informe a nota do {bimenstre[b]} bimestre: "))
            if 0 <= nota <= 10:
                break 
            else:
                print("Nota inválida!")
        
        print("---")
        notas_aluno.append(nota)
        soma_notas += nota
    
    #faz a média
    media_aluno = soma_notas / len(bimenstre)

    #teste de verificação
    if media_aluno >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    #Relatório final com o resultado
    print(f"Relatório --- \nAluno(a): {nome_aluno}\nRegistro das notas do primeiro até o quarto bimestre respectivamente:{notas_aluno}\nMédia obtida: {media_aluno}\nSituação regular: {situacao}")

#Chamado da função
sistema_de_aprovacao()