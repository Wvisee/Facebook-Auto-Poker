#! /usr/bin/python
#############################################################################
# Facebook Auto-Poker Python V1.5					    #
# Written By: Dennis Linuz <dennismald@gmail.com> 			    #
# Edited By: William Visée <william.visee@student.uclouvain.be>             #
# Auto-pokes anyone on Facebook that has poked you with a Variable Delay    #
# and a file to specify which Facebook IDs NOT to poke (blockPokes.txt)	    #
#############################################################################
FACEBOOK_USERNAME = ""
FACEBOOK_PASSWORD = ""
import mechanize, time, os
MAX_DELAY = 60
delay = MAX_DELAY
totalPokes = 0
browser = mechanize.Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.61')]
browser.set_handle_robots(False)
browser.open("http://m.facebook.com/pokes")
browser._factory.is_html = True
browser.select_form(nr=0)
browser.form['email'] = FACEBOOK_USERNAME
browser.form['pass'] = FACEBOOK_PASSWORD
browser.submit()
browser._factory.is_html = True
while True:
	try:
		tempPokeCount = 0
		browser.open("http://m.facebook.com/pokes")
		browser._factory.is_html = True
		for l in browser.links(text_regex="Envoyer un poke en retour"):
			result = True
			browser._factory.is_html = True
			if result:
				browser.follow_link(text_regex="Envoyer un poke en retour",nr=0)
				tempPokeCount += 1
				totalPokes += 1
				print "Poked! Total Pokes: " + str(totalPokes) + "\n"
		if (tempPokeCount != 0 and delay > 1): delay /= 2
		if (tempPokeCount == 0 and delay < MAX_DELAY): delay *= 2
	except:
		print "There was some sort of error :("
	time.sleep(delay)
