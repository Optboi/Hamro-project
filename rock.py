def RPS(comp,you):
  if comp=='R':
   if you=='S':
    return False
   elif you=='P':
    return True
   else :
    return None
  elif comp=='P':
   if you=='S':
    return True
   elif you=='R':
    return False
   else :
    return None
  elif comp=='S':
   if you=='R':
    return True
   elif you=='P':
    return False
   else :
    return None


print("computer; Rock(R), Paper(P), or scissor(S)?")
import random
a=random.randint(1,3)
if a==1:
    comp = 'R'
elif a==2:
    comp='P'
else:
    comp ='S'
you =input("Player; Rock(R), Paper(P), or scissor(S)?")
b = RPS(comp,you)
if b== True:
    print("you won!!!!!")
elif b== False:
    print("You lost")
else :
    print("The game is draw")