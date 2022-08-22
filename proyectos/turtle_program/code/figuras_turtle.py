import turtle
import math

def dibujar_figura(lados, tamaño, t):

    for i in range(lados):
        t.fd(tamaño)
        t.lt(360/lados)

def dibujar_rectangulo(lados, tlado1, tlado2, t):

    for i in range(int(lados/2)):
        t.fd(tlado1)
        t.lt(360/lados)
        t.fd(tlado2)
        t.lt(360/lados)

def dibujar_rombo(lados, tamaño, t):

    t.lt(90/2)

    for i in range(lados):
        t.fd(tamaño)
        t.lt(360/lados)

def dibujar_rombo_ha(altura, anchura, lados, t):

    t.lt(90/2)

    medida_h = ((altura/2)**2 + (anchura/2)**2)
    medida_h = math.sqrt(medida_h)

    tamaño_lado = medida_h

    for i in range(lados):
        t.fd(tamaño_lado)
        t.lt(360/lados)

def teoria_seno(ang_b, a, b):
    formula = (math.sin(math.sin(ang_b) * a) / b)**(-1)
    resultado_ang_a = formula
    return resultado_ang_a

def dibujar_rombo_ir(medida_ar, medida_izq, medida_ab, medida_der, t):    ## No da resultado esperado
    
    turtle.setheading(0)

    hipo_1 = (medida_ab**2) + (medida_der**2)
    hipo_1 = math.sqrt(hipo_1)

    hipo_2 = (medida_ar**2) + (medida_der**2)
    hipo_2 = math.sqrt(hipo_2)

    hipo_3 = (medida_ar**2) + (medida_izq**2)
    hipo_3 = math.sqrt(hipo_3)

    hipo_4 = (medida_ab**2) + (medida_izq**2)
    hipo_4 = math.sqrt(hipo_4)

    resultado_ang1 = teoria_seno(90, medida_ab, hipo_1) - 90
    resultado_ang2 = teoria_seno(90, medida_der, hipo_2) - 90
    resultado_ang3 = teoria_seno(90, medida_izq, hipo_3) - 90
    resultado_ang4 = teoria_seno(90, medida_izq, hipo_4) - 90

    lista_angulos = [resultado_ang1, resultado_ang2, resultado_ang3, resultado_ang4]
    movimientos = [hipo_1, hipo_2, hipo_3, hipo_4]

    for i in lista_angulos:
        t.lt(i)
        for n in movimientos:
            t.fd(n)
            break


    
    


wn = turtle.Screen()
mariana = turtle.Turtle()

dibujar_rombo_ir(50, 100, 50, 80, mariana)

wn.mainloop()