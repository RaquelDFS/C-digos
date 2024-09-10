class Filmes: 
    def __init__(self,codigo,genero,ingressos):
        self.codigo = codigo
        self.genero = genero
        self.ingressos = ingressos
    
    def comprar_ingressos(self,qtd_compra):
        while qtd_compra <= 0:
            print(f"Quantidade errada")
            qtd_compra = int(input("Quantos ingressos você gostaria de adquirir?"))     
        while self.ingressos < qtd_compra:
            print(f"Desculpe, mas há apenas {self.ingressos} disponíveis.")
            qtd_compra = int(input("Quantos ingressos você gostaria de adquirir?"))
        print(f"Pedido realizado com sucesso! {qtd_compra} ingresso(s) para filme de {self.genero}. Bom filme!")

f1 = Filmes(1,"Ação",5)
f2 = Filmes(2,"Comédia",1)
f3 = Filmes(3,"Terror",15)

def filme_escolhido(filme):
    print(f"Você escolheu filme de {filme.genero}.")
    print(f"Este filme contém: {filme.ingressos} ingressos disponíveis.")
    qtd_compra = int(input("Quantos ingressos deseja adquirir?"))
    filme.comprar_ingressos(qtd_compra)

def maquina():      
    idade = int(input("Antes de começarmos com o atendimento, quantos anos você tem?"))
    if idade < 18:
            print(f"Desculpe, mas você não pode continuar a compra, até logo!")
            return
    else:
        print("Temos 3 opções de filme para você:")
        print("1 - Ação")
        print("2 - Comédia") 
        print("3 - Terror")       
        passou = False
        while passou == False :
            codigo = int(input("Qual é o filme escolhido? ( digite apenas o número )"))
            match codigo:
                case 1: 
                    filme_escolhido(f1)
                    passou = True
                case 2: 
                    filme_escolhido(f2)
                    passou = True
                case 3: 
                    filme_escolhido(f3)
                    passou = True
                case _:
                    print(f"Opção inválida! Por favor, tente novamente.")
    
print("Olá, bem vindo a Máquina de Ingressos")
filmeCodigo = 0
maquina()