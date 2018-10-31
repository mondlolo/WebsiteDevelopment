import sqlite3
import sys
myData = sqlite3.connect("tourGude.db")
allEvents = (myData.execute("select * from events"))

<img src = "hedge.jpg">


for i in allEvents:
    print(i[0])


''''<table>'+
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
        '</tr>'
        
        '<tr>'+
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'+
                
         '</tr>'+
         
         '<tr>'+
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'+
                
         '</tr>'+
         
         '<tr>'+
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'+
                
         '</tr>'+
         
         '<tr>'+
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'+
                
         '</tr>'+
         
         '<tr>'+
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'
            
            '<td class = "label">'+
                 
            '</td>'+
                
         '</tr>'+
         
'</table>'+
'''