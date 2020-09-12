from hashlib import sha512,pbkdf2_hmac

class SimpleEncryptor: #My own simple encryption algoritm
    Key = ''
    rKey = '' # reversed key
    KeySum = 0
    separator = '-'

    def __init__(self,Key):

        salt = sha512(bytes(Key,"UTF-8")).digest()  
                    
        self.Key = pbkdf2_hmac('sha512',bytes(Key,'UTF-8'),salt,100000).hex() # it work without this but i dont want to store plain text in memory
        self.rKey = pbkdf2_hmac('sha512',bytes(Key[::-1],'UTF-8'),salt,100000).hex()

        #self.Key = Key                 #Alternative without hashing
        #self.rKey = self.Key[::-1] 

        for x in range(len(Key)): 
            ke = ord(self.Key[x])
            rk = ord(self.rKey[x])
            self.KeySum += (ke*rk) - (ke+rk)

    def Encrypt(self,text): #Return False if failed
        output = ""

        k=0 #key iterator
        try:

            for i in range(len(text)):

                tx = ord(text[i])
                ke = ord(self.Key[k])
                rk = ord(self.rKey[k])

                output += hex( (tx + len(text) + ke) + self.KeySum - (ke*rk) )

                if i+1 != len(text): output += self.separator
                if k+1 == len(self.Key): k=0
                else: k += 1

            return output

        except: return False

    def Decrypt(self,encryptedText): #Return False if failed
        output = ""

        k=0 #key iterator
        try:

            splitedText = encryptedText.split(self.separator)

            for i in range(len(splitedText)):

                enc = int(splitedText[i],base=16)
                ke = ord(self.Key[k])
                rk = ord(self.rKey[k])

                output += chr( int( (enc + (ke * rk)) - self.KeySum - len(splitedText) - ke) )

                if k+1 == len(self.Key): k=0
                else: k += 1

            return output

        except: return False