myIP = '192.168.28.50'
myIP.split('.')
if int(myIP.split('.')[-1]) <= 62:
    print("This IP falls within that range")
else:
    return
# Slicing
list = ['195', '168', '28', '50'
list[start:stop:step]

# Range uses commas [start,stop,step]

range(0,1024) # well known port range

#Format

first = 'aaron'
middle = 'andrew'
last = 'anderson'
domain = 'cornetto'
'{}.{}.{}@{}.com'.format(first, middle[0], last, domain)
        
#Dictionary
myDict = {'Pvt': 'E-1'}
myDict = {'PFC': 'E-2'}
for i in myDict:
    return [i] # Key or myDict[i] for values
myDict = []
myRoster = ['PFC', 'LCpl', 'LCpl', 'Pvt', 'PFC', 'Pvt', 'Sgt']
for i in myRoster:
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[1] = 1

        
        
        
#fileIO
with open('myfile.txt', 'r') as fp0:
    print(fp.read()[:3]) #first 3 charcters
    print(fp.readlines()[:3]) #first 3 lines
    lines0 = fp.readlines()
        
with open(outfile, 'w')as fp1:
    fp1.writelines(lines0)

        
        #or
        
        
with open(infile, 'r') as fp0:
    with open (outfile, 'w')as fp1:
        fp1.writelines(fp0.readlines())
