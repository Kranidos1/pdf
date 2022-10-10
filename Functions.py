from PIL import Image
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import utils
from reportlab.lib.units import inch, cm

def get_image(path, width = 1 * cm):
    
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return width ,(width * aspect)

def resizeImmagine(path ,x ,y):
    
    image = Image.open(path)
        
    MAX_SIZE = (x,y)
    
    image.thumbnail(MAX_SIZE)
    
    # creating thumbnail
    image.save(path)

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

#quando il testo e' a destra e immagine a sinistra ridimensiona il pointsize per entrare in un determinato spazio
def resizingOrizzontaleLatoDestro(width ,posXLongest ,listaValutazione ,listaFields ,listaStringhe ,flagSide ,loopFlag ,fontsList ,pointSizeList ,maxPointX):
    
    while loopFlag == 1:

        
        if not all(elem > maxPointX for elem in listaFields) or not listaValutazione[0] > maxPointX:
            
            
            #resizing
            pointSizeList[0] = pointSizeList[0] - 1
            pointSizeList[1] = pointSizeList[1] - 1
            pointSizeList[2] = pointSizeList[2] - 1
            pointSizeList[3] = pointSizeList[3] - 1   
            
        else:
                    
            loopFlag = 0
            
        #ricalcola
        posXTitolo = getStringX(width ,posXLongest ,listaStringhe[0] ,fontsList[0] ,pointSizeList[0] ,flagSide)
        posXIndirizzo = getStringX(width ,posXLongest ,listaStringhe[1] ,fontsList[1] ,pointSizeList[1] ,flagSide)
        posXSitoEmail = getStringX(width ,posXLongest ,listaStringhe[3] ,fontsList[3] ,pointSizeList[3] ,flagSide)
        posXTelefonoIva = getStringX(width ,posXLongest ,listaStringhe[2] ,fontsList[2] ,pointSizeList[2] ,flagSide)
        listaValutazione = [posXTitolo ,posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]
        listaFields = [posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]
        
        #stringa più lunga che permette di centralizzare le stirnghe
        longestString = min(listaValutazione)
        indexLongest = listaValutazione.index(longestString)
        
        #CASO TITOLO
        if(listaStringhe[indexLongest] == listaStringhe[0]):
            
            posXLongest = getStringX(width ,None ,listaStringhe[indexLongest] ,fontsList[0] ,pointSizeList[0] ,flagSide)
        
        else:
            
            if(indexLongest == 1):
                
                longestFaceNameFont = fontsList[1]
                longestPointSize = pointSizeList[1]
                
            elif(indexLongest == 2):
                
                longestFaceNameFont = fontsList[2]
                longestPointSize = pointSizeList[2]
                
            else:     
                
                longestFaceNameFont = fontsList[3]
                longestPointSize = pointSizeList[3]                           
                
            posXLongest = getStringX(width ,None ,listaStringhe[indexLongest] ,longestFaceNameFont ,longestPointSize ,flagSide)
    
        
    return posXLongest ,pointSizeList

#quando il testo e' a sinistra e immagine a destra ridimensiona il pointsize per entrare in un determinato spazio
def resizingOrizzontaleLatoSinistro(width ,posXLongest ,listaValutazione ,listaLunghezze ,listaStringhe ,flagSide ,loopFlag ,fontsList ,pointSizeList):
    
    
    while loopFlag == 1:
        
        lunghezzaTitolo = stringWidth(listaStringhe[0] ,fontsList[0] ,pointSizeList[0])
        lunghezzaIndirizzo = stringWidth(listaStringhe[1] ,fontsList[1] ,pointSizeList[1])
        lunghezzaTelefonoIva = stringWidth(listaStringhe[2] ,fontsList[2] ,pointSizeList[2])
        lunghezzaSitoEmail = stringWidth(listaStringhe[3] ,fontsList[3] ,pointSizeList[3])
            
        listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail]
            
        if not all(elem < 380 for elem in listaLunghezze):     
            
            #resizing
            pointSizeList[0] = pointSizeList[0] - 1
            pointSizeList[1] = pointSizeList[1] - 1
            pointSizeList[2] = pointSizeList[2] - 2
            pointSizeList[3] = pointSizeList[3] - 1
            
        else:
                    
            loopFlag = 0
        #ricalcola
        posXTitolo = getStringX(width ,posXLongest ,listaStringhe[0] ,fontsList[0] ,pointSizeList[0] ,flagSide)
        posXIndirizzo = getStringX(width ,posXLongest ,listaStringhe[1] ,fontsList[1] ,pointSizeList[1] ,flagSide)
        posXSitoEmail = getStringX(width ,posXLongest ,listaStringhe[3] ,fontsList[3] ,pointSizeList[3] ,flagSide)
        posXTelefonoIva = getStringX(width ,posXLongest ,listaStringhe[2] ,fontsList[2] ,pointSizeList[2] ,flagSide)
        listaValutazione = [posXTitolo ,posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]
        
        #stringa più lunga che permette di centralizzare le stirnghe
        longestString = min(listaValutazione)
        indexLongest = listaValutazione.index(longestString)
        
        #CASO TITOLO
        if(listaStringhe[indexLongest] == listaStringhe[0]):
            
            posXLongest = getStringX(width ,None ,listaStringhe[indexLongest] ,fontsList[0] ,pointSizeList[0] ,flagSide)
        
        else:
            
            if(indexLongest == 1):
                
                longestFaceNameFont = fontsList[1]
                longestPointSize = pointSizeList[1]
                
            elif(indexLongest == 2):
                
                longestFaceNameFont = fontsList[2]
                longestPointSize = pointSizeList[2]
                
            else:     
                
                longestFaceNameFont = fontsList[3]
                longestPointSize = pointSizeList[3]                           
                
            posXLongest = getStringX(width ,None ,listaStringhe[indexLongest] ,longestFaceNameFont ,longestPointSize ,flagSide)
            
    return posXLongest ,pointSizeList
        
