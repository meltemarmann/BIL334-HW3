# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:33:52 2023

@author: MeltemArman
"""

import re

f = open("log_q2.txt","r")
lines = f.readlines()
f.close()

refresh = open("output_q2.txt", "w")
refresh.write("")
refresh.close()
output_f = open("output_q2.txt", "a")

file_names = []
item_count = []
file_regex = re.compile(r'GET /*[\S]*(/[\S]*)*') #GET /[\S]*(/[\S])*
fname_regex = re.compile(r'/([A-Z]|[a-z]|\.|[0-9]|_|-)+$')
x = re.compile(r'/')
count =0
for line in lines:
    count += 1
    #print("Line{}: {}".format(count, line.strip()))
    if file_regex.search(line) != None: 
        file_item = file_regex.search(line).group()
        
        if fname_regex.search(file_item) != None:
            file_name = fname_regex.search(file_item).group()
            if file_names.__contains__(file_name) is False and x.fullmatch(file_name) is None:  #ilk kayit
                file_names.append(file_name)
                item_count.append(1)
            
            elif file_names.__contains__(file_name) and x.fullmatch(file_name) is None:
                item_count[file_names.index(file_name)] += 1
#http://137.74.94.26:80/db/scripts/setup.php
rows = len(file_names)
cols = 2
arr = [[0] * cols for _ in range(rows)]

for i in range(rows):
    arr[i][0] = file_names[i]
    arr[i][1] = item_count[i]
  
sorted_list = sorted(arr, key=lambda x: x[1],reverse=True)
for i in range(len(file_names)):
    output_f.write(f"{sorted_list[i][0]} {sorted_list[i][1]}\n")



output_f.close()    