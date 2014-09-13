tabby = "tabbed"
backslash = "\\ a \\"

tabby_cat = "\tI'm %r in." % tabby
persian_cat = "I'm split\non a line."
backslash_cat = "I'm %s cat." % backslash

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat