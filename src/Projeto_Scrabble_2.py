abecedario = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O',
'P','Q','R','S','T','U','V','X','Z')
##----------------------------------cria_casa-----------------------------------
def cria_casa(lin,col):
    #verifica que os argumentos recebidos são inteiros, caso nao sejam dá erro
    if not isinstance(lin, int) or not isinstance(col, int):
        raise ValueError("cria_casa: argumentos inválidos")
    #verifica que os argumentos são maiores que 0 e menores ou iguais a 15 caso nao sejam da erro
    if not 0 < lin <= 15 or not 0 < col <= 15:
        raise ValueError("cria_casa: argumentos inválidos")
    #caso os argumentos sejam válidos retorna um dicionario
    return {
        "identificador": "casa",
        "lin": lin,
        "col": col,
    }
##----------------------------------obtem_col-----------------------------------
def obtem_col(c):
    if not eh_casa(c):
        raise ValueError("obtem_col: argumento inválido")
    return c["col"]
##----------------------------------obtem_lin-----------------------------------

def obtem_lin(c):
    if not eh_casa(c):
        raise ValueError("obtem_lin: argumento inválido")
    return c["lin"]
##----------------------------------eh_casa-----------------------------------

def eh_casa(arg):
    #verifica se o argumento dado é um dicionario e que tem o identificador da TAD cria_casa
    if isinstance(arg, dict) and arg["identificador"] == "casa":
        return True
    return False
##----------------------------------casas_iguais-----------------------------------

def casas_iguais(c1,c2):
    #verifica se os argumentos sao validos 
    if eh_casa(c1) and eh_casa(c2):
        #caso sejam verifica se a as linhas e colunas da casa 1 e casa 2 sao iguais
        if c1["lin"] == c2["lin"] and c1["col"] == c2["col"]:
            return True
    return False

##----------------------------------casa_para_str-----------------------------------

def casa_para_str(c):
    if not eh_casa(c):
        raise ValueError("casa_para_str: argumento inválido")
    #retorna os valores da linha e da coluna da casa em string removendo o espaço entre ambos
    return str((c["lin"],c["col"])).replace(" ", "")


##----------------------------------str_para_casa-----------------------------------

def str_para_casa(s):
    # ['1', '2', ',', '1', '5']
    #str_casa remove o primeiro e ultimo caracter da string ou seja passa de "[12,15]" para "12,15" por exemplo
    str_casa = s[1:len(s)-1]
    #string vazia para a linha e coluna
    lin, col = "", ""
    #ainda não foi encontrada virgula(,)
    comma_seen = False
    #percorre todos os caracteres  da str_casa
    for elem in str_casa:
        #se o caracter for um digito e ainda nao tenha passado a virgula, adiciona-o a lin
        if elem.isdigit() and not comma_seen:
            lin += elem
            #se o caracter for um digito e já tenha passado a virgula, adiciona o a col
        if elem.isdigit() and comma_seen:
            col += elem
            #se o elemento for uma virgula muda comma_seen para True
        if elem==",":
            comma_seen = True
    #retorna a casa 
    return cria_casa(int(lin), int(col))

##----------------------------------incrementa_casa-----------------------------------
def incrementa_casa(c,d,s):
    if not eh_casa(c):
        raise ValueError("incrementa_casa: argumento inválido")
    #linha = value do key lin de c e coluna=value do key col de c
    lin, col =c["lin"], c["col"]
    #se a direçao for horizontal adiciona a distancia s a coluna se col+s <=15 e mantem coluna igual se col+s >15
    col = col+s if d=="H" and col+s <= 15 else col
    #se a direçao for vertical adiciona a distancia s a linha se lin+s <=15 e mantem linha igual se lin+s >15
    lin = lin + s if d=="V" and lin+s<=15 else lin
    #retorna a casa com os novos valores de linha e de coluna
    return cria_casa(lin, col)

##----------------------------------TAD JOGADOR-----------------------------------
def cria_humano(nome):
    #verifica se o argumento dado é um string e que não é vazio e caso nao seja dá erro
    if not isinstance(nome, str) or not nome:
        raise ValueError("cria_humano: argumento inválido")
    #caso seja valido retorna um dicionario 
    return {
        "identificador": "jogador",
        "nome": nome,
        "pontos": 0,
        "letras": []
    }

def cria_agente(nivel):
    #verifica se o argumento é um string e que é um dos seguintes ('FACIL', 'MEDIO','DIFICIL'), caso nao seja dá erro
    if not isinstance(nivel, str) or nivel not in ('FACIL', 'MEDIO','DIFICIL'):
        raise ValueError("cria_agente: argumento inválido")
    #caso seja válido retorna um dicionario
    return {
        "identificador": "jogador",
        "nivel": nivel,
        "pontos": 0,
        "letras": []
    }

def jogador_identidade(j):
    #verifica que o identificador é o mesmo da TAD cria_humano/cria_agente e que o argumento j tem o key nome ou o key nivel
    if j["identificador"]=="jogador" and ("nome" in j or "nivel" in j):
        #retorna o nome se o jogador for humano ou o nivel se for um agente
        return j["nome"] if "nome" in j else j["nivel"]

