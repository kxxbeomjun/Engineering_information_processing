#morse code 과제

ENGLISH_TO_MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": '..-.', "G": "--.",
                    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
                    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
                    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", " ": " "}

MORSE_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
  MORSE_TO_ENGLISH[value] = key

print("Converting English to Morse : 'M', Converting Morse to English : 'E' ")
type_code = input("What would you choose 'M' or 'E' ?  : ")
while type_code !='M' and type_code !='E':
  print("Please enter again between 'M' or 'E'")
  type_code = input(" 'M' or 'E' ?  : ")    
      
if type_code == 'M':
  english = input('Enter your english message: ')
  english_upper = english.upper()
  for char in english_upper:
    if char in ENGLISH_TO_MORSE:
      print('>', ENGLISH_TO_MORSE[char])
    else:
      print("Error: wrong text ")

if type_code == 'E':
  print('Enter your morse code by one by one')
  english = []
  stop_input = False
  while not stop_input:
    k = input('> ')
    if k in MORSE_TO_ENGLISH:
      english.append(MORSE_TO_ENGLISH[k])
    elif k == 'q':
      break
    else:
      print('Error: wrong code')
  print(" ")
  for a in english:
      print(a, end='')
