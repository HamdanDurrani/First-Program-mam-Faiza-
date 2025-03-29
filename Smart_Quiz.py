
questions ={"\nQ1.What keyword is used to exit a loop? ?":"break",
            "\nQ2.Are Functions and Methods different in python (yes/no) ?":"yes",
            "\nQ3.The maker of Python Language is (dead or alive) ?":"alive",
            "\nQ4.What is the result of 5//2 in python?":"2",
            "\nQ5.{} What is its type?":"dictionary",
            "\nQ6.What is the result when we print(z) z='A' in 'apple' ?":"false",
            "\nQ7.What is the standard file extension for Python files?":".py",
            "\nQ8._1num=(0**9**9**9**9**9)\nprint (_1num) \n#Is there any error (yes/no ) ?":"no",
            "\nQ9.print (\'I will get print\') if True else print (\'no i will get print\') \n#is there any error (yes/no) ?":"no",
            "\nQ10.Orange is a colour or a fruit ?":"both"}

print ("\nWelcome to the Quiz\n")

def real():
    marks =0
    for key,val in questions.items():
        print (key)
        u_answer=input ("Enter your Answer:  ").lower()
        if u_answer==val:
            print ("correct answer ")
            marks = marks + 1
        else :
            print ("wrong answer")
        
    print (f"""
    Quiz is completed """)
    if marks>=9:
        print (f"Your marks is {marks}/10 which is really good. \nHave to say you are Pro!! ")
        
    elif marks<=8 and marks >=6:
        print (f"Your marks is {marks}/10 which is Just sastisfying")
    elif marks<6:
        print (f"""Your marks is {marks}/10 Regretfully I Have To Say That \"Go And Learn\"""")
    

authorize={"hamdan durrani":"24797",
           "itisham ullah durrani":"25092",
           "mujeeb":"24842",
           "hasnain":"25081",
           "sabtain":"24962",
           "hamza":"25066"}

authorize2={"faiza ghaffar":"0367",
            "saqib shahid":"0"}
print("!!For verification !!") 
name =input ("Enter Your Full Name: ").strip().lower()
identity =input ("Enter Your Secret Identity number: ").strip()

if name in authorize and identity==authorize[name]:
    print ("!!IDENTITY VERIFIED !!")
    real()
elif name in authorize2 and identity==authorize2[name]:
    print ("!!IDENTITY VERIFIED !!")
    real() #hard()
else:
    print ("Sorry You Are Not Authorized To Use This Software!, Contact the Developer!!")
input ("")