from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
import webbrowser
import pyfiglet
import time
from random import randint
from yaspin import yaspin, Spinner

URL = 'https://www.ncuindia.edu/announcements'
content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
contentDiv  = soup.find('section', { "id" : "placements"})
notices=contentDiv.find_all('a')
list1=[]
for n in notices:
  list1.append(n.get_text())

project_href = [i['href'] for i in contentDiv.find_all('a', href=True)]
# for a in announcements:
#   print(a.get_text())

mapped={}

keys=[]
for i in range(1,len(list1)+1):
  keys.append(i)

for key in keys:
   for value in project_href:
     mapped[key]=value
     project_href.remove(value)
     break
x=1

banner=pyfiglet.figlet_format("NCU  SOOCHNA")
print(banner)
for i in list1:

  print(str(x)+":",i)
  x=x+1
result = pyfiglet.figlet_format("Choose from above options", font = "digital" ) 
print(result)
while True:
 enter=int(input("Enter the option:"))

 if(enter in keys):
  #sp = Spinner(["😈", "👿"], 200)
  #with yaspin(sp, text="Loading.."):
    #time.sleep(6) 
  with yaspin(text="Loading", color="yellow") as spinner:
   time.sleep(4)  # time consuming code
  webbrowser.open_new(mapped[enter])


 else:
 
  print("Enter the correct option")


