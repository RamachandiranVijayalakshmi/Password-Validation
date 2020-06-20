def sample(pa):
    while True:
        l, u, p, d = 0, 0, 0, 0
        if (len(pa) >= 8): 
            for i in pa: 
                if (i.islower()): 
                    l+=1            
                if (i.isupper()): 
                    u+=1            
                if (i.isdigit()): 
                    d+=1            
                if(i=='@'or i=='$' or i=='_'): 
                    p+=1           
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(pa)): 
            print("Valid Password") 
            break
        else: 
            print("Invalid Password")
            break
b=str.upper("Password Validation")
print(b.center(50))
print('- Minimum 8 characters.')
print('- The alphabets must be between [a-z]')
print('- At least one alphabet should be of Upper Case [A-Z]')
print('- At least 1 number or digit between [0-9].')
print('- At least 1 character from [ _ or @ or $ ].')
a=input('Create your Password:')
sample(a)