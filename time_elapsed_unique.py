#time zone icin sadece saatlik cozunurluk oldugunu varsaydim. 
import re

def calculate_eclipse_time (time_str, first_oc):
    #print(time_str, " " , first_oc)
    months = [re.compile(r'Jan'), re.compile(r'Feb'), re.compile(r'Mar'), re.compile(r'Apr'), 
              re.compile(r'May'), re.compile(r'Jun'), re.compile(r'Jul'), re.compile(r'Aug'), 
              re.compile(r'Sep'), re.compile(r'Oct'),re.compile(r'Nov'), re.compile(r'Dec')]
    
    date_regex = re.compile('(0[1-9]|[1-2][0-9]|3[0-1])')
    month_regex = re.compile('[A-Z][a-z][a-z]')
    year_regex = re.compile('[0-9]{4}')
    hour_regex = re.compile('0[0-9]|1[0-9]|2[0-3]')
    min_regex = re.compile('[0-5][0-9]')
    sec_regex = re.compile('[0-5][0-9]')
    tz_regex = re.compile('\+[0][0-9][0][0]')
    added_regex = re.compile('[0][0-9][0][0]')
    
    month = ""
    date = -1
    year = -1
    
    year = int(year_regex.search(time_str).group())
    month = month_regex.search(time_str).group()
    
    j=1
    for item in months:
        
        if item.search(month):
            month = j 
            break;
        j = j+1
        
    date = int(date_regex.search(time_str).group())    
    hour = int(hour_regex.search(time_str,13,16).group())
    minute = int(min_regex.search(time_str,16,19).group())
    sec = int(sec_regex.search(time_str,19,22).group())
    tz = tz_regex.search(time_str).group()
    added = int(added_regex.search(tz).group())
    
    month_fo = ""
    date_fo = -1
    year_fo = -1
    
    year_fo = int(year_regex.search(first_oc).group())
    month_fo = month_regex.search(first_oc).group()
    
    k=1
    for item in months:
        if item.search(month_fo):
            month_fo = k
            break;
        k= k+1
        
    date_fo = int(date_regex.search(first_oc).group())    
    hour_fo = int(hour_regex.search(first_oc,13,16).group())
    minute_fo = int(min_regex.search(first_oc,16,19).group())
    sec_fo = int(sec_regex.search(first_oc,19,22).group())
    tz_fo = tz_regex.search(first_oc).group()
    added_fo = int(added_regex.search(tz_fo).group())
    
    if added_fo != added:
        hour = int((added_fo - added)/100) + hour
    total_ec = 0;
    if date_fo == date and year_fo == year and month_fo == month :
        total_ec = (hour - hour_fo)*3600 + (minute - minute_fo)*60 + (sec - sec_fo)
        return total_ec
    elif year_fo == year and month_fo == month :
        total_ec = (date - date_fo)*24*3600 + (hour - hour_fo)*3600 + (minute - minute_fo)*60 + (sec - sec_fo)
        return total_ec 
    
    prev_months = [] #previous months of entry
    next_months = [] #next months of first occurance.
    
    i=1
    while i<month:
        prev_months.append(i)
        i = i+1
    
    i=month_fo + 1
    while i<=12:
        next_months.append(i)
        i = i+1
    
    day_count = 0
    if month >= month_fo:
        between_months = []
        i=month_fo + 1
        while i<month:
            between_months.append(i)
            i = i+1
            
        for item in between_months:
            if (item == 4 or item ==6 or item==9 or item==11):
                day_count = day_count + 30
            elif item == 2 and year%4==0:
                day_count = day_count + 29
            elif item == 2 and year%4 != 0:
                day_count = day_count + 28
            else:
                day_count = day_count + 31
        
        if (month_fo == 4 or month_fo ==6 or month_fo==9 or month_fo==11):
            day_count = day_count + 30 - date_fo
        elif month_fo == 2 and year_fo%4==0:
            day_count = day_count + 29 - date_fo
        elif month_fo == 2 and year_fo%4 != 0:
            day_count = day_count + 28 - date_fo
        else:
            day_count = day_count + 31 - date_fo
        day_count = day_count + date
        
        if year == year_fo:
            total_ec = day_count*24*3600 + (hour - hour_fo)*3600 + (minute - minute_fo)*60 + (sec - sec_fo)
            return total_ec
        else:
            between_years = []
            m = year_fo + 1
            while m<year:
                between_years.append(m)
                m = m + 1
            
            for item in between_years:
                if item%4 == 0:
                    day_count = day_count + 366
                else:
                    day_count = day_count + 365
            
            if year_fo%4 == 0:
                day_count = day_count + 366
            else:
                day_count = day_count + 365
            if month == month_fo:
                if (month_fo == 4 or month_fo ==6 or month_fo==9 or month_fo==11):
                    day_count = day_count - 30
                elif month_fo == 2 and year_fo%4==0:
                    day_count = day_count - 29
                elif month_fo == 2 and year_fo%4 != 0:
                    day_count = day_count - 28
                else:
                    day_count = day_count - 31
                    
            total_ec = day_count*24*3600 + (hour - hour_fo)*3600 + (minute - minute_fo)*60 + (sec - sec_fo)
            
            return total_ec
            
    else:  # if month < month_fo
        for item in prev_months:
            if (item == 4 or item ==6 or item==9 or item==11):
                day_count = day_count + 30
            elif item == 2 and year%4==0:
                day_count = day_count + 29
            elif item == 2 and year%4 != 0:
                day_count = day_count + 28
            else:
                day_count = day_count + 31
                
        for item in next_months:
            if (item == 4 or item ==6 or item==9 or item==11):
                day_count = day_count + 30
            elif item == 2 and year%4==0:
                day_count = day_count + 29
            elif item == 2 and year%4 != 0:
                day_count = day_count + 28
            else:
                day_count = day_count + 31        
        
        day_count = day_count + date
        
        if (month_fo == 4 or month_fo ==6 or month_fo==9 or month_fo==11):
            day_count = day_count + 30 - date_fo
        elif month_fo == 2 and year_fo%4==0:
            day_count = day_count + 29 - date_fo
        elif month_fo == 2 and year_fo%4 != 0:
            day_count = day_count + 28 - date_fo
        else:
            day_count = day_count + 31 - date_fo
    
    if year_fo == year:
        if year%4==0:
            day_count = 366 - day_count
        else:
            day_count = 365 - day_count
        total_ec = day_count*24*3600 + (hour - hour_fo)*3600 + (minute - minute_fo)*60 + (sec - sec_fo)
        return total_ec
    elif (year - year_fo) > 1:
        between_years = []
        m = year_fo + 1
        while m<year:
            between_years.append(m)
            m = m + 1
        
        for item in between_years:
            if item%4 == 0:
                day_count = day_count + 366
            else:
                day_count = day_count + 365
        total_ec = day_count*24*3600 + (hour - hour_fo)*3600 + (minute - minute_fo)*60 + (sec - sec_fo)
        return total_ec
    
    total_ec = total_ec + day_count*24*60*60
    total_ec = day_count*24*3600 + (hour - hour_fo)*3600 + (minute - minute_fo)*60 + (sec - sec_fo)
    return total_ec     