def jogador_pontos(j):
    #verifica que usa o TAD 
    if j["identificador"]=="jogador":
        #retorna os pontos 
        return j["pontos"]
    
def ordenar_lista(l):
    #lista vazia 
    ordenado=[]
    #percorre as letras do abecedario
    for let_a in abecedario:
        #para cada letra do abecedario percorre as letras do l
        for let_l in l:
            #se let_a==let_l adiciona a á lista ordenado e depois passa para a letra seguinte do abecedario e repete o processo
            if let_a==let_l:
                ordenado.append(let_a)
    # retorna a lista ordenada 
    return ordenado

def jogador_letras(j):  
    #verifica que usa a TAD 
    if j["identificador"]=="jogador":
        #retorna um string contendo as letras ordenadas separadas por um espaço
        return "".join(ordenar_lista(j["letras"]))
        
def recebe_letra(j, l):
    #adiciona a letra l ao jogador j
    j["letras"].append(l)
    return j

def usa_letra(j, l):
    #remove a letra l ao jogador j 
    j["letras"].remove(l)
    return j

def soma_pontos(j, p):
    #somas os pontos p ao jogador j 
    j["pontos"] += p
    return j

def eh_jogador(arg):
    #verifica que o arg usa a TAD jogador
    if not isinstance(arg, dict):
        return False
    return True if arg["identificador"]=="jogador" else False

def eh_humano(arg):
    if not isinstance(arg, dict):
        return False
    #verifica que o arg usa a TAD cria_humano
    return True if arg["identificador"]=="jogador" and "nome" in arg else False

def eh_agente(arg):
    if not isinstance(arg, dict):
        return False
    #verifica que o arg usa a TAD cria_agente
    return True if arg["identificador"]=="jogador" and "nivel" in arg else False

def jogadores_iguais(j1, j2):
    #verifica se ambos os jogadores usam a mesma TAD 
    if j1["identificador"]!="jogador" and j2["identificador"]!="jogador":
        return False
    #verifica que ambos sao humanos ou ambos sao agentes
    if ("nome" in j1 and "nivel" in j2) or( "nivel" in j1 and "nome" in j2):
        return False
    #verifica que ambos os jogadores humanos tÊm o mesmo nome
    if ("nome" in j1 and "nome" in j2) and j1["nome"]!=j2["nome"]:
        return False
    #verifica que ambos os jogadores agentes tÊm o mesmo nivel
    if ("nivel" in j1 and "nivel" in j2) and j1["nivel"]!=j2["nivel"]:
        return False
    #verifica se as letras do jogador 1 e do jogador 2 tÊm o mesmo tamanho 
    if len(j1["letras"])!=len(j2["letras"]):
        return False
    #criaçao de duas listas que usam a funçao ordenar_lista para ordenar as letras do j1 e do j2
    j1_ordered, j2_ordered = ordenar_lista(j1["letras"]),ordenar_lista(j2["letras"])
    #percorre os indices da lista letras do jogador 1 
    for i in range(len(j1["letras"])):
        #verifica se as letras ordenadas do j1 e j2 sao iguais
        if j1_ordered[i]!=j2_ordered[i]:
            return False
        #verifica se os pontos do jogador 1 e do jogador 2 sao iguais
    if j1["pontos"]!=j2["pontos"]:
        return False
    #se tudo for igual retorna True
    return True


def jogador_para_str(t):
    #atribui o nome se for humano ou "BOT"nivel se for agente
    nome = t["nome"] if "nome" in t else f"BOT({t['nivel']})"
    #transforma os pontos em string
    pontos = str(t["pontos"])
    #atribui as letras 
    j_letras = " " + " ".join(jogador_letras(t)) if jogador_letras(t) else ""
    #retorna uma string como 'Maria ( 17): A A C D'
    return f"{nome} ({pontos.rjust(3)}):{j_letras}"

def distribui_letras(jog, saco, num):
    #variavel nula 
    count = 0
    saco_length = len(saco)
    #loop de tamanho== len(saco)
    for i in range (saco_length):
        #acaba quando o count==num ou seja quando sao removidas e atribuidas num vezes as letras
        if count==num:
            return jog
        #popped sao as letras removidas do saco
        popped = saco.pop()
        #distribui as letras removidas do saco ao jogador 
        recebe_letra(jog, popped)
        #foi percorrido mais um ciclo
        count+=1
    return jog

def cria_vocabulario(v):
    #verifica que o tuplo contem no minimo uma palavra
    if len(v)<1:
        raise ValueError("cria_vocabulario: argumento inválido")
    #percorre as palavras no tuplo v
    for word in v:
        for let in word:
            if not isinstance(word, str):
                raise ValueError("cria_vocabulario: argumento inválido")
            #verifica que as letras das palavras sao maiusculas e presentes no abecedario
            if not let.isupper() or let not in abecedario:
                raise ValueError("cria_vocabulario: argumento inválido")
        #verifica que cada palavra tem entre 2 a 15 letras
        if not 2 <= len(word) <=15:
            raise ValueError("cria_vocabulario: argumento inválido")            
    #se as condiçoes necessarias forem cumpridas retorna o tuplo vocabulario em forma de dicionario
    return {
        "identificador": "vocabulario",
        "vocab": v
    }

