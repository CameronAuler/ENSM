
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

def format_log(log):
    for entry in log:
        if entry[0] == "Message":
            for item in entry:
                if ":" in item and item != ":" and "C:" not in item:
                    print()
                    print(f"- {item}", end="")
                else:
                    print(item, end="")
        else:
            for item in entry:
                print(item, end="")
        print()

format_log(win_packet)