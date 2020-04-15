import calendar
year = 2020

#(a)

cal = calendar.TextCalendar() # Create an instance
cal.pryear( year ) # print the whole calendar

#(b)

cal.setfirstweekday(3)
cal.pryear( year )

#(c)

cal.prmonth( year, 11 ) # print only the 11th month

#(d)

d = calendar.LocaleTextCalendar(6, "ITALIAN") # change language
d.pryear( year )

#(e)

print( calendar.isleap( year ) ) # tell you if the year is leap