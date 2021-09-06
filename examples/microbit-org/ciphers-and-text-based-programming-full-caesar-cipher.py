from microbit import *

# Define a function that can perform the 'shift' of letters in the alphabet
def shift_letter(letter, shift_amount):
    letter_num = ord(letter) - ord('A')
    shifted_letter_num = (letter_num + shift_amount) % 26
    return chr(ord('A') + shifted_letter_num)

# Define a function that shifts all the letters in a message
def shift_message(message, shift_amount):
    shifted_message = " "
    for letter in message:
        shifted_message = shifted_message + shift_letter(letter, shift_amount)
    return shifted_message

# Insert message between the " " below and the number of letters for the shift: 
message = "SECRETMESSAGE"
shift_key = 3
    
# The message will scroll once, before the while True loop starts
display.scroll(message, wait=False, delay=150)
    
while True:
    # press button A to display the shifted message
    if button_a.is_pressed(): 
        display.scroll(str(shift_key), delay=150)
        display.clear()
        sleep(200) 
        display.scroll(shift_message(message, shift_key), wait=False, delay=150)
    
    

    
