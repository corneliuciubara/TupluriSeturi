import datetime
import calendar

def numarazilele(inceput, sfarsit):
  start_date = datetime.datetime.strptime(inceput, '%d/%m/%Y')
  end_date = datetime.datetime.strptime(sfarsit, '%d/%m/%Y')
  week = {}
  for i in range((end_date - start_date).days):
    day = calendar.day_name[(start_date + datetime.timedelta(days=i+1)).weekday()]
    week[day] = week[day] + 1 if day in week else 1
  return week

print(numarazilele("01/01/2022", "01/11/2022"))


