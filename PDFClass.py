
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
import Functions as func
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import cv2
class PDF(canvas.Canvas):
    
    def __init__(self ,title):
        
        super().__init__(title ,pagesize = A4 ,bottomup = 1)
        
    def __headerFattura__(self ,listaStringhe ,path ,flagSide ,fontsInfo):
        
        #riferimenti
        #for i in range(0 ,800 ,100):
            #self.drawString(15 ,i ,str(i))
           
        #for i in range(0 ,600 ,100):
            #self.drawString(i ,820 ,str(i)) 
        
        #font prima riga
        fontsInfosTitle = list(fontsInfo[0])
        tuplaFaceTTF = fontsInfosTitle[0]
        faceNameFontTitle = tuplaFaceTTF[0]
        fileTTF = tuplaFaceTTF[1]
        #inserimento font
        pdfmetrics.registerFont(TTFont(faceNameFontTitle, fileTTF))
        #colore prima riga
        colourTitle = fontsInfosTitle[1][0:3]
        #pointSize prima riga
        pointSizeTitle = fontsInfosTitle[2]
        
        #font seconda riga
        fontsInfosSecondLine = list(fontsInfo[1])
        tuplaFaceTTF = fontsInfosSecondLine[0]
        faceNameFontSecondLine = tuplaFaceTTF[0]
        fileTTFSecondLine = tuplaFaceTTF[1]
        #inserimento font
        pdfmetrics.registerFont(TTFont(faceNameFontSecondLine, fileTTFSecondLine))
        #colore seconda riga
        colourSecondLine = fontsInfosSecondLine[1][0:3]
        #pointSize seconda riga
        pointSizeSecondLine = fontsInfosSecondLine[2]

        #font terza riga
        fontsInfosThirdLine = list(fontsInfo[2])
        tuplaFaceTTF = fontsInfosThirdLine[0]
        faceNameFontThirdLine = tuplaFaceTTF[0]
        fileTTFThirdLine = tuplaFaceTTF[1]
        #inserimento font
        pdfmetrics.registerFont(TTFont(faceNameFontThirdLine, fileTTFThirdLine))
        #colore terza riga
        colourThirdLine = fontsInfosThirdLine[1][0:3]
        #pointSize terza riga
        pointSizeThirdLine = fontsInfosThirdLine[2]

        #font quarta riga
        fontsInfosFourthLine = list(fontsInfo[3])
        tuplaFaceTTF = fontsInfosFourthLine[0]
        faceNameFontFourthLine = tuplaFaceTTF[0]
        fileTTFFourthLine = tuplaFaceTTF[1]
        #inserimento font
        pdfmetrics.registerFont(TTFont(faceNameFontFourthLine, fileTTFFourthLine))
        #colore quarta riga
        colourFourthLine = fontsInfosFourthLine[1][0:3]
        #pointSize quarta riga
        pointSizeFourthLine = fontsInfosFourthLine[2]      
             
        #indice ridimensionamento
       # i = 7
        #prendi altezza e larghezza immagine scalata
        #widthImage ,heightImage = func.get_image(path ,i * cm)
        width,height = A4
        
        #image_y = 830 - heightImage
        #centralizza l'immagine
       # if(image_y > 680):
                
            #image_y = image_y - ((height - image_y) // 4)
                
        
        #gestione immagine con altezza troppo grande
        #while image_y < 680 :
    
            #i -= 1
            #widthImage ,heightImage = func.get_image(path ,i * cm)

            #image_y = 830 - heightImage
            #if(image_y > 680):
                
                #image_y = image_y - ((height - image_y) // 4)
                
        #gestione immagine con larghezza troppo grande
        #while widthImage > 170 :
            #i -= 1
            #widthImage ,heightImage = func.get_image(path ,i * cm)

            #image_y = 830 - heightImage           
            #if(image_y > 680):
                
                #image_y = image_y - ((height - image_y) // 4)
                
        #viene inserita a sinistra con uno spazio dal bordo
        func.resizeImage(path ,230 ,170)
        if flagSide == "s":
            
            self.drawInlineImage(path ,20 ,660 ,230 ,170)
            
        else:
                #ridimensioni e salvi l'immagine in un box definito di larghezza 230 e altezza 170 considerando che il foglio e' lungo 595 e altezza 841

                self.drawInlineImage(path ,350 ,660 ,230 ,170)
        
        
       # #calcolo la stringa piu' lunga rispetto al proprio font
        lunghezzaTitolo = stringWidth(listaStringhe[0] ,faceNameFontTitle ,pointSizeTitle)
        lunghezzaIndirizzo = stringWidth(listaStringhe[1] ,faceNameFontSecondLine ,pointSizeSecondLine)
        lunghezzaTelefonoIva = stringWidth(listaStringhe[2] ,faceNameFontThirdLine ,pointSizeThirdLine)
        lunghezzaSitoEmail = stringWidth(listaStringhe[3] ,faceNameFontFourthLine ,pointSizeFourthLine)
            
        listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail] 
        fontsList = [faceNameFontTitle ,faceNameFontSecondLine ,faceNameFontThirdLine ,faceNameFontFourthLine]
        pointsSizeList = [pointSizeTitle ,pointSizeSecondLine ,pointSizeThirdLine ,pointSizeFourthLine]  
                               
        #stringa più lunga che permette di centralizzare le stringhe
        ma = max(listaLunghezze)
        indexLongest = listaLunghezze.index(ma)                   
                
        if(indexLongest == 0) :
                    
            pointSizeLongest = pointSizeTitle
                
        if(indexLongest == 1) :
                    
            pointSizeLongest = pointSizeSecondLine
                    
        if(indexLongest == 2) :
                    
            pointSizeLongest = pointSizeThirdLine
                    
        if(indexLongest == 3) :
                    
            pointSizeLongest = pointSizeFourthLine
                    
            #calcolo la massima
        posXLongest = func.getStringX(width ,None ,listaStringhe[indexLongest] ,fontsList[indexLongest] ,pointSizeLongest ,flagSide)
        
        #Una volta calcolate le size ideali in base al font ,possiamo calcolare l'altezza e gestirla
        posYTitolo = func.getStartingStringHeight(height ,faceNameFontTitle ,pointSizeTitle)
        posYIndirizzo = func.getStringHeight(posYTitolo ,faceNameFontSecondLine ,pointSizeSecondLine)
        posYTelefonoIva = func.getStringHeight(posYIndirizzo ,faceNameFontThirdLine ,pointSizeThirdLine)
        posYSitoEmail = func.getStringHeight(posYTelefonoIva ,faceNameFontFourthLine ,pointSizeFourthLine)
        
        #TODO: modifica
        #sostanzialmente vede se il titolo ha un pointsize maggiore dei field e nel caso lo ridimensiona altrimenti ridimensiona quello dei fields
        while(posYSitoEmail < 650):
            
            if((pointSizeTitle - sizeFields) > 2):
                
                pointSizeTitle = pointSizeTitle - 1
                
            else:
                
                sizeFields = sizeFields - 1
            #ricalcolo
            posYTitolo = func.getStartingStringHeight(height ,faceNameFontTitle ,pointSizeTitle)
            posYIndirizzo = func.getStringHeight(posYTitolo ,faceNameFontSecondLine ,pointSizeSecondLine)
            posYTelefonoIva = func.getStringHeight(posYIndirizzo ,faceNameFontThirdLine ,pointSizeThirdLine)
            posYSitoEmail = func.getStringHeight(posYTelefonoIva ,faceNameFontFourthLine ,pointSizeFourthLine)
        
        #IL CONTROLLO AVVIENE RISPETTO L'INSERIMENTO DI UN IMMAGINE E UNA DETERMINATA STRINGA CHE NON RISPETTA IL FONT
        #controllo che le stringhe rispettino una determinata lunghezza rispetto all'immagine inserita  a destra l'immagine viene inserita a 400     
        #funziona ma devi gestire meglio il resizing in base alle grandezze. E' stupido diminuire tutto.
        if flagSide == "r":
            
            lunghezzaTitolo = stringWidth(listaStringhe[0] ,faceNameFontTitle ,pointSizeTitle)
            lunghezzaIndirizzo = stringWidth(listaStringhe[1] ,faceNameFontSecondLine ,pointSizeSecondLine)
            lunghezzaTelefonoIva = stringWidth(listaStringhe[2] ,faceNameFontThirdLine ,pointSizeThirdLine)
            lunghezzaSitoEmail = stringWidth(listaStringhe[3] ,faceNameFontFourthLine ,pointSizeFourthLine)
        
            listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail]                   
            #TODO:MODIFICA 350 CON VALORE IMMAGINE
            posXLongest ,pointsSizeList = func.resizingLeft(width ,350 ,listaStringhe ,fontsList ,pointsSizeList ,listaLunghezze ,posXLongest ,flagSide)
                
        #controllo che le stringhe rispettino una determinata lunghezza rispetto all'immagine inserita 
        if flagSide == "s":
            
            posXLongest ,pointsSizeList = func.resizingRight(width ,230 ,listaStringhe ,fontsList ,pointsSizeList ,listaLunghezze ,posXLongest ,flagSide)
                                                       
        
        #Una volta calcolate le size ideali in base al font ,possiamo calcolare l'altezza e gestirla
        posYTitolo = func.getStartingStringHeight(height ,faceNameFontTitle ,pointsSizeList[0])
        posYIndirizzo = func.getStringHeight(posYTitolo ,faceNameFontSecondLine ,pointsSizeList[1])
        posYTelefonoIva = func.getStringHeight(posYIndirizzo ,faceNameFontThirdLine ,pointsSizeList[2])
        posYSitoEmail = func.getStringHeight(posYTelefonoIva ,faceNameFontFourthLine ,pointsSizeList[3])
        
        #GESTIONE TITOLO
        posXTitolo = func.getStringX(width ,posXLongest ,listaStringhe[0] ,faceNameFontTitle ,pointsSizeList[0] ,flagSide)
        #GESTIONE INDIRIZZO
        posXIndirizzo = func.getStringX(width ,posXLongest ,listaStringhe[1] ,faceNameFontSecondLine ,pointsSizeList[1] ,flagSide)
        ##GESTIONE TELEFONO IVA
        posXTelefonoIva = func.getStringX(width ,posXLongest ,listaStringhe[2] ,faceNameFontThirdLine ,pointsSizeList[2] ,flagSide) 
        
        #GESTIONE SITO EMAIL
        posXSitoEmail = func.getStringX(width ,posXLongest ,listaStringhe[3] ,faceNameFontFourthLine ,pointsSizeList[3] ,flagSide)
        
        
        print([colourTitle])
        self.setFillColorRGB(colourTitle[0] / 256 ,colourTitle[1] / 256 ,colourTitle[2] / 256)         
        self.setFont(faceNameFontTitle ,pointsSizeList[0])
        self.drawString(posXTitolo ,posYTitolo ,listaStringhe[0])

        self.setFillColorRGB(colourSecondLine[0] / 256 ,colourSecondLine[1] / 256 ,colourSecondLine[2] / 256)    
        self.setFont(faceNameFontSecondLine ,pointsSizeList[1])
        self.drawString(posXIndirizzo  ,posYIndirizzo ,listaStringhe[1])
        
        self.setFillColorRGB(colourThirdLine[0]  / 256 ,colourThirdLine[1] / 256 ,colourThirdLine[2] / 256) 
        self.setFont(faceNameFontThirdLine ,pointsSizeList[2])
        self.drawString(posXTelefonoIva ,posYTelefonoIva ,listaStringhe[2])
        
        self.setFillColorRGB(colourFourthLine[0] / 256 ,colourFourthLine[1] / 256 ,colourFourthLine[2] / 256) 
        self.setFont(faceNameFontFourthLine ,pointsSizeList[3])
        self.drawString(posXSitoEmail ,posYSitoEmail ,listaStringhe[3])
        
        #SALVATAGGIO PDF
        self.save()