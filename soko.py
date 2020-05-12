mensajeBienvenida = ''''
Sokoban is a puzzle style game in which the objective is to place every box ($)
in an objective (.)

Author: Luciano Martin Calabresi
Github: https://github.com/klucalabresi
'''



def crear_grilla(desc):
    '''
    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador
    '''
    grilla = []
    for fila in desc:
        linea = []
        for campo in fila:
            linea.append(campo)
        grilla.append(linea)

    return grilla

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    c = len(grilla[0])
    f = len(grilla)
    return c, f

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    if grilla[f][c] == '#':
        return True

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    if grilla[f][c] in {'.','*','+'}:
        return True

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    if grilla[f][c] in {'$','*'}:
        return True

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    if grilla[f][c] in {'@','+'}:
        return True

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    checkeredFlag = True
    for fila in grilla:
        for campo in fila:
            if campo in {'.','+'}:
                checkeredFlag = False

    if checkeredFlag == True:
        return True
    else:
        return False

def ubicacion_jugador(grillaMod):
    for f in range(len(grillaMod)):
        for c in range(len(grillaMod[f])):
            if grillaMod[f][c] in {'@','+'}:
                return f, c

def coor_destino(l, direccion, y, x):
    b, a = y, x 
    if direccion in ('N', 'n'):
        b = b-l
    if direccion in ('S', 's'):
        b = b+l
    if direccion in ('E', 'e'):
        a = a+l
    if direccion in ('W', 'O', 'w', 'o'):
        a = a-l

    return b, a

def mover(grillaOld, direccion):
    '''
Eje y, Eje x
    y, x | Posicion del jugador
    b, a | Posicion de la celda destino
    t, s | Posicion de la celda contigua

    '''
    grillaMod = []
    for fila in grillaOld:
        filaNew = fila.copy()
        grillaMod.append(filaNew)

    y, x = ubicacion_jugador(grillaMod)
    contJugador = grillaMod[y][x]

    b, a = coor_destino(1, direccion, y, x)
    contDestino = grillaMod[b][a]
           
    if contDestino == '#':
        print ('El destino es una pared')

    if contDestino == ' ':
        print('Your destination is a blank')
        grillaMod[b][a] = '@' 
        if   contJugador == '@':
            grillaMod[y][x] = ' '
        elif contJugador == '+':
              grillaMod[y][x] = '.'

    if contDestino == '.':
        print('Your destination is an objective')
        grillaMod[b][a] = '+' 
        if   contJugador == '@':
              grillaMod[y][x] = ' '
        elif contJugador == '+':
              grillaMod[y][x] = '.'

    if contDestino == '$':
        print('Your destination is a box')
        t, s = coor_destino(2, direccion, y, x)
        contContigua = grillaMod[t][s]
        if contContigua in {'$','*'}:
            print ('La contigua es otra caja')
        if contContigua == ' ':
            grillaMod[b][a] = "@"
            grillaMod[t][s] = '$'
            if   contJugador == '@':
                grillaMod[y][x] = ' '
            elif contJugador == '+':
                  grillaMod[y][x] = '.'
        if contContigua == '#':
            print ('La contigua es una pared')
        if contContigua == '.':
            grillaMod[t][s] = '*'
            grillaMod[b][a] = '@'
            if   contJugador == '@':
                  grillaMod[y][x] = ' '
            elif contJugador == '+':
                  grillaMod[y][x] = '.'

    if contDestino == '*':
        print('Your destination is a boxjective')
        t, s = coor_destino(2, direccion, y, x)
        contContigua = grillaMod[t][s]
        if contContigua == ' ':
            grillaMod[t][s] = '$'
            grillaMod[b][a] = "+"
            if   contJugador == '@':
                  grillaMod[y][x] = ' '
            elif contJugador == '+':
                  grillaMod[y][x] = '.'
        if contContigua == '#':
            print ('La contigua es una pared')
        if contContigua == '.':
            grillaMod[t][s] = '*'
            grillaMod[b][a] = '+'
            if   contJugador == '@':
                  grillaMod[y][x] = ' '
            elif contJugador == '+':
                  grillaMod[y][x] = '.'
        if contContigua in {'$','*'}:
            print ('La contigua es otra caja')
    return grillaMod



def bienvenida():
    startGame = input('Do you want to start the game? (Y/N): ')
    if startGame in ('Y', 'y', 'yes'):
        print('''Let's go!''')
        nivel = elegir_nivel()
        return nivel
    elif startGame in ('N', 'n', 'no'):
        print('Why are you even here then?')
        exit()
    else:
        print('Y and N are the only valid options')
        bienvenida()

def elegir_nivel():
    lvl1 = ['########',
            '#@ $ . #',
            '########',]

    lvl2 = ['#####',
            '#.$ #',
            '#@  #',
            '#####',]

    lvl3 = ['########',
            '###   ##',
            '#.@$  ##',
            '### $.##',
            '#.##$ ##',
            '# # . ##',
            '#$ *$$.#',
            '#   .  #',
            '########',]

    numeroNivel = input('Choose a level from 1 to 3: ')
    if numeroNivel.isdigit():
        numeroNivel = int(numeroNivel)
        if numeroNivel > 0 and numeroNivel < 4:
            if numeroNivel == 1:
                nivel = lvl1
            elif numeroNivel == 2:
                nivel = lvl2
            elif numeroNivel == 3:
                nivel = lvl3
        else:
            print('Levels: 1, 2, 3')
            nivel = elegir_nivel()
    else:
        print('Levels: 1, 2, 3')
        nivel = elegir_nivel()
    return nivel

def visualizar(grilla):
    for fila in grilla:
        string = ''
        for campo in fila:
            string = string + campo
        print(string)

def jugando(grilla):
    gameEnd = juego_ganado(grilla)
    visualizar(grilla)
    while gameEnd == False:
        direccion = input('Choose a direction (N, S, E, W): ')
        if direccion in (' '):
            return
        resultado = mover(grilla, direccion)
        grilla = resultado
        visualizar(resultado)
        gameEnd = juego_ganado(grilla)

    if gameEnd == True:
        print("You won!")

def main():
    print('Welcome, this is SOKOBAN')
    print(mensajeBienvenida)
    nivel = bienvenida()
    grilla = crear_grilla(nivel)
    jugando(grilla)
main()



    
    

    



            





