
from alphabets import alphabet 

from art import logo
print(logo)

#function for encryption
def encrypt(text,shift):
    cipher_text=""
    for i in text:
        position = alphabet.index(i)
        if((position+shift)>25):
            new_letter = alphabet[position+shift-26]
        else:
            new_letter = alphabet[position+shift]
        cipher_text += new_letter

    print(f"The encoded message is {cipher_text}\n")

#function to decrypt
def decrypt(text,shift):
    message=""
    for i in text:
        position = alphabet.index(i)
        if((position-shift)<0):
            new_letter = alphabet[position-shift+26]
        else:
            new_letter = alphabet[position-shift]
        message += new_letter

    print(f"The decoded message is {message}\n")


#function which contain encrypt and decrypt both facility
def ceaser(start_text,shift_amount,cipher_direction):
    final_text=""
    if(cipher_direction=="decode"):
        shift_amount *= -1
    for i in start_text:
        position = alphabet.index(i)
        new_position = position+shift_amount
        if(new_position<0):
            new_position +=26
        if(new_position>25):
            new_position -=26
        new_letter = alphabet[new_position]
        final_text += new_letter
    
    print(f"The {direction}ion of the message :  {final_text}")


#calling for function encryption and decryption 
# if(direction == "encode"):
#     encrypt(text,shift)
# elif(direction == "decode"):
#     decrypt(text,shift)

#calling for ceaser function 
should_continue = True
while(should_continue):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift =int(input("Type the shift number\n"))
    ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
    temp = input("If you want to go again type YES otherwie type NO\n")
    if(temp == "NO"):
     should_continue=False
     print("!!  GOODBYE  !!")