f = open("log_q1.txt","r")

lines = f.readlines()

count=0
refresh = open("output_q1.txt", "w")
refresh.write("")
refresh.close()
output_f = open("output_q1.txt", "a")

ip_regex = re.compile('([0-9]{1,3}\.){3}[0-9]{1,3}')
ts_regex = re.compile('\[(0[1-9]|[1-2][0-9]|3[0-1])/[A-Z][a-z][a-z]/[0-9]{4}:(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]) \+[0-9]{4}\]')

        
i=0       
ip_list = []
ts_list = []
eclipse_time = 0

for line in lines:
    count += 1
    #print("Line{}: {}".format(count, line.strip()))
    
    
    if ip_regex.search(line) != None: 
        ip_item = ip_regex.search(line).group()
    else:
        continue
    
    if ts_regex.search(line) != None:    
        ts_item = ts_regex.search(line).group()
        
    else:
        continue
    
    if ip_list.__contains__(ip_item) is False: #first occurence
        ip_list.append(ip_item)
        ts_list.append(ts_item)
        output_f.write(ip_item)
        output_f.write(" ")
        output_f.write("0")
        output_f.write('\n')
    else:
        output_f.write(ip_item)
        output_f.write(" ")
        #print(ip_item, " ", ip_list[ip_list.index(ip_item)])
        #print(ts_list[ip_list.index(ip_item)], " " , ip_list[ip_list.index(ip_item)])
        eclipse_time = calculate_eclipse_time(ts_item, ts_list[ip_list.index(ip_item)])
        output_f.write(str(eclipse_time))
        output_f.write('\n')
        
           

f.close()
output_f.close()
    
    
