with open("naive_input.txt", "r") as file:
    info = [line.strip().split() for line in file]  
print(info)

rows = len(info)
cols = len(info[1])


Yes = 1
No = 1
PYes = 1
PNo = 1

# Outlook = [[None] * 3 for _ in range(rows)]
# weather = [[None] * 3 for _ in range(rows)]
# Humidity = [[None] * 3 for _ in range(rows)]
# Windy = [None] * rows
first_column = [row[0] for row in info]
second_column = [row[1] for row in info]
third_column = [row[2] for row in info]
fourth_column = [row[3] for row in info]
fifth_column = [row[4] for row in info]

Yes = fifth_column.count("Yes")
No = fifth_column.count("No")
Sunny = first_column.count("Sunny")
Rainy = first_column.count("Rainy")
Overcast = first_column.count("Overcast")
Hot = second_column.count("Hot")
Mild = second_column.count("Mild")
Cool = second_column.count("Cool")
High = third_column.count("High")
Normal = third_column.count("Normal")
Windy = fourth_column.count("True")
notWindy = fourth_column.count("False")

PYes = Yes/rows
PNo = No/rows
PSunny = Sunny/rows
PRainy = Rainy/rows
POvercast = Overcast/rows
PHot = Hot/rows
PMild = Mild/rows
PCool = Cool/rows
PHigh = High/rows
PNormal = Normal/rows
PWindy = Windy/rows
PnotWindy = notWindy/rows

SunnyGivenYes = 0
RainyGivenYes = 0
OvercastGivenYes = 0
HotGivenYes = 0
MildGivenYes = 0
CoolGivenYes = 0
HighGivenYes = 0
NormalGivenYes = 0
WindyGivenYes = 0
notWindyGivenYes = 0

SunnyGivenNo = 0
RainyGivenNo = 0
OvercastGivenNo = 0 
HotGivenNo = 0
MildGivenNo = 0
CoolGivenNo = 0
HighGivenNo = 0
NormalGivenNo = 0
WindyGivenNo = 0
notWindyGivenNo = 0

i = 0
j = 0

for i in range(rows):
    for j in range(cols):
        if(info[i][j]=="Sunny" and info[i][cols-1]=="Yes"):
            SunnyGivenYes+=1
        elif(info[i][j]=="Sunny" and info[i][cols-1]=="No"):
            SunnyGivenNo+=1
        elif(info[i][j]=="Rainy" and info[i][cols-1]=="Yes"):
            RainyGivenYes+=1
        elif(info[i][j]=="Rainy" and info[i][cols-1]=="No"):
            RainyGivenNo+=1
        elif(info[i][j]=="Overcast" and info[i][cols-1]=="Yes"):
            OvercastGivenYes+=1
        elif(info[i][j]=="Overcast" and info[i][cols-1]=="No"):
            OvercastGivenNo+=1
        elif(info[i][j]=="Hot" and info[i][cols-1]=="Yes"):
            HotGivenYes+=1
        elif(info[i][j]=="Hot" and info[i][cols-1]=="No"):
            HotGivenNo+=1
        elif(info[i][j]=="Mild" and info[i][cols-1]=="Yes"):
            MildGivenYes+=1
        elif(info[i][j]=="Mild" and info[i][cols-1]=="No"):
            MildGivenNo+=1
        elif(info[i][j]=="Cool" and info[i][cols-1]=="Yes"):
            CoolGivenYes+=1
        elif(info[i][j]=="Cool" and info[i][cols-1]=="No"):
            CoolGivenNo+=1
        elif(info[i][j]=="High" and info[i][cols-1]=="Yes"):
            HighGivenYes+=1
        elif(info[i][j]=="High" and info[i][cols-1]=="No"):
            HighGivenNo+=1
        elif(info[i][j]=="Normal" and info[i][cols-1]=="Yes"):
            NormalGivenYes+=1
        elif(info[i][j]=="Normal" and info[i][cols-1]=="No"):
            NormalGivenNo+=1
        elif(info[i][j]=="True" and info[i][cols-1]=="Yes"):
            WindyGivenYes+=1
        elif(info[i][j]=="True" and info[i][cols-1]=="No"):
            WindyGivenNo+=1
        elif(info[i][j]=="False" and info[i][cols-1]=="Yes"):
            notWindyGivenYes+=1
        elif(info[i][j]=="False" and info[i][cols-1]=="No"):
            notWindyGivenNo+=1


