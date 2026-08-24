#NextGenCoder Simple calculator
head = "NextGenCoder's Simple Calculator" 
print(head)

#loop for restart program after finishing
#a calculation in it
restart = True
while restart == True:
    
#input boxes
    a = input("Enter value a : ")
    b = input("Enter value b : ")
    print()#to create gap
    
#Results
    
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
#All the results        
        print("a + b : ",a+b)
        print("a - b : ",a-b)
        print("a * b : ",a*b)
        print("a / b : ",a/b)
        print()#to create gap
 #Error message       
    else:
        print("Only numbers allowed")  
        print()#to create gap  
    
        
    
    