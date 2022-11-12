import os
import sys



banner ="""\n
███    ███ ██████     ██     ██ ██ ██████  ██████  
████  ████ ██   ██    ██     ██ ██ ██   ██ ██   ██ 
██ ████ ██ ██████     ██  █  ██ ██ ██████  ██████  
██  ██  ██ ██   ██    ██ ███ ██ ██ ██      ██      
██      ██ ██   ██ ██  ███ ███  ██ ██      ██    
Github Link: \n"""



print(banner)
occs_values = []
occs_names = []

print("file path example: C:\\Users\\Eric\Desktop\\beeline.txt")
filename = input("\nPlease type the file path: ")


def count_occurences(text):

  new_text = list(text.split())
  list_size = int(len(new_text))
  total = 0

  while total < list_size:
    for i in new_text:
        if i not in occs_names:
          occurences = new_text.count(i)
          occs_names.append(i)
          occs_values.append(occurences)
          total+=1
        else:
          total+=1
          continue
  names_and_values = [list(e) for e in zip(occs_names, occs_values)]
  most_occurring = max(names_and_values, key=lambda x: x[1])
  print(f'\nThe most occurring word is {most_occurring[0]}: {most_occurring[1]}')


def openfile(file):
  if os.path.exists(file):
    with open(file, 'r') as f:
      text = f.read()
      count_occurences(text)
  else:
    print("Please type a valid file path, eg: C:\\Users\\Eric\Desktop\\beeline.txt")
    sys.exit()

openfile(filename)

# Todo: 1. Accept parentheses () and slashes \ and - or any symbol and remove them.