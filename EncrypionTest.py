from SimplePasswordManagerCore.SimpleEncryption import SimpleEncryptor

pass1 = 'Test1'
pass2 = 'Test2'

encryptor1 = SimpleEncryptor(pass1)
encryptor2 = SimpleEncryptor(pass2)

text = "Testowy tekst"

encText1 = encryptor1.Encrypt(text)
encText2 = encryptor2.Encrypt(text)

print("Text to encrypt:",text)
print("Encryptor1 pass:",pass1,"Encrypted: ",encText1)
print("Encryptor2 pass:",pass2,"Encrypted:",encText2)

print("Encryptor1 with Encryptor1 input:",encryptor1.Decrypt(encText1))
print("Encryptor2 with Encryptor2 input:",encryptor2.Decrypt(encText2))

print("Encryptor1 with Encryptor2 input:",encryptor1.Decrypt(encText2))
print("Encryptor2 with Encryptor1 input:",encryptor2.Decrypt(encText1))