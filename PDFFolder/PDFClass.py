
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from PDFFolder import Functions as func
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
class PDF(canvas.Canvas):
    
    def __init__(self ,pdfPath):
        
        super().__init__(pdfPath ,pagesize = A4 ,bottomup = 1)
    
    #Le misure sono calcolate in base alla misura di default ovvero 1/72 di inch che corrisponde circa a 2,53 cm
    #1 inch sono circa 96 px 
    def __headerFattura__(self ,listaStringhe ,path ,flagSide ,fontsInfo):
        
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
        
        #prendi altezza e larghezza immagine scalata
        width ,height = A4
        
        #crea logo ridimensionato
        widthIm ,heightIm = func.createLogo(path)

        #centralizza l'immagine rispetto l'altezza se necessario
        val = 0
        if(height - heightIm) > 690 :

            val = ((height - heightIm) - 690) // 2

        #setto posizione massima delle stringhe
        #considerando maxLunghezzaImmagine di 325 unita 325 + spazio = 350 max
        if(flagSide == "s") :
            
            valX = 350
            if(20 + widthIm) < 330 :

                valX = 330 - (20 + widthIm)

        if(flagSide == "r") :
            
            #considerando maxLunghezzaImmagine di 325 unita 250 + 325 + spazio = bordo - 15
            valX = 250

            if(width - (widthIm + 20)) > valX :

                valX = width - (widthIm + 20)

        #aggiorna punti inserimento
        if(flagSide == "s") :
            
            self.drawInlineImage("newImage.jpg" ,20 ,690 + val ,widthIm ,heightIm)
            
        else :
            #da modificare
    
            self.drawInlineImage("newImage.jpg" ,valX ,690 + val ,widthIm ,heightIm)
            

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
        

        #Il ridimensionamento avviene se e solo se le stringhe raggiungono l'immagine.Viene ridimensionat il point size solo di queste
        if flagSide == "r":
            
            lunghezzaTitolo = stringWidth(listaStringhe[0] ,faceNameFontTitle ,pointSizeTitle)
            lunghezzaIndirizzo = stringWidth(listaStringhe[1] ,faceNameFontSecondLine ,pointSizeSecondLine)
            lunghezzaTelefonoIva = stringWidth(listaStringhe[2] ,faceNameFontThirdLine ,pointSizeThirdLine)
            lunghezzaSitoEmail = stringWidth(listaStringhe[3] ,faceNameFontFourthLine ,pointSizeFourthLine)
        
            listaLunghezze = [lunghezzaTitolo ,lunghezzaIndirizzo ,lunghezzaTelefonoIva ,lunghezzaSitoEmail]                   
            
            posXLongest ,pointsSizeList = func.resizingLeft(width ,valX ,listaStringhe ,fontsList ,pointsSizeList ,listaLunghezze ,posXLongest ,flagSide)

        #350 e 240 sono i limiti approssimativi dell'immagine        
        #controllo che le stringhe rispettino una determinata lunghezza rispetto all'immagine inserita 
        if flagSide == "s":
            
            posXLongest ,pointsSizeList = func.resizingRight(width ,valX ,listaStringhe ,fontsList ,pointsSizeList ,listaLunghezze ,posXLongest ,flagSide)
                                                       
        
        #Una volta calcolate le size ideali in base al font ,possiamo calcolare l'altezza
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

        #i colori sono mappati come (255,255,255) = (1,1,1) l'equazione vien da se
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