def obtem_pontos(vocabulario, palavra):
    #verifica que vocabulario é um dicionário com a estrutura correta
    if not isinstance(vocabulario, dict) or "vocab" not in vocabulario:
        return 0
    #dicionario com os pontos de cada letra
    pontos_abc = {
    'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2,
    'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8 
    }
    #se a palavra nao estiver nos values da key "vocab" retorna 0
    if palavra not in vocabulario["vocab"]:
        return 0
    pontos = 0
    #percorre cada letra na palavra 
    for let in palavra:
        #adiciona aos pontos o valor equivalente á letra no pontos_abc
        pontos += pontos_abc[let]
        #retorna os pontos
    return pontos


def obtem_palavras(vocabulario, comp, letra):
     #valida vocabulario
    if not isinstance(vocabulario, dict) or "vocab" not in vocabulario:
        return ()
    #criaçao de lista vazia 
    memory_list = []
    #percorre as palavras nps valores do key vocab de vocabulario
    for word in vocabulario["vocab"]:
        #se o comprimento da palavra for igual ao do comp e se a primeira letra da palavra for igual a letra
        if len(word)==comp and word[0] == letra:
            #adiciona a palvra e os pontos correspondentes á lista memory_list
            memory_list.append([word, obtem_pontos(vocabulario, word)])
            #se a memory_list for vazia devolve um tuplo vazio
    if len(memory_list)<1:
        return ()
    #ordena a memory_list usando key=lambda. primeiro ordena por ordem decrescente(-1*)de pontos que é o index 1 da memory_list e de seguida por ordem lexicografica da palvra usando uma funçao auxiliar
    ls_ordenada = sorted(memory_list, key=lambda item: (-1*item[1], ordem_lexicografica(item[0])))
    #retorna um tuplo de um tuplo dos pares (palavra,pontos)
    return tuple(tuple(item) for item in ls_ordenada)


def ordem_lexicografica(word):
    #transforma o alfabeto num dicionario com keys e values do genero do tipo {"A": 0, "B": 1 ....}
    indexed_alphabet = {let: i for i, let in enumerate(abecedario)}
    #percorre a palavra e substitui cada letra pelo indice correspondente
    return [indexed_alphabet[l] for l in word]



def testa_palavra_padrao(vocabulario, palavra, padrao, letras):
    # Valida vocabulario
    if not isinstance(vocabulario, dict) or "vocab" not in vocabulario:
        return False
    #transforma as letras em lista removendo espaços
    else:
        letras_lista = list(letras)
    #verifica se a palavra esta no vocabulario e se o comprimento da palvra é igual ao do padrao e se uma delas nao for retorna false
    if palavra not in vocabulario["vocab"] or len(palavra) != len(padrao):
        return False
    #loop que dura o len(palavra)
    for i in range(len(palavra)):
        #atribui valor á letra e ao padrao 
        let = palavra[i]
        pad = padrao[i]
        #se o padrao for um ponto
        if pad==".":
            #se a let estiver na letras_lista remove a letra da lista
            if let in letras_lista:
                letras_lista.remove(let)
            #se nao estiver retorna false
            else:
                return False
            #se o padrao for uma letra, verifica se a letra da palavra naquela posicao é igual á do padrao e se nao for retorna true
        else:
            if let!=pad:
                return False
            #se as condiçoes forem todas verificadas retorna true
    return True

def ficheiro_para_vocabulario(arg):
    #abre o ficheiro 
    with open(arg) as file:
    #lista das palavras é a as do ficheiro separadas por uma nova linha 
        word_ls = file.read().split("\n")
    #lista vazia para as palavras validas
    valid_words = []
    #percorre as palavras do ficheiro 
    for word in word_ls:
        is_valid = True
        #verifica se cada palvra tem entre 2 e 15 caracteres
        if not 2 <= len(word)<=15:
             is_valid = False
             #percorre cada letra na palavra e verifica se essa letra(maiuscula) está no abecedario
        for let in word:
            if let.upper() not in abecedario:
                is_valid = False
                #se as condiçoes todas forem verificadas adiciona a palavra á lista valid_words
        if is_valid:
            valid_words.append(word.upper())
            #retorna o vocabulario com as palavras validas
    return cria_vocabulario(tuple(valid_words))

