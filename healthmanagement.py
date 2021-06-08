# health management system
# 3 clients - Rohan,Tejas,Karan
# Total 6 Files
# Write a function that when executed takes as input client name 

import datetime
def gettime():
    return datetime.datetime.now()
    





def take(k):
    if k==1:
        c=int(input('1) For Food \n2) For exercise ?\n '))
        if c==1:
            value=input('1) enter the food here \n' )
            with open('Rohanfood.txt','a')as op:

                op.write (str([str(gettime())])+value+'\n')
            
            print('sucessfully written')
        else:
            value=(input('1) enter the exercise here \n' ))
            with open('Rohanexercise.txt','a')as op:
                op.write (str([str(gettime())])+value+'\n')
            
            print('sucessfully written')

    elif k==2:
        c=int(input('1) For Food  \n2) For exercise ?\n '))
        if c==1:
            value=(input('1) enter the food here \n' ))
            with open('Tejasfood.txt','a')as op:
                op.write (str([str(gettime())])+value+'\n')
            
            print('sucessfully written')
        else:
            value=(input('1) enter the exercise here \n' ))
            with open('Tejasexercise.txt','a')as op:
                op.write (str([str(gettime())])+value+'\n')
            
            print('sucessfully written')
    elif k==3:
        c=int(input('1) For Food  \n2) For exercise ?\n '))
        if c==1:
            value=(input('1) enter the food here \n' ))
            with open('Karanfood.txt','a')as op:
                op.write (str([str(gettime())])+value+'\n')
            
            print('sucessfully written')
        else:
            value=(input('1) enter the exercise here \n' ))
            with open('Karanexercise.txt','a')as op:
                op.write (str([str(gettime())])+value+'\n')
            
            print('sucessfully written')

            
def read(j):
    if j==1:
        c=int(input('1) For Food  \n2) For exercise ?\n '))
        if c==1:
            with open('Rohanfood.txt')as op:
                print(op.read())
        elif c==2:
            with open('Rohanexercise.txt')as op:
                print(op.read())
        else:
            print('enter a valid option')
    elif j==2:
        c=int(input('1) For Food  \n2) For exercise ?\n '))
        if c==1:
            with open('Tejasfood.txt')as op:
                print(op.read())
        elif c==2:
            with open('Tejasexercise.txt')as op:
                print(op.read())
        else:
            print('enter a valid option')
    elif j==3:
        c=int(input('1) For Food  \n2) For exercise ?\n '))
        if c==1:
            with open('Karanfood.txt')as op:
                print(op.read())
        elif c==2:
            with open('Karanexercise.txt')as op:
                print(op.read())
        else:
            print('enter a valid option')







print("Welcome to health Management System")
b=int(input('Press 1 to write information \nPress 2 to retrive information\n::'))
if b==1:
    k=int(input('enter 1 for(Rohan)\n,2 for (Tejas)\n, 3 for (Karan)\n'))
    if k==1:
        take(1)
    elif k==2:
        take(2)
        
    elif k==3:
        take(3)

    else:
        print('error code=200b00 select a valid option ')
    
elif b==2:
    j=int(input('enter 1 for(Rohan)\n,2 for (Tejas)\n, 3 for (Karan)\n'))
    if j==1:
        read(1)
    elif j==2:
        read(2)
        
    elif j==3:
        read(3)

    else:
        print('error code=200b00 select a valid option ')
