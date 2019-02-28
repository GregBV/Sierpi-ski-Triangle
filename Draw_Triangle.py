# -*- coding: utf-8 -*-

#You need to click on the canvas to set the point the algorithm will start with

from turtle import *
import random as rd
import time



def drawTriangle(x, y):
    goto(x, y)
    dot(4, 'red')
    p=pos()
    n=0
    #◙tracer(True, 5)
    onscreenclick(None)
    while True :
        #time.sleep(2)
       
        prd=P[rd.randint(0, 2)]
        p = ((p[0] + prd[0])/2, (p[1] + prd[1])/2)
        goto(p)
        dot(3)
        n+=1
        if n==50000 :
            break

screensize(500, 500)
#speed(0)
tracer(False)#Very fast when False, shows points being drawn when True and speed(0)
penup()
goto((0, -100))
left(90)
forward(500)
p1=pos()

left(180)
forward(500)

left(60)
forward(500)
p2=pos()

left(180)
forward(500)

left(60)
forward(500)
p3=pos()

P=(p1, p2, p3)
#P = ((-500, -500), (500, -500), (500, 500), (-500, 500))
#p = (rd.randint(-500, 500), rd.randint(-500, 500))
onscreenclick(drawTriangle)


done()


    

