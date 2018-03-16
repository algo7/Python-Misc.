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
d0 = datetime.datetime.today() #Today's Date

def GetDatefunc():

        UserIn = input("Start Date (DD/MM/YYYY):")
        try:
            ds = datetime.datetime.strptime(UserIn, "%d/%m/%Y")
        except Exception as e:
            print ("ops watch the format!")
        else:
            return ds

def GetDatefunc2():
        UserIn2 = input("End Date (DD/MM/YYYY):")
        try:
            df = datetime.datetime.strptime(UserIn2, "%d/%m/%Y")
        except Exception as e:
            print ("ops watch the format!")
        else:
            return df

ds = GetDatefunc()
df = GetDatefunc2()



#ds = datetime.date(2017,12,13)
#df = datetime.date(2017,12,27)
#tmr = datetime.date.today() + datetime.timedelta(days=1)

#-------------------------Calculate Differences-------------------------
dealta = df - d0
dealtac = df - ds
dealc = d0 - ds

#-------------------------Define Page Number and Calculate Average Page per Day-------------------------
#Page = 300.0
Page = int(input("Enter the Amount of Page:"))
PageLeftc = Page / dealtac.days
PageLeft = Page - dealc.days * PageLeftc

#PageLeft = Page - dealta.days * PageLeftc
#PageLeft = Page - dealta.days * int(PageLeftc)
#round (Page / dealta.days, 2)

#-------------------------Print Outputs-------------------------
print(calendar.month(x,y))
print ("Time till Exam:", dealta.days)
print ("Page Per Day:", round(PageLeftc,2))
print ("Page Left:", PageLeft)
