import re

def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]','', cpf)

    if not cpf or len(cpf) != 11:
        return False
    
    novo_cpf = cpf[:-2] #ELIMINA OS DOIS ULTIMOS DIGITOS DO CPF
    reverso = 10 #CONTATOR REVERVSO
    total = 0

    for index in range(19):
        if index > 8: # PRIMEIRO INDICE VAI DE 0 A 9
            index -= 9 # SÃO OS 9 PRIMEIROS DIGITOS DO CPF

        total += int(novo_cpf[index]) * reverso # VALOR TOTAL DA MULTIPLICAÇÃO
        reverso -= 1 # DECREMENTA O CONTATOR REVERSO
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9: # SE O DIGITO FOR > QUE 9 O VALOR É 0 
                d = 0
            total = 0 # ZERA O TOTAL
            novo_cpf += str(d) #CONCATENA O DIGITO GERADO NO NOVO CPF

    # EVITA SEQUENCIAS EX: 111111111, 0000000
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # DESCOBRI QUE SEQUENCIAS AVALIAVAM COMO VERDADEIRO ENTAO TAMBEM
    #ADICIONEI ESSA CHECAGEM AQUI
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False