# -*- coding: utf-8 -*-
"""colores.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tsh5NcdynDbGzlpb9ZcTPln860rxDQ_1
"""

###Crea copia de la imagen
file = open("/home/volcan.bmp","rb")
fileo = open("/home/volcan1.bmp","wb")
### Invierte colores rojo y azul

metadata= file.read(54)
fileo.write(metadata)
file.seek(54,0)
no_pix = 0

while(True):
    pixel_data = file.read(3)
    if(len(pixel_data) > 0):
      pixel_data = pixel_data[::-1] # esta parte invierte la imagen
      fileo.write(pixel_data)
      no_pix += 1

    else:
        break

file.close()
fileo.close()