#!/usr/bin/env python2

import mechanize
from time import sleep
'''
Used to bulk enter names and email addresses to a contest web form.  Currently, data entry is done by manually populating
the 'user_entries' list with dict items containing first, last and email.

Future updates will allow for providing a CSV file in order to inport and parse this data. 
'''

br=mechanize.Browser()
url="http://www.janbrett.com/contest_2018/2018_free_school_or_library_visit.htm" #Simple http site that contains the web form we need to use
br.set_handle_robots(False) #Site robots.txt does not like automation - we will ignore, but will make sure we do not abuse!
br.open(url)
'''
Use the below to eplore the various forms a page has to offer, if needed
'''
#for form in br.forms():
#    print "Form name:", form.name
#    print form

'''
Our page only has a single form, so easy to identify.  If necessary, use the below to iterate through the various form fields that are
available to use.
'''
#for control in br.form.controls:
#    print control
#    print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

br.select_form("FrontPage_Form1")
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]
'''
Let's now select the appropriate form to fill out, and set our browser header.
'''

user_entries=[
{'first':"Firstname", 'last':"Lastname", 'email':"someone@somewhere.net"}
]
'''
User data is a list of dictionaries - formatted with first name, last name and email.  (The rest of the form data is all static, so we will define that 
within the for itself as it will stay the same for every entry)
'''
for entry in user_entries:
    fullname=entry["first"] + ' ' + entry["last"]
    emadd=entry["email"]
    print '*' * 50
    print "Adding record for %s (%s)" % (fullname,emadd)
    print '*' * 50
    '''
    After parsing through the list of user_entries and creating the records for the user (first and last) as well as email address, we submit that data - 
    along with the static data for the school - to the webform
    '''
    br.form['your_name'] = fullname
    br.form['your_email'] = emadd
    br.form['school_library'] = 'St Mark School'
    br.form['address'] = '500 Wigwam Lane'
    br.form['city'] = 'Stratford'
    br.form['state'] = 'CT'
    br.form['zipcode'] = '06614'
    response=br.submit()
    print response.read()
    print "Complete, waiting 5 seconds before sending next record"
    sleep(5.0) #Adjust sleep as needed - we set this so as to not cause a denial of service against the web form 
    br.back() #After submission and sleep, go back in browser and re-select the form in order to submit the next record.
    br.select_form("FrontPage_Form1")
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]

'''
Once all records have been sent, the loop exits and we end the program, citing the number of records we sent
'''
records=len(user_entries)
print '*' * 50
print "%s records sent successfully, now exiting" % (records)
print '*' * 50
