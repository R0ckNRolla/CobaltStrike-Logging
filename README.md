# mrbs.py
mrbs = (most recent beacon survey)
## Author: Matt Batten (SleepZ3R0)  Special Thank you to Nate (m4dh4tt3r)
### Survey Script to .CSV

This script allows an operator to take data from the CobaltStrike Logs and outputs it to a CSV.  When you run this script it takes the text from the most recent beacon in your log files between the START and END points that you specify in the script and outputs it to a .CSV

* In the script make sure that you specify where your Cobalt Strike Logs are for the directory=os.path.join("/opt/cobaltstrike/logs/%s") %(date)

Also specify the Starting and End points

* start = "where you want it to start"

* end = "where you want it to end" 

that way you only pull the data you want



here is an example for someone who wants to watch a video

# Video Example

  [![Alt text](https://img.youtube.com/vi/XWV60J8m3S4/0.jpg)](https://youtu.be/XWV60J8m3S4)
