#! /usr/bin/python

from sys import argv

command = argv[1]
PATH = '/Users/lucasamodeonewman/Desktop/Stuff/Now/Docs/phonebooks/'
default = 'friends'

def open_phonebook(phonebook_name, permission,  path=PATH):
    file_name = phonebook_name + '.pb'
    file_path = path + file_name
    phonebook = open(file_path, permission)
    return phonebook

# phonebook create friends
def create_phonebook(new_phonebook_name):
    new_phonebook = open_phonebook(new_phonebook_name, 'w')
    new_phonebook.close()
    print 'Phonebook:', new_phonebook_name, 'has been created.'

# phonebook add 'Lucas Newman' '310 266 3305' friends
def add_entry(name, number, phonebook_name=default):
    phonebook = open_phonebook(phonebook_name, 'a')
    new_entry = '%s : %s \n' % (name, number)
    phonebook.write(new_entry)
    phonebook.close()
    print 'Entry:', new_entry, 'has been added.'

# phonebook lookup 'Lucas' friends
def lookup_entry(name, phonebook_name=default):
    phonebook = open_phonebook(phonebook_name, 'r')
    matching_lines = 0
    for line in phonebook:
        if name in line:
            print line
            matching_lines += 1
    if matching_lines == 0:
        print 'No matching entries found.'
    phonebook.close()            
    
# phonebook change 'Lucas Newman' '703 536 2180' friends
def change_entry(name, number, phonebook_name=default):
    phonebook_original = open_phonebook(phonebook_name, 'r')
    phonebook_lines = phonebook_original.readlines()
    entry_update = '%s : %s \n' %  (name, number)
    
    possible_entries = []
    for line_number in range(len(phonebook_lines)):
        if name in phonebook_lines[line_number]:
                possible_entries.append((phonebook_lines[line_number], line_number))
                
    if len(possible_entries) < 1:
        print 'No matching entries found.'
    elif len(possible_entries) > 1:
        print 'Please be more specific in your search:'
        for i in possible_entries:
            print i[0]
    else:
        phonebook_lines[possible_entries[0][1]] = entry_update
        phonebook_new = open_phonebook(phonebook_name, 'w')
        for line in phonebook_lines:
            phonebook_new.write(line)
        phonebook_new.close()
        
        print 'Entry updated:', entry_update

# phonebook del 'Lucas Newman' friends        
def del_entry(name, phonebook_name=default):
    phonebook_old = open_phonebook(phonebook_name, 'r')
    phonebook_lines = phonebook_old.readlines()
    
    possible_entries=[]
    for line in phonebook_lines:
        if name in line:
            possible_entries.append(line)

    if len(possible_entries) < 1:
        print 'No matching entries found.'
    elif len(possible_entries) > 1:
        print 'Please be more specific:'
        for line in possible_entries:
            print line
    else:
        del phonebook_lines[possible_entries[0][1]]
        phonebook_new = open_phonebook(phonebook_name, 'w')
        for line in phonebook_lines:
            phonebook_new.write(line)
        phonebook_new.close()
        print 'Entry:', possible_entries[0], 'has been deleted.'

if command == 'create':
    create_phonebook(argv[2])
        
elif command == 'add':
    add_entry(argv[2], argv[3], argv[4])

elif command == 'lookup':
    lookup_entry(argv[2], argv[3])

elif command == 'change':
    change_entry(argv[2], argv[3], argv[4])

elif command == 'del':
    del_entry(argv[2], argv[3])

else:
    print 'Command not found.'
