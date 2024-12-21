number=int(input ("Enter Number to check"))
print ("Number to be checked :",number)

if number% 2==0:
    print("This is an even number")

else:
    print ("This an odd number")

    #BMI
height=float (input("Enter your height in cm :"))
weight=float(input("Enter your weight in kg :"))
BMI=weight/ (height/100)**2
print("Your BMI is",BMI)
if BMI <=18.4:
    print("you are under weight.")

elif BMI <=24.9:
 print("you are healthy.")

elif BMI <=29.9:
    print("you are  over weight.")

elif BMI <=34.9:
    print("you are  obese.")

else:
    print("you are severly obese")

    # Nasted condition
num = int(input("Enter number to check"))
if num>50:
 print("Number is greater than 50")
 if num%2==0:
    print("Number is even")
 else :
    print("Number is odd")
else:
   print("Number is less than 50")
   #Date time operation
import datetime
# using now() to get current time
current_time=datetime.datetime.now()
#printing values of now
print ("Time now at greenwich meridian is:",end="")
print (current_time)
#print claendar of year 2021
import calendar
print("\n",calendar.claendar(2021))