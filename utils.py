import string

def readline(filepath: string) -> string:
  file = open(filepath, 'r')
  return file.read()
