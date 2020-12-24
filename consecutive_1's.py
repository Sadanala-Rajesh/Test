import re
def find_max_consecutives(lst1):
    string = ""
    lst=[]
    for i in lst1:
        string +=str(i)
    matcher = re.finditer('1+',string)
    for i in matcher:
        lst.append(len(i.group()))
    print("The number of maximum consecutive  one’s present in the array :",'1'*max(lst),max(lst))
lst1=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
find_max_consecutives(lst1)
