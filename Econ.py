#import calendar

#x=int(input("Number of Pages:"))
#y=int(input("Input the date:"))
#print(calendar.month(x,y))
#now = datetime.datetime.now()
#print(now)
#d0 = datetime.datetime.now()
#a= datetime.datetime.now().date
#print x,y

#-------------------------Libraries-------------------------
import datetime
import calendar

#-------------------------Define Var. For Current Month and Year-------------------------
x = datetime.datetime.now().year
y = datetime.datetime.now().month

#-------------------------Define Var. For Current Date and Target Date-------------------------
d0 = datetime.date.today()
ds = datetime.date(2017,12,13)
df = datetime.date(2017,12,27)
#tmr = datetime.date.today() + datetime.timedelta(days=1)

#-------------------------Calculate Differences-------------------------
dealta = df - d0
dealtac = df - ds
dealc = d0 - ds 

#-------------------------Define Page Number and Calculate Average Page per Day-------------------------
Page = 300.0
PageLeftc = Page / dealtac.days
PageLeft = Page - dealc.days * PageLeftc
#PageLeft = Page - dealta.days * PageLeftc
#PageLeft = Page - dealta.days * int(PageLeftc)
#round (Page / dealta.days, 2)

#-------------------------Print Outputs-------------------------
print(calendar.month(x,y))
print "Time till Exam:",dealta.days
print "Page Per Day:", round(PageLeftc,2)
print "Page Left:", PageLeft



