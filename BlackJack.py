import random
import os

class Cartas():
    def __init__(self, naipe, face):
        self.naipe = naipe
        self.face = face
        self.valor = valor[face]
        self.impresso = (f'{face} de {naipe}')

    def __str__(self):
        return (f'{self.face} de {self.naipe}')

class Baralho():
    def __init__(self):
        self.baralho = []
        for n in naipe:
            for f in face:
                carta_criada = Cartas(n,f)
                self.baralho.append(carta_criada)
                random.shuffle(self.baralho)

    def sacar_carta(self):
        return self.baralho.pop()

class Banco():
    def __init__(self):
        print('Quantas fichas o senhor traz para a mesa?')
        self.fichas = int(input('Resposta: '))

    def receber(self, valor):
        self.fichas += valor
    
    def apostar(self):
        
        while True:
            print('Gostaria de apostar quantas fichas nesta rodada, senhor?')
            try:
                aposta = int(input('Resposta: '))
                if aposta > self.fichas:
                    print('Infelizmente não será possível. O senhor não possui o suficiente...')
                elif aposta == 0:
                    print('Senhor, é necessário apostar alguma ficha.')
                else:
                    self.fichas -= aposta
                    break
            except:
                print('Por favor apresente um número inteiro, senhor.')
                continue
        return aposta
    
    def __str__(self):
        return str(self.fichas)

class Mesa():                                                       
    def __init__(self, jogador):
        try:
            os.system('cls')                                                                                        # Limpa tela para usuários Windows
        except:
            os.system('clear')                                                                                      # Limpa tela para usuários Linux/ Mac
        print(f'Bem-vindo à mesa de Black Jack, senhor {jogador}.')
    
    def mostrar_jogo_escondido(self, aposta, cartas_dealer, cartas_jogador, valor_jogador, jogador):
        try:
            os.system('cls')                                                                                        
        except:
            os.system('clear')                                           
        print('Cartas da banca:')
        print(f'{cartas_dealer[0]}| ...')
        
        print(f'\nCartas de {jogador}:')
        for i in range(len(cartas_jogador)):
            print(cartas_jogador[i], end= ' | ')
        print(f'\nValor da mão do jogador = {valor_jogador}')
        print(f'Tamanho da aposta: {aposta} fichas.')

    def mostrar_jogo_revelado(self, aposta, cartas_dealer, cartas_jogador, valor_jogador, valor_dealer, jogador):
        try:
            os.system('cls')                                                                                        
        except:
            os.system('clear')  
        print('Cartas da banca:')
        for i in range(len(cartas_dealer)):
            print(cartas_dealer[i], end= ' | ')
        print(f'\nValor da mão da banca = {valor_dealer}')

        print(f'\nCartas de {jogador}:')
        for i in range(len(cartas_jogador)):
            print(cartas_jogador[i], end= ' | ')
        print(f'\nValor da mão do jogador = {valor_jogador}')
        print(f'Tamanho da aposta: {aposta} fichas.')

class Jogador():
    def __init__(self):
        self.nome = input('Nome do jogador: ')
        print('\n')

    def soma(self, cartas_jogador):
        self.valor_mao = 0
        possui_as = False
        for carta in cartas_jogador:
            if carta.valor == 11:
                possui_as = True
            self.valor_mao += carta.valor
        if self.valor_mao > 21 and possui_as == True:
            self.valor_mao -= 10               
        return self.valor_mao
    
    def __str__(self):
        return self.nome

class Dealer():
    def __init__(self):
        pass

    def soma(self, cartas_dealer):
        self.valor_dealer = 0
        possui_as = False
        for carta in cartas_dealer:
            if carta.valor == 11:
                possui_as = True
            self.valor_dealer += carta.valor
            
        if self.valor_dealer > 21 and possui_as == True:
            self.valor_dealer -= 10               

        return self.valor_dealer


if __name__ == '__main__':
    
