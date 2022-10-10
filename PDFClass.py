from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
import Functions as func
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class PDF(canvas.Canvas):
    
    def __init__(self ,title):
        
        super().__init__(title ,pagesize = A4 ,bottomup = 1)
        
    def __headerFattura__(self ,listaStringhe ,path ,flagSide ,fontsInfo):
        
        for i in range(0 ,800 ,100):
            self.drawString(15 ,i ,str(i))
           
        for i in range(0 ,600 ,100):
            self.drawString(i ,820 ,str(i)) 
        
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
        i = 7
        #prendi altezza e larghezza immagine scalata
        widthImage ,heightImage = func.get_image(path ,i * cm)
        width,height = A4
        
        image_y = 830 - heightImage
        #centralizza l'immagine
        if(image_y > 680):
                
            image_y = image_y - ((height - image_y) // 4)
                
        
        #gestione immagine con altezza troppo grande
        while image_y < 680 :
    
            i -= 1
            widthImage ,heightImage = func.get_image(path ,i * cm)

            image_y = 830 - heightImage
            if(image_y > 680):
                
                image_y = image_y - ((height - image_y) // 4)
                
        #gestione immagine con larghezza troppo grande
        while widthImage > 170 :
            i -= 1
            widthImage ,heightImage = func.get_image(path ,i * cm)

            image_y = 830 - heightImage           
            if(image_y > 680):
                
                image_y = image_y - ((height - image_y) // 4)
                
        #viene inserita a sinistra con uno spazio dal bordo
        if flagSide == "s":
            
            val = 20
            #immagine centralizzata nel suo spazio(ascisse)
            if((val + widthImage) < 250):
                
                val = val + ((250 - (val + widthImage)) // 4)
            self.drawInlineImage(path ,val ,image_y ,widthImage ,heightImage)
            
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
        posXTitolo = func.getStringX(width ,None ,listaStringhe[0] ,faceNameFontTitle ,pointSizeTitle ,flagSide)
        posXIndirizzo = func.getStringX(width ,None ,listaStringhe[1] ,faceNameFontSecondLine ,pointSizeSecondLine ,flagSide)
        posXSitoEmail = func.getStringX(width ,None ,listaStringhe[3] ,faceNameFontThirdLine ,pointSizeThirdLine ,flagSide)
        posXTelefonoIva = func.getStringX(width ,None ,listaStringhe[2] ,faceNameFontFourthLine ,pointSizeFourthLine ,flagSide)
        listaValutazione = [posXTitolo ,posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]

                                  
        #stringa più lunga che permette di centralizzare le stringhe
        longestString = min(listaValutazione)
        indexLongest = listaValutazione.index(longestString)
        
        #CASO TITOLO
        if(listaStringhe[indexLongest] == listaStringhe[0]):
            
            posXLongest = func.getStringX(width ,None ,listaStringhe[indexLongest] ,faceNameFontTitle ,pointSizeTitle ,flagSide)
        
        else:
            
            if(indexLongest == 1):
                
                longestFaceNameFont = faceNameFontSecondLine
                longestPointSize = pointSizeSecondLine
                
            elif(indexLongest == 2):
                
                longestFaceNameFont = faceNameFontThirdLine
                longestPointSize = pointSizeThirdLine
                
            else:     
                
                longestFaceNameFont = faceNameFontFourthLine
                longestPointSize = pointSizeFourthLine                           
                
            posXLongest = func.getStringX(width ,None ,listaStringhe[indexLongest] ,longestFaceNameFont ,longestPointSize ,flagSide)

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
            
            
            
        #GESTIONE TITOLO
        posXTitolo = func.getStringX(width ,posXLongest ,listaStringhe[0] ,faceNameFontTitle ,pointSizeTitle ,flagSide)
        #GESTIONE INDIRIZZO
        posXIndirizzo = func.getStringX(width ,posXLongest ,listaStringhe[1] ,faceNameFontSecondLine ,pointSizeSecondLine ,flagSide)
        #GESTIONE TELEFONO IVA
        posXTelefonoIva = func.getStringX(width ,posXLongest ,listaStringhe[2] ,faceNameFontThirdLine ,pointSizeThirdLine ,flagSide) 
        #GESTIONE SITO EMAIL
        posXSitoEmail = func.getStringX(width ,posXLongest ,listaStringhe[3] ,faceNameFontFourthLine ,pointSizeFourthLine ,flagSide)
        #resizing
        listaFields = [posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]
        listaValutazione = [posXTitolo ,posXIndirizzo ,posXTelefonoIva ,posXSitoEmail]
        
        loopFlag = 0
        
        #IL CONTROLLO AVVIENE RISPETTO L'INSERIMENTO DI UN IMMAGINE E UNA DETERMINATA STRINGA CHE NON RISPETTA IL FONT
        #controllo che le stringhe rispettino una determinata lunghezza rispetto all'immagine inserita  a destra l'immagine viene inserita a 400     
        fontsList = [faceNameFontTitle ,faceNameFontSecondLine ,faceNameFontThirdLine ,faceNameFontFourthLine]
        pointsSizeList = [pointSizeTitle ,pointSizeSecondLine ,pointSizeThirdLine ,pointSizeFourthLine]
        
        if flagSide == "r":
            
            lunghezzaTitolo = stringWidth(listaStringhe[0] ,faceNameFontTitle ,pointSizeTitle)
            lunghezzaIndirizzo = stringWidth(listaStringhe[1] ,faceNameFontSecondLine ,pointSizeSecondLine)
            lunghezzaTelefonoIva = stringWidth(listaStringhe[2] ,faceNameFontThirdLine ,pointSizeThirdLine)
            lunghezzaSitoEmail = stringWidth(listaStringhe[3] ,faceNameFontFourthLine ,pointSizeFourthLine)
        
            listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail]                   
            
            while not all((elem + 20) < val for elem in listaLunghezze):
                
                pointSizeTitle = pointSizeTitle - 1
                pointSizeSecondLine = pointSizeSecondLine - 1
                pointSizeThirdLine = pointSizeThirdLine - 1
                pointSizeFourthLine = pointSizeFourthLine - 1
                
                lunghezzaTitolo = stringWidth(listaStringhe[0] ,faceNameFontTitle ,pointSizeTitle)
                lunghezzaIndirizzo = stringWidth(listaStringhe[1] ,faceNameFontSecondLine ,pointSizeSecondLine)
                lunghezzaTelefonoIva = stringWidth(listaStringhe[2] ,faceNameFontThirdLine ,pointSizeThirdLine)
                lunghezzaSitoEmail = stringWidth(listaStringhe[3] ,faceNameFontFourthLine ,pointSizeFourthLine)
            
                listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail] 
                
                ma = max(listaLunghezze)
                pos = listaLunghezze.index(ma)

                posXLongest = func.getStringX(width ,None ,listaStringhe[pos] ,fontsList[pos] ,pointsSizeList[pos] ,flagSide)
                

        
                #TODO DA RIVEDERE
                #quando immaggine e' a destra avviene un resizing automatico dei campi che sforano
                #posXLongest ,pointsSizeList = func.resizingOrizzontaleLatoSinistro(width ,posXLongest ,listaValutazione ,listaLunghezze ,listaStringhe ,flagSide ,loopFlag ,fontsList ,pointsSizeList )

        #controllo che le stringhe rispettino una determinata lunghezza rispetto all'immagine inserita 
        #if flagSide == "s":
            #if not all(elem > val + widthImage for elem in listaValutazione) or not posXTitolo > val + widthImage:
                
                #loopFlag = 1
        
            #quando immaggine e' a sinsitra avviene un resizing automatico dei campi che sforano
            #posXLongest ,pointsSizeList = func.resizingOrizzontaleLatoDestro(width ,posXLongest ,listaValutazione ,listaFields ,listaStringhe ,flagSide ,loopFlag ,fontsList ,pointsSizeList ,val + widthImage)      
        
        #Una volta calcolate le size ideali in base al font ,possiamo calcolare l'altezza e gestirla
        posYTitolo = func.getStartingStringHeight(height ,faceNameFontTitle ,pointSizeTitle)
        posYIndirizzo = func.getStringHeight(posYTitolo ,faceNameFontSecondLine ,pointSizeSecondLine)
        posYTelefonoIva = func.getStringHeight(posYIndirizzo ,faceNameFontThirdLine ,pointSizeThirdLine)
        posYSitoEmail = func.getStringHeight(posYTelefonoIva ,faceNameFontFourthLine ,pointSizeFourthLine)
                   
        #GESTIONE TITOLO
        posXTitolo = func.getStringX(width ,posXLongest ,listaStringhe[0] ,faceNameFontTitle ,pointsSizeList[0] ,flagSide)
        #GESTIONE INDIRIZZO
        posXIndirizzo = func.getStringX(width ,posXLongest ,listaStringhe[1] ,faceNameFontSecondLine ,pointsSizeList[1] ,flagSide)
        ##GESTIONE TELEFONO IVA
        posXTelefonoIva = func.getStringX(width ,posXLongest ,listaStringhe[2] ,faceNameFontThirdLine ,pointsSizeList[2] ,flagSide) 
        #GESTIONE SITO EMAIL
        posXSitoEmail = func.getStringX(width ,posXLongest ,listaStringhe[3] ,faceNameFontFourthLine ,pointsSizeList[3] ,flagSide)
        
        
        self.setFillColorRGB(colourTitle[0] ,colourTitle[1] ,colourTitle[2])         
        self.setFont(faceNameFontTitle ,pointSizeTitle)
        self.drawString(posXTitolo - 20,posYTitolo ,listaStringhe[0])

        self.setFillColorRGB(colourSecondLine[0] ,colourSecondLine[1] ,colourSecondLine[2])    
        self.setFont(faceNameFontSecondLine ,pointSizeSecondLine)
        self.drawString(posXIndirizzo  ,posYIndirizzo ,listaStringhe[1])
        
        self.setFillColorRGB(colourThirdLine[0] ,colourThirdLine[1] ,colourThirdLine[2]) 
        self.setFont(faceNameFontThirdLine ,pointSizeThirdLine)
        self.drawString(posXTelefonoIva ,posYTelefonoIva ,listaStringhe[2])
        
        self.setFillColorRGB(colourFourthLine[0] ,colourFourthLine[1] ,colourFourthLine[2]) 
        self.setFont(faceNameFontFourthLine ,pointSizeFourthLine)
        self.drawString(posXSitoEmail ,posYSitoEmail ,listaStringhe[3])
        
        #SALVATAGGIO PDF
        self.save()