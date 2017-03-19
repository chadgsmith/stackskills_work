import re

f = open('ringCheckResults.txt', 'r')
numFailedNodes = 0
for line in f:
    if "Connecting to " in line:
        ip = None
        fail = None
        printed = False

    fIp = re.search('Connecting to ([\d\.]+)', line)
    fFail = re.search('fail&', flags = re.I)

    if fIp:
        ip = fIp.groups()[0]
    if fFail:
        print(ip)
        numFailedNodes += 1
        printed = True
