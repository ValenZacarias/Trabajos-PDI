import cv2 as cv
import numpy as np

######################################################################################
#                                                                                    #
#                          FUNCIONES DE OPERACION                                    #
#                                                                                    #
######################################################################################

#########################################################
#                 OPERADOR UMBRAL BINARIO               #
# Binariza la imagen                                    #
# @param: imagen, umbral                                #
#########################################################

def opUmbral(img, umbral):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i,j] < umbral):
                img[i,j] = 0
            else:
                img[i,j] = 255

#########################################################
#         OPERADOR INTERVALO UMBRAL ESCALA GRISES        #
# Ref: umbral es la intensidad (0,255)                   #
# Mantiene escala de grises en el intervalo umbral       #
# lo que este fuera del intervalo se transforma a @color #
# @param: imagen, umbral, color                          #
#########################################################

def opUmbralGrises(img, umbral, color):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (not(img[i,j] >= umbral[0] and img[i,j] <= umbral[1])):
                img[i,j] = color


#########################################################
#                 OPERADOR OFFSET                       #
# agrega/quita brillo a la imagen                       #
# @param: imagen, offset                                #
#########################################################

def opOffset(img, offset):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            px = img[i,j]
            px = px + offset
            if (px < 0):
                img[i,j] = 0
            elif (px > 255):
                img[i,j] = 255
            else:
                img[i,j] = px



