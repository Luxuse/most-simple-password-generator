import random
import string
print ("ton mot de passe")

chars = string.printable
taille = 8
 
password = "".join(random.sample(chars,taille))

print (f"ton mot de passe est: {password}")