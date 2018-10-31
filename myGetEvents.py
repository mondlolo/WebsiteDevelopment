import sqlite3
myData = sqlite3.connect("tourGude.db")
allEvents = (myData.execute("select * from events"))

print('Content-type: text/html\n\n') 
#print("<html>")
#print("<head>")
#print("</head>")
#print("<body style = 'background-color:green'>")
#print("<h1>mond</h1>")
#print("</body>")
#print("</html>")
print(''+
'<html>'+
'<head>'+
    '<LINK rel = "stylesheet" href = "style.css">'+
'</head>'+
+'<body>'+
    +'<ul>'+
    '<li><a href="myWebsite.html">Home</a></li>'+
        '<li><a  href="events.html">Events</a></li>'+
        '<li><a class="active" href="registration.html">Registration</a></li>'+
        '<li style="float:right"><a href="#about">About</a>'+
    '</li>'+
    '</ul>'+


'<table>'+
    '<tr>'+
            '<th>EVENTS</th>'+
    '</tr>'+
    '<tr>'+
            '<td class = "label">'+
                'TITLE: '+
            '</td>'+
                 
            '<td class = "label">'+
                'DESCRIPTION: '+
            '</td>'
            
            '<td class = "label">'+
                'VENUE AND DATE: '+
            '</td>'+
        '</tr>')
print(
        
        '<tr>'+
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'+
                
         '</tr>'.format(allEvents[0][0],allEvents[0][1],allEvents[0][2]))
         
print(    '<tr>'+
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'+
                
         '</tr>'.format(allEvents[1][0],allEvents[1][1],allEvents[1][2]))
         
print(    '<tr>'+
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'+
                
         '</tr>'.format(allEvents[2][0],allEvents[2][1],allEvents[2][2]))
         
print(     '<tr>'+
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'+
                
         '</tr>'.format(allEvents[3][0],allEvents[3][1],allEvents[3][2]))
         
print(     '<tr>'+
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'
            
            '<td class = "label">'+"{}"+
                 
            '</td>'+
                
         '</tr>'.format(allEvents[4][0],allEvents[4][1],allEvents[4][2]))
         
print(
'</body>'+
'</html>')
