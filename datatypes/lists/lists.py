names = ['Vladimir', 'Valeriy', 'Elena']
 
# update names in list
names[2] = 'Igor'

# append names
names.append('John')

# extend names
names.extend(['Timati', 'Buzova'])

# remove names
names.remove('Vladimir')

# remove first name from list
removed = names.pop(1)
print(removed)

#  Print list of names
print(names)

# print name as index
print(names[0])

if 'Vladimir' in names:
    print(f'Vladimir is in the list')
else:
    print('Where is Vladimir?')
    
if 'Elena' not in names:
    print(f'Elena is not in the list')