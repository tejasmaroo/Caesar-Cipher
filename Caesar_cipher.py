from art import logo

print (logo)
print("\n Welcome to the Caesar Cipher game!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_no , cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
       shift_no *= -1
    for char in start_text:
        if char in alphabet:
           position = alphabet.index(char)
           new_postion = position + shift_no
           end_text += alphabet[new_postion]
        else: 
           end_text += char
    print(f"\nThe {cipher_direction}d result is: {end_text}")

end = False

while end == False:
    direction = input("\nType 'encode' to encrypt or 'decode' to decrypt: ")
    text = input("\nType your message here: ").lower()
    shift = int(input("\nType the shift number: "))
    shift = shift % 26

    caesar(start_text = text, shift_no = shift, cipher_direction = direction)

    restart = input("\nType 'yes' if you want to play again or type 'no' to exit: ")

    if(restart == "no"):
        print("\nGoodbye!")
        end = True
        