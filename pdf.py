from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
import Functions as func
import PIL

class PDF(canvas.Canvas):
    
    def __init__(self ,title):
        
        super().__init__(title ,pagesize = A4 ,bottomup = 1)
        
    def __headerFattura__(self ,listaStringhe ,fontTitle ,sizeTitle ,fontFields ,sizeFields ,path):
        
        #image = Image.open(path)
        #width,heigth = image.size
        
        #func.resizeImmagine(path ,150 ,200)
        #if(width <= heigth):
            
            #self.drawInlineImage(path ,50 ,600 ,100 ,200)
            
        #else:
            #self.drawInlineImage(path ,50 ,600 ,200 ,150)
            
        #salvi in due variabili lunghezza e altezza foglio
        width,heigth = A4
        
        #stringa più lunga che permette di centralizzare le stirnghe
        longestString = max(listaStringhe ,key = len)
        
        #CASO TITOLO
        if(longestString == listaStringhe[0]):
            
            posXLongest = func.getStringWidth(width ,None ,longestString ,fontTitle ,sizeTitle)
        
        else:
            
            posXLongest = func.getStringWidth(width ,None ,longestString ,fontFields ,sizeFields)

        #GESTIONE TITOLO
        posXTitolo = func.getStringWidth(width ,posXLongest ,listaStringhe[0] ,fontTitle ,sizeTitle)
        posYTitolo = func.getStartingStringHeigth(heigth ,fontTitle ,sizeTitle)

        self.setFont(fontTitle ,sizeTitle)
        self.drawString(posXTitolo ,posYTitolo ,listaStringhe[0])

        #GESTIONE INDIRIZZO
        posXIndirizzo = func.getStringWidth(width ,posXLongest ,listaStringhe[1] ,fontFields ,sizeFields)
        posYIndirizzo = func.getStringHeigth(posYTitolo ,fontFields ,sizeFields)

        self.setFont(fontFields ,sizeFields)
        self.drawString(posXIndirizzo  ,posYIndirizzo ,listaStringhe[1])

        #GESTIONE TELEFONO IVA
        posXTelefonoIva = func.getStringWidth(width ,posXLongest ,listaStringhe[2] ,fontFields ,sizeFields)
        posYTelefonoIva = func.getStringHeigth(posYIndirizzo ,fontFields ,sizeFields)

        self.setFont(fontFields ,sizeFields)
        self.drawString(posXTelefonoIva ,posYTelefonoIva ,listaStringhe[2])

        #GESTIONE SITO EMAIL
        posXSitoEmail = func.getStringWidth(width ,posXLongest ,listaStringhe[3] ,fontFields ,sizeFields)
        posYSitoEmail = func.getStringHeigth(posYTelefonoIva ,fontFields ,sizeFields)

        self.setFont(fontFields ,sizeFields)
        self.drawString(posXSitoEmail ,posYSitoEmail ,listaStringhe[3])
        
        
        #SALVATAGGIO PDF
        self.save()