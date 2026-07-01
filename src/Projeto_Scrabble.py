letras = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O',
'P','Q','R','S','T','U','V','X','Z')

def cria_conjunto(let, occ):
    #verifica se os dois argumentos sao tuplos
    if not isinstance(let, tuple) or not isinstance(occ, tuple): 
        raise ValueError("cria_conjunto: argumentos inválidos")   
    #verifica se os dois tuplos tem o mesmo tamanho
    if len(let) != len(occ):
        raise ValueError("cria_conjunto: argumentos inválidos")
    #Verifica se as letras são todas diferentes pois set nao aceita repetidas
    if len(set(let)) != len(let):
        raise ValueError("cria_conjunto: argumentos inválidos")
    #compara as letras do tuplo com as letras aceitas do alfabeto
    for l in let:
        if l not in letras:
            raise ValueError("cria_conjunto: argumentos inválidos")
    #verifica se todas as ocorrencias são inteiros positivos
    for elem in occ:
        if elem < 1:
            raise ValueError("cria_conjunto: argumentos inválidos")
    #inicialiaza o dicionario final e retorna a letra com a sua ocorrencia
    final_obj = {}
    for i in range(0,len(let)):
        final_obj[let[i]] = occ[i]
    return final_obj

##-----------------gera numero aleatorio-----------------##
def gera_numero_aleatorio(estado):
    binary_mask = 0xFFFFFFFF
    #como no python dá para ter numeros de tamanho infinito, usamos bitwise AND operator para estar em 32 bits
    s = estado & binary_mask
    #algoritmo xorshift faz shift ao binario do estado
    s ^= (s << 13) & binary_mask
    s ^= (s >> 17) & binary_mask
    s ^= (s << 5) & binary_mask
    return s & binary_mask

 ##-----------------permuta letras-----------------##
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

 ##-----------------baralha conjunto-----------------##

    
def baralha_conjunto(conj, estado):
    letras = []
    #loop que percorre as letras do conjunto
    for elem in conj:
        #loop que percorre o numero de ocorrencias da letra no conjunto 
        for i in range(conj[elem]):
            #adiciona a letra a lista o numero de vezes que ocorre
            letras.append(elem)
    lista_ordenada = ordenar_conjunto(conj)
    permuta_letras(lista_ordenada, estado)
    return lista_ordenada

 #helper function que recebe um conjunto de letras e ordena-o
def ordenar_conjunto(conj):
    #inicializa uma lista vazia 
    letras_ordenadas = []
    #percorre as letras do alfabeto e se estao no conjunto adiciona-as a lista
    for let in letras:
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

##-----------------testa palavra padrao-----------------##
def testa_palavra_padrao(palavra, padrao, conj):
    #cria uma copia do conjunto para nao alterar o original
    check_set = conj.copy()
    #verifica se a palavra e o padrao tem o mesmo tamanho
    if len(palavra) != len(padrao):
        return False
    #percorre a palavra 
    for i in range(len(palavra)):
        if padrao[i] == ".":
             # Se a letra da palavra não existir no conjunto permitido, falha
            if palavra[i] not in conj:
                return False
            # Se já usamos todas as ocorrências permitidas dessa letra, falha.
            if check_set[palavra[i]] < 1:
                print("You ran out of " + palavra[i] + "'s")
                return False
            # Caso a letra seja válida, reduz o número de vezes que ainda pode ser usada.
            check_set[palavra[i]] = check_set[palavra[i]] - 1
        else:
         # Se o caractere do padrão não for ponto e não corresponder à letra da palavra, falha.
            if padrao[i] != palavra[i]:
                print(padrao[i] + " instead of " + palavra[i])
                return False
    return True

##-----------------TABULEIRO-----------------##
 ##-----------------cria_tabuleiro-----------------##
def cria_tabuleiro():
    # Cria uma lista vazia que irá conter o tabuleiro
    tab = []
    # Loop para criar 15 linhas — cada linha representa uma linha horizontal do tabuleiro.
    for x in range(15):
        hor_tab = []
        # Loop interno para preencher cada posição da linha com um ponto
        for y in range(15):
            hor_tab.append(".")
        tab.append(hor_tab)
    return tab

 ##-----------------cria_casa-----------------##
def cria_casa(l, c):
    #verifica se os argumentos sao inteiros e se estao entre 1 e 15
    if not isinstance(l, int) or not isinstance(c, int) or not (0 < l <= 15) or not (0 < c <= 15):
        raise ValueError("cria_casa: argumentos inválidos")
    return (l,c)

 ##-----------------obtem_valor-----------------##
