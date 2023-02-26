
win_packet = [['EventID', ':', '4672'],
              ['MachineName', ':', 'ZEUS'],
              ['Data', ':', '{}'],
              ['Index', ':', '109583'],
              ['Category', ':', '(12548)'],
              ['CategoryNumber', ':', '12548'],
              ['EntryType', ':', 'SuccessAudit'],
              ['Message', ':', 'Special', 'privileges', 'assigned', 'to', 'new', 'logon.', 'Subject:', 'Security', 'ID:', 'S-1-5-18', 'Account', 'Name:', 'SYSTEM', 'Account', 'Domain:', 'NT', 'AUTHORITY', 'Logon', 'ID:', '0x3e7', 'Privileges:', 'SeAssignPrimaryTokenPrivilege', 'SeTcbPrivilege', 'SeSecurityPrivilege', 'SeTakeOwnershipPrivilege', 'SeLoadDriverPrivilege', 'SeBackupPrivilege', 'SeRestorePrivilege', 'SeDebugPrivilege', 'SeAuditPrivilege', 'SeSystemEnvironmentPrivilege', 'SeImpersonatePrivilege', 'SeDelegateSessionUserImpersonatePrivilege'],
              ['Source', ':', 'Microsoft-Windows-Security-Auditing'],
              ['ReplacementStrings', ':', '{S-1-5-18,', 'SYSTEM,', 'NT', 'AUTHORITY,', '0x3e7...}'],
              ['InstanceId', ':', '4672'], ['TimeGenerated', ':', '10/10/2022', '11:54:43', 'AM'],
              ['TimeWritten', ':', '10/10/2022', '11:54:43', 'AM'],
              ['UserName', ':'],
              ['Site', ':'],
              ['Container', ':']]

#make class for adding key value pairs a bit more functional and easy
class mydict(dict):
    def __init__(self):
        self = dict()

    #allows add function on children of this class
    def add(self,key ,value):
        self[key] = value
    
parsedict = mydict()


def format_log_to_dict(log):
    
    #Format is messy, need to pick it apart and concat areas that are spaced out by word.
    #This checks the length of each entry, and since each entry is a list it is easy to target each individual part
    #If length > 2, comcat everything after the 0 index as it is all data and then add to dict with loop
    for entry in log:
        if len(entry) > 2: 
            key1 = entry[0]
            stringdata = ''
            for I in entry[1::]:
                if I != ':':
                    stringdata = stringdata+' '+str(I)
            parsedict.add(key1, stringdata)
        else:
            #everything that is only two items gets added here.
            #if the value is just a colon, then the value is empty on the key pair 
            for item in entry:
                parsedict.add(entry[0], item)
        print()


format_log_to_dict(win_packet)

print(parsedict)
parsedata = open('parse.txt', 'w')
parsedata.write(str(parsedict))
parsedata.close()