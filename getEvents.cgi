import sqlite3
myData = sqlite3.connect("tourGude.db") # connecting to the database
allEvents = (myData.execute("select * from events")) # creates a directory for selects all the items from the database

print('Content-type: text/html\n\n')  # creates the html code using python

print('<html>') 
print('<head>')
print('<LINK rel = "stylesheet" href = "style.css">') # links the styles to the css style page
print('<body>')
print('<ul>')       # unordered list necessary for the tracking the navigation bar
print('<li><a href="myWebsite.html">Home</a></li>')
print('<li><a class="active"  href="events.html">Events</a></li>')     
print('<li><a  href="registration.html">Registration</a></li>')
print('<li style="float:right"><a href="#about">About</a>')
print('</li>')
print('</ul>')

print('<div id = "pos">')
print('<table>')   # creates atable for displaying all the events to the events page
print('<tr>')
print('<th>EVENTS</th>')
print('</tr>')
print('<tr>')
print('<td class = "label">')
print('TITLE: ')
print('</td>')
                 
print('<td class = "label">')       
print('DESCRIPTION: ')
print('</td>')
            
print('<td class = "label">')
print('VENUE AND DATE: ')
print('</td></tr>')


# for loop for all the events to be displayed into the table
for  i in allEvents:
    
    print('<tr><td class = "label">{}</td><td class = "label">{}</td><td class = "label">{}</td></tr>'.format(i[0],i[1],i[2]))
         

         
print("</div>")
print('</body></html>') # ends the css page
