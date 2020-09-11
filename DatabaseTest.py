from SimplePasswordManagerCore.SimpleDB import SimpleDB

DB = SimpleDB("nameᅧadminᅥloginᅧadminᅥpasswordᅧadmin123ᅥurlᅧurlasdᅤnameᅧtestᅥloginᅧtestloginᅥpasswordᅧtestpasswordᅥurlᅧtesturl")
#DB = SimpleDB("")

DB.AddEntry("nameᅧadminᅥloginᅧadminᅥpasswordᅧadmin123ᅥurlᅧurlasd")

DB.AddEntry("nameᅧtestᅥloginᅧtestloginᅥpasswordᅧtestpasswordᅥurlᅧtesturl")


print(DB.isGood)

print('Entries count:',len(DB.entries))

for x in DB.entries:
    print('-----------------------')
    print(x.GetParmValue('name'))
    print(x.GetParmValue('login'))
    print(x.GetParmValue('password'))
    print(x.GetParmValue('url'))
    

print(DB.GetRawDBData())