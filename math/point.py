# first version
# one year ago
# imports:
from math import fabs

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
Var1=int(input("Punkte der ganzrationalen Funktion haben sie (Zahl): "))
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

