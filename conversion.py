# -*- coding: utf-8 -*-
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/
"""

GRAMS_PER_POUND = 453.592
CENTIMETERS_PER_INCH = 2.54
KILOMETERS_PER_MILE  = 1.60934

while True:
  print('\nEnter desired conversation')
  print('----------------------------')
  print('1 - Pound  (lb) -> Grams      (g )')
  print('2 - Grams  ( g) -> Pound      (lb)')
  print("")
  print('3 - Inches (in) -> Centimeters(cm)')
  print('4 - Centimeters(cm) -> Inches (in)')
  print("")
  print('5 - Miles      (mi) -> Killometers(km)')
  print('6 - Killometers(km) -> Miles      (mi)')
  
  
  

  conv_type = input('Enter: ')
  while conv_type not in ('1', '2', '3', '4', '5', '6'):
    print('Invalid Selection')
    print('Please enter number in 1~6')
    conv_type = input('Enter: ')

  if conv_type == '1':
    # Ib -> gram
    pound = input("Enter the number in Pound(Ib) :")
    # weight conversion
    gram = float(pound) * GRAMS_PER_POUND
    print ("{:.2f} (lb) ==> {:.2f} (g)".format(float(pound), gram))

  elif conv_type == '2':
    # gram -> lb
    Grams = input("Enter the number in Grams(g) :")
    # weight conversion ( reverse to Ib -> gram )
    Pound = float(Grams) / GRAMS_PER_POUND
    print ("{:.2f} (g) ==> {:.2f} (lb)".format(float(Grams), Pound))

  elif conv_type == '3':
    # in -> cm
    Inches = input("Enter the number in Inches(in) :")
    # weight conversion
    Centimeters = float(Inches) * CENTIMETERS_PER_INCH
    print ("{:.2f} (in) ==> {:.2f} (cm)".format(float(Inches), Centimeters))

  elif conv_type == '4':
    # cm -> in
    Centimeters = input("Enter the number in Centimeters(cm) :")
    # weight conversion ( reverse to in -> cm )
    Inches = float(Centimeters) / CENTIMETERS_PER_INCH
    print ("{:.2f} (cm) ==> {:.2f} (in)".format(float(Centimeters), Inches))

  elif conv_type == '5':
    # mi -> km
    Miles = input("Enter the number in Miles(mi) :")
    # weight conversion
    km = float(Miles) * KILOMETERS_PER_MILE
    print ("{:.2f} (mi) ==> {:.2f} (km)".format(float(Miles), km))

  else:
    # km -> mi
    km = input("Enter the number in Kilometers(km) :")
    # weight conversion ( reverse to mi -> km )
    Miles = float(km) / KILOMETERS_PER_MILE
    print ("{:.2f} (km) ==> {:.2f} (mi)".format(float(km), Miles))

  print("done conversion")

  cont = input("Do another conversion (y/n)?")
  while cont not in ('y', 'Y', 'n', 'N'):
    print('Invalid Selection')
    cont = input("Do another conversion (y/n)?")
  
  if cont == 'N' or cont =='n':
    break

print("tereminate")
