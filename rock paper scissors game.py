while(True):
   one_user=input("ashmitha\t: ").casefold()
   two_user=input("pythonshell\t: ").casefold()

   if(one_user=='r')and(two_user=='r'):
       print("match draw")
   elif(one_user=='r')and(two_user=='p'):
        print("pythonshell won the game")
   elif(one_user=='r')and(two_user=='s'):
        print("ashmitha won this game")
   elif(one_user=='p')and(two_user=='r'):
        print("pythonshell won the game")
   elif(one_user=='p')and(two_user=='s'):
        print("pythonshell won this game")
   elif(one_user=='p')and(two_user=='p'):
        print("match draw")
   elif(one_user=='s')and(two_user=='s'):
        print("match draw")
   elif(one_user=='s')and(two_user=='p'):
        print("ashmitha won the game")
   elif(one_user=='s')and(two_user=='r'):
        print("pythonshell won this game")
   else:
        print("please enter valid inputs['r','p','s']")
        
   print("\n")
   continue_input=input("want to try again?(y/n):").casefold()
   print("\n")
   if (continue_input=='y')or(continue_input=='yes'):
        continue
   else:
        print("see you again.bye")
        break
