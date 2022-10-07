
import wx
import cv2

from PIL import Image
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics


def resizeImmagine(path ,x ,y):
    
    image = Image.open(path)
        
    MAX_SIZE = (x,y)
    
    image.thumbnail(MAX_SIZE)
    
    # creating thumbnail
    image.save(path)

#calcola posizionamento scrittura coordinata x basandosi sulla lunghezza della stringa tenendo conto di uno spazio x dal bordo
def getStringWidth(widthPDF ,posXLongest ,stringInput ,font ,fontSize):
    
    string_x = stringWidth(stringInput ,font ,fontSize)
    val_x = widthPDF - string_x - 20
    
    #CALCOLO POSIZIONE RISPETTO LA STRINGA PIU' LUNGA
    if(posXLongest != None):
        
        val = (val_x - posXLongest) // 2
        
        return val_x - val
        
    else:
        #CASO STRINGA PIU'
        return val_x
    

def getStartingStringHeigth(heigthPDF ,font ,fontSize):
    
    face = pdfmetrics.getFont(font).face
    string_height = (face.ascent - face.descent) / 1000 * fontSize

    val_h = heigthPDF - 20 - string_height
    
    return val_h

def getStringHeigth(heigthPDF ,font ,fontSize):
    
    face = pdfmetrics.getFont(font).face
    string_height = (face.ascent - face.descent) / 1000 * fontSize

    val_h = heigthPDF - string_height
    
    return val_h