def vocabulario_para_str(vocabulario):
    #transforma o vocabulario em lista
    lista_vocab = list(vocabulario["vocab"])
    #memory_order_set cria um dicionario com os elementos que precisamos(palavra,pontos,ordem lexicografica)
    memory_order_set = [{"word": word, "pontos": obtem_pontos(vocabulario, word), "lexi": ordem_lexicografica(word)} for word in lista_vocab]
    #sorted ordena o memory_order_set usando a funçao key=lambda começando pelo comprimento da palavram, depois pela primeira letra , depois pela ordem decrescente dos pontos e finalmente pela ordem lexicografica
    sorted_dic = sorted(memory_order_set, key=lambda item: (len(item["word"]), item["word"][0], -1*item["pontos"], item["lexi"]))
    #string vazia
    final_str = ""
    #percorre o sorted_dic obtendo o indice e a palavra ao mesmo tempo
    for i, word in enumerate(sorted_dic):
        #adiciona a final_str é string com a palvra do dicionario sortes_dic + uma linha a nao ser depois da ultima palavra 
        final_str +=word["word"] + ("\n" if i!= len(sorted_dic)-1 else "")
        #retorna a final_str
    return final_str

def procura_palavra_padrao(vocabulario, padrao, letras, min_pontos):
    #lista vazia
    valid_words = []
    #percorre as palavras no vocabulario 
    for word in vocabulario["vocab"]:
        #se o comprimento da palavra e do padrao forem iguais e testa_palavra_padrao ambas forem validas 
        if len(word)==len(padrao) and testa_palavra_padrao(vocabulario, word, padrao, letras):
            #cria um dicionario com a palavra, os pontos e a ordem lexicografica
            mem_set = {
                "word": word, 
                "pontos":obtem_pontos(vocabulario, word), 
                "lexi": ordem_lexicografica(word)
            }
            #verifica se o primeiro elemento é letra e que a primeira letra da palavra e do padrao sao iguais e que os pontos sao >0 que min_pontos
            if padrao[0]!="." and word[0]==padrao[0] and mem_set["pontos"] >= min_pontos :
                #se as condicoes forem todas verificadas, dá append de mem_set a valid_words
                valid_words.append(mem_set)
                #se o primeiro elemento é um "." e os pontos sao maiores ou iguais a min_pontos 
            if padrao[0]=="."  and mem_set["pontos"] >= min_pontos:
                #dá append de mem_set a valid_words
                valid_words.append(mem_set)
                #se nao existirem palavras validas retorna ("", 0)
    if len(valid_words)<1:
        return ("", 0)
    #ordena a lista pela ordem decrescente dos pontos e de seguida pela ordem lexicografica 
    sorted_ls = sorted(valid_words, key=lambda item: (-1*item["pontos"], item["lexi"] ))
    #retorna um tuplo com a palavra e os pontos correspondentes
    return (sorted_ls[0]["word"], sorted_ls[0]["pontos"])

##----------------------------------TAD TABULEIRO-----------------------------------

def cria_tabuleiro():
    #retorna dicionario com um tabuleiro vazio
    return {
        "identificador": "tabuleiro",
        "tab": [["." for i in range(15)] for i in range(15)]    #double loop começa por adicionar 15 pontos e de seguida repete o processo 15 vezes
    }

def obtem_letra(t, c):
    if not eh_tabuleiro(t):
        raise ValueError("obtem_letra: argumentos inválidos")
    if not eh_casa(c):
        raise ValueError("obtem_letra: argumentos inválidos")
    #menos 1 porque index começa por 0
    lin, col = c["lin"]-1, c["col"]-1
    return t["tab"][lin][col]


def insere_letra(t,c, l):
    if not eh_tabuleiro(t):
        raise ValueError("insere_letra: argumentos inválidos")
    if not eh_casa(c):
        raise ValueError("insere_letra: argumentos inválidos")
    lin, col = c["lin"]-1, c["col"]-1
    #insere letra ao aceder ao key"tab" e substitui a linha lin e coluna col pela letra l
    t["tab"][lin][col] = l
    #retorna o tabuleiro já com a letra inserida
    return t

def eh_tabuleiro(arg):
    if not isinstance(arg, dict):
        return False
    #verifica que está a usar o TAD tabuleiro
    return arg["identificador"]== "tabuleiro"

def eh_tabuleiro_vazio(arg):
    #verifica se está a usar o TAD tabuleiro
    if not eh_tabuleiro(arg):
        return False
    #percorre as colunas do tabuleiro
    for colunas in arg["tab"]:
        #percorre cada elemento nas colunas
        for elem in colunas:
            #se o elemento for uma letra retorna falso 
            if elem!=".":
                return False
    #se as condiçoes forem todas validas retorna true
    return True

def tabuleiros_iguais(t1,t2):
    #verifica que ambos os tabuleiros usam a TAD Tabuleiro e caso um deles nao use retorna False
    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2):
        return False
    #loop 15 vezes 
    for l in range(15):
        #loop interno 15 vezes
        for elem in range(15):
            #verifica todos os valores de linha e coluna possiveis para t1 e t2
            t1Val = t1["tab"][l][elem]
            t2Val = t2["tab"][l][elem]
            #se t1Val != t2Val retorna False
            if t1Val != t2Val:
                return False
    #caso sejam iguais retorna True
    return True

