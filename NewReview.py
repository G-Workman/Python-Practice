myIP = 192.168.28.50
myIP.split('.') # <------- splits ip on the .
if int(myIP.split('.')[-1] <= 62:
       print("This IP falls within that range"


#Dictionaries
myDict = {'PVT':'E-1'}
myDict['PVT']
'E1'
myDict['PFC'] = 'E-2'
myDict = {'VT':'E-1', 'PFC':'E-2'}
for i in myDict
  print(myDict[i])
E1
E2

for i in myDict:
   print(myDict(i))
PVT
PFC
             

             
#format
first = 'aaron'
middle = 'andrew'
last = 'anderson'
domain = 'cornetto'             
'{}.{}.{}@{}.com.format(first, middle[0], last, domain)             
             
# SLICING: list vs range
# LIST
mylist = ['195' '168' '28' '50']
myOctets[0:3]
['195' '168' '28']
[:-1] <--------- # start at the beginning of the list and stop at the end of the list
             
# RANGE
list(range(0,10))
[0,1,2,3,4,5,6,7,8,9]
 
# FILEIO
with open('myfile.txt, 'r') as fp:
  print(read*([:3])
      
# Copy from one file to another
infile = 'myfile.txt
outfile = 'outfile.txt'
with open(infile, 'r') as fp0:
  lines0 = fp0.readlines()
with open(outfile, 'w')as fp:
  fp.writelines(lines0)
        
        OR
        
with open(infile, 'r') as fp0:
    with open(outfile, 'w')as fp:
        fp.writelines(fp0.readlines()[2]) <-----# readlines puts the text in a list and the index of 2 grabs the second index of that list
        
        
        
        
     #----------------------------- Extra notes added by smarter individual-------------------------------
>>> myStringEx = 'this is my list'
>>> mylist = myStringEx.split("")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: empty separator
>>> mylist = myStringEx.split(" ")
>>> mylist
['this', 'is', 'my', 'list']
>>> list[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> mylist[3]
'list'
>>> list(mylist[3])
['l', 'i', 's', 't']
>>> '*'.join(list(mylist[3]))
'l*i*s*t'
>>> myIP = '192.168.28.50'
>>> myIP
'192.168.28.50'
>>> #this is a string, if wanted to split into octet then split on "."
... myIP.split(".")
['192', '168', '28', '50']
>>> #if wanted to check if ip in range 12.168.28.0 and 192.168.28.62
... 
>>> if int(myIP.split(".")[-1]) <= 62:
...     print ("in range")
... 
in range
>>> lastOctet = myIP.split(".")[-1]
>>> lastOctet
'50'
>>> #range is start, stop, step
... 
>>> myOctets = myIP.split('.')
>>> myOctets[1]
'168'
>>> myOctets[0:3]
['192', '168', '28']
>>> myOctets[0:3:1]
['192', '168', '28']
>>> myOctets[-1]
'50'
>>> myOctets[-2:]
['28', '50']
>>> #[-2:] goes from 2nd to last and goes to the end
... 
>>> myString = 'The quick brown fox jumps over the lazy dog'
>>> myString[::-1]
'god yzal eht revo spmuj xof nworb kciuq ehT'
>>> myString[3::]
' quick brown fox jumps over the lazy dog'
>>> myString[::3]
'T i o xusv ea g'
>>> range(0,10)
range(0, 10)
>>> type(range(0,10))
<class 'range'>
>>> #goes from 0-9
... 
>>> for i in range(0,10):
...     print(i)
... 
0
1
2
3
4
5
6
7
8
9
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,50,10))
[0, 10, 20, 30, 40]
>>> list(range(50,0,-10))
[50, 40, 30, 20, 10]
>>> list(range(51,0,-10))
[51, 41, 31, 21, 11, 1]
         
         
         
         
>>> first = 'aaron'
>>> middle = 'andrew'
>>> last = 'anderson'
>>> domain = 'cornetto'
>>> #make in to an email address first.middleinitial.last@domain.com
... 
>>> '{}.{}.{}@{}.com'.format(first,middle[0],last,domain)
'aaron.a.anderson@cornetto.com'
>>> f'{first].{middle[0]}.{last}@{domain}.com'
  File "<stdin>", line 1
SyntaxError: f-string: expecting '}'
>>> f'{first}.{middle[0]}.{last}@{domain}.com'
'aaron.a.anderson@cornetto.com'
>>> #if only want fitst 5 letters of last name
... 
>>> f'{first}.{middle[0]}.{last[:5]}@{domain}.com'
'aaron.a.ander@cornetto.com'
>>> f'{first[0]}{middle[0]}{last[:5]}@{domain}.com'
'aaander@cornetto.com'


>>> #DICTONARY----------------------
... 
>>> myDict = {}
>>> #things in dictonaries get referenced my key value pairs
... myDict['Pvt'] = 'E-1'
>>> myDict
{'Pvt': 'E-1'}
>>> myDict['PFC'] = 'E-2'
>>> myDict
{'Pvt': 'E-1', 'PFC': 'E-2'}
>>> #iterate through this dict, pull out the keys
... 
>>> for i in myDict:
...     print(myDict[i])
... 
E-1
E-2
>>> for i in myDict:
...     print(i)
... 
Pvt
PFC
>>> myDict1 = {}
>>> myRoster = ['PFC', 'Lcpl', 'Lcpl', 'Pvt', 'PFC', 'Pvt', 'Sgt']
>>> myRoster
['PFC', 'Lcpl', 'Lcpl', 'Pvt', 'PFC', 'Pvt', 'Sgt']
>>> #want to count how many times in roster
... 
>>> for i in myRoster:
...     if i in myDict:
...             myDict[i] +=1
...     else:
...             myDict[i] = 1
... 
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: must be str, not int
>>> for i in myRoster:
...     if i in myDict1:
...             myDict1[i] +=1
...     else:
...             myDict1[i] = 1
... 
>>> myDict1
{'PFC': 2, 'Lcpl': 2, 'Pvt': 2, 'Sgt': 1}
>>> myDict1['PFC']
2
>>> myRank = 'Sgt'
>>> myDict1[myRank]
1


>>> #dictonaries, format, and file io are key things students miss
... 


>>> myEmail = f'{first}.{middle[0]}.{last}@{domain}.com'
>>> myEmail
'aaron.a.anderson@cornetto.com'
>>> noT = myEmail.split("@")[0].split(".")
>>> noT
['aaron', 'a', 'anderson']
>>> noAt = myEmail.split('@')
>>> noAt
['aaron.a.anderson', 'cornetto.com']
>>> dots = '.'.join(noAt)
>>> dots
'aaron.a.anderson.cornetto.com'
>>> split = dots.split('.')
>>> split
['aaron', 'a', 'anderson', 'cornetto', 'com']
>>> final = split[:-1]
>>> final
['aaron', 'a', 'anderson', 'cornetto']
>>> 
