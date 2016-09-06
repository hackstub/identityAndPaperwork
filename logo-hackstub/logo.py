##############################################################################
# Usage : 
# $ python2 logo.py > logo.svg && eog logo.svg
##############################################################################

from math import pi, sin, cos, atan2

# Configuration

#color = "#222222"
color = "#ffffff"
thickness = 36

paths = [
    # Ha
    [(81, 393), (81, 703)], [(81, 509), (219, 433), (381, 529), (219, 627), (219, 433)], 
    # ck
    [(485, 469), (317, 375), (613, 201)], [(485, 281), (651, 375)], [(485, 161), (485, 779)], 
    # stub
    [(319, 879), (485, 779), (317, 685), (581, 529), (749, 627), (917, 529), (749, 433)], [(749, 615), (749, 317)]
    ]

# Functions

def rotate(Ptorotate, Pcenter, theta) :

    #  Translation +        Rotation                  matrix
    x = Pcenter[0] + Ptorotate[0] * cos(theta) - Ptorotate[1] * sin(theta)
    y = Pcenter[1] + Ptorotate[0] * sin(theta) + Ptorotate[1] * cos(theta)

    return (x,y)

def makeSVGPolygon(P1, P2, r) :

   theta = atan2(P2[1]-P1[1], P2[0]-P1[0])

   Pcenter = (r,0)
   Pup     = (r*cos( pi/3), r*sin( pi/3))
   Pdown   = (r*cos(-pi/3), r*sin(-pi/3))
 
   P1center = rotate(Pcenter, P1, theta+pi)
   P1up     = rotate(Pup,     P1, theta+pi)
   P1down   = rotate(Pdown,   P1, theta+pi)

   P2center = rotate(Pcenter, P2,  theta)
   P2up     = rotate(Pup,     P2,  theta)
   P2down   = rotate(Pdown,   P2,  theta)

   points = ""
   for P in [P1down, P1center, P1up, P2down, P2center, P2up] :
      points += str(round(P[0], 2))+","+str(round(P[1],2))+" "

   return "<polygon points=\""+points+"\" />"

def makeLogo() :

    # Print SVG Header
    print '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg 
       xmlns:dc="http://purl.org/dc/elements/1.1/"
       xmlns:cc="http://creativecommons.org/ns#"
       xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
       xmlns:svg="http://www.w3.org/2000/svg"
       xmlns="http://www.w3.org/2000/svg"
       version="1.1"
       height="1000" 
       width="1000"
       id="logo">
    <style type=\"text/css\" >
    <![CDATA[ polygon { fill:'''+color+'''; stroke-width:0; } ]]>
    </style>
    '''

    # Print polygons from path list

    for path in paths :
        previousPoint = None
        for currentPoint in path :
            if (previousPoint != None) :
                print makeSVGPolygon(previousPoint, currentPoint, thickness)
            previousPoint = currentPoint

    # Print SVG footer

    print "</svg>"



makeLogo()
