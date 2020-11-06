#Integrantes:
#Enrique José Carvallo Rioseco     
#César Tomás Roudergue Fuentes


ALTO = 3 #6
ANCHO = 3 #6
VACIO = 0
O = 1
X = 2

#funcion base para delimitar la dimensión del tablero estando vacío
def tableroVacio(alto : int = ALTO, ancho : int = ANCHO) -> list():
  return [[VACIO for i in range(alto)] for j in range(ancho)]

def juegoFinalizado(tablero):
  #if(#vertical
   #  tablero[0][0] ==  tablero[1][0] == tablero[2][0] != VACIO
   #  or tablero[0][1] ==  tablero[1][1] == tablero[2][1] != VACIO
   #  or tablero[0][2] ==  tablero[1][2] == tablero[2][2] != VACIO
     #horizontal
   #  or tablero[0][0] ==  tablero[0][1] == tablero[0][2] != VACIO
   #  or tablero[1][0] ==  tablero[1][1] == tablero[1][2] != VACIO
   #  or tablero[2][0] ==  tablero[2][1] == tablero[2][2] != VACIO
     #diagonal
   #  or tablero[0][0] == tablero[1][1] ==  tablero[2][2] != VACIO
   #  or tablero[0][2] == tablero[1][1] ==  tablero[2][0] != VACIO):
  if n_piezas_rojas == 0:
    return True
  elif n_piezas_azules == 0:
    return True
  else:
    return False

#Con esto pretendo representar las posibles jugadas
#retorna una lista con todas las casillas vacías, como coordenadas
#((X1,Y1), (X2,Y2))
def buscarPosiblesJugadas(jugador, tablero: list()) -> list():
  salida = list()
  alto = len(tablero)
  ancho = len(tablero[0])
  if(not juegoFinalizado(tablero)):
    if jugador: #O
      for y in range(alto):
        for x in range(ancho):
          if(tablero[y][x] == VACIO):

          salida.append((y,x))
    else: #X
      for y in range(alto):
        for x in range(ancho):
          if(tablero[y][x] == VACIO):
          salida.append((y,x))
  return salida

#listaJugadas = lista((Jugador, Fila (Y), Columna(X)))
#Aquí se registran las jugadas hechas dentro del tablero, el cual está vacío desde un inicio.
def llenarTablero(listaJugadas):
  tablero = tableroVacio()
  for jugada in listaJugadas:
    tablero[jugada[1]][jugada[2]] = jugada[0]
  return tablero

#En las funciones calcularTablero y calcularTablero2 se calculan los puntajes en base a las jugadas hechas.
def calcularTablero(tablero: list(), jugador: int):
  #Puntajes: 2 seguidos  = 3, 3 seguidos = 10, interrumpido = 0
  puntaje = 0
  #Verticales
    #Col 0
  if(tablero[0][0] == jugador and tablero[1][0] == jugador and tablero[2][0] == 0):
    puntaje += 3
  if(tablero[0][0] == 0 and tablero[1][0] == jugador and tablero[2][0] == jugador):
    puntaje += 3
  if(tablero[0][0] == jugador and tablero[1][0] == jugador and tablero[2][0] == jugador):
    puntaje += 10
  #***no es necesario, sólo para ejemplificar***
  if(tablero[0][0] == jugador and tablero[1][0] == jugador and tablero[2][0] not in (0,jugador)):
    puntaje += 0
    #Col 1
  if(tablero[0][1] == jugador and tablero[1][1] == jugador and tablero[2][1] == VACIO):
    puntaje += 3
  if(tablero[0][1] == VACIO and tablero[1][1] == jugador and tablero[2][1] == jugador):
    puntaje += 3
  if(tablero[0][1] == jugador and tablero[1][1] == jugador and tablero[2][1] == jugador):
    puntaje += 10
    #Col 2
  if(tablero[0][2] == jugador and tablero[1][2] == jugador and tablero[2][2] == VACIO):
    puntaje += 3
  if(tablero[0][2] == VACIO and tablero[1][2] == jugador and tablero[2][2] == jugador):
    puntaje += 3
  if(tablero[0][2] == jugador and tablero[1][2] == jugador and tablero[2][2] == jugador):
    puntaje += 10
  #Horizontales
    #Row 0
  if(tablero[0][0] == jugador and tablero[0][1] == jugador and tablero[0][2] == VACIO):
    puntaje += 3
  if(tablero[0][0] == VACIO and tablero[0][1] == jugador and tablero[0][2] == jugador):
    puntaje += 3
  if(tablero[0][0] == jugador and tablero[0][1] == jugador and tablero[0][2] == jugador):
    puntaje += 10
    #Row 1
  if(tablero[1][0] == jugador and tablero[1][1] == jugador and tablero[1][2] == VACIO):
    puntaje += 3
  if(tablero[1][0] == VACIO and tablero[1][1] == jugador and tablero[1][2] == jugador):
    puntaje += 3
  if(tablero[1][0] == jugador and tablero[1][1] == jugador and tablero[1][2] == jugador):
    puntaje += 10
    #Row 2
  if(tablero[2][0] == jugador and tablero[2][1] == jugador and tablero[2][2] == VACIO):
    puntaje += 3
  if(tablero[2][0] == VACIO and tablero[2][1] == jugador and tablero[2][2] == jugador):
    puntaje += 3
  if(tablero[2][0] == jugador and tablero[2][1] == jugador and tablero[2][2] == jugador):
    puntaje += 10

  #Diagonales
  if(tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == VACIO):
    puntaje += 3
  if(tablero[0][0] == VACIO and tablero[1][1] == jugador and tablero[2][2] == jugador):
    puntaje += 3
  if(tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == VACIO):
    puntaje += 3
  if(tablero[0][2] == VACIO and tablero[1][1] == jugador and tablero[2][0] == jugador):
    puntaje += 3
  if(tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador):
    puntaje += 10
  if(tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador):
    puntaje += 10

  return puntaje

