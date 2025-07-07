# #ask user to enter a password 
# password=input("enter your password:")
# #check if the paswword is correct
# if password=="letmein":
#     print("access granted")
# else:
#     print("access denied")





# #correct username and password
# correct_username = "ibra"
# correct_password = "2003"
# #loop until correct  username and password are enter
# while True:
#   username = input("enter username:")
#   password = input("enter password:")
  
#   if username==correct_username and password==correct_password:
#      print("access granted")
#      #break #eixt the loop when correct credentials are provided
# #else:
#    # print("incorrect username and password.please try again")



# for letter in "hello":
#  print(letter)

# for x in range(6):
#     print(x)

# def my_function(firstname,lastname):
#     print(firstname,lastname)
# my_function("john","james")


#function to perform calculation 
# num1=float(input("enter first number:"))
# operator=input("enter operator(+,-,*,/):")
# num2=float(input("enter second number:"))
# if operator=="+":
#     print("result:",num1+num2) 
# elif operator=="-":
#      print("result:",num1-num2)
# elif operator=="*":
#      print("result:",num1*num2)
# elif operator=="/":
#     if num2==0:
#      print("error:cannot divide by zero.")
#     else:
#         print("result:",num1/num2)





# def greeting(name):
#     print("hello"+name)


# import platform
# x=platform.system()
# print(x)

# import platform
# x=dir(platform)
# print(x)

# def greeting(name):
#     print("hello",+name)
# person1={"name":"john","age":40,"country":"norway"}   

#enhanced bmi calculator
def calculate_bmi(weight,height):
    return weight/(height**2)
#function to interpret the bmi value
def interpret_bmi(bmi):
    if bmi<19.5:
        return "your are underweight."
    elif 19.5<=bmi<24.9:
        return "your have normal weight."
    elif 25<=bmi<29.5:
        return "your are overweight."
    else:
        return "you are obese."
    
    #function to display the menu
    def show_menu():
        print("/n---BMI CALCULATOR MENU---")
        print("1.Calculate BMI")
        print("2.Exit")

 #main function 
def main():
    while True:
        choice=input("enter your choice (1 or 2):")

        if choice=="1":
            try:
                weight=float(input("enter your weight in kilograms:"))
                height=float(input("enter your height in meters:"))
                bmi=calculate_bmi(weight,height)
                print(f"/nyour BMI is:{bmi:2f}")
                print(interpret_bmi(bmi))
            except ValueError:
                print("invalid input! Please enter numeric values.")
        elif choice=="2":
            print("Thank you for using the BMI Calculator.Goodbye!")
            break
        else:
            print("invalid choice! Please select 1 or 2.")

#run the program
main()