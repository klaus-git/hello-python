# windrad.py

# Revision 0.01 vom 21.12.2020

from turtle import *
color('black')

pendown()

hideturtle()


def rechteck(seite): # Prozedur rechteck wird definiert
    for i in [1,2]:
        forward(seite); left(90)
        forward(seite/4); left(90)

speed(0) # maximale Zeichengeschwindigkeit
width(2) # Zeichenstiftbreite
for i in range(1,9):
    rechteck(100)
    left(45)
    