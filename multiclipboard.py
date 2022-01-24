import sys
import clipboard
import json


SAVED_DATA = 'clipboard.json'


def save_data(filepath, data):
  with open(filepath, 'w') as f:
    json.dump(data, f)


def load_data(filepath):
  try:
    with open(filepath, 'r') as f:
      data = json.load(f)
      return data
  except:
    return {}


if len(sys.argv) == 2:
  command = sys.argv[1]

  data = load_data(SAVED_DATA)
  
  # Save a data
  if command == 'save':
    key = input('Enter a key: ')
    data[key] = clipboard.paste()
    save_data(SAVED_DATA, data)
    print('Data saved!')

  # Load a data
  elif command == 'load':
    key = input('Enter a key: ')
    if key in data:
      clipboard.copy(data[key])
      print('Data copied to clipboard.')
    else:
      print('Key does not exist.')

  # Remove a data
  elif command == 'remove' or command == 'rm':
    key = input('Enter a key: ')
    if key in data:
      data.pop(key)
      save_data(SAVED_DATA, data)
      print('Data removed!')
    else:
      print('Key does not exist.')

  # List all data
  elif command == 'list' or command == 'ls':
    print(data)

  else: 
    print('Unknow command.')

else: 
  print('Please pass exactly one command.')
  