def tabuleiro_para_str(t):
    #cria o visual do tabuleiro
    header ="    " +  "".join([" ".rjust(2) if i<9 else "1".rjust(2) for i in range(15)]) + "\n"
    header += "    " + "".join([str(i+1).rjust(2) if i<9 else str(((i+1)%10)).rjust(2) for i in range(15)])
    sep = "   " + "".join(["-" if i!=0 and i!= 32 else "+" for i in range(33)])
    body = " |\n".join([(str(r+1).rjust(2) + " |" + "".join([t["tab"][r][s].rjust(2) for s in range(15)]) )for r in range(15)])
    return (header+ "\n" + sep + "\n" + body + " |" + "\n" + sep)

def obtem_padrao(t, i, f):
    #atribuiçao de valores á linha e coluna inicial e final
    l_i, c_i = obtem_lin(i), obtem_col(i)
    l_f, c_f = obtem_lin(f), obtem_col(f)
    #a direçao é H se a linha nao mudar e V se a linha mudar
    direcao = "H" if l_i==l_f else "V"
    #comprimento da palavra é (diferenca entre valores)+1
    word_length = (l_f - l_i)+1 if direcao=="V" else (c_f - c_i)+1
    #string vazia
    str_val = ""
    #loop que se repete word_length vezes
    for i in range(word_length):
        #cria as casas sendo que se direçao H as colunas vao aumentando e se V as linhas vao aumentando
        casa = cria_casa(l_i,(c_i +i)) if direcao=="H" else cria_casa(l_i+i ,c_i)
        #atribui a str_value a letra correspondente a cada uma das casas
        str_val += obtem_letra(t, casa)
        #retorna a string com o padrao
    return str_val

def insere_palavra(t,c,d,p):
    #atribui a l e a c os valores da linha e coluna da casa
    l,col = obtem_lin(c),obtem_col(c)
    #loop que se repete len(p) vezes
    for i in range(len(p)):
        #cria casa em que se H coluna vai aumentando e se V linha vai aumentando
        casa = cria_casa(l,col+i) if d=="H" else cria_casa(l+i,col)
        #insere as letras(p[i]) nas casas correspondentes 
        insere_letra(t, casa, p[i])
    return t 


def obtem_subpadroes(t, i, f, l):
    #usa a funcao obtem_padrao para obter o padrao entre as casas i e f
    pattern = obtem_padrao(t,i, f)
    #atribui valores á linha e coluna inicial e final
    l_i, c_i = obtem_lin(i), obtem_col(i)
    l_f, c_f = obtem_lin(f), obtem_col(f)
    #A direçao é H se a linha nao mudar e é V se a linha mudar
    direcao = "H" if l_i==l_f else "V"
    #Houses é uma lista com todas as casas que o padrao ocupa
    houses = [cria_casa(l_i, c_i + index) if direcao=="H" else cria_casa(l_i + index, c_i) for index in range(len(pattern))]
    #criaçao de duas listas vazias para os padroes validos e para as casas validas
    valid_patterns = []
    valid_houses = []
    #loop externo que percorre todas as posiçoes inicias do subpadrao 
    for i in range(len(pattern)):
        #loop interno que percorre todas as posiçoes finais do subpadrao (de tras para a frente) até i (i nao e incluido)
        for j in range(len(pattern), i, -1):
            #obtained_pattern é o subpadrao entre os indices i e j (j nao incluido)
            obtained_pattern = pattern[i:j]
            #numero de pontos e de letras é inicialmente vazio 
            n_points, n_letters = 0,0
            #percorre os caracteres no padrao obtido
            for let in obtained_pattern:
                #se for um ponto adiciona 1 a n_points
                if let == ".":
                    n_points +=1
                #se for uma letra adiciona 1 a n_letters
                else:
                    n_letters +=1
            isValid = True
            #verifica se o caracter imediatamente depois de j é uma letra e se for isValid=False
            if j<len(pattern) and pattern[j]!="." :
                isValid = False
            #Verifica se o caracter imediatamente antes de i é uma letra e se for isValid=False
            if i>0 and pattern[i-1] !=".":
                isValid = False
            #se o subpadrao nao for só pontos e o numero de pontos for igual ou inferior ao numero máximo de pontos(l) e se nao for só letras e se isValid=True
            if not n_points == len(obtained_pattern) and n_points <= l and not n_letters == len(obtained_pattern) and isValid:
                #cria as casas com indice i ao aceder ao dicionario das casas para obter a linha e coluna
                casa = cria_casa(houses[i]["lin"], houses[i]["col"])
                #atribui á lista valid_houses as casas possiveis
                valid_houses.append(casa)
                #atribui á lista valid_patterns os subpadroes possiveis
                valid_patterns.append(obtained_pattern)
    #retorna o tuplo com os padroes válidos e com as casas válidas
    return [tuple(valid_patterns), valid_houses]

