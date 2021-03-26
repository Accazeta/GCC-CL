import cv2, os, sys

#Si assicura che la current directory sia quella in cui si trova lo script quando viene fatto partire
pathAssoluto = os.path.abspath(sys.argv[0])
mainDir = os.path.dirname(pathAssoluto)
os.chdir(mainDir)

nomeImg = "1615639004.jpg"
img = cv2.imread(nomeImg)
larghImg = 1920
altImg = 1080
xCentro, yCentro, largh, alt = 0, 0, 0, 0
with open('myYOLO.txt','r') as f:
    count = 0
    for riga in f:
        valori = riga.split()
        xCentro = float(valori[1])*larghImg
        yCentro = float(valori[2])*altImg
        largh = float(valori[3])*larghImg
        alt = float(valori[4])*altImg
        if count < 1:
            print(str(xCentro)+","+str(yCentro)+","+str(largh)+","+str(alt))
        xAltoSx = int(round(xCentro - (largh/2)))
        yAltoSx = int(round(yCentro - (alt/2)))
        xBassoDx = int(round(xCentro + (largh/2)))
        yBassoDx = int(round(yCentro + (alt/2)))
        if count < 1:
            print(str(xAltoSx)+","+str(yAltoSx)+","+str(xBassoDx)+","+str(yBassoDx))
            count += 1
        cv2.rectangle(img, (xAltoSx, yAltoSx), (xBassoDx, yBassoDx), (0, 255, 0), 2)
cv2.namedWindow('Immagine', cv2.WINDOW_NORMAL)
cv2.imshow('Immagine',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
