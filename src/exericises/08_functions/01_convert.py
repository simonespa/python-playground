# Miles and kilometers

def convert(miles):
  '''Converts miles in kilometers'''
  return round(miles * 1.6, 1)

miles = int(input('Enter miles: '))

print(f'{miles} miles convert to {convert(miles)} kilometers')
