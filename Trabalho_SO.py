# corredores tem que chegar em um tempo aleatorio entre 8 e 10 segundos.
# chegada dos corredores em ordem aleatoria.
import threading
import datetime
import random
import time


def cronometro(t):
    total_de_segundos = 0

    while total_de_segundos <= t:
        tempo = datetime.timedelta(seconds=total_de_segundos)
        print(tempo, end='\r')
        time.sleep(1)
        total_de_segundos += 1

    """Verificar o tempo de execução{
        print("cronometro", str(int(time.time())))
    }
    """


def corrida(corredores):
    time.sleep(corredores[0][0])
    print("===========Resultado============")
    print("Tempo:", "%.2f" % corredores[0][0], "- 1º Lugar:", corredores[0][1])
    time.sleep(corredores[1][0] - corredores[0][0])
    print("Tempo:", "%.2f" % corredores[1][0], "- 2º Lugar:", corredores[1][1])
    time.sleep(corredores[2][0] - corredores[1][0])
    print("Tempo:", "%.2f" % corredores[2][0], "- 3º Lugar:", corredores[2][1])

    """Verificar o tempo de execução{
        print("corredores", str(int(time.time())))
    }
    """


runner1 = (random.uniform(8.0, 10.0), "corredor 1")
runner2 = (random.uniform(8.0, 10.0), "corredor 2")
runner3 = (random.uniform(8.0, 10.0), "corredor 3")

corredores = []
tempo_max = max(runner1[0], runner2[0], runner3[0])

if (runner1[0] < runner2[0]) and (runner1[0] < runner3[0]):
    corredores.append(runner1)
    if runner2[0] < runner3[0]:
        corredores.append(runner2)
        corredores.append(runner3)
    else:
        corredores.append(runner3)
        corredores.append(runner2)
elif (runner2[0] < runner1[0]) and (runner2[0] < runner3[0]):
    corredores.append(runner2)
    if runner1[0] < runner3[0]:
        corredores.append(runner1)
        corredores.append(runner3)
    else:
        corredores.append(runner3)
        corredores.append(runner1)
else:
    corredores.append(runner3)
    if runner1[0] < runner2[0]:
        corredores.append(runner1)
        corredores.append(runner2)
    else:
        corredores.append(runner2)
        corredores.append(runner1)

t1 = threading.Thread(target=cronometro, args=(tempo_max,))
t2 = threading.Thread(target=corrida, args=(corredores,))

t1.start()
t2.start()
