alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for item in text:
        if item in alphabet:
            position = alphabet.index(item)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += item
    print(f"Here's the {direction}d result: {end_text}")

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye!")