def obtem_valor(tab, casa):
    #retorna o tabuleiro com as coordenadas da casa (-1 porque o indice inicial é 0 e nao 1)
    return tab[casa[0]-1][casa[1]-1]

 ##-----------------insere_letra-----------------##
def insere_letra(tab, casa, letra):
    # Coloca a letra (em maiúscula) na posição indicada no tabuleiro.
    tab[casa[0]-1][casa[1]-1] = letra.upper()
    return tab


##-----------------obtem_sequencia-----------------##
def obtem_sequencia(tab, casa, direcao, tamanho):
    # Inicializa a string onde será feita a sequência
    str = ""
    #se a direcao for horizontal percorre as colunas e adiciona 
    if direcao=="H":
        v_count = casa[1]-1
        #adiciona as letras ao tabuleiro tamanho vezes ao adicionar 1 ao indice da coluna(v_count)
        for i in range(0, tamanho):
            str = str + tab[casa[0]-1][v_count]
            v_count = v_count + 1
            #faz a mesma coisa mas para a direcao vertical adicionando 1 ao indice da linha(h_count)
    if direcao=="V":
        h_count = casa[0]-1
        for i in range(0, tamanho):
            str = str + tab[h_count][casa[1]-1]
            h_count = h_count + 1        
    return str
##-----------------insere_palavra-----------------##
def insere_palavra(tab, casa, direcao, palavra):
    l, c = casa[0]-1, casa[1]-1
    c_increment = c
    l_increment = l
    #percorre cada letra da palavra
    for i in range(len(palavra)):
        if direcao=="H":
            #insere a letra na linha fixa e na coluna que vai incrementando
            tab[l_increment ][c_increment] = palavra[i]
            #Avança para a próxima coluna
            c_increment = c_increment + 1
        if direcao=="V":
            #insere a letra na coluna fixa e na linha que vai incrementando
            tab[l_increment][c_increment] = palavra[i]
            #Avança para a próxima linha
            l_increment = l_increment + 1
    return tab
#tabuleiro_para_string
def tabuleiro_para_str(tab):
    #header-------------
    upper_header = ""
    for i in range(15):
         #Resulta num cabeçalho com espaços para colunas 1-9 e '1' para colunas 10-15, formando o "dezena" dos números
        if i>=9:
            upper_header = upper_header + "1".rjust(2)
        elif i<10:
            upper_header = upper_header + " ".rjust(2)
    lower_header = ""
    count = 0
    for i in range(15):
        #Escreve a unidade dos números das colunas: 1 a 9, depois 0 a 5 para 10 a 15
        if i>=9:
            lower_header = lower_header + str(count).rjust(2)
            count = count +1
        elif i<10:
            lower_header = lower_header + str(i+1).rjust(2)
    #separator-------------
    sep_length = 33
    sep_str=""
     # Cria uma linha do tipo "+---------------------------------+"
    for i in range(sep_length):
        if i==0:
            sep_str = "+"
        elif i == sep_length-1:
            sep_str = sep_str + "+"
        else:
            sep_str = sep_str + "-"
    #Body-------------
    body_str=""
      #Cada linha tem o número da linha, uma barra vertical, os valores das casas e termina com barra vertical
    for linha_i in range(15):
        linha_str = str(linha_i+1).rjust(2) + "|".rjust(2)
        for col_i in range(15):
            linha_str = linha_str + tab[linha_i][col_i].rjust(2)
        body_str = body_str + "\n" + linha_str + "|".rjust(2)
    left_padding = "    "
    all_header = left_padding+ upper_header + "\n" + left_padding+ lower_header + "\n" + "   " + sep_str
    all_str =all_header + body_str + "\n" + "   " + sep_str
    return all_str

#def cria_jogador-----------------##
def cria_jogador(ordem, pontos, conj_letras):
    #verifica se a ordem é um inteiro entre 1 e 4
    if not 0<ordem<=4:
        raise ValueError("cria_jogador: argumentos inválidos")
    #atribuimos os valores do jogador a um dicionario
    jog = {
        "id" : ordem,
        "pontos" : pontos,
        "letras" : conj_letras
    }
    return jog
#def jogador_para_str-----------------##
def jogador_para_str(jog):
    #converte os valores do dicionario para string
    user_id = str(jog["id"])
    user_points = str(jog["pontos"]).rjust(3)
    conj_ordenado = ordenar_conjunto(jog["letras"])
    str_f =  f"#{user_id} ({user_points}):"
    #acrescenta as letras do conjunto ordenado separadas por espaço
    for let in conj_ordenado:
        str_f = str_f + " " + let
    return str_f

