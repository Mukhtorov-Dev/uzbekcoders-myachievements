# -*- coding: utf-8 -*-
"""
Sat Apr 17 12:47:05 2021
GitHub:
Telegram: @Oybek_Mukhtarov
"""

# Bu 1 - kod
text = "again"
def reverse(text):
    #complete this function so that it takes string x as an input 
    #and returns its reverse
    a = text
    return a[::-1]
print("the reversed text is: "+reverse(text))


# Bu 2 - kod
no_list = [22,68,90,78,90,88]
def average(x):
    #complete the function's body to return the average
    a = (no_list[0]+no_list[1]+no_list[2]+no_list[3]+no_list[4]+no_list[5])/6
    return a
print(average(no_list))


# Bu 3 - kod
no_list = [1,2,3,4]

def maximum(no_list):
    #complete the function to return the highest number in the list
    a = max(no_list)
    return a
print(maximum(no_list))


# Bu 4 - kod
no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]
def unique_list(list1):
    #complete the function's body to return the unique list of numbers
    a = set(list1)
    return list(dict.fromkeys(list1))
print(unique_list(no_list))