PSunnyGivenYes = SunnyGivenYes/Yes
PRainyGivenYes = RainyGivenYes/Yes
POvercastGivenYes = OvercastGivenYes/Yes
PHotGivenYes = HotGivenYes/Yes
PMildGivenYes = MildGivenYes/Yes
PCoolGivenYes = CoolGivenYes/Yes
PHighGivenYes = HighGivenYes/Yes
PNormalGivenYes = NormalGivenYes/Yes
PWindyGivenYes = WindyGivenYes/Yes
PnotWindyGivenYes = notWindyGivenYes/Yes

PSunnyGivenNo = SunnyGivenNo/No
PRainyGivenNo = RainyGivenNo/No
POvercastGivenNo = OvercastGivenNo/No
PHotGivenNo = HotGivenNo/No
PMildGivenNo = MildGivenNo/No
PCoolGivenNo = CoolGivenNo/No
PHighGivenNo = HighGivenNo/No
PNormalGivenNo = NormalGivenNo/No
PWindyGivenNo = WindyGivenNo/No
PnotWindyGivenNo = notWindyGivenNo/No


print(Sunny,Rainy,Overcast,Hot,Mild,Cool,High,Normal,Windy,notWindy,Yes,No)
print(Rainy,Cool,Normal,notWindy)
Px1GivenYes = 0
Px2GivenYes = 0
Px3GivenYes = 0
Px4GivenYes = 0

Px1 = 0
Px2 = 0
Px3 = 0
Px4 = 0

x1 = "Rainy"
x2 = "Cool"
x3 = "Normal"
x4 = "False"

PYesGivenx1x2x3x4 = 0
PNoGivenx1x2x3x4 = 0

x1 = input("Sunny or Rainy or Overcast?")
x2 = input("Weather Hot or Mild or Cool?")
x3 = input("Humidity High or normal?")
x4 = input("Windy or notWindy?")

if(x1=="Sunny"):
    Px1 = PSunny
    Px1GivenYes = PSunnyGivenYes
if(x1=="Rainy"):
    Px1 = PRainy
    Px1GivenYes = PRainyGivenYes
if(x1=="Overcast"):
    Px1 = POvercast
    Px1GivenYes = POvercastGivenYes

if(x2=="Hot"):
    Px2 = PHot
    Px2GivenYes = PHotGivenYes
if(x2=="Mild"):
    Px2 = PMild
    Px2GivenYes = PMildGivenYes
if(x2=="Cool"):
    Px2 = PCool
    Px2GivenYes = PCoolGivenYes    

if(x3=="High"):
    Px3 = PHigh
    Px3GivenYes = PHighGivenYes
if(x3=="Normal"):
    Px3 = PNormal
    Px3GivenYes = PNormalGivenYes

if(x4=="Windy"):
    Px4 = PWindy
    Px4GivenYes = PWindyGivenYes
if(x4=="notWindy"):
    Px4 = PnotWindy
    Px4GivenYes = PnotWindyGivenYes

print(Px1GivenYes,Px2GivenYes,Px3GivenYes,Px4GivenYes)
PYesGivenx1x2x3x4 = (Px1GivenYes*Px2GivenYes*Px3GivenYes*Px4GivenYes)*PYes/(Px1*Px2*Px3*Px4)

print("P(Yes|",x1,x2,x3,x4,"): ",round(PYesGivenx1x2x3x4*100,2),"%")