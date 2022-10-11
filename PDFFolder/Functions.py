from PIL import Image
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics

#crea il logo ridimensionato nella cartella del progetto
def createLogo(path):
    
    image = Image.open(path)
    image_new = Image.new('RGB' ,(307 ,227))
    format = image.format
    image.save("newImage." + format)
    
    return format
    
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
    
#calcola ordinata del titolo basandosi sul font e pointsize
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
def resizingRight(width ,maxX ,stringList ,fontsList ,pointsSizeList ,listaLunghezze ,posXLongest ,flagSide):
    
    
    while not all((width - (elem + 20)) > (maxX + 10) for elem in listaLunghezze): 
                
                
        if (width - (listaLunghezze[0] + 20)) < (maxX + 10) :
                    
            pointsSizeList[0] = pointsSizeList[0] - 1
                    
        if (width - (listaLunghezze[1] + 20)) < (maxX + 10) :
                    
            pointsSizeList[1] = pointsSizeList[1] - 1 
                
               
        if (width - (listaLunghezze[2] + 20)) < (maxX + 10) :
                    
            pointsSizeList[2] = pointsSizeList[2] - 1

        if (width - (listaLunghezze[3] + 20)) < (maxX + 10) :
                    
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
def resizingLeft(width ,maxX ,stringList ,fontsList ,pointsSizeList ,listaLunghezze ,posXLongest ,flagSide) :
    
    
    while not all((elem + 20) < maxX for elem in listaLunghezze) :
                
    #resizing dei pointsize in base alle stringhe troppo lunghe e aggiornamento del valore in lista
        if(listaLunghezze[0] + 20) > maxX :
                    
            pointsSizeList[0] = pointsSizeList[0] - 1
                    
        if(listaLunghezze[1] + 20) > maxX :
                    
            pointsSizeList[1] = pointsSizeList[1] - 1
                    
        if(listaLunghezze[2] + 20) > maxX :
                    
            pointsSizeList[2] = pointsSizeList[2] - 1
                    
        if(listaLunghezze[3] + 20) > maxX :
                    
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