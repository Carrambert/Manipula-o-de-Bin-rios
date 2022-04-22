#TRANSFORMA O PAR DE ENTRADAS QUE ESTÁ EM BINÁRIO EM DECIMAL E MOSTRA
def binario_decimal(num1, num2):
    soma1, soma2 = 0, 0
    contador1, contador2 = 31, 31
    for algarismo in num1:
        if algarismo == '1':
            soma1 += 2**contador1
        contador1 -= 1
    if num1[0] == '1':
        soma1 -= 2**31
        soma1 = soma1*(-1)
    print(soma1)

    for algarismo in num2:
        if algarismo == '1':
            #print(2**contador1)
            soma2 += 2**contador2
        contador2 -= 1
    if num2[0] == '1':
        soma2 -= 2**31
        soma2 = soma2*(-1)
    print(soma2)
    print()
    return soma1,soma2 


#ENCONTRA O MAIOR VALOR DAS DUAS ENTRADAS
def acha_maior(num1,num2,deci1,deci2):
    maior = max(abs(deci1),abs(deci2))
    menor = min(abs(deci1),abs(deci2))
    if maior == abs(deci1):
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1
    return maior, menor


#ORGANIZAR AS OPERAÇÕES DE ACORDO COM OS SINAIS E ORDEM DOS NUMEROS    
def saber_forma(num1, num2, maior, menor):
    
    if(num1[0] == '0' and num2[0] == '0' ):

        return adicao_binarios_positivos(num1, num2) , adicao_binarios_diferentes(maior, menor)
        
    elif(num1[0] == '1' and num2[0] == '1' ):

        return adicao_binarios_negativos(num1, num2) , adicao_binarios_diferentes(maior, menor)

    else:

        if num1[0] == '0' and num2[0] == '1':
            return adicao_binarios_diferentes(maior, menor), adicao_binarios_positivos(num1, num2) 
            #VIRA UMA SUBTRAÇÃO                                 E A SOMA UMA SOMA NORMAL

        else:
            #VIRA UMA SUBTRAÇÃO                              E UMA SOMA DE NEGATIVOS
            return adicao_binarios_diferentes(maior, menor), adicao_binarios_negativos(num1, num2)
            
    
#SOMA DE BINÁRIOS POSITIVOS
def adicao_binarios_positivos(num1, num2):
    ajuda = 0
    resultado = ''
    for i in range(31,-1,-1):
        aux = int(num1[i])+int(num2[i])+ajuda
        if aux <2:
            resultado += str(aux)
            ajuda = 0    
        else:
            resultado += str(aux%2)
            ajuda = aux//2
    resultado = resultado[::-1]
    print(resultado)
    return resultado


#SOMA DE BINÁRIOS NEGATIVOS
def adicao_binarios_negativos(num1, num2):
    ajuda = 0
    resultado = ''
    for i in range(31,-1,-1):
        aux = int(num1[i])+int(num2[i])+ajuda
        if aux <2:
            resultado += str(aux)
            ajuda = 0    
        else:
            resultado += str(aux%2)
            ajuda = aux//2
    resultado = resultado[::-1]
    resultado = resultado.replace(resultado[0],'1',1)
    print(resultado)
    return resultado

#SOMA DE BINÁRIOS COM SINAIS DIFERENTES (É UMA SUBTRAÇÃO)
def adicao_binarios_diferentes(num1, num2):
    ajuda = 0
    resultado = ''
    for i in range(31,-1,-1):
        aux = (int(num1[i])-ajuda)-int(num2[i])
        if aux < 0:
            resultado += '1'
            ajuda = 1
        else:    
            resultado += str(aux)
            ajuda = 0
    resultado = resultado[::-1]
    resultado = resultado.replace(resultado[0],num1[0],1)
    print(resultado)    
    return resultado


#INVERTE PARA REALIZAR A OPERAÇÃO DE C2
def binario_c2_decimal(numero1):
    resultado = ''
    numero1 = str(numero1)
    for c in range(0,32):
        if numero1[c] == '1':
            resultado += '0'
        if numero1[c] == '0':
            resultado += '1'
    #print(resultado)
    return resultado


#UMA FUNÇÃO AUXILIAR PARA SOMAR E APENAS NÃO PRINTAR (PARA SE ADEQUAR A FORMATAÇÃO DA SAÍDA)
def adicao_binarios_positivos_semprint(num1, num2):
    ajuda = 0
    resultado = ''
    for i in range(31,-1,-1):
        aux = int(num1[i])+int(num2[i])+ajuda
        if aux <2:
            resultado += str(aux)
            ajuda = 0    
        else:
            resultado += str(aux%2)
            ajuda = aux//2
    resultado = resultado[::-1]
    return resultado


#VERIFICA QUAIS NÚMEROS DA ENTRADA SÃO NEGATIVOS PARA A OPERAÇÃO DE C2
def teste_negativo(num1, num2):
    if num1[0] == '1':
        numero1_invertido = binario_c2_decimal(num1)
        num1 = adicao_binarios_positivos_semprint(numero1_invertido, binario_auxiliar_C2)
        num1 = num1.replace(num1[0],'1',1)


    if num2[0] == '1':

        numero2_invertido = binario_c2_decimal(num2)
        num2 = adicao_binarios_positivos_semprint(numero2_invertido, binario_auxiliar_C2)
        num2 = num2.replace(num2[0],'1',1)

    return binario_decimal(num1,num2)


#PROGRAMA PRINCIPAL
#LER ARQUIVOS
arquivo = open('arquivo.txt', "r")
listas = arquivo.readlines()
arquivo.close()

aux = 0

#ESSES 2 LOOP'S SÃO PARA "LIMPAR" O VETOR CRIADO COM A LEITURA DO ARQUIVO, LIMPAR DE QUEBRA DE LINHAS E DE ESPAÇOS EM BRANCO!

for i in range(len(listas)):
    listas[i] = listas[i].strip()
    if listas[i] == '':
        aux +=1

for i in range(aux):
    listas.remove('')

    
#AUXÍLIO PARA A LEITURA DAS ENTRADAS DE PARES DE DADOS E A REALIZAÇAO DAS OPERAÇOES EM RELAÇOES AOS PARES
for i in range(0,len(listas),2):
    #SALVANDO OS ELEMENTOS DAS LISTA EM 2 VARIÁVEIS QUE SERÃO UM VETOR PARA A MANIPULAÇÃO EM BINÁRIO!
    numero1, numero2 = listas[i], listas[i+1]
    
#CHAMANDO OPERAÇÕES
    decimal1, decimal2 = binario_decimal(numero1, numero2)
    maior, menor = acha_maior(numero1, numero2, decimal1, decimal2)
    binario_soma, binario_subtracao = saber_forma(numero1, numero2, maior, menor)
    print()
    binario_decimal(binario_soma, binario_subtracao)

    #VARIAVEL PARA NOS AUXILIAR NA OPERAÇAO DE C2
    binario_auxiliar_C2 = '00000000000000000000000000000001'

    #TESTANDO E PRINTANDO OS C2 NEGATIVOS
    teste_negativo(numero1, numero2)

    #EXIBIÇÃO DA SOMA E SUBTRAÇÃO ANTERIORES
    print(binario_subtracao)
    print(binario_soma)

    print()

    #TESTAR QUEM É NEGATIVO PARA REALIZAR A OPERAÇÃO DE C2 OU NÃO
    teste_negativo(binario_subtracao, binario_soma)
 