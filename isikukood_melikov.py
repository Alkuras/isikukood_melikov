arvud=[]
ikodid=[]
while True:
    try:
        isikukood=input("Sisestage isikukood: ")
        
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
            print(hnum)
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
                    print(f"See in mees, tema sünnipäev on {num6}{num7}.{num4}{num5}.{num2}{num3} ja sünikoht on {haigla}")

    except Exception as e:
         print ("Viga:",e)