def distribui_letra(letras, jogador):
    #se não houver letras para distribuir retorna False
    if len(letras)==0:
        return False
    #remove a ultima letra da lista e adiciona ao conjunto do jogador
    popped = letras.pop()
    #se a letra nao estiver no conjunto do jogador adiciona-a com a quantidade 1
    if popped not in jogador["letras"]:
        jogador["letras"][popped] = 1
    else:
        #se ja estiver no conjunto incrementa a quantidade dessa letra por 1
        jogador["letras"][popped]= jogador["letras"][popped]+1
    return True

def joga_palavra(tab, palavra, casa, direcao, conj_letras, primeira):
    l,c = casa[0]-1, casa[1]-1
    #verifica se a palavra cabe no tabuleiro
    if direcao=="H":
        spaces_left = 15 - c
        if len(palavra) > spaces_left:
            return ()
    if direcao=="V":
        spaces_left = 15 - l
        if len(palavra) > spaces_left:
            return ()
        #se for a primeira palavra
    if primeira==True:
        #verifica se a palavra passa pelo centro do tabuleiro
        isCenter = False
        for i in range(len(palavra)):
            if l==7 and c==7:
                isCenter = True
            if direcao=="H":
                c = c + 1
            if direcao=="V":
                l = l + 1
          # se nao passar pelo centro retorna ()      
        if isCenter == False:
            return ()
        #obtem a sequencia do tabuleiro onde a palavra vai ser inserida
    seq = obtem_sequencia(tab, casa, direcao, len(palavra))
    # Verifica se a palavra se encaixa no padrão do tabuleiro e se pode ser formada com as letras disponíveis
    isValid = testa_palavra_padrao(palavra, seq, conj_letras)
    if isValid ==False:
        return ()
    overlapped_letters = []
    if primeira==False:
        #verifica se cruza com outras letras já no tabuleiro
        for let in seq:
            if let!=".":
                overlapped_letters.append(let)
        if len(overlapped_letters) < 1:
            return ()
        
    #insere a palavra no tabuleiro
    insere_palavra(tab, casa, direcao, palavra)
    returnArr = []
    #se for a primeira palavra retorna todas as letras da palavra
    if primeira==True:
        returnArr = list(palavra)
        #se nao for a primeira palavra retorna as letras que nao se cruzam com outras ja no tabuleiro
    else:
        overlap_index = []
        #enumerate retorna o indice e a letra da palavra
        for i,let in enumerate(palavra):
            for let_o in overlapped_letters:
                #se a letra e a letra do tabuleiro forem iguais adiciona o indice a overlap_index
                if let == let_o:
                    overlap_index.append(i)
                    #remove a letra da lista overlapped_letters para nao contar duas vezes a mesma letra
                    overlapped_letters.pop(0)
                    #cria uma string com as letras que nao se cruzam
        returnStr = ""
        for i in range(len(palavra)):
            if i not in overlap_index:
                returnStr = returnStr + palavra[i]
                #ordena a lista das letras novas e retorna-a como tuplo
        returnArr = list(returnStr)
    return tuple(ordenar_lista(returnArr))
      

def ordenar_lista(l):
    #lista vazia onde vamos adicionar as letras ordenadas
    ordenado=[]
        #percorre as letras do alfabeto e se estao na lista l adiciona-as a lista ordenado mantendo a ordem de letras
    for let_a in letras:
        for let_l in l:
            if let_a==let_l:
                ordenado.append(let_a)
    return ordenado

def check_casa_str(n):
    #se n nao for numerico ou < 1 ou > 15 retorna False
    if not n.isnumeric():
        return False
    if not 1 <= int(n) <= 15:
        return False
    return True