def gera_todos_padroes(t,l):
    #patterns é uma lista com tres listas vazias
    patterns = [[],[],[]]
    #percorre as linhas todas 
    for i in range(15):
        #initial e final sao os valores da linha e da coluna 
        initial = (i+1, 1)
        final = (i+1, 15)
        #obtem todos os subpadroes possiveis em cada linha
        valid_patterns = obtem_subpadroes(t, cria_casa(initial[0], initial[1]), cria_casa(final[0], final[1]), l)
        #percorre todos os subpadroes encontrados 
        for index in range(len(valid_patterns[0])):
            #adiciona os padroes válidos á primeira lista 
            patterns[0].append(valid_patterns[0][index])
            #adiciona as casas á segunda lista 
            patterns[1].append(valid_patterns[1][index])
            #adiciona a direçao á terceira lista
            patterns[2].append("H")
    #percorre todas as colunas 
    for i in range(15):
        initial = (1, i+1)
        final = (15, i+1)
        valid_patterns = obtem_subpadroes(t, cria_casa(initial[0], initial[1]), cria_casa(final[0], final[1]), l)
        for index in range(len(valid_patterns[0])):
            patterns[0].append(valid_patterns[0][index])
            patterns[1].append(valid_patterns[1][index])
            patterns[2].append("V")
    #retorna um tuplo com os padroes, as casas e as direçoes
    return (tuple(patterns[0]), tuple(patterns[1]), tuple(patterns[2]))

def gera_numero_aleatorio(estado):
    binary_mask = 0xFFFFFFFF
    #como no python dá para ter numeros de tamanho infinito, usamos bitwise AND operator para estar em 32 bits
    s = estado & binary_mask
    #algoritmo xorshift faz shift ao binario do estado
    s ^= (s << 13) & binary_mask
    s ^= (s >> 17) & binary_mask
    s ^= (s << 5) & binary_mask
    return s & binary_mask

def permuta_letras(letras, estado):
    A = letras
    n = len(A)
    n_aleatorio = estado
    #Fisher-Yates shuffle começa do fim da lista até ao inicio, subtraindo 1
    for i in range(n-1,0, -1):
        n_aleatorio = gera_numero_aleatorio(n_aleatorio)
        #usa a operacao modulo para obter um indice j entre 0 e i+1
        j = n_aleatorio % (i+1)
        #criamos um tuplo e fazemos a troca dos valores A[i] e A[j]
        tuplo = (A[i], A[j])
        A[i] = tuplo[1]
        A[j] = tuplo[0]

def ordenar_conjunto(conj):
    #inicializa uma lista vazia 
    letras_ordenadas = []
    #percorre as letras do alfabeto e se estao no conjunto adiciona-as a lista
    for let in abecedario:
        if let in conj:
            letras_ordenadas.append({
                "letra": let,
                "occ": conj[let]
            })
    final = []
    #percorre a lista letras_ordenadas e adiciona a letra e o numero de vezes que ocorre
    for elem in letras_ordenadas:
        let, occ = elem["letra"], elem["occ"]
       #adiciona a letra occ vezes
        for i in range(occ):
            final.append(let)
    return final

def make_space_jogadores(jog_letras_str):
    str_final = ""
    for i in range(len(jog_letras_str)):
        str_final += jog_letras_str[i] + (" " if i!=len(jog_letras_str)-1 else "")
    return str_final


def baralha_saco(seed):
    #saco é um dicionario com as letras como key e com as ocorrencias como value
    saco = {
        'A': 14, 'B': 3, 'C': 4, 'Ç': 2, 'D': 5, 'E': 11,
            'F': 2, 'G': 2, 'H': 2, 'I': 10, 'J': 2, 'L': 5,
            'M': 6, 'N': 4, 'O': 10, 'P': 4, 'Q': 1, 'R': 6,
            'S': 8, 'T': 5, 'U': 7, 'V': 2, 'X': 1, 'Z': 1 
    }
    #usa a funçao ordenar_conjunto para ordenar o saco
    ordenado = ordenar_conjunto(saco)
    seed = int(seed) 
    #usa a funçao permuta letras para baralhar o saco
    permuta_letras(ordenado, seed)
    #retorna o saco baralhado
    return ordenado

