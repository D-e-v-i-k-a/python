name = 'John Doe'
len_name= len (name)
print(len_name)
if len_name > 20:
    print("Name {} is more than 20 chars long".format(name))
    
elif len_name > 15:
    print("Name {} is more than 15 chars long".format(name))
    
elif len_name > 10:
    print("Name {} is more than 10 chars long".format(name))
    
elif 8<=len_name <=10:
    print("Name {} is 8, 9 or 10 chars long".format(name))
   
else:
    print("Name {} is a short name".format(name))