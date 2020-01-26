class SuffixTree:
    def __init__(self,string):
        #Initializing
        global new
        new=string
        self.addSuffix(string)
        

    def addSuffix(self,string):
        
        if string != new:
            string = new+string
        #Adding Terminating Character '$' to the end of string.
        string+= '$'
        global visual
        visual= string
        self.rootnode={}
        for i in range(len(string)): 
            suff=self.rootnode
            for j in string[i:]:
                if j not in suff:
                    suff[j]={}
                suff=suff[j]

    def followPath(self,text):
        
        suff= self.rootnode
        #Check if it follows path or not
        for i in text:
            if i not in suff:
                return None
            suff=suff[i]
        return suff
    
    def Substring(self,text):
        #Check if it follows the path in string
        if self.followPath(text) == None:
            return False
        else:
            return True

    def CheckSuffix(self,text):
        #Check for given parameter if it is suffix or not
        x=self.followPath(text)
        if x != None and '$' in x:
            return True
        else:
            return False

    def IsPalindrome(self,string):
        
        #For Palindrome string must have length greater or equal to 2
        if len(string)>= 2:
            #reversing the string
            p=string[::-1]
            #return True if string and reverse string are equal
            return string.lower() == p.lower()
        else:
            return 'Plaindrome not possible'
        
    def CheckSuffixPalindrome(self):
        
        success=0
        lst=[]
        for i in range(len(visual)):
            #Stores all possible suffixes in a list
            if visual[i:len(visual)-1] != '':
                lst.append(visual[i:len(visual)-1])
        #Check each Suffix if it is Palindrome or not
        for j in lst:
            if self.IsPalindrome(j) == True:
                print('Suffix','"'+j+'"','is a Palindrome')
                success=1
        if success != 1:
            print('No suffix is a Palindrome')
        return ''
    def LongestPalindrome(self):
    
        success=0
        lst=[]
        max=0
        for i in range(len(visual)):
            #Stores all possible suffixes in a list
            if visual[i:len(visual)-1] != '':
                lst.append(visual[i:len(visual)-1])
        #Check each Suffix if it is Palindrome or not
        for j in lst:
            if self.IsPalindrome(j) == True:
                if len(j)>max:
                    max=len(j)
                    print('Suffix','"'+j+'"','is the Longest Palindrome')
                    success=1
        if success != 1:
            print('No suffix is a Palindrome')
        return ''
    
    def Print(self):
        
        print('All Possible Suffixes of string with terminating character are: ')
        for i in range(len(visual)):
            print('->',visual[i:])

    


c=SuffixTree('aaaaa')
print(c.Substring('ba'))
print(c.CheckSuffix('baab'))
c.addSuffix('aa')
c.Print()
print(c.Substring('aaRus'))
print(c.CheckSuffix('aaRushan'))
print(c.CheckSuffixPalindrome())
print(c.IsPalindrome('Maam'))
print(c.LongestPalindrome())
