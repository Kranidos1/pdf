from PIL import Image
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import utils
from reportlab.lib.units import cm
import cv2
#non usata
def get_image(path, width = 1 * cm):
    
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return width ,(width * aspect)

#non usata
def resizeImmagine(path ,x ,y):
    
    image = Image.open(path)
        
    MAX_SIZE = (x,y)
    
    image.thumbnail(MAX_SIZE)
    
    # creating thumbnail
    image.save(path)

#usata
#230x170 quando a destra

def resizeImage(path ,maxX ,maxY) :
    
        image = cv2.imread(path)
        (image_height ,image_width ,_) = image.shape
        resize_metric = 0.8
        while(image_height > maxY or image_width > maxX) :
                    
            image_width = int(image_width * resize_metric)
            image_height = int(image_height * resize_metric)
                    
            resize_metric = resize_metric - 0.05
                    
        image = cv2.resize(image ,(image_width ,image_height))
        cv2.imwrite(path ,image)
            
#calcola ascissa stringa rispetto al font e il suo pointsize
def getStringX(widthPDF ,posXLongest ,stringInput ,font ,fontSize ,flagSide):
    
    #flagSide serve a gestire dove mettere l'immagine se destra o sinistra
    
    string_x = stringWidth(stringInput ,font ,fontSize)
    val_x = widthPDF - string_x - 20
    
    #CALCOLO POSIZIONE RISPETTO LA STRINGA PIU' LUNGA
    if(posXLongest != None):
        
        
        val = (val_x - posXLongest) // 2
        #solo val caso sinistra
        if flagSide == "s" :
            
            return val_x - val
        
        else:
           
            return val
        
    else:
        #CASO STRINGA PIU' LUNGA
        if flagSide == "s" :
            
            return val_x
        
        else :
            
            return val_x - 20
        #-20 caso sinistra
    
#calcola ascissa del titolo basandosi sul font e pointsize
def getStartingStringHeight(heightPDF ,font ,fontSize):
    
    face = pdfmetrics.getFont(font).face
    string_height = (face.ascent - face.descent) / 1000 * fontSize

    val_h = heightPDF - 20 - string_height
    
    return val_h

#calcolo ordinata rispetto a un altezza definita(altezzaA4 o altezza stringa precedente)
def getStringHeight(heightGiven ,font ,fontSize):
    
    face = pdfmetrics.getFont(font).face
    string_height = (face.ascent - face.descent) / 1000 * fontSize

    val_h = heightGiven - string_height
    
    return val_h

#QUANDO L'IMMAGINE E' A SINISTRA
def resizingRight(width ,widthImage ,stringList ,fontsList ,pointsSizeList ,listaLunghezze ,posXLongest ,flagSide):
    
    
    while not all((width - (elem + 20)) > (widthImage + 10) for elem in listaLunghezze): 
                
                
        if (width - (listaLunghezze[0] + 20)) < (widthImage + 10) :
                    
            pointsSizeList[0] = pointsSizeList[0] - 1
                    
        if (width - (listaLunghezze[1] + 20)) < (widthImage + 10) :
                    
            pointsSizeList[1] = pointsSizeList[1] - 1 
                
               
        if (width - (listaLunghezze[2] + 20)) < (widthImage + 10) :
                    
            pointsSizeList[2] = pointsSizeList[2] - 1

        if (width - (listaLunghezze[3] + 20)) < (widthImage + 10) :
                    
            pointsSizeList[3] = pointsSizeList[3] - 1
                      
        #ricalcolo lunghezze in base al font
        lunghezzaTitolo = stringWidth(stringList[0] ,fontsList[0] ,pointsSizeList[0])
        lunghezzaIndirizzo = stringWidth(stringList[1] ,fontsList[1] ,pointsSizeList[1])
        lunghezzaTelefonoIva = stringWidth(stringList[2] ,fontsList[2] ,pointsSizeList[2])
        lunghezzaSitoEmail = stringWidth(stringList[3] ,fontsList[2] ,pointsSizeList[3])
            
        listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail] 
                
        maxLun = max(listaLunghezze)
        indexLongest = listaLunghezze.index(maxLun)
        if(indexLongest == 0) :
                    
            pointSizeLongest = pointsSizeList[0]
            faceName = fontsList[0]
                
        if(indexLongest == 1) :
                    
            pointSizeLongest = pointsSizeList[1]
            faceName = fontsList[1]
                    
        if(indexLongest == 2) :
                    
            pointSizeLongest = pointsSizeList[2]
            faceName = fontsList[2]
                    
        if(indexLongest == 3) :
                    
            pointSizeLongest = pointsSizeList[3]
            faceName = fontsList[3]
                    
        #calcolo la massima
        posXLongest = getStringX(width ,None ,stringList[indexLongest] ,faceName ,pointSizeLongest ,flagSide)
        
    return posXLongest ,pointsSizeList
#resizing quando immagine a destra
def resizingLeft(width ,val ,stringList ,fontsList ,pointsSizeList ,listaLunghezze ,posXLongest ,flagSide) :
    
    
    while not all((elem + 20) < val - 20 for elem in listaLunghezze) :
                
    #resizing dei pointsize in base alle stringhe troppo lunghe e aggiornamento del valore in lista
        if(listaLunghezze[0] + 20) > val - 20 :
                    
            pointsSizeList[0] = pointsSizeList[0] - 1
                    
        if(listaLunghezze[1] + 20) > val - 20 :
                    
            pointsSizeList[1] = pointsSizeList[1] - 1
                    
        if(listaLunghezze[2] + 20) > val - 20 :
                    
            pointsSizeList[2] = pointsSizeList[2] - 1
                    
        if(listaLunghezze[3] + 20) > val - 20 :
                    
            pointsSizeList[3] = pointsSizeList[3] - 1
                
        #ricalcolo lunghezze in base al font
        lunghezzaTitolo = stringWidth(stringList[0] ,fontsList[0] ,pointsSizeList[0])
        lunghezzaIndirizzo = stringWidth(stringList[1] ,fontsList[1] ,pointsSizeList[1])
        lunghezzaTelefonoIva = stringWidth(stringList[2] ,fontsList[2] ,pointsSizeList[2])
        lunghezzaSitoEmail = stringWidth(stringList[3] ,fontsList[3] ,pointsSizeList[3])
            
        listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail] 
                
        maxLun = max(listaLunghezze)
        indexLongest = listaLunghezze.index(maxLun)
        if(indexLongest == 0) :
                    
            pointSizeLongest = pointsSizeList[0]
            faceName = fontsList[0]
                    
        if(indexLongest == 1) :
                    
            pointSizeLongest = pointsSizeList[1]
            faceName = fontsList[1]
                    
        if(indexLongest == 2) :
                    
            pointSizeLongest = pointsSizeList[2]
            faceName = fontsList[2]
                    
        if(indexLongest == 3) :
                    
            pointSizeLongest = pointsSizeList[3]
            faceName = fontsList[3]
                    
        #calcolo la massima
        posXLongest = getStringX(width ,None ,stringList[indexLongest] ,faceName ,pointSizeLongest ,flagSide)
        
    return posXLongest ,pointsSizeList