from sys import argv

script, user_name, drink = argv
prompt = 'answer me now... '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "I know your fav drink is %s but how about food?" % drink
favfood = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
Your favourite food is %s.
And you have a %r computer. Nice.
""" % (likes, lives, favfood, computer)