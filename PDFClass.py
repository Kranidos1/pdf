from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
import Functions as func
from reportlab.lib.units import inch, cm

class PDF(canvas.Canvas):
    
    def __init__(self ,title):
        
        super().__init__(title ,pagesize = A4 ,bottomup = 1)
        
    def __headerFattura__(self ,listaStringhe ,fontTitle ,sizeTitle ,fontFields ,sizeFields ,path ,flagSide):
        
        for i in range(0 ,800 ,100):
            self.drawString(15 ,i ,str(i))
           
        for i in range(0 ,600 ,100):
            self.drawString(i ,820 ,str(i)) 
            
        #indice ridimensionamento
        i = 7
        #prendi altezza e larghezza immagine scalata
        widthImage ,heightImage = func.get_image(path ,i * cm)
        width,height = A4
        
        image_y = 830 - heightImage
        #centralizza l'immagine
        if(image_y > 650):
                
            image_y = image_y - ((height - image_y) // 4)
                
        
        #gestione immagine con altezza troppo grande
        while image_y < 650 :
    
            i -= 1
            widthImage ,heightImage = func.get_image(path ,i * cm)

            image_y = 830 - heightImage
            if(image_y > 650):
                
                image_y = image_y - ((height - image_y) // 4)
                
        #gestione immagine con larghezza troppo grande
        while widthImage > 170 :
            i -= 1
            widthImage ,heightImage = func.get_image(path ,i * cm)

            image_y = 830 - heightImage           
            if(image_y > 650):
                
                image_y = image_y - ((height - image_y) // 4)
                
        #viene inserita a sinistra con uno spazio dal bordo
        if flagSide == "s":
            
            val = 20
            #immagine centralizzata nel suo spazio(ascisse)
            if((val + widthImage) > 250):
                
                val = val + (250 - (val + widthImage) // 4)
                
            self.drawInlineImage(path ,20 ,image_y ,widthImage ,heightImage)
            
        else:
            #viene inserita a destra con uno spazio dal bordo
            val = 400
            #595 - (larghezza immagine + spazio) > 400 ? 
            if((width - (widthImage + 20)) > val):
                
                #immagine centralizzata nel suo spazio(ascisse)
                val = val + ((width - (width - widthImage)) // 4)
                
            self.drawInlineImage(path ,val ,image_y ,widthImage ,heightImage)
            
        #salvi in due variabili lunghezza e altezza foglio
        width,height = A4
        
        #calcolo la stringa piu' lunga rispetto al proprio font
        posXTitolo = func.getStringX(width ,None ,listaStringhe[0] ,fontTitle ,sizeTitle ,flagSide)
        posXIndirizzo = func.getStringX(width ,None ,listaStringhe[1] ,fontFields ,sizeFields ,flagSide)
        posXSitoEmail = func.getStringX(width ,None ,listaStringhe[3] ,fontFields ,sizeFields ,flagSide)
        posXTelefonoIva = func.getStringX(width ,None ,listaStringhe[2] ,fontFields ,sizeFields ,flagSide)
        listaValutazione = [posXTitolo ,posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]

                                  
        #stringa più lunga che permette di centralizzare le stirnghe
        longestString = min(listaValutazione)
        indexLongest = listaValutazione.index(longestString)
        
        #CASO TITOLO
        if(listaStringhe[indexLongest] == listaStringhe[0]):
            
            posXLongest = func.getStringX(width ,None ,listaStringhe[indexLongest] ,fontTitle ,sizeTitle ,flagSide)
        
        else:
            
            posXLongest = func.getStringX(width ,None ,listaStringhe[indexLongest] ,fontFields ,sizeFields ,flagSide)

        #Una volta calcolate le size ideali in base al font ,possiamo calcolare l'altezza e gestirla
        posYTitolo = func.getStartingStringHeight(height ,fontTitle ,sizeTitle)
        posYIndirizzo = func.getStringHeight(posYTitolo ,fontFields ,sizeFields)
        posYTelefonoIva = func.getStringHeight(posYIndirizzo ,fontFields ,sizeFields)
        posYSitoEmail = func.getStringHeight(posYTelefonoIva ,fontFields ,sizeFields)
        
        #sostanzialmente vede se il titolo ha un pointsize maggiore dei field e nel caso lo ridimensiona altrimenti ridimensiona quello dei fields
        while(posYSitoEmail < 650):
            
            if((sizeTitle - sizeFields) > 2):
                
                sizeTitle = sizeTitle - 1
                
            else:
                
                sizeFields = sizeFields - 1
            #ricalcolo
            posYTitolo = func.getStartingStringHeight(height ,fontTitle ,sizeTitle)
            posYIndirizzo = func.getStringHeight(posYTitolo ,fontFields ,sizeFields)
            posYTelefonoIva = func.getStringHeight(posYIndirizzo ,fontFields ,sizeFields)
            posYSitoEmail = func.getStringHeight(posYTelefonoIva ,fontFields ,sizeFields)
            
            
            
        #GESTIONE TITOLO
        posXTitolo = func.getStringX(width ,posXLongest ,listaStringhe[0] ,fontTitle ,sizeTitle ,flagSide)
        #GESTIONE INDIRIZZO
        posXIndirizzo = func.getStringX(width ,posXLongest ,listaStringhe[1] ,fontFields ,sizeFields ,flagSide)
        #GESTIONE TELEFONO IVA
        posXTelefonoIva = func.getStringX(width ,posXLongest ,listaStringhe[2] ,fontFields ,sizeFields ,flagSide) 
        #GESTIONE SITO EMAIL
        posXSitoEmail = func.getStringX(width ,posXLongest ,listaStringhe[3] ,fontFields ,sizeFields ,flagSide)
        #resizing
        listaFields = [posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]
        listaValutazione = [posXTitolo ,posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]
        
        loopFlag = 0
        
        #IL CONTROLLO AVVIENE RISPETTO L'INSERIMENTO DI UN IMMAGINE E UNA DETERMINATA STRINGA CHE NON RISPETTA IL FONT
        #controllo che le stringhe rispettino una determinata lunghezza rispetto all'immagine inserita  a destra l'immagine viene inserita a 400
        if flagSide == "r":
            
            lunghezzaTitolo = stringWidth(listaStringhe[0] ,fontTitle ,sizeTitle)
            lunghezzaIndirizzo = stringWidth(listaStringhe[1] ,fontFields ,sizeFields)
            lunghezzaTelefonoIva = stringWidth(listaStringhe[2] ,fontFields ,sizeFields)
            lunghezzaSitoEmail = stringWidth(listaStringhe[3] ,fontFields ,sizeFields)
        
            listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail]                   
              
            if not all(elem < 380 for elem in listaLunghezze):
                
                loopFlag = 1
        
                #quando immaggine e' a destra avviene un resizing automatico dei campi che sforano
                posXLongest ,sizeTitle ,sizeFields = func.resizingOrizzontaleLatoSinistro(width ,posXLongest ,listaValutazione ,listaLunghezze ,listaStringhe ,fontTitle ,fontFields ,sizeTitle ,sizeFields ,flagSide ,loopFlag)

        #controllo che le stringhe rispettino una determinata lunghezza rispetto all'immagine inserita 
        if flagSide == "s":
            
            if not all(elem > 250 for elem in listaValutazione) or not posXTitolo > 250:
                
                loopFlag = 1
        
            #quando immaggine e' a sinsitra avviene un resizing automatico dei campi che sforano
            posXLongest ,sizeTitle ,sizeFields = func.resizingOrizzontaleLatoDestro(width ,posXLongest ,listaValutazione ,listaFields ,listaStringhe ,fontTitle ,fontFields ,sizeTitle ,sizeFields ,flagSide ,loopFlag)      
        
        #Una volta calcolate le size ideali in base al font ,possiamo calcolare l'altezza e gestirla
        posYTitolo = func.getStartingStringHeight(height ,fontTitle ,sizeTitle)
        posYIndirizzo = func.getStringHeight(posYTitolo ,fontFields ,sizeFields)
        posYTelefonoIva = func.getStringHeight(posYIndirizzo ,fontFields ,sizeFields)
        posYSitoEmail = func.getStringHeight(posYTelefonoIva ,fontFields ,sizeFields)
                   
        #GESTIONE TITOLO
        posXTitolo = func.getStringX(width ,posXLongest ,listaStringhe[0] ,fontTitle ,sizeTitle ,flagSide)
        #GESTIONE INDIRIZZO
        posXIndirizzo = func.getStringX(width ,posXLongest ,listaStringhe[1] ,fontFields ,sizeFields ,flagSide)
        #GESTIONE TELEFONO IVA
        posXTelefonoIva = func.getStringX(width ,posXLongest ,listaStringhe[2] ,fontFields ,sizeFields ,flagSide) 
        #GESTIONE SITO EMAIL
        posXSitoEmail = func.getStringX(width ,posXLongest ,listaStringhe[3] ,fontFields ,sizeFields ,flagSide)
                  
        self.setFont(fontTitle ,sizeTitle)
        self.drawString(posXTitolo ,posYTitolo ,listaStringhe[0])


        self.setFont(fontFields ,sizeFields)
        self.drawString(posXIndirizzo  ,posYIndirizzo ,listaStringhe[1])

        
        self.setFont(fontFields ,sizeFields)
        self.drawString(posXTelefonoIva ,posYTelefonoIva ,listaStringhe[2])

        self.setFont(fontFields ,sizeFields)
        self.drawString(posXSitoEmail ,posYSitoEmail ,listaStringhe[3])
        
        
        #SALVATAGGIO PDF
        self.save()