from microbit import *

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 3
message = "secretmessage"
cipher = ""

for letter in message:
  pos = alphabet.find(letter)
  newpos = (pos + key) % 26
  cipher = cipher + alphabet[newpos]

display.scroll(str(key))
display.scroll(message)

while True:
    if button_a.is_pressed():
        display.scroll(str(key))
        display.scroll(cipher, delay=300)
        
