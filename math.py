from sys import argv
from string import punctuation, digits
try:
  complete = ''
  for x in argv[1]:
    if x in punctuation or x in digits:
      complete += x
  data = float(eval(complete))
  if int(str(data).split('.')[1]) == 0:
    print(int(data))
  else:
    print(data)
except IndexError:
  print('Not enough args')
except Exception: pass

