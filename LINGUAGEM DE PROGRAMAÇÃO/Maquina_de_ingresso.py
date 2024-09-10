#Objetivos:
    #A Máquina saúda a pessoa e pergunta a idade
    #Se for menor de 18, impede a compra e encerra o atendimento
    #Se for + 18 recomenda 3 filmes
    # filme 1 - ação ; filme 2 romance ; filme 3 terror; 
    # Caso escolha um valor diferente, avisa e pergunta de novo
    # avisa quantos ingressos tem disponíveis de cada e a opção de voltar
    # Caso escolha um valor diferente, avisa e pergunta de novo
    # ao escolher a quantidade de ingressos, se disponível conclui a compra e agradece




def quantidade_Ingressos(genero,quantidade_disponivel, quantidade_escolhido):
    print(f"Você escolheu {genero[genero-1]}, existem {quantidade_ingressos_disponiveis} ingressos disponíveis.")
    quantidade_ingressos_disponiveis = quantidade_disponivel
    quantidade_escolhido = int(input("Quantos ingressos você gostaria de adquirir?"))
    if quantidade_escolhido > quantidade_ingressos_disponiveis:
        print(f"Desculpe, o máximo é de {quantidade_ingressos_disponiveis} ingressos. Tente novamente")
    else:
         if quantidade_escolhido == 1:
            print(f"Pedido realizado de {quantidade_escolhido} ingresso. Bom filme pra você!")
         else:
            print(f"Pedido realizado de {quantidade_escolhido} ingressos. Bom filme pra vocês")

def maquina():      
    filme_escolhido = 0
    idade = int(input("Antes de começarmos com o atendimento, quantos anos você tem?"))

    if idade < 18:
            print(f"Desculpe, mas você não pode continuar a compra, até logo!")
            return

    else:
            print("Temos 3 opções de filme para você:")
            print("1 - Ação")
            print("2 - Comédia")
            print("1 - Terror")


    while filme_escolhido == 0:
        quantidade_ingressos_disponiveis = 0
        filme_escolhido = int(input("Qual é o filme escolhido? ( digite apenas o número )"))
        match filme_escolhido:
            case 1: 
                 filme_escolhido = 1
                 quantidade_Ingressos(1,quantidade_ingressos_disponiveis,5)       
            case 2: 
                 filme_escolhido = 2
                 quantidade_Ingressos(quantidade_ingressos_disponiveis,1)
            case 3: 
                 filme_escolhido = 3
                 quantidade_Ingressos(quantidade_ingressos_disponiveis,15)
            case _:
                print("Opção inválida! Por favor, tente novamente.")
                filme_escolhido = 0

print("Olá, bem vindo a Máquina de Ingressos")
maquina()