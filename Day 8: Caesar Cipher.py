alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceasar(text, shift, direction):
    start_text = []
    for item in text:
        start_text += item

    end_text = []
    for letter in start_text:
        if letter in alphabet:
            if direction == "e":
                new_position = alphabet.index(letter) + shift
            elif direction == "d":
                new_position = alphabet.index(letter) - shift

            end_text += alphabet[new_position]

        else:
            end_text += letter

    print(f"Your text is {''.join(end_text)}")


should_restart = True
while should_restart:

    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    ceasar(text, shift, direction)

    restart = input("Do you want to go again? Type 'yes' or 'no': ")

    if restart == "yes":
        should_restart = True
    else:
        should_restart = False
        print("Goodbye!")