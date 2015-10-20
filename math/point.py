# first version
# one year ago
# imports:
from math import fabs # 	position after decimal point

# Listen:
ListeX=[]
ListeY=[]

Liste=[]

Array1=[]

# Integer:
Zah=0
Zah1=0
Zah2=0

Zah5=0
Zah8=0

ZahE=0

# Strings:
Estr=""
Funk="Eine Funktion "
VarS=""

# Boolean:
Boo1=True


# Eingabe:
Var1=int(input("Anzahl der Punkte der ganzrationalen Funktion: "))
Potenz=Var1-1
Potenz2=Potenz
print("\nMaximal eine Funktion",str(Potenz)+".","Grades:\n")

while Zah<Var1:
     
     X=eval(input("X-Koordinate: "))
     Y=eval(input("Y-Koordinate: "))

     X=float(X)
     Y=float(Y)

     ListeX.append(X)
     ListeY.append(Y)

     print("\n")
     Zah+=1


if ListeX[0]==0:
    del ListeX[0]
    Var2= ListeY[0]
    del ListeY[0]
    ListeX.append(0)
    ListeY.append(Var2)

# Rechnung:

# Array bzw. Gleichung erstellen:
while Zah1<(len(ListeX)):
    Liste1=[]
    Liste1.append(ListeY[Zah1])
    while Potenz>=0:
        Liste1.append((ListeX[Zah1])**Potenz)

        Potenz -= 1
    Array1.append(Liste1)
    Potenz=Potenz2
    Zah1 +=1

# Entfernung der überschüssigen Elemente:
while Zah2<len(ListeY)-1:
   Zah3=1
   while Zah3<len(Array1[Zah2])-1:
      Var4=Array1[Zah2][len(Array1[Zah2])-1]
      Var5=Array1[Zah2+Zah3][len(Array1[Zah2])-1]
      Zah4=0
      if Var5==0:
       Zah4=len(Array1[Zah2])
      else:
       Var6=float(Var5/Var4)

      while Zah4<len(Array1[Zah2]):
            Var7=Array1[Zah2][Zah4]
            Var8=Array1[Zah2+Zah3][Zah4]
            Var9=Var8-(Var7*Var6)
            Array1[Zah2+Zah3][Zah4]=Var9

            Zah4 +=1
      if Array1[Zah2+Zah3][len(Array1[Zah2+Zah3])-1]==0:
         del Array1[Zah2+Zah3][len(Array1[Zah2+Zah3])-1]
      Zah3 +=1


   Zah2 +=1

# Berechnung der Elemente bzw. der einzelnen Vorvariabeln:
while Zah5<len(Array1):
    Zah6=0
    while Zah6<len(Liste):
        Var7= Array1[len(Array1)-Zah5-1][1+Zah6]
        Var8= Liste[Zah6]
        Var9= Var7*Var8
        Array1[len(Array1)-Zah5-1][1+Zah6]= Var9
        
        Zah6 +=1

    Zah7=1
    Var11= (len(Array1[len(Array1)-Zah5-1])-1)

    while Zah7<Var11:
        Var10=Array1[len(Array1)-Zah5-1][0]-(Array1[len(Array1)-Zah5-1]).pop(1)
        Array1[len(Array1)-Zah5-1][0]=Var10
        Zah7 +=1


    if (Array1[len(Array1)-Zah5-1][1])!=0:
        Var100= Array1[len(Array1)-Zah5-1][0]/(Array1[len(Array1)-Zah5-1][1])
        Liste.append(Var100)    

    else:
        Var100=Array1[len(Array1)-Zah5-1][0]
        Liste.append(0)
    Zah5 +=1


# Ausgabe:
L=len(Liste)

while Liste[Zah8]==0:
    Zah8 +=1
Grad=L-1-Zah8

Funk=Funk+str(Grad)+". Grades:"

while ZahE<L:
    Pot=L-1-ZahE
    if Liste[ZahE]==0:
        Liste[ZahE]=0
        if ZahE!=0:
          VarS="+  "
    elif Liste[ZahE]>0 and ZahE!=0:
        VarS="+  "
    elif Liste[ZahE]<0:
        VarS="-  "
    Estr= Estr+VarS+str(round(fabs(Liste[ZahE]),7))+" x**"+str(Pot)+"  "
    ZahE +=1

print(Funk,"\n ",Estr)

