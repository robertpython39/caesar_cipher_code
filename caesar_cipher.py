print("Encryption with Caesar code is based on an alphabet shift (move of letters further in the alphabet),\n"
      "it is a monoalphabetic substitution cipher, ie. a same letter is replaced with only one other (always the same for given cipher message).")

def caesar_cipher():

    tryAgain = True
    while tryAgain == True:
        alphabet = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
        direction = input("Select Encode or Decode:\n").lower()
        start_text = input("Type your message:\n").lower()
        shift_ammount = int(input("type the shift number:\n"))
        shift_ammount = shift_ammount % 26
        end_text = ""
        if direction == "decode":
            shift_ammount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_ammount
                end_text = end_text + alphabet[new_position]
            else:
                end_text += char
            print(f"The {direction}d message is : {end_text}")
        result = input("Type YES to continue or NO to stop: \n").lower()
        if result == "no":
            print("Goodbye!")
            tryAgain = False

    print(f"The {direction}d message is : {end_text}")

caesar_cipher()
