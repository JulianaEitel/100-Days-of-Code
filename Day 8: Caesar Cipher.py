alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceasar(text, shift, direction):
    output_text = ""
    for item in text:
        if item in alphabet:
            position = alphabet.index(item)
            if direction == "encode":
                new_position = position + shift
            elif direction == "decode":
                new_position = position - shift
            output_text += alphabet[new_position]
        else:
            output_text += item

    print(f"Your message is: {output_text}")


start_again = True
while start_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    ceasar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "yes":
        start_again = True

    elif restart == "no":
        start_again = False
        print("Goodbye!")