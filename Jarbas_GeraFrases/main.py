#Criando um gerador de frases aleatórios utilizando uma Gramática Livre de Contexto
#Autor: Jarbas Ribeiro

import random
import os
import ast
import csv
#Listando os arquivos .csv presentes na pasta que está a main.py
def listar_arquivos():
    arquivos_csv = [arquivo for arquivo in os.listdir() if arquivo.endswith('.csv')]
    
    if not arquivos_csv:
        print("Nenhum arquivo .csv encontrado")
        return None
    for i, arquivo in enumerate(arquivos_csv,1):
        print(f"{i} - {arquivo}")
    #Escolhendo um arquivo
    while True:
        try:
            op=int(input("Escolha um arquivo (ou digite 0 para sair): ")) -1
            if op == -1:
                print("Saindo do programa")
                exit()
            if op <=0 or op > len(arquivos_csv):
                caminho_arquivo = arquivos_csv[op]
                gramatica = []
                with open(caminho_arquivo, 'r',encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines() 
                    for linha in linhas: 
                        linha = linha.strip() #Removendo os espaços em branco     
                        if linha: #Verificando se a linha não está vazia
                            regra = eval(linha) #Transformando a string em uma lista
                            gramatica.append(regra)
                print('f"Arquivo {caminho_arquivo} lido com sucesso"')
                #Mostrando a gramática lida
                print("Gramática lida: ")
                for regra in gramatica:
                    naoTerminal = regra[0]
                    producao ="".join(regra[1:])
                    print(f"{naoTerminal} -> {producao}")
                return gramatica
            else:
                print("Opção inválida")
        except ValueError:
            print("Digite um número inteiro")

def printCadeia(cadeia):
    if type(cadeia) is list:
        for filho in cadeia:
            printCadeia(filho)
    else:
        print(cadeia,end="")
#Função para escolher uma regra aleatória. É a mesma função que foi utilizada no exemplo do professor. 
def escolheRegra(naoTerminal,gramatica):
    return [regra[1:] for regra in gramatica if regra[0] == naoTerminal] #Seleciona as regras que estão mais a direita

def geradora(simbolo, naoTerminais, gramatica):
    # Empilhando os simbolos que vão ser processados
    stack = [simbolo]
    while stack:
        atual = stack.pop()
        # Verificando e expandindo se o simbolo atual é um não terminal
        for i in range(len(atual)):
            if atual[i] in naoTerminais:
                # Pega uma regra aleatória
                regra = random.choice(escolheRegra(atual[i], gramatica))
                # Substitui o não terminal pela regra escolhida
                atual[i:i + 1] = regra
                # Empilha a regra escolhida
                stack.append(atual)
                break
    return simbolo

#Função para extrair os não terminais da gramática
def extrair_nao_terminais(gramatica):
    naoTerminais=[]
    for regra in gramatica:
        #Vamos verificar se o não terminal já está na lista
        if regra[0] not in naoTerminais:
            naoTerminais.append(regra[0])
    return naoTerminais

#Vamos pegar apenas o símbolo inicial da gramática
def extrair_simbolo_inicial(gramatica):
    return gramatica[0][0]

#Função para gerar as frases aleatórias
def gerar_frase_aleatoria(token,n):
    if token == 1: #Aqui vamos utilizar a gramática pré definida;
        gramatica = [['S','MP','.'],
             ['MP', 'P'],
             ['MP', 'P', ',','MP'],
             ['P','O ERIC CLAPTON ','A', 'L'],
             ['P','A MARIA BETHÂNIA ', 'A', 'L'],
             ['P','O BOCELLI ', 'A', 'L'],
             ['A','CANTOU COM '],
             ['A','TOCOU COM '],            
             ['L','C', ',', 'L'],
             ['L','C'],
             ['C', 'O MILTON NASCIMENTO '],
             ['C', 'O GILBERTO GIL '],
             ['C', 'A GAL COSTA ']               
            ]
        
        # Lista dos símbolos que são não terminais
        naoTerminais = ['S','MP','P','A','L','C']
        # Símbolo Inicial da gramática
        inicial='S'
        #Mostrando os símbolos não terminais e o símbolo inicial
        print(f"Símbolos não terminais:{naoTerminais}\n")
        print(f"Símbolo Inicial: {inicial}\n")
        #Mostrando a gramática
        print(f"Gramática utilizada: ")
        for regra in gramatica:
            naoTerminal = regra[0]
            producao ="".join(regra[1:])
            print(f"{naoTerminal} -> {producao}")
        print("\n")

        input("Pressione Enter para gerar as frases aleatórias")
        print(f"Frases Aleatórias geradas: ")
        for i in range(0,n,1): #Aqui geramos n frases aleatórias
            simbolo = [inicial]
            frase_gerada = geradora(simbolo,naoTerminais,gramatica)
            print(f"Frase {i+1}: ")
            printCadeia(frase_gerada)
            print()
        print('\n')

    elif token == 2: #Aqui vamos utilizar a gramática que foi lida de um arquivo .csv
        #Selecionando o arquivos .csv
        gramatica = listar_arquivos()
        # Lista dos símbolos que são não terminais
        naoTerminais = extrair_nao_terminais(gramatica)
        # Símbolo Inicial da gramática
        inicial = extrair_simbolo_inicial(gramatica)
        #Mostrando os símbolos não terminais e o símbolo inicial
        print(f"Símbolos não terminais:{naoTerminais}\n")
        print(f"Símbolo Inicial: {inicial}\n")
        #Mostrando a gramática
        print(f"Gramática utilizada: ")
        for regra in gramatica:
            naoTerminal = regra[0]
            producao ="".join(regra[1:])
            print(f"{naoTerminal} -> {producao}")
        print("\n")
        input("Pressione Enter para gerar as frases aleatórias")
        print(f"Frases Aleatórias geradas: ")
        for i in range(0,n,1):
            simbolo = [inicial]
            frase_gerada = geradora(simbolo,naoTerminais,gramatica)
            print(f"Frase {i+1}: ")
            printCadeia(frase_gerada)
            print()

def main():
    try:
        print("Gerador de Frases Aleatórias usando uma Gramática Livre de Contexto")
        print("Selecione uma opção:")
        print("0 - Sair")
        print("1 - Frase Aleatória")
        print("2 - Ler uma gramática dentro de um arquivo CSV")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            print("Saindo...")

        elif opcao == 1:
            print("Frase Aleatória")
            print("Deseja gerar quantas frases?")
            n = int(input("Digite a quantidade de frases: "))
            print("\n")
            gerar_frase_aleatoria(1,n)
        
        elif opcao == 2:
            print("Ler a gramática dentro de um arquivo CSV")
            print("Deseja gerar quantas frases?")
            n = int(input("Digite a quantidade de frases: "))
            print("\n")
            gerar_frase_aleatoria(2,n)

        else:
            print("Opção Inválida")
    except ValueError:
        print("Digite um número inteiro")
    except Exception:
        print("Erro desconhecido")
    finally:
        print("Fim do Programa")

if __name__ == "__main__":
    main()