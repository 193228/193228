import threading
import random
import time

class filosofosCenando(threading.Thread):
 
    corriendo = True
 
    def __init__(self, nombre, tenedorIzquierdo, tenedorDerecho):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tenedorIzquierdo = tenedorIzquierdo
        self.tenedorDerecho = tenedorDerecho
 
    def run(self):
        while(self.corriendo):
            time.sleep( random.uniform(3,13)) #generando un tiempo aleatorio
            print ('%s Esta hambriento.' % self.nombre)
            self.cenar()
 
    def cenar(self):
        tenedor1, tenedor2 = self.tenedorIzquierdo, self.tenedorDerecho
 
        while self.corriendo:

            tenedor1.acquire(True)
            bloqueo = tenedor2.acquire(False)

            if bloqueo: 
                break

            tenedor1.release()
            #print(self.tenedorIzquierdo,self.tenedorDerecho) ambos tenedores
            print ('%s Intercambio los tenedores.' % self.nombre)
            tenedor1, tenedor2 = tenedor2, tenedor1

        else:
            return
 
        self.cenando()
        tenedor2.release()
        tenedor1.release()
 
    def cenando(self):			
        print ('%s Esta empezando a comer. '% self.nombre)
        time.sleep(random.uniform(1,10))
        print ('%s Termino de comer y se va a pensar.' % self.nombre)

def cenaFilosofos():
    nombreFilosofos = ('Eduardo','Andres','Carlos','Lorena', 'Bethoven') #establezco los nombres de los 5 filosofos
    tenedores = [threading.Lock() for n in range(len(nombreFilosofos))] #establezco los tenedores
    philosophers= [filosofosCenando(nombreFilosofos[i], tenedores[i%5], tenedores[(i+1)%5]) for i in range(len(nombreFilosofos))] #filosofos

    random.seed(507129) #generador de numeros aleatorios
    filosofosCenando.running = True #corriendo el proceso

    for p in philosophers:
        #print(p) impresion de los hilos
        p.start() #inicializo el proceso

    time.sleep(100)
    filosofosCenando.running = False #finalizo el proceso
    print ("Estamos terminados.")
 

if __name__ == "__main__":
    print("Empezando Ejecucion: ")
    cenaFilosofos()