def processa_jogada(tab, jog, pilha, pontos, primeira):
    isValid = False
    while isValid==False:
        #pede input ao jogador e converte para maiusculas
        user_input_str = input("Jogada J"+str(jog["id"]) + ": ").upper()
        #extrai o primeiro caracter do input para decidir o tipo de jogada
        input_list = list(user_input_str)
        first_l = input_list[0]
        #se o primeiro caracter for P(passar), T(trocar) ou J(jogar)
        if first_l in ["P", "T", "J"]:
            #se for passar e o input apenas tiver 1 caracter retorna False para passar a vez)
            if first_l=="P" and len(input_list)==1:
                isValid = True
                return False   
            #se for trocar verifica se o input tem o formato correto
            if first_l=="T":
                for i, let in enumerate(input_list):
                    #se i for 0 o caracter tem de ser T e seguido de um espaço logo vÊ se i é par e maior que 1
                    if i>1 and i%2==0:
                        #remove a letra do jogador e distribui uma nova letra usando a funcao distribui_letra
                        if let in jog["letras"]:
                            jog["letras"][let] = jog["letras"][let]-1
                            distribui_letra(pilha, jog)
                isValid = True
                return True
            if first_l=="J":
                #verifica se o input tem o formato correto (espaço depois do j e nao terminar com espaço)
                if input_list[1]!=" " or input_list[len(input_list)-1]==" ":
                    continue
                #remove J e espaco do inicio para facilitar a extração das outras partes
                input_list.pop(0)
                input_list.pop(0)
                #extrai a palavra comecando do fim da lista ate encontrar um espaço ou uma letra que nao esteja no conjunto
                palavra = ""
                for i in range(len(input_list)-1, 0, -1):
                    if input_list[i]==" " or input_list[i] not in letras:
                        break
                    else:
                        palavra = palavra + input_list[i]
                #reverte a palavra para a ordem correta exemplo "OLÁ" em vez de "ÁLO"
                palavra = palavra[::-1]
                #remove as letras usadas do input_list
                for i in range(len(palavra)+1):
                    input_list.pop()
                #extrai a direção
                if input_list[len(input_list)-2]!=" ":
                    continue
                d = input_list[len(input_list)-1]
                if d!="V" and d!="H":
                    continue
                input_list.pop()
                input_list.pop()
                #extrai as coordenadas da casa len tem de ser entre 3 e 5(ex: 8"8 ou 12"12)
                r, c="",""
                if not 3 <= len(input_list) <=5:
                    isValid= False
                #se ambas as casas forem de 1 digito como 8 8
                if len(input_list)==3:
                    #verifica se o caracter do meio é um espaço
                    if(input_list[1])!=" ":
                        continue
                    #verifica se as casas sao validas
                    if not check_casa_str(input_list[0]) or not check_casa_str(input_list[2]):
                        continue
                    #atribui os valores de r e c transformando os valores da lista para inteiros e subtraindo 1 para coincidir com o indice do tabuleiro
                    r, c = int(input_list[0])-1, int(input_list[2])-1
                # se um for de 1 digito e o outro de 2 digitos como 8 12 ou 12 8
                if len(input_list)==4:
                    #------se o primeiro for de 1 digito como['8', ' ', '1', '5']
                    if input_list[1]==" ":
                        check_r = check_casa_str(input_list[0])
                        check_c = check_casa_str(input_list[2])+check_casa_str(input_list[3])
                        if not check_r or not check_c:
                            continue
                        r, c = int(input_list[0])-1, int(input_list[2]+input_list[3])-1
                        #se o segundo for de 1 digito como ['1', '2', ' ', '8']
                    if input_list[2]==" ":
                        check_r = check_casa_str(input_list[0])+check_casa_str(input_list[1])
                        check_c = check_casa_str(input_list[3])
                        if not check_r or not check_c:
                            continue
                        r, c = int(input_list[0]+input_list[1])-1, int(input_list[3])-1                             
                # se ambas as casas forem de 2 digitos como 12 12
                if len(input_list)==5:
                    if input_list[2]==" ":
                        check_r = check_casa_str(input_list[0])+check_casa_str(input_list[1])
                        check_c = check_casa_str(input_list[3])+check_casa_str(input_list[4])
                        if not check_r or not check_c:
                            continue
                        r, c = int(input_list[0]+input_list[1])-1, int(input_list[3]+input_list[4])-1 
                        #verifica se r e c sao inteiros
                if not isinstance(r, int) or not isinstance(c, int):
                    continue
                            #tab, jog, pilha, pontos, primeira  
                            #obtem a sequencia do tabuleiro para verificar se a palavra pode ser jogada ali
                seq = obtem_sequencia(tab, cria_casa(r+1,c+1), d, len(palavra))
                isValid = testa_palavra_padrao(palavra, seq, jog["letras"])
                if isValid ==False:
                    continue
                #Se a jogada é válida, insere a palavra no tabuleiro e atualiza os pontos
                jogada = joga_palavra(tab, palavra, cria_casa(r+1,c+1), d, jog["letras"], primeira)
                if len(jogada)==0:
                    continue
                #Calcula pontos da palavra
                palavra_pontos = 0
                for letra in palavra:
                    palavra_pontos = palavra_pontos + pontos[letra]
                jog["pontos"] = jog["pontos"] + palavra_pontos
                #remove as letras usadas do conjunto do jogador e distribui novas letras
                for used_letter in jogada:
                    jog["letras"][used_letter] = jog["letras"][used_letter] - 1
                    distribui_letra(pilha, jog)
                    #se a letra ja nao existir no conjunto do jogador remove-a
                    if jog["letras"][used_letter]==0:
                        jog["letras"].pop(used_letter)
                isValid=True
                return True         
            
