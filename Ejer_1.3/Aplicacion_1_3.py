import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

import sys
sys.path.append('../Utils/')

from Utils_Edicion import *
from Utils_Operaciones import *
from Utils_GUI import *

#Se tomó una de las botellas llenas para tener como referencia para los calculos
def botellaReferencia():
    img_modelo = cv.imread("../Data/modelo_botela.tif",cv.IMREAD_GRAYSCALE)
    print(img_modelo)
    opUmbralGrises(img_modelo,(0,210),255)
    pt_med = centroBotella(img_modelo)
    fila_med = img_modelo[pt_med[0]:,pt_med[1]]
    px_llena = np.average(fila_med)
    return px_llena

ref_llena = botellaReferencia()
p_umbral = 0.15   # 15% con respecto a la botella llena
umbral = ref_llena * (1 + p_umbral)     #Si no esta llena, va a tener mas blanco ->255

#Pre-procesamiento
#Se carga la imagen a analizar, se la pre procesa mateniendo la escala de grises dentro del
#intervalo de intensidad (0,210) y por fuera se lo lleva a 255, para eliminar ruido
img = cv.imread("../Data/botellas.tif",cv.IMREAD_GRAYSCALE)
opUmbralGrises(img,(0,210),255)
cv.imshow("transformada ", img)
cv.waitKey(0)
cv.destroyAllWindows()

#Se procesara la imagen tomando de a una botella, aislandola mediante límites en la imagen
#luego se recorta la parte analizada para realizar el mismo procedimiento con el resto de la imagen
#Si se encuentra una botella con menos contenido, se guardan sus coordenadas absolutas de "aislamiento"
#y se guarda su porcentaje de llenado. Una vez analizada toda la imagen, por medio de una imagen copiada
#a RGB, se le realiza un bounding box a cada botella que tenga menos contenido, mediante las coordenadas 
# guardadas
col = 0
contador = 0
vuelta = 1
img_print = img.copy()
roi_i = []
roi_f = []
porcentaje = []
while(img.shape[1]!=0):   
    inicio, fin = coord_bounding_box(img,0,2)
    x_i = inicio[0]
    y_i = inicio[1]
    x_f = fin[0]
    y_f = fin[1]
    
    pt_med = centroBotella(img[:,:x_f])     #Ubica el centro aproximado (en x) de la botella

    col_med = img[pt_med[0]:,pt_med[1]]     #Toma toda la columna

    avg_botella = np.average(col_med)
    #Si la botella tiene menos contenido (teniendo en cuenta un umbral de error de llenado)
    #Se coloca la agrega al vector la posicion absoluta el inicio y final (diagonalmente opuestos)
    #de la ROI donde se encuentra la botella defectuosa. Ademas se guarda su porcentaje de llenado
    #el cual sera >100% debido a que el prom será un numero mayor (por contener mas blanco), por lo
    #que se acomoda mediante algebra
    if(avg_botella > umbral):
        inicio = (x_i + col, y_i)
        fin = (x_f + col, y_f)
        roi_i.append(inicio)
        roi_f.append(fin)

        porc = 200 - (avg_botella*100/ref_llena) 
        porcentaje.append(porc)

    img_rgb, _, _ = bounding_box(img)
    cv.imshow("transformada ", img_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()
    col += x_f
    img = img[:,x_f:].copy()

roi_i = np.array(roi_i)
roi_f = np.array(roi_f)
porcentaje = np.array(porcentaje)
img_RGB = cv.cvtColor(img_print, cv.COLOR_GRAY2RGB)

for i in range(roi_i.shape[0]):
    inicio = (roi_i[0][0],roi_i[0][1])
    fin = (roi_f[0][0],roi_f[0][1])
    cv.rectangle(img_RGB, inicio, fin, color=(0,0,255), thickness=1)
    print("Porcentaje de llenado: ", porcentaje[i], "%")

cv.imshow("transformada ", img_RGB)
cv.waitKey(0)
cv.destroyAllWindows()
   
    






