#!/usr/bin/python
from sys import argv

def safe_eval(string, d={"__builtins__":None}):
  return eval(string, d)

if __name__ == '__main__':
  print(eval(' '.join(argv[1:])))

