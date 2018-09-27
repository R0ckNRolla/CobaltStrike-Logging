#!/usr/bin/env python
#Author: Matt Batten (SleepZ3R0)  Special Thank you to Nate (m4dh4tt3r)
#09/08/2018  Version 1
#Survey Script to CSV for most recent beacon
#csv will be saved in this directory: /redteam/logging/cobaltstrike/beaconid.csv
#Change Start = "wherever you want to start at"
#Change End = "Wherever you want to end at"
#mrbs=most recent beacon survey


import csv, os, sys,time, datetime, time, operator, os.path, re

date = datetime.datetime.today().strftime('%y%m%d')

alist={}
now = time.time()
directory=os.path.join("/opt/cobaltstrike/logs/%s") %(date)
os.chdir(directory)
for file in os.listdir("."):
    if os.path.isdir(file):
        timestamp = os.path.getmtime( file )

        # get timestamp and directory name and store to dictionary

        alist[os.path.join(os.getcwd(),file)]=timestamp

# sort the timestamp 

for i in sorted(alist.iteritems(), key=operator.itemgetter(1)):
    latest="%s" % ( i[0])

# latest=sorted(alist.iteritems(), key=operator.itemgetter(1))[-1]

newip = latest

os.chdir(latest)

beaconlog = min(os.listdir(newip), key=os.path.getctime)

place = "%s/%s" %(newip, beaconlog)
#Adds the beacon.log to the path

beaconlog = beaconlog.replace(".log", ".csv")
#Get rid of the .log so it can be .csv

beaconlog = '/redteam/logging/cobaltstrike/' + beaconlog
#inserts the directory that we want the .csv to end up at

if not os.path.exists('/redteam/logging/cobaltstrike'):
	os.makedirs('/redteam/logging/cobaltstrike')

#checks if directory exists, if not creates it

start = "=========System Info=========="
end = "eNd"
buffer = ""
log = False

for line in open(place):
  if line.startswith(start):
    buffer = line
    log = True
  elif line.startswith("received output:"):
    log = True
  elif re.match(r"\d\d/\d\d+", line):
    log = True
  elif line.startswith(end):
    buffer += line
    log = False
  elif log:
    buffer += line

open('stuff.log', 'w').write(buffer)

if log == True:
  print("End string was not found")


with open('stuff.log', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open(beaconlog, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow((''))
        writer.writerows(lines)

stuff = "/stuff.log"

delete = "%s/%s" %(newip,stuff)

os.remove(delete)
#cleanup so it's not the newest file created in the directory
