from sys import argv
try:
  print(eval(argv[1]))
except Exception:
  print('Not enough args')
