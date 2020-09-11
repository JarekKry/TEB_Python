from SimplePasswordManagerCore.PasswordDB import *

#DB = PasswordDB("nameᅧtestᅥloginᅧtestloginᅥpasswordᅧtestpasswordᅥurlᅧtesturlᅤnameᅧtest2ᅥloginᅧtestlogin2ᅥpasswordᅧtestpassword2ᅥurlᅧtesturl2")
DB = PasswordDB("")

DB.AddEntry("nameᅧadminᅥloginᅧadminᅥpasswordᅧadmin123ᅥurlᅧurlasd")

DB.AddEntry("nameᅧtestᅥloginᅧtestloginᅥpasswordᅧtestpasswordᅥurlᅧtesturl")


print(DB.isGood)

print('Entries count:',len(DB.entries))

for x in DB.entries:
    print(x.GetParmValue('name'))
    print(x.GetParmValue('login'))
    print(x.GetParmValue('password'))
    print(x.GetParmValue('url'))
    print('-----------------------')

print(bytes(DB.GetRawDBData(),'UTF-8'),file=open('test.txt','w'))

input()

