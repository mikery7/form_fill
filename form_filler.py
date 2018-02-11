#

import mechanize
from time import sleep

br=mechanize.Browser()
url="http://www.janbrett.com/contest_2018/2018_free_school_or_library_visit.htm"
br.set_handle_robots(False)
br.open(url)
#for form in br.forms():
#    print "Form name:", form.name
#    print form

br.select_form("FrontPage_Form1")
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]
#for control in br.form.controls:
#    print control
#    print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

user_entries=[
{'first':"Firstname", 'last':"Lastname", 'email':"someone@somewhere.net"}
]

for entry in user_entries:
    fname=entry["first"]
    lname=entry["last"]
    fullname=fname + ' ' + lname
    emadd=entry["email"]
    print '*' * 50
    print "Adding record for:"
    print fullname, emadd
    print '*' * 50
    br.form['your_name'] = fullname
    br.form['your_email'] = emadd
    br.form['school_library'] = 'St Mark School'
    br.form['address'] = '500 Wigwam Lane'
    br.form['city'] = 'Stratford'
    br.form['state'] = 'CT'
    br.form['zipcode'] = '06614'
    response=br.submit()
    print response.read()
    print "Complete, waiting 10 seconds before sending next record"
    sleep(0.0)
    br.back()
    br.select_form("FrontPage_Form1")
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]

records=len(user_entries)
print '*' * 50
print "%s records sent successfully, now exiting" % (records)
print '*' * 50
