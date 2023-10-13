"""
En este programa te pelearas por turnos contra el ordenador haciendo uso de 2 opciones de ataque y una opción de bloqueo
"""

import random

#DEFINO LA FUNCIÓN ATAQUE RÁPIDO QUE ME DARÁ EL DAÑO
def ataque_rapido (atacado):
    probabilidad = random.randint(1,10)#CUANTO HACE DE DAÑO ESTE ATAQUE SERÁ 0,10 O 15. PARA ELLO LE PIDO AL ORDENADOR QUE ESCOJA UN NÚMERO ENTRE 1 Y 10 Y ASIGNO UN DAÑO A CADA NÚMERO
    if probabilidad < 2:#EL ATAQUE TENDRÁ CIERTA POSIBILIDAD DE FALLAR
        daño = 0
    elif 2<probabilidad<7:
        daño = 10
    else:
        daño = 15#AÑADO UNA POSIBILIDAD DE ATAQUE CRÍTICO
    return daño

#DEFINO LA FUNCIÓN ATAQUE FUERTE QUE ME DARÁ OTRO DAÑO
def ataque_fuerte (atacado):
    probabilidad=random.randint(1,20)#EL DAÑO DE ESTE ATAQUE SELÁ 0,20 O 25 SEGÚN EL NÚMERO QUE ESCOJA EL ORDENADOR
    if probabilidad<10: #EL ATAQUE TENDRÁ BASTANTE POSIBILIDAD DE FALLAR
        daño = 0
    elif 10<probabilidad<19:
        daño = 20
    else:
        daño = 25#AÑADO UNA POSIBILIDAD DE ATAQUE CRÍTICO
    return daño


