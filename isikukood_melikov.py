arvud=[]
ikodid=[]
I_astme=[1,2,3,4,5,6,7,8,9,1]
II_astme=[3,4,5,6,7,8,9,1,2,3]
while True:
    controll=0
    summa=0
    try:
        isikukood=input("Sisestage isikukood: ")
        if isikukood.isdigit():

        
            if len(isikukood)==11:
                isikukood_con=list(isikukood)
                num1=isikukood_con[0]
                num1=int(num1)
                num2=isikukood_con[1]
                num2=int(num2)
                num3=isikukood_con[2]
                num3=int(num3)
                num4=isikukood_con[3]
                num4=int(num4)
                num5=isikukood_con[4]
                num5=int(num5)
                num6=isikukood_con[5]
                num6=int(num6)
                num7=isikukood_con[6]
                num7=int(num7)
                num8s=isikukood_con[7]
                num8=int(num8s)
                num9s=isikukood_con[8]
                num9=int(num9s)
                num10s=isikukood_con[9]
                num10=int(num10s)
                num11s=isikukood_con[10]
                num11=int(num11s)
                hnums=str(num8s+num9s+num10s)
                hnum=int(hnums)
                haigla=0
                if int(isikukood_con[1]+isikukood_con[2]) in range(0,100):
                    print("2,3 sümbolid on ok")
                    if int(isikukood_con[3]+isikukood_con[4]) in range(1,13):
                        print("Sümbolid 4,5 on ok")
                        if int(isikukood_con[5]+isikukood_con[6]) in range(1,32) and int(isikukood_con[3]+isikukood_con[4]) in range(1,13,2) or int(isikukood_con[5]+isikukood_con[6]) in range(1,32) and int(isikukood_con[3]+isikukood_con[4]) in range(4,13,2) or int(isikukood_con[5]+isikukood_con[6]) in range(1,30) and int(isikukood_con[3]+isikukood_con[4])==2:
                            print("Sümbolid 6,7 on ok")
                
                            if isikukood_con[0]=="1" or isikukood_con[0]=="2" or isikukood_con[0]=="3" or isikukood_con[0]=="4" or isikukood_con[0]=="5" or isikukood_con[0]=="6":
                                if hnum in range(1,11):
                                    haigla="Kuressaare Haigla"
                                elif hnum in range(11,20):
                                    haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
                                elif hnum in range(20,221):
                                    haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                                elif hnum in range(221,271):
                                    haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
                                elif hnum in range(271,371):
                                    haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
                                elif hnum in range(371,421):
                                    haigla="Narva Haigla"
                                elif hnum in range(421,471):
                                    haigla="Pärnu Haigla"
                                elif hnum in range(471,491):
                                    haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
                                elif hnum in range(491,521):
                                    haigla="Järvamaa Haigla (Paide)"
                                elif hnum in range(521,271):
                                    haigla="Rakvere, Tapa haigla"
                                elif hnum in range(571,601):
                                    haigla="Valga Haigla"
                                elif hnum in range(601,651):
                                    haigla="Viljandi Haigla"
                                elif hnum in range(651,701):
                                    haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
                                if isikukood_con[0]=="1" or isikukood_con[0]=="3" or isikukood_con[0]=="5":
                                    print(f"See on mees, tema sünnipäev on {num6}{num7}.{num4}{num5}.{num2}{num3} ja sünikoht on {haigla}")
                                if isikukood_con[0]=="2" or isikukood_con[0]=="4" or isikukood_con[0]=="6":
                                    print(f"See on naine, tema sünnipäev on {num6}{num7}.{num4}{num5}.{num2}{num3} ja sünikoht on {haigla}")
                                ikodid.append(isikukood)
                            else:
                                print("Esimene number ei ole õige")
                                arvud.append(isikukood)
                                continue
                            
                        else:
                            print("Valed 6 ja 7 sümbolid")
                            arvud.append(isikukood)
                            continue
                        
                    else:
                        print("Valed 4 ja 5 sümbolid on valed")
                        arvud.append(isikukood)
                        continue
                    
                else: 
                    print("Valed 2 ja 3 sümbolid")
                    arvud.append(isikukood)
                    continue
                
            else:
                print("Isikukoodis on 11 numbri")
                arvud.append(isikukood)
                continue
                
        else:
            print("Isikukoodis on nubmrid")
            arvud.append(isikukood)
            continue
        summa=int(I_astme[0])*int(isikukood_con[0])+int(I_astme[1])*int(isikukood_con[1])+int(I_astme[2])*int(isikukood_con[2])+int(I_astme[3])*int(isikukood_con[3])+int(I_astme[4])*int(isikukood_con[4])+int(I_astme[5])*int(isikukood_con[5])+int(I_astme[6])*int(isikukood_con[6])+int(I_astme[7])*int(isikukood_con[7])+int(I_astme[8])*int(isikukood_con[8])+int(I_astme[9])*int(isikukood_con[9])
        jääk=summa//11
        if jääk==10:
            summa=int(II_astme[0])*int(isikukood_con[0])+int(II_astme[1])*int(isikukood_con[1])+int(II_astme[2])*int(isikukood_con[2])+int(II_astme[3])*int(isikukood_con[3])+int(II_astme[4])*int(isikukood_con[4])+int(II_astme[5])*int(isikukood_con[5])+int(II_astme[6])*int(isikukood_con[6])+int(II_astme[7])*int(isikukood_con[7])+int(II_astme[8])*int(isikukood_con[8])+int(II_astme[9])*int(isikukood_con[9])
            jääk=summa//11
            if jääk==10:
                controll=0
            else:
                jääk=jääk*11
                controll=summa-jääk
            
        else:

            jääk=jääk*11
            controll=summa-jääk

        print("Kontrollnumber on ",controll)
        soov=input("Soovite veel isikukoodi sisestada? jah/ei ")
        if soov.lower()=="jah":
            continue
        else:
            break
    except Exception as e:
             print ("Viga:",e)
arvud.sort()
print(arvud)
print(ikodid)

    


