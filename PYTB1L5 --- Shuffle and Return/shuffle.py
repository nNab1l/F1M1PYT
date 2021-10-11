import random

def shuffle(original):
    

    
    randomised = ''.join(random.sample(original, len(original)))  
    return randomised

print(shuffle("laptop"))
print(shuffle("Nabil"))
print(shuffle("huis"))