#DEFINO EL SISTEMA DEL MINIJUEGO
def batalla (jugador,contrincante):
    while jugador["vida"]>0 and contrincante["vida"]>0:
        decision = input(f"Tu turno, {jugador['nombre']},¿cuál es tu movimiento? (1=ataque rápido/2=ataque fuerte/3=bloquear): ")#LE PIDO AL USUARIO QUE ESCOJA ENTRE LAS 2 OPCIONES DE ATAQUE Y LA DE BLOQUEO

        #DEFINO LAS DISTINTAS ELECCIONES QUE PUEDE HACER EL USUARIO (2 OPCIONES DE ATAQUE Y UNA DE DEFENSA)
        #SI EL USUARIO DECIDE ATACAR, EL ORDENADOR TENDRÁ LAS MISMAS OPCIONES QUE EL JUGADOR
        if decision == "1":
            print("Turno de",contrincante["nombre"])
            decision_maquina_ataque_rapido = random.randint(1,3)
            
            #PLANTEO LOS DISTINTOS ESCENARIOS QUE SE PUEDAN DAR DEPENDIENDO DE LA OPCIÓN QUE ESCOJA EL ORDENADOR HABIENDO EL USUARIO ESCOGIDO LA OPCION DE ATAQUE RÁPIDO
            if decision_maquina_ataque_rapido == 1:
                daño_ataque_rapido=ataque_rapido(contrincante)#UTILIZO LA FUNCIÓN ATAQUE RAPIDO PARA DETERMINAR CUÁNTO DAÑO HA HECHO EL ATAQUE DEL USUARIO O SI LO HA FALLADO
                contrincante["vida"]-=daño_ataque_rapido#SE LE RESTA EL DAÑO DEL ATAQUE A LA VIDA DEL CONTRINCANTE
                if daño_ataque_rapido == 0:#DEFINO LOS DISTINTOS ESCENARIOS QUE PUEDEN OCURRIR DEPENDIENDO DEL DAÑO QUE HAGA EL ATAQUE
                    print("Has fallado el ataque")
                elif daño_ataque_rapido==10:
                    print("El ataque ha hecho", daño_ataque_rapido,"de daño a",contrincante["nombre"],"     vida:",contrincante["vida"])
                else:
                    print("¡El ataque ha sido crítico! Le has hecho",daño_ataque_rapido,"de daño a",contrincante["nombre"],"     vida:",contrincante["vida"])
                daño_ataque_rapido_maquina = ataque_rapido(jugador)#UTILIZO DE NUEVO LA FUNCIÓN ATAQUE RAPIDO ESTA VEZ APLICADA AL ATAQUE DEL ORDENADOR
                jugador["vida"]-=daño_ataque_rapido_maquina#SE LE RESTA EL DAÑO DEL ATAQUE A LA VIDA DEL USUARIO
                if daño_ataque_rapido_maquina == 0:
                    print(contrincante["nombre"],"ha fallado el ataque.     vida:",jugador["vida"])
                elif 0<daño_ataque_rapido_maquina<15:
                    print(contrincante["nombre"],"ha efectuado un ataque rápido haciendote",daño_ataque_rapido_maquina,"de daño.     vida:",jugador["vida"])
                else:
                    print("¡El ataque ha sido crítico!",contrincante["nombre"],"ha efectuado un ataque rápido que te ha hecho",daño_ataque_rapido_maquina,"de daño.     vida:",jugador["vida"])

            #REPITO EL PROCESO ESTA VEZ HABIENDO ESCOGIDO EL ORDENADOR LA OPCIÓN DE ATAQUE FUERTE
            elif decision_maquina_ataque_rapido == 2:
                daño_ataque_rapido=ataque_rapido(contrincante)
                contrincante["vida"]-=daño_ataque_rapido
                if daño_ataque_rapido == 0:
                    print("Has fallado el ataque")
                elif 0<daño_ataque_rapido<15:
                    print("El ataque ha hecho", daño_ataque_rapido,"de daño a",contrincante["nombre"],"     vida:",contrincante["vida"])
                else:
                    print("¡El ataque ha sido crítico! Le has hecho",daño_ataque_rapido,"de daño a",contrincante["nombre"],"     vida:",contrincante["vida"])
                daño_ataque_fuerte_maquina = ataque_fuerte(jugador)
                jugador["vida"]-=daño_ataque_fuerte_maquina
                if daño_ataque_fuerte_maquina == 0:
                    print(contrincante["nombre"],"ha fallado el ataque.     vida:",jugador["vida"])
                elif 0<daño_ataque_fuerte_maquina<25:
                    print(contrincante["nombre"],"ha efectuado un ataque fuerte haciendote",daño_ataque_fuerte_maquina,"de daño.     vida:",jugador["vida"])
                else:
                    print("¡El ataque ha sido crítico!",contrincante["nombre"],"ha efectuado un ataque fuerte que te ha hecho",daño_ataque_fuerte_maquina,"de daño.     vida:",jugador["vida"])
            #DEFINO EL ESCENARIO EN EL QUE EL ORDENADOR BLOQUEA
            elif decision_maquina_ataque_rapido == 3:
                print("Tu ataque rápido ha sido bloqueado por",contrincante["nombre"])
                #SI EL ORDENADOR ESCOGE LA OPCIÓN 3 (BLOQUEAR EL ATAQUE), EL JUGADOR NO LE INFLINGIRÁ DAÑO

        #REPITO EL PROCESO PERO ESTA VEZ PLANTEO LOS DISTINTOS ESCENARIOS HABIENDO ESCOGIDO EL JUGADOR LA OPCIÓN DE ATAQUE FUERTE
        elif decision == "2":
            print("Turno de",contrincante["nombre"])
            decision_maquina_ataque_fuerte=random.randint(1,3)

            if decision_maquina_ataque_fuerte == 1:
                daño_ataque_fuerte=ataque_fuerte(contrincante)
                contrincante["vida"]-=daño_ataque_fuerte
                if daño_ataque_fuerte == 0:
                    print("Has fallado el ataque")
                elif 0<daño_ataque_fuerte<25:
                    print("El ataque ha hecho",daño_ataque_fuerte,"de daño a",contrincante["nombre"],"     vida:",contrincante["vida"])
                else:
                    print("¡El ataque ha sido crítico! Le has hecho",daño_ataque_fuerte,"de daño a",contrincante["nombre"],"     vida:",contrincante["vida"])
                daño_ataque_rapido_maquina = ataque_rapido(jugador)
                jugador["vida"]-=daño_ataque_rapido_maquina
                if daño_ataque_rapido_maquina == 0:
                    print(contrincante["nombre"],"ha fallado el ataque.     vida:",jugador["vida"])
                elif 0<daño_ataque_rapido_maquina<15:
                    print(contrincante["nombre"],"ha efectuado un ataque rápido haciendote",daño_ataque_rapido_maquina,"de daño.     vida:",jugador["vida"])
                else:
                    print("¡El ataque ha sido crítico!",contrincante["nombre"],"ha efectuado un ataque rápido que te ha hecho",daño_ataque_rapido_maquina,"de daño.     vida:",jugador["vida"])

            elif decision_maquina_ataque_fuerte == 2:
                daño_ataque_fuerte=ataque_fuerte(contrincante)
                contrincante["vida"]-=daño_ataque_fuerte
                if daño_ataque_fuerte == 0:
                    print("Has fallado el ataque")
                elif 0<daño_ataque_fuerte<25:
                    print("El ataque ha hecho",daño_ataque_fuerte,"de daño a",contrincante["nombre"],"     vida:",contrincante["vida"])
                else:
                    print("¡El ataque ha sido crítico! Le has hecho",daño_ataque_fuerte,"de daño a",contrincante["nombre"],"     vida:",contrincante["vida"])
                daño_ataque_fuerte_maquina = ataque_fuerte(jugador)
                jugador["vida"]-=daño_ataque_fuerte_maquina
                if daño_ataque_fuerte_maquina == 0:
                    print(contrincante["nombre"],"ha fallado el ataque.")
                elif 0<daño_ataque_fuerte_maquina<25:
                    print(contrincante["nombre"],"ha efectuado un ataque rápido haciendote",daño_ataque_fuerte_maquina,"de daño.     vida:",jugador["vida"])
                else:
                    print("¡El ataque ha sido crítico!",contrincante["nombre"],"ha efectuado un ataque fuerte que te ha hecho",daño_ataque_fuerte_maquina,"de daño.     vida:",jugador["vida"])

            else:
                print("Tu ataque fuerte ha sido bloqueado por",contrincante["nombre"])
                #SI EL ORDENADOR ESCOGE LA OPCIÓN DE BLOQUEAR, DE NUEVO EL USUARIO NO PODRÁ INFINGIRLE DAÑO

        #PLANTEO LOS ESCENARIOS QUE SE PUEDEN DAR SI EL USUARIO DECIDE BLOQUEAR. EN ESTA OPCIÓN EL ORDENADOR NO TENDRÁ LA OPCIÓN DE BLOQUEAR SIN EMBARGO SUS ATAQUES NO INFINGIRÁN DAÑO AL USUARIO
        elif decision == "3":
            print("Turno de",contrincante["nombre"])
            decision_maquina = random.randint(1,2)
            if decision_maquina == 1:
                print("Has bloqueado el ataque rápido de",contrincante["nombre"])
            else:
                print("Has bloqueado el ataque fuerte de",contrincante["nombre"])

        #EN CASO DE QUE EL USUARIO ESCRIBA MAL EL COMANDO U OTRA COSA QUE NO SEAN LAS TRES OPCIONES QUE SE LE DA, DEJO DEFINIDO LO QUE TIENE QUE HACER EL PROGRAMA
        else:
            print("Ha habido un error, intentalo de nuevo.")

        #CUANDO EL USUARIO O EL ORDENADOR SE QUEDEN SIN PUNTOS DE VIDA SE ACABARÁ EL JUEGO
        if contrincante["vida"]<=0:
            print("Has vencido a",contrincante["nombre"])
            break
        
        if jugador["vida"]<=0:
            print("¡Oh no",jugador["nombre"],", has sido derrotado por", contrincante["nombre"])
            break

print("Bien venido al minijuego de pelea de RyperoneR")

#HAGO EL DICCIONARIO DEL "PERSONAJE" DEL USUARIO DE MANERA QUE PUEDA ESCOGER EL NOMBRE
usuario = {
    "nombre": input("Nombre de tu personaje: "),
    "vida": 50
}

#HAGO EL DICCIONARIO DEL "PERSONAJE DEL ORDENADOR"
ordenador = {
    "nombre": "Giuseppe",
    "vida": 50
}  

#UNA VEZ ESPECIFICADO EL NOMBRE DEL "PERSONAJE" DEL USUARIO DARÁ COMIENZO EL JUEGO
batalla(usuario,ordenador)