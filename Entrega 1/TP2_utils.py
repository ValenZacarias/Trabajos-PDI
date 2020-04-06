import numpy as np
import cv2 as cv
import math

def onclick(event, pto_i, pto_f):
    x_ievent.x, event.y, event.xdata, event.ydata

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


##########################################################
#                                                        #
#            LUT: Transformacion logaritmica             #
# Realiza un mapeo logaritmico en el vector s para la    #
# LUT                                                    #
# imagen de entrada con un rango dinámico grande,        #
# expande las intensidades oscuras y comprime las        #
# intensidades claras.                                   #
#                                                        #
# @param: c                                              #
# @return: s                                             #
#                                                        #
##########################################################

def mapeo_log(c):
    s = np.zeros(256)

    for i in range(256):
        s[i] = (c * np.log(1 + i)) / np.log(256) * 255
        s[i] = max(s[i],0)
        s[i] = min(s[i],255)

    s = s.astype(int)
    return s


##########################################################
#                                                        #
#   LUT: Transformacion de potencia - Correccion gamma   #
# Realiza un mapeo potencial en el vector s para la LUT  #
# Imagen de entrada tiene un rango dinámico bajo, ex-    #
# pande las intensidades claras y comprime las intensi-  #
# dades oscuras.                                         #
#                                                        #
# @param: c                                              #
# @return: s                                             #
##########################################################

def mapeo_potencia(c,gamma):
    s = np.zeros(256)
    for i in range(256):
        s[i] = c * pow(i, gamma)
        s[i] = max(s[i], 0)
        s[i] = min(s[i], 255)
    s = s.astype(np.uint8)
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
# Si el parametro admite valores negativos, entonces el track-  #
# bar debera ser inicializado en 50                             #
#                                                               #
# @param: trackbarName, windowName, valor_inicial, delta        #
# @return: val                                                  #                                        
#################################################################

def param_trackBar(trackbarName, windowName, valor_inicial, delta, negativo=False):
    pos = cv.getTrackbarPos(trackbarName, windowName)
    if(negativo):
        pos = cv.getTrackbarPos(trackbarName, windowName) - 50
    val = valor_inicial + (pos * delta)
    return val

# cv.createTrackBar se le debe pasar una funcion como parametro, como
# se necesita solo la posicion del track bar, le pasamos una que no
# hace nada
def track_change(val):
    pass

