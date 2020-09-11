
# ᅤ - separate entries
# ᅥ - separate parms in entry
# ᅧ - separate value name and value

class SimpleDB: 

    isGood = False
    
    def __init__(self,DB_Data):

        self.entries = []      
        try:
            entriesRaw = DB_Data.split('ᅤ')

            for x in entriesRaw:

                self.AddEntry(x)
                
            self.isGood = True

        except: return

    def AddEntry(self,entryString):
       
        tempEntry = Entry(entryString)

        if(tempEntry.isGood): self.entries.append(tempEntry)

        return tempEntry.isGood
   
    def RemoveEntry(self,Index):

        del(self.entries[Index])
    
    def GetRawDBData(self):
        output=''

        for x in range(len(self.entries)):

            for i in range(len(self.entries[x].parms)):

                output += self.entries[x].parms[i].Name + 'ᅧ' + self.entries[x].parms[i].Value
                
                if i+1 != len(self.entries[x].parms): output += 'ᅥ'

            if x+1 != len(self.entries):output += 'ᅤ'

        return output

    
class Entry:

    isGood = False
    

    def __init__(self,entryString): #create db entry 

        self.parms = []
        try:
            parameters = entryString.split('ᅥ')

            for x in parameters:
                tm = x.split('ᅧ')

                self.parms.append(Parameter(tm[0],tm[1]))
            
            self.isGood = True
            
        except: return 

    def _GetParm(self,Name):

        for x in self.parms:
            if(x.Name == Name): return x
        return None

    def GetParmValue(self,Name):

        parm = self._GetParm(Name)

        if parm != None: return parm.Value
        else: return None
        
    def SetParmValue(self,Name,Value): #if parm with given name dont exist will create new parm
        parm = self._GetParm(Name)

        if parm != None: parm.Value = Value
        else: self.parms.append(Parameter(Name,Value))
   

class Parameter:
    
    def __init__(self,Name,Value):

        self.Name = Name
        self.Value = Value