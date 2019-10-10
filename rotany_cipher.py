# ROT-Any

import sys

print("\n\n_________________________________RotAny Cipher_________________________________\n")
print("Enter '0' to exit")

while(1):
    print("\n\nEnter Text : " ,end ="")
    text = str(input())

    if(text == '0'):
        sys.exit()

    print("Enter Rotator : " ,end ="")
    rot = int(input())
    
    i = 0
    while(i <= len(text)-1):
        print(chr(((ord(text[i])-97+rot)%26)+97),end ="")
        i = i + 1
        
    
