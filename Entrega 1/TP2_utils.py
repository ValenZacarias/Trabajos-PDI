import numpy as np
import cv2 as cv


def onclick(event, pto_i, pto_f):
    return event.button, event.x, event.y, event.xdata, event.ydata

##########################################################
#                                                        #
#           LUT: Transformacion lineal                   #
# Genera un vector con la transformacion lineal, donde   #
# el indice del vector es el valor de gris de la entrada #
# r (0-255) y s (0-255) es el resultado transformado     #
# a ese valor de intensidad r                            #
# //s = a*r + c                                          #
# @param: a, c                                           #
# @return: s                                             #
#                                                        #
##########################################################

def mapeo_ac(a, c):
    s = np.zeros(256)
    for i in range (s.shape[0]):
        s[i] = a*i + c
        s[i] = max(s[i], 0)
        s[i] = min(s[i], 255)
    return np.array(s)

def mapeo_negativo_ac(a,c):
    s = np.zeros(256)
    for i in range (s.shape[0]):
        s[i] = 255 - (a*i + c)
        s[i] = max(s[i], 0)
        s[i] = min(s[i], 255)
    return s

#################################################################
#                                                               #
#         Variacion de valores mediante un trackbar             #
#                                                               #
# Con un trackbar previamente inicializado en una image         #
# Recibe un valor desde el cual arranca el parametro y se le    #
# un delta a ese valor que esta dado por la posicion del        #
# trackbar sobre un "delta" que da el factor de escala (1, 0.1  #
# 0.01, etc)                                                    #
#                                                               #
# @param: trackbarName, windowName, valor_inicial, delta        #
# @return: val                                                  #                                        
#################################################################

def param_trackBar(trackbarName, windowName, valor_inicial, delta):
    val = valor_inicial + (cv.getTrackbarPos(trackbarName, windowName) * delta)
    return val