# VARIÁVEIS CARTAS
    naipe = ['espadas', 'copas', 'paus', 'ouros']
    face  = ['Às', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Rainha', 'Rei']
    valor = {'Às':11, 'Dois':2, 'Três':3, 'Quatro':4, 'Cinco':5, 'Seis':6, 'Sete':7, 'Oito':8, 'Nove':9, 'Dez':10, 'Valete':10, 'Rainha':10, 'Rei':10}

# VARIÁVEIS PARA INICIAR JOGO
    jogo = 'S'
    numero_jogo = 0
    jogador = Jogador()
    mesa = Mesa(jogador)
    dealer = Dealer()
    banco = Banco()

# NOVO JOGO
    while jogo == 'S':                                                                                              # Condição para início de jogo (primeiro e próximos)
        numero_jogo += 1
        aposta = banco.apostar()                                                                                    # Define tamanho da aposta
        baralho = Baralho()                                                                                         # Cria e embaralha o baralho
        cartas_jogador = []                                                                                         # Mão do jogador
        cartas_dealer = []                                                                                          # Mão da banca


        for i in (1,2):
            cartas_jogador.append(baralho.sacar_carta())
            cartas_dealer.append(baralho.sacar_carta())
        
        soma_jogador = jogador.soma(cartas_jogador)                                                                 # Soma pontos do jogador

        mesa.mostrar_jogo_escondido(aposta, cartas_dealer, cartas_jogador, soma_jogador, jogador)                   # Mostra mesa
        if soma_jogador == 21:                                                                                      # Fim da rodada
            print(f'Blackjack, senhor! Meus parabéns! Você receberá {aposta * 2} fichas.')
            jogador_continua = False                                                                                # Jogador não joga mais
            banca_continua = False                                                                                  # Banca não joga mais
        else:
            jogador_continua = True                                                                                 # Jogador continua jogando

        while jogador_continua == True:                                                                             # Próximas jogadas do jogador
            print('\nDeseja sacar uma nova carta, senhor?')                              
            decisao = input('Resposta (S/N): ')
            while decisao.upper() != 'S' and decisao.upper() != 'N':
                print('Por favor, responda "S" ou "N".')
                print('Deseja sacar uma nova carta, senhor?')
                decisao = input('Resposta (S/N): ')
            if decisao.upper() == 'S':
                cartas_jogador.append(baralho.sacar_carta())                                                        # Nova carta para jogador                    
                soma_jogador = jogador.soma(cartas_jogador)
                mesa.mostrar_jogo_escondido(aposta, cartas_dealer, cartas_jogador, soma_jogador, jogador)
                if soma_jogador == 21:                                                                              # Fim da rordada
                    print(f'\nBlackjack, senhor! Meus parabéns! Você receberá {aposta * 2} fichas.')
                    banco.receber(aposta*2)                                                                         # Jogador recebe o dobro da aposta no objeto Banco
                    jogador_continua = False
                    banca_continua = False
                elif soma_jogador > 21:                                                                             # Fim da rodada
                    print('\nA banca vence essa rodada.')
                    jogador_continua = False
                    banca_continua = False
                else:
                    continue                                                                                        # Retorno loop: jogador pode sacar nova carta
            else:                                                                                                   # Jogador opta por não sacar nova carta
                jogador_continua = False
                banca_continua = True
                
        print('A banca irá revelar sua carta.')
        while banca_continua == True:                                                                               # Banca joga    
            soma_dealer = dealer.soma(cartas_dealer)
            mesa.mostrar_jogo_revelado(aposta, cartas_dealer, cartas_jogador, soma_jogador, soma_dealer, jogador)   # Banca mostra suas cartas
            if soma_dealer == 21:                                                                                   # Fim da rodada
                print('\nA banca possui vinte-e-um pontos e portanto vence.')
                banca_continua = False
            elif soma_dealer > 21:                                                                                  # Fim da rodada
                print(f'\nA banca estourou. Parabéns, senhor. Você receberá {aposta *2} fichas.')
                banco.receber(aposta*2)                                                                             # Jogador recebe o dobro da aposta no objeto Banco
                banca_continua = False
            elif soma_dealer > soma_jogador:
                print('\nA banca possui mais pontos que o jogador e portanto vence.')
                banca_continua = False
            else:
                print('\nA banca irá sacar uma nova carta.\n')
                pausa = input('Pressione enter para continuar')                                                     # Controle para visualização da mesa
                cartas_dealer.append(baralho.sacar_carta())                                                         # Banca saca nova carta

# FIM DA RODADA
        print(f'\nO senhor possui {banco} fichas.')                                                                 # Apresenta quantidade de fichas que jogador possui   
        print('Gostaria de jogar uma nova rodada?')
        jogo = input('Resposta (S/N): ')                                                                            # Decide se haverá novo jogo
        while decisao.upper() != 'S' and decisao.upper() != 'N':
                print('Por favor, responda "S" ou "N".')
                print('Gostaria de jogar uma nova rodada, senhor?')
                decisao = input('Resposta (S/N): ')
        if decisao.upper() == 'S':
            continue
        else:
            jogo = 'N'

    print(f'\nFoi um prazer tê-lo conosco, senhor {jogador}')                                                       # Encerramento do programa