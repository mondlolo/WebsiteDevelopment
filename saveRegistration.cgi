

import cgi
import sqlite3







def write2file(Name,Surname,StudentNumber,Interests,date):  # returns a boolean whether information stored or not true for stored, not true for not stored.
    
    try:
        myClub =  sqlite3.connect("tourGude.db") # connects to the database
        myClub.execute("insert into Members values(?,?,?,?,?)",(Name,Surname,StudentNumber,Interests,date)) # inserts values into the table in the database
        myClub.commit()
        return True
    except:
        return False

def main():
    fields = cgi.FieldStorage() # since gci has fields stored, this enables indo to be extracted in a form of a dictionary such that you can call the values using keys
    written = write2file(fields.getvalue("Name"),fields.getvalue("Surname"),fields.getvalue("StudentNumber"),fields.getvalue("Interests"),fields.getvalue("Date"))# gets all the information stored by calling the keys
    Name = fields.getvalue('Name') 
    Surname = fields.getvalue('Surname')

    # generate results HTML page
    print('Content-type: text/html\n\n') #specify html content type
   
    
    print('<html>')
    print('<head> <TITLE>Registration</TITLE>')
    print('<LINK rel = "stylesheet" href = "style.css">')
    print('<body>')
    print('<ul>')       # navigation bar
    print('<li><a href="myWebsite.html">Home</a></li>') 
    print('<li><a   href="events.html">Events</a></li>')     
    print('<li><a class="active" href="registration.html">Registration</a></li>')
    print('<li style="float:right"><a href="#about">About</a>')
    print('</li>')
    print('</ul>')
    
    
    if written: # writes ito the page and reports back whether registered or not.
        print('<P class = "textColor">' + Name + " "+Surname + ' CONGRATULATIONS! YOU HAVE BEEN REGISTERED, YOU ARE NOW A MEMBER OF TOURISM SOUTH AFRICA.</P>')
    else:    
        print('<Pclass = "textColor">' +Name + " "+Surname  + 'SORRY! YOU ARE NOT REGISTERED. THERE MIGHT BE SOME TECHNICAL PROBLEMS, PLEASE TRY AGAIN LATER.</P>')
    print('</body></html>')
main()
