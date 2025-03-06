import math
import string
import random

income = float(input('Enter monthly salary: \n'))
credit = float(input('Enter credit score: \n'))


if income >= 5000 and credit >= 55:
     print('Eligble')
else:
    print("Not Eligible")
   