#!/usr/bin/env python
#Author: Matt Batten (SleepZ3R0)  Special Thank you to Nate (m4dh4tt3r)
#09/06/2018  Version 1
#All Beacon Logs to CSV for most recent beacon
#csv will be saved in this directory: /redteam/logging/cobaltstrike/beaconid_All.csv
# Make sure you change the directory to where you have your cobaltstrike logs go


import csv, os, sys,time, datetime, time, operator, os.path

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

beaconlog = beaconlog.replace(".log", "_All.csv")
#Append All.csv

beaconlog = '/redteam/logging/cobaltstrike/' + beaconlog
#inserts the directory that we want the .csv to end up at

if not os.path.exists('/redteam/logging/cobaltstrike'):
	os.makedirs('/redteam/logging/cobaltstrike')

#checks if directory exists, if not creates it


with open(place, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open(beaconlog, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('')) 
        writer.writerows(lines)
