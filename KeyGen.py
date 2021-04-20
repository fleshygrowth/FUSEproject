import random
import string

def generate_key():

    key = []
    
    for x in range(255):
        string.ascii_lowercase
        key.insert(x, 
        random.choice(
            string.ascii_lowercase + 
            string.digits + 
            string.ascii_uppercase + 
            string.punctuation))
    return key
    
    
    
def main():
	key = generate_key()

	f = open("Key", "a")
	f.write(key)
	f.close()
