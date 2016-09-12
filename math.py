from sys import argv
from string import punctuation, digits
try:
  complete = ''
  for x in argv[1]:
    if x in punctuation or x in digits:
      complete += x
  print(eval(complete))
except IndexError:
  print('Not enough args')
except Exception: pass
