import os, sys, re
#Si assicura che la current directory sia quella in cui si trova lo script quando viene fatto partire
pathAssoluto = os.path.abspath(sys.argv[0])
mainDir = os.path.dirname(pathAssoluto)
os.chdir(mainDir)

#Scansiona la cartella in cui lo script è stato fatto partire alla ricerca delle sotto cartelle
with os.scandir(mainDir) as cartelle:
    for cartella in cartelle:
        if cartella.name.startswith("part_"):
            os.chdir(cartella)
            print("Ho cambiato cartella principale!")
            with os.scandir(cartella) as sottoCartelle:
                for sottoCart in sottoCartelle:
                    os.chdir(sottoCart)
                    if sottoCart.name.startswith("1"):
                        print("Cartella numero {}".format(sottoCart))
                        #Apre il file con le coordinate e le salva in un dizionario, usando l'id del pedone come chiave
                        #L'i-esimo elemento contenuto nel diz. e' una lista di liste con cardinalita' 8x2
                        dictPedBones = {} 
                        bonesList = []
                        idPed = 0
                        with open("bonesCoords.xml", 'r') as f:
                            for riga in f:
                                match = re.search(r'<ped id=(.*?)>', riga)
                                if match:
                                    idPed = match[1]
                                    dictPedBones[idPed] = []
                                    continue
                                match = re.search(r'SKEL_Head x=(.*?) y=(.*?) />', riga)
                                if match:
                                    bonesList.append([match[1], match[2]])
                                    continue
                                match = re.search(r'<SKEL_RightFootFront x=(.*?) y=(.*?) />', riga)
                                if match:
                                    bonesList.append([match[1], match[2]])
                                    continue
                                match = re.search(r'<SKEL_RightFootBack x=(.*?) y=(.*?) />', riga)
                                if match:
                                    bonesList.append([match[1], match[2]])
                                    continue
                                match = re.search(r'<SKEL_LeftFootBack x=(.*?) y=(.*?) />', riga)
                                if match:
                                    bonesList.append([match[1], match[2]])
                                    continue
                                match = re.search(r'<SKEL_LeftHand x=(.*?) y=(.*?) />', riga)
                                if match:
                                    bonesList.append([match[1], match[2]])
                                    continue
                                match = re.search(r'<SKEL_RightHand x=(.*?) y=(.*?) />', riga)
                                if match:
                                    bonesList.append([match[1], match[2]])
                                    continue
                                match = re.search(r'<SKEL_Stomach x=(.*?) y=(.*?) />', riga)
                                if match:
                                    bonesList.append([match[1], match[2]])
                                    continue
                                match = re.search(r'<SKEL_Neck x=(.*?) y=(.*?) />', riga)
                                if match:
                                    bonesList.append([match[1], match[2]])
                                    dictPedBones[idPed] = bonesList
                                    bonesList = []
                                    continue
                        #Finito l'ultimo "with open", esegue questa parte
                        #Ossia finito di scansionare il file bonesCoords.xml calcola i valori massimi e minimi lungo i due assi
                        for chiave in dictPedBones:
                            xMax, xMin, yMax, yMin = 0,10,0,10
                            for bone in dictPedBones[chiave]:
                                xTemp = float(bone[0])
                                yTemp = float(bone[1])
                                if xTemp > xMax:
                                    xMax = xTemp
                                if xTemp < xMin:
                                    xMin = xTemp
                                if yTemp > yMax:
                                    yMax = yTemp
                                if yTemp < yMin:
                                    yMin = yTemp
                        #Scrive il file .txt nel formato YOLO
                        #Formato YOLO: <classe dell'oggetto> <xCentro> <yCentro> <larghezza> <altezza>
                            with open("myYOLO.txt",'a') as myTxt:
                                largh = xMax - xMin
                                alt = yMax - yMin
                                xCentro = (xMax + xMin)/2
                                yCentro = (yMax + yMin)/2
                                myTxt.write('0 {} {} {} {}\n'.format(xCentro, yCentro, largh, alt))
                    
                            
                