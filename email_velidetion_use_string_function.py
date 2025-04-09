email=input("enter the email ")
k=j=d=0
if len(email)>=8:
    if email[0].isalpha():
        if("@"in email)and(email.count("@")==1):
            if(email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_"or"."or"@":
                        continue
                    else:
                        d=1
                        
                if k==1 or j==1 or d==1:
                    print("wrong email ")
                else:
                    print("this email is wright ")
                    
            else:       
                print("wrong email incorect posisson of point ")
        else:
            print("only one @ is user in email ")
    else:
        print("first charecter in emali is alphabet ")
else:
    print("email mustby includ  minmum 8 charecters")