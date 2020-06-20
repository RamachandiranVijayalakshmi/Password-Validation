# Password-Validation
### **First Create The Some Induvidual Privacy In the Websites, Using Password, That Password Create The Some Condition in The Website.**
### **Condition are:**
- **Minimum 8 characters**
- **The alphabets must be between *lower case[a-z]***
- **At least one alphabet should be of *Upper Case [A-Z]***
- **At least 1 number or digit between *[0-9].***
- **At least 1 character from *[ _ or @ or $ ].***
## Sample Code For Password Validation
```
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
```
## Expceted Output
```
                PASSWORD VALIDATION
- Minimum 8 characters.
- The alphabets must be between [a-z]
- At least one alphabet should be of Upper Case [A-Z]
- At least 1 number or digit between [0-9].
- At least 1 character from [ _ or @ or $ ].
Create your Password:vijiA@123
Valid Password
```