def jogada_humano(tab, jog, vocab, pilha):
    is_valid = True
    #enquanto isValid for true 
    while is_valid:
        #user input que mostra a mensagem "Jogada nome:"
        user_input = input(f"Jogada {jog['nome']}: ")
        #se nao houver input volta ao inicio do loop sem executar o resto do codigo
        if not user_input:
            continue
        #separa a string com espaços e adiciona a uma lista 
        user_list = user_input.split()
        #primeira letra é o indice 0
        first_letter = user_list[0]
        #verifica que a primeira letra é P,T ou J
        if first_letter not in ("P", "T", "J"):
            continue
        #Se a primeira letra for P e nao houver mais nada no input retorna False
        if first_letter == "P" and len(user_input)==1:
            return False
        #Se a primeira letra é T e a pilha tem 7 ou mais letras
        if first_letter=="T" and len(pilha)>=7:
            #percorre cada letra que o jogadore quer trocar
            for i, let in enumerate(user_input):
                #ignora o primeiro caracter("T") e verifica que o jogador tem essa letra
                if i>0 and let in jog["letras"]:
                    #usa letra remove a letra do jogador 
                    usa_letra(jog, let)
                    #distribui_letras adiciona a ultima letra da pilha ao jogador
                    distribui_letras(jog, pilha, 1)
            #retrona True
            return True
        #Se a primeira letra for J e user_list ter comprimento 5 ou seja tem apenas o J Linha Coluna Direçao Palavra
        if first_letter=="J" and len(user_list) == 5:
            #atribuimos os valores ás variáveis
            play, l, c, dir, palavra = user_list
            #Verifica que a linha e coluna sao digitos e entre 1 a 15 e que direçao é H ou V e caso nao sejam volta ao inicio do loop
            if not l.isdigit() or not c.isdigit() or not 0<int(l)<=15 or not 0<int(c)<=15 or dir not in ("H", "V"):
                continue
            #cria casa inicial
            initial = cria_casa(int(l), int(c))
            #cria casa final ao incrementar á cada inicial
            final = incrementa_casa(initial, dir, len(palavra)-1)
            #obtem o padrao entre as duas casas
            pattern = obtem_padrao(tab, initial, final)
            #testa o padrao 
            test_pattern = testa_palavra_padrao(vocab, palavra, pattern, jogador_letras(jog))
            #se o padrao nao for válido volta ao inicio do loop
            if not test_pattern:
                continue
            #atribui valores á linha e á coluna
            linha,col = int(l), int(c)
            passes_center = False
            #percorre a palavra 
            for i in range(len(palavra)):
                #se a linha e a coluna forem iguais a 8 significa que passa pelo centro
                if linha == 8 and col == 8:
                    passes_center = True
                    #sai do loop
                    break
                #se dir==H adiciona 1 á coluna 
                if dir=="H":
                    col +=1
                    #se dir==V adiciona 1 á linha 
                if dir=="V":
                    linha +=1
            #se o tabuleiro for vazio e a palavra nao passa pelo centro rejeita a jogada e volta ao inicio do loop
            if eh_tabuleiro_vazio(tab) and not passes_center:
                continue
            #percorre a palavra
            for i, let in enumerate(palavra):
                #se o caracter do padrao for um ponto
                if pattern[i] == ".":
                    #remove a letra do jogador e distribui uma nova da pilha
                    distribui_letras(jog, pilha, 1)
                    usa_letra(jog, let)
            #insere a palavra no tabuleiro 
            insere_palavra(tab, cria_casa(int(l), int(c)), dir, palavra)
            #adiciona os pontos ao jogador 
            soma_pontos(jog, obtem_pontos(vocab, palavra))
            #retorna True
            return True
    
def jogada_agente(tab, jog, vocab, pilha):
    #gera todos os padroes possiveis considerando as letras do jogador e o tabuleiro
    patterns = gera_todos_padroes(tab,len(jog["letras"]))
    #dicionario para organizar os diferentes niveis
    level_map = {"FACIL": 100, "MEDIO": 50, "DIFICIL": 10}
    #diff_slice serve para obter o value que vai usar para fazer slice
    diff_slice = level_map[jog["nivel"]]
    #padroes viaveis sao alguns dos padroes dependendo do nivel  
    viable_patterns = patterns[0][::diff_slice]
    viable_casas = patterns[1][::diff_slice]
    viable_dirs = patterns[2][::diff_slice]
    #max_point é um dicionário com a informaçao necessaria para o loop
    max_point = {
       "word": None,
        "points": 0,
        "casa": None,
        "dir": None,
        "pat": None
    }
    # percorre os padroes viaveis e procura a palavra com mais pontos
    for i, pat in enumerate(viable_patterns):
        #procura a palavra com mais pontos(retorna (palavra,pontos))
        search_pattern = procura_palavra_padrao(vocab, pat, jogador_letras(jog), 0)
        #se os pontos da palavra forem maiores que os pontos de max_point(ou seja da melhor palavra até agora)
        if search_pattern[1] > max_point["points"]:
            #muda a palavra para a palavra encontrada
            max_point["word"] = search_pattern[0]
            #muda os pontos para os pontos da palavra encontrada 
            max_point["points"] = search_pattern[1]
            #casa é a casa inicial 
            max_point["casa"] = viable_casas[i]
            #atualiza a direçao
            max_point["dir"] = viable_dirs[i]
            #guarda o padrao
            max_point["pat"] = pat
    #se encontrar uma palavra 
    if max_point["word"]!=None:
        #percorre a palavra
        for i, let in enumerate(max_point["word"]):
            #se o caracter for um ponto 
            if max_point["pat"][i] == ".":
                #usa a letra do jogador e atribui-lhe uma nova
                distribui_letras(jog, pilha, 1)
                usa_letra(jog, let)
        #insere a palavra e atualiza os pontos do jogador
        insere_palavra(tab, max_point["casa"], max_point["dir"],max_point["word"])
        soma_pontos(jog,  max_point["points"]) 
        #imprime a jogador por exemplo Jogada MEDIO: J 8 8 H CASA" e retorna True
        print(f"Jogada {jog['nivel']}: J {obtem_lin(max_point['casa'])} {obtem_col(max_point['casa'])} {max_point['dir']} {max_point['word']}")
        return True
    #Se nao encontrar uma palavra e a pilha tiver no minimo 7 letras e o tabuleiro nao estiver vazio tenta trocar
    if max_point["word"]==None and len(pilha) >= 7 and not eh_tabuleiro_vazio(tab):
        #Imprime a jogada por exemplo "Jogada MEDIO: T A B C D E F G"
        letras = make_space_jogadores(jogador_letras(jog))
        print(f"Jogada {jog['nivel']}: T {letras}")
        #percorre as letras do jogador
        for let in jogador_letras(jog):
            #se houver letras na pilha
            if len(pilha)>0:
                #remove a letra do jogador e distribui-lhe uma nova
                usa_letra(jog, let)
                distribui_letras(jog, pilha, 1)
        #retorna True
        return True
    #Se o tabuleiro está vazio ou nao encontrou palavra e nao pode trocar passa a sua vez
    if eh_tabuleiro_vazio(tab) or max_point["word"]==None:
        #Imprime a jogada por exemplo Jogada MEDIO: P
        print(f"Jogada {jog['nivel']}: P")
        #Retorna False
        return False