def scrabble(jogadores, saco, pontos, seed):
    #verifica se o numero de jogadores é entre 1 e 4
    if not 0 < jogadores <=4:
        raise ValueError("scrabble: argumentos inválidos")
    #verifica se o conjunto de pontos sao validos
    if check_points(pontos)== False:
        raise ValueError("scrabble: argumentos inválidos")
    print("Bem-vindo ao SCRABBLE.")
    tab = cria_tabuleiro()
    print(tabuleiro_para_str(tab))
    #criar jogadores
    list_jogadores = []
    for i in range(jogadores):
        jogador = {
            "id": i+1,
            "pontos": 0,
            "letras": cria_conjunto((),())
        }
        list_jogadores.append(jogador)
    #usando a funçao baralha_conjunto baralhamos o saco
    shuffled_saco = baralha_conjunto(saco, seed)
    #distribui 7 letras a cada jogador
    for jog in list_jogadores:
        for i in range(7):
            distribui_letra(shuffled_saco, jog)
    for jog in list_jogadores:
        print(jogador_para_str(jog))
    #---------------inicio da gameplay-----------------##
    isFirst = True
    passes = 0
    playerTurn = 0
    endGame = False
    #enquanto o jogo está ativo
    while endGame==False:
        #gameplay retorna True se o jogador jogou ou trocou letras
        gameplay = processa_jogada(tab, list_jogadores[playerTurn], shuffled_saco, pontos, isFirst)
        #Se o jogador passar (porque gameplay retorna false quando o jogador passa) a vez incrementa o numero de passes
        if not gameplay:
            passes = passes +1
            #Se todos os jogadores passarem a vez o jogo termina
        if passes==len(list_jogadores):
            endGame = True
            break
        #Se a casa central dor diferente de "." significa que a primeira jogada ja foi feita 
        if tab[7][7]!=".":
            isFirst=False
            #se o conjunto do jogador e o saco estiverem ambos vazios o jogo termina
        if saco_vazio(list_jogadores[playerTurn],shuffled_saco):
            endGame=True
            #incrementa a vez do jogador por 1 
        playerTurn = playerTurn + 1
        #se o jogador for o ultimo da lista volta ao primeiro jogador e zera o numero de passes
        if playerTurn == len(list_jogadores):
            playerTurn= 0
            passes = 0
        print(tabuleiro_para_str(tab))
        for jog in list_jogadores:
            print(jogador_para_str(jog))
    #acabou a jogada e inicializa uma lista vazia para os pontos
    pontos_list = []
    #adiciona os pontos de cada jogador a pontos_list e retorna em tuplo
    for jog in list_jogadores:
        pontos_list.append(jog["pontos"])
    return tuple(pontos_list)

def saco_vazio(jog, saco):
    if len(jog["letras"])<1:
        return True
    #se o conjunto de letras do jogador estiver vazio retorna True
    for let in jog["letras"]:
        #se o jogador ainda tiver letras saco_jogador_vazio=False
        if jog["letras"][let]!=0:
            return False
    saco_vazio = True
    for let in saco:
        #verifica se o saco ainda tem letras
        if saco[let]!=0:
            saco_vazio=False
        #se o saco e o conjunto do jogador estiverem ambos vazios retorna True
    if saco_vazio==True:
        return True
    return False

def check_points(point_set):
    #verifica se o conjunto de pontos tem todas as letras do alfabeto
    for let in letras:
        if let not in point_set:
            return False
    return True



def letras_linha(tab,lin):
    casas=[]
    for i in range(15):
        if tab[lin-1][i-1] != ".":
            casas.append(cria_casa(lin,i))
    return tuple(casas)

tab=cria_tabuleiro()
insere_palavra(tab,cria_casa(8,3),"H","FUNDAMENTOS")
print(letras_linha(tab,7))