#simple grocery system
from numpy import *
List=('1. bread = 20 Rs.','2. butter = 50 Rs.','3. cheese = 80 Rs.','4. gum = 1 Rs.','5. chips = 10 Rs.','6. chicken = 153 Rs.per kg','7. icecream = 20 Rs.','8. toothpaste = 40 Rs.','9. chocolate = 20 Rs.','10.milk = 60 Rs. per liter ')
print(">>>>>>>>  ITEMS AVAILABLE IN STORE  <<<<<<<<")
for lis in List:
    print(lis)
print(">>>>>>>>>>  LIST OF ITEM PURCHASED  <<<<<<<<<<<")
print()
u=input()
l1=array(u.split( ), str)
print(">>>>>>>>>>  ENTER QUANTITY OF ITEM PURCHASED  <<<<<<<<<<<")
print()
r=input()
l2=array(r.split( ), int)
a=0
l3=array([10, 50, 153], int)
l4=array((),str)
b=input('would you like to add any items ?')
if b.lower=='add':
    o=input('enter the items you want to add')
    o1=input('enter how many of these items you want to add respectively')
    l5=array(o.split( ))
    l6=array(o1.split( ),int)
    l1=l1+l5
    l2=l2+l6

print(">>>>>>>>>  ENTER NUMBER OF ITEM SPECIFIC COUPON CODES  <<<<<<<<")
d=int(input())
if d!=0:
    for j in range (0,d+1):
        print(">>>>>>   ENTER ITEM SPECIFIC COUPON CODE IF ANY   <<<<<<")
        c=input()
        w=array(c.split( ))
        l4=l4+w
for k in l4:
    if k.lower=='riseup':
        l3[1]=l3[1]/2
    elif k.lower=='clockadoodledo':
        l3[6]=(l3[6]/3)*2
    elif k.lower=='smoothlike':
        l3[2]=(l3[2]/3)*2
i=-1
for m in l1:
    i=i+1
    a= a + l3[i]
    if m.lower=='bread':
        a= a + l3[0] * l2[i]
    elif m.lower=='butter':
        a= a + l3[1] * l2[i]
    elif m.lower=='cheese':
        a= a + 80 * l2[i]
    elif m.lower=='gum':
        a= a + 1 * l2[i]
    elif m.lower=='chips':
        a= a + 10 * l2[i]
    elif m.lower=='chicken':
        a= a + l3[2] * l2[i]
    elif m.lower=='icecream':
        a= a + 20 * l2[i]
    elif m.lower=='toothpaste':
        a= a + 40 * l2[i]
    elif m.lower=='chocolate':
         a= a + 20 * l2[i]
    elif m.lower=='milk':
        a= a + 60 * l2[i]
print(">>>>>>>>   TO GET COUPON ENTER YOUR PHONE NUMBER    <<<<<<<< ")
num=input()
if len(num)==10:
    print(">>>>>>>>>   YOUR COUPON CODE   <<<<<<<<<")
    print("                   🡇")
    print("               MONEYHEIST")
else:
    print("      Invalid Number >>> No Coupon For You        ")
print()
print(">>>>>>>>  ENTER COUPON CODE IF ANY  <<<<<<<<")
print()
t=input("                     ")
h=array(t.split( ))
for g in h:
    if g.lower=='money':
        a=a*0.7
    elif g.lower=='moneyheist':
        a=a*0.8
    elif g.lower=='father':
        a=a*0.6
a1=a*0.05+a
for y in range (0,len(l1)):
    print(l1[y],'➔',l2[y])
print()
print()
print()
print(f"The Total price before tax = {a} ")
print(f"The Grand Total = {a1}")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
