from SimplePasswordManagerCore.SimpleEncryption import SimpleEncryptor
from SimplePasswordManagerCore.SimpleDB import SimpleDB

DB = SimpleDB("nameᅧadminᅥloginᅧadminᅥpasswordᅧadmin123ᅥurlᅧurlasdᅤnameᅧtestᅥloginᅧtestloginᅥpasswordᅧtestpasswordᅥurlᅧtesturl")
print(DB.isGood)

encryptor = SimpleEncryptor('test')

#file = open('testDB.txt','w')
#file.write(encryptor.Encrypt(DB.GetRawDBData()))
#file.close()

file = open('testDB.txt','r')

DB = SimpleDB(encryptor.Decrypt(file.readline()))
print(DB.isGood)

for x in DB.entries:
    print('-----------------------')
    print(x.GetParmValue('name'))
    print(x.GetParmValue('login'))
    print(x.GetParmValue('password'))
    print(x.GetParmValue('url'))

file.close()