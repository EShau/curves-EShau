from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
    x_first = r * math.cos(2 * math.pi * 0) + cx
    y_first = r * math.sin(2 * math.pi * 0) + cy
    for i in range( 1, int(round(1 / step)) + 1 ):
        x_second = r * math.cos(2 * math.pi * i * step) + cx
        y_second = r * math.sin(2 * math.pi * i * step) + cy
        add_edge(   points,
                    int(round(x_first)), int(round(y_first)), int(cz),
                    int(round(x_second)), int(round(y_second)), int(cz) )
        x_first, y_first = x_second, y_second

def add_hermite( points, x0, y0, x1, y1, rx0, ry0, rx1, ry1, step):
    x = generate_hermite_curve_coefs( x0, x1, rx0, rx1 )
    y = generate_hermite_curve_coefs( y0, y1, ry0, ry1 )
    x_first = x[0][0] * 0**3 + x[0][1] * 0**2 + x[0][2] * 0 + x[0][3]
    y_first = y[0][0] * 0**3 + y[0][1] * 0**2 + y[0][2] * 0 + y[0][3]
    for i in range( 1, int(round(1 / step)) + 1 ):
        x_second = x[0][0] * (i * step)**3 + x[0][1] * (i * step)**2 + x[0][2] * (i * step) + x[0][3]
        y_second = y[0][0] * (i * step)**3 + y[0][1] * (i * step)**2 + y[0][2] * (i * step) + y[0][3]
        add_edge(   points,
                    int(round(x_first)), int(round(y_first)), 0,
                    int(round(x_second)), int(round(y_second)), 0 )
        x_first, y_first = x_second, y_second

def add_bezier( points, x0, y0, x1, y1, x2, y2, x3, y3, step):
    x = generate_bezier_curve_coefs( x0, x1, x2, x3 )
    y = generate_bezier_curve_coefs( y0, y1, y2, y3 )
    x_first = x[0][0] * 0**3 + x[0][1] * 0**2 + x[0][2] * 0 + x[0][3]
    y_first = y[0][0] * 0**3 + y[0][1] * 0**2 + y[0][2] * 0 + y[0][3]
    for i in range( 1, int(round(1 / step)) + 1 ):
        x_second = x[0][0] * (i * step)**3 + x[0][1] * (i * step)**2 + x[0][2] * (i * step) + x[0][3]
        y_second = y[0][0] * (i * step)**3 + y[0][1] * (i * step)**2 + y[0][2] * (i * step) + y[0][3]
        add_edge(   points,
                    int(round(x_first)), int(round(y_first)), 0,
                    int(round(x_second)), int(round(y_second)), 0 )
        x_first, y_first = x_second, y_second


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
