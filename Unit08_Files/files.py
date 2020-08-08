import dbm


fout = open('output.txt', 'w')

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land.\n"

fout.close()


# Except clause
try:
    fin = open('bad_file')
except:
    print("This file isn't available.")


db = dbm.open('captions', 'c')
db['cleese.png'] = 'Photo of John Cleese.'
db['terry.png'] = 'Photo of Terry.'

for key in db:
    print(key)

db.close()
