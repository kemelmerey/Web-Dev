lower=[] 
upper=[] 
odd=[] 
even=[]  
s=input() 
for character in sorted(s):
    if character.isalpha(): 
        element = upper if character.isupper() else lower 
    else: 
      element= odd if int(character)%2 else even 
    
    element.append(character)
s="".join(lower+upper+odd+even) 
print(s)