def scrabble2(jogadores, nome_fich, seed):
    # Valida se jogadores é uma lista/tuplo primeiro:
    if not isinstance(jogadores, (list, tuple)):
        raise ValueError('scrabble2: argumentos inválidos')
    #Verifica que há entre 2 a 4 jogadores e que all(jogadores) #all(jogadores) devolve true se todos os jogadores tiverem caracteres ou seja nao forem strings vazias
    if not 2<=len(jogadores)<=4 or not all(jogadores):
        #se nao forem dá Erro 
        raise ValueError('scrabble2: argumentos inválidos')
    #Valida que todos são strings não vazias:
    for j in jogadores:
        if not isinstance(j, str) or not j:
            raise ValueError('scrabble2: argumentos inválidos')
    #usa funçao baralha_saco para baralhar e organizar a pilha 
    pilha = baralha_saco(seed)
    #inicializa uma lista vazia para os jogadores
    lista_jogadores = []
    #percorre os nomes dos jogadores
    for i,j in enumerate(jogadores):
        #se o primeiro caracter do jogador for @
        if j[0]=="@":
            #cria um agente e adiciona-o á lista de jogadores
            lista_jogadores.append(cria_agente(j[1:]))
        #Se nao for cria um humano e adiciona-o á lista de jogadores
        else:
            lista_jogadores.append(cria_humano(j))
        #pega no jogador que acabou de criar 
        jog = lista_jogadores[i]
        #dá-lhe 7 letras da pilha
        distribui_letras(jog, pilha, 7)
    #cria um tabuleiro vazio
    tab = cria_tabuleiro()
    #lÊ o ficheiro e cria o vocabuláro de palavras válidas 
    vocab = ficheiro_para_vocabulario(nome_fich)
    print("Bem-vindo ao SCRABBLE2.")
    def print_jogadores_para_str():
        #percorre os jogadores já criados
        for j in lista_jogadores:
            #dá print aos jogadores
            print(jogador_para_str(j))
    #imprime o tabuleiro e os jogadores
    print(tabuleiro_para_str(tab))
    print_jogadores_para_str()
    #
    is_valid = True
    player_turn = 0
    n_of_passes = 0
    #Enquanto is_Valid for True
    while is_valid:
        #se o turno for igual ao numero de jogadores dá reset e volta a ser 0
        if player_turn == len(lista_jogadores):
            player_turn = 0
        #jogador é o jogador do qual é o turno
        jog = lista_jogadores[player_turn]
        #gameplay é jogada_humano se o jogador for humano e é jogada_agente se for agente
        gameplay = jogada_humano(tab, jog, vocab, pilha) if eh_humano(jog) else jogada_agente(tab, jog, vocab, pilha)
        #numero de passes é mais um se gameplay for false ou seja se Passar ou volta a 0 se houver uma jogada ou troca
        n_of_passes =  n_of_passes+1 if not gameplay else 0
        #o turno acrescenta 1
        player_turn+=1
        #se o numero de passes for igual ao numero de jogadores is_Valid passa para False e o jogo termina
        if n_of_passes==len(lista_jogadores):
            is_valid = False
            continue
        #Se um jogador nao tiver letras e a pilha nao tiver letras o jogo termina
        if len(jog["letras"])<1 and len(pilha)<1:
            is_valid = False
            continue
        #imprime o tabuleiro e os jogadores depois de cada jogada
        print(tabuleiro_para_str(tab))
        print_jogadores_para_str()
    #Retorna os pontos de todos os jogadores como tuplo
    return tuple([jogador_pontos(j) for j in lista_jogadores])