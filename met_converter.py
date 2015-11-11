import numpy as np
import re
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import sys
import glob

def process(time):
    br = Browser()
    # Ignore robots.txt
    br.set_handle_robots( False )
    # Google demands a user-agent that isn't a robot
    br.addheaders = [('User-agent', 'Firefox')]
    br.open("http://heasarc.gsfc.nasa.gov/cgi-bin/Tools/xTime/xTime.pl")



    br.select_form("form")

    br["time_in_i"] = time # Enter your time in here in the format "2015-06-27 04:23:23.68"

    response=br.submit()

    html=response.read()
    soup = BeautifulSoup(html)


    table =soup.find("table", border=5)

    g = table.findAll('tr')

    row= g[7]

    cols = row.findAll('td')
    value = cols[1].string #This is the MET time

    print value

    return value



with open('times.txt') as f:
    content = f.readlines()

new_times=[]
for i in range(len(content)):
    t = content[i]
    MET =process(t)

    new_times.extend([MET])

with open('new_times.txt', 'w') as file:
    for i in new_times:
        file.write("%s " % i)
        file.write("\n " )