def calcularTablero2(tablero: list(), jugador: int):
  #Puntajes: 2 seguidos  = 3, 3 seguidos = 10, interrumpido = 0
  puntaje = 0



  return puntaje

#Se muestra el tablero por pantalla.
def imprimirTablero(tablero):
  #[[x,y,0][][]]
  for y in tablero:
    for x in y:
      if(x == VACIO):
        print("_", end = " ")
      elif(x == O):
        print("O", end = " ")
      else:
        print("X", end = " ")
    print()

#((X, 0, 0), (O,0,1))
#Se conservan las jugadas hechas.
def obtenerJugadas(tablero: list()):
  jugadas = list()
  for i, fila in enumerate(tablero):
    for j, valor in enumerate(fila):
      if(valor != VACIO):
        jugadas.append((valor, i, j))
  return jugadas

#Función para los turnos de cada jugador.
def permutar_jugador(jugador):
  if(jugador == X):
    return O
  else:
    return X


def minmax(tablero, jugador, profundidad, favorecer = True):
  #jugadas representa las jugadas actuales en el tablero
  jugadas = obtenerJugadas(tablero)
  #posibles_jugadas representa aquellas posibles jugadas que puede realizar... pero que aún no se han manifestado
  posibles_jugadas = buscarPosiblesJugadas(tablero)
  if(profundidad != 1 and len(posibles_jugadas)>0):
    valores = list()
    for jugada in posibles_jugadas:
      tablero_tmp = llenarTablero(jugadas + [(jugador, jugada[0], jugada[1])])
      valor_de_tablero = minmax(tablero_tmp, permutar_jugador(jugador), profundidad - 1, not favorecer)
      valores.append(valor_de_tablero[0])
    if(favorecer):
      maximo = max(valores)
      jugada = posibles_jugadas[valores.index(maximo)]
      return ((maximo, jugada))
    else:
      minimo = min(valores)
      jugada = posibles_jugadas[valores.index(minimo)]
      return ((minimo, jugada))
  else:
    valores = list()
    for jugada in posibles_jugadas:
      tablero_tmp = llenarTablero(jugadas + [(jugador, jugada[0], jugada[1])])
      valor_de_tablero = calcularTablero(tablero_tmp, jugador)
      valores.append(valor_de_tablero)
    #devolver el resultado calculado
    print(valores, favorecer)
    imprimirTablero(tablero_tmp)
    if(favorecer):
      maximo = max(valores)
      jugada = posibles_jugadas[valores.index(maximo)]
      return ((maximo, jugada))
    else:
      minimo = min(valores)
      jugada = posibles_jugadas[valores.index(minimo)]
      return ((minimo, jugada))

#true O, false X
turno = True

tablero = tableroVacio(ALTO, ANCHO)
imprimirTablero(tablero)

cont = 0
#Aquí se muestran por pantalla todos los datos relevantes del juego, incluyendo el tablero mismo.
while(not juegoFinalizado(tablero) and cont < 33):
  posiblesJugadas = buscarPosiblesJugadas(turno, tablero)
  print(posiblesJugadas)
  print(obtenerJugadas(tablero))
  jugadas = obtenerJugadas(tablero)
  if(turno):
    tablero = llenarTablero(jugadas + [(O, posiblesJugadas[0][0], posiblesJugadas[0][1])])
  else:
    tablero = llenarTablero(jugadas + [(X, posiblesJugadas[0][0], posiblesJugadas[0][1])])
  print("*****************_____\t*****************______")
  imprimirTablero(tablero)
  print(calcularTablero(tablero, O))
  turno = not turno
  cont += 1
  break