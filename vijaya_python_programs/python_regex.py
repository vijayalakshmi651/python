 

import re
class Regex:
    def __init__(self,text):
        self.text = text
    def substring(self):
        result  = re.findall(r"exercises",self.text)
        print("found:",result)
        print("occurences:",len(result))
        
    def position(self):
        for match in re.finditer("exercises", self.text):
            result1 = match.start()
            result2 = match.end()
            print("Starting index:", result1)
            print("Ending index:", result2)
    def replace(self):
        result1 = re.sub(" ","_",self.text)
        result2 = re.sub("_"," ",self.text)
        print(result1)
        print(result2)
    def extracting_date(self):
        pattern = re.findall(r"\d+",self.text)
        print(pattern)
    def converting_date(self):
        pattern = re.sub("2004-05-20","20-05-2004",self.text)
        print(pattern)
    def starting_with_p(self):
        pattern = re.findall(r"p\w+",self.text)
        print(pattern)
    def extract_numbers(self):
        pattern = re.findall(r"(\d+)",self.text)
        print(pattern)

    def words_startsae(self):
        pattern = re.findall(r"a\w+,e\w+",self.text)
        print(pattern)

    def numbers_positions(self):
        #pattern = re.search(r"\d+",self.text)
        #print(pattern.start())
        for m in re.finditer("(\d+)",self.text):
            print(m.group(1))
            print("starting index:",m.start())
            print("ending index:",m.end())
       
    def checkfor_lower_upper_digits(self):
        pattern = re.findall(r"[a-zA-Z0-9]+",self.text)
        return bool (pattern)    
    
    def checking_for_aandb(self):
        pattern = r"^ab*$"
        words =self.text.split()
        for word in words:
            if re.fullmatch(pattern,word):
                print(f"'{word}'matched")
            else:
                print(f"'{word}'not matched")
    
    def checking_for_aandb1(self):
        pattern = r"^ab+$"
        words = self.text.split()
        for word in words:
            if re.fullmatch(pattern,word):
                print(f"'{word}'matched")
            else:
                print(f"'{word}'not matched")
   
    def checking_for_aandb2(self):
        pattern = r"ab?"
        #words = self.text.split()
        #print(words)
        #for word in words:
            #if re.findall(pattern,ord):
                #print(word)
        result = re.findall(pattern,self.text)
        print(result)
    
    def checking_for_aandb3(self):
        pattern = re.findall(r"ab{3}",self.text)
        print(pattern)
    def checking_for_aandb4(self):
        pattern = re.findall(r"ab{2,3}",self.text)
        print(pattern)
    
    def uppercase_underscore(self):
        pattern = re.findall(r"[a-z]+_",self.text)
        print(pattern)

    def uppercase_lowercase(self):
        pattern = re.findall(r"[A-Z][a-z]*",self.text)
        print(pattern)

    def startwith_a_endswith_b(self):
        pattern = re.findall(r"a.*b",self.text)
        print(pattern)

    def match_startingword(self):
        pattern = re.match(r"vijaya",self.text)
        print(pattern.group())
    
    def match_endingword(self):
        pattern = re.findall(r"girl$",self.text)
        print(pattern)
    def word_containing_z(self):
        pattern = re.findall(r"\w*z\w*",self.text)
        print(pattern)
    def word_containing_z_inmiddle(self):
        pattern = re.findall(r"\w+z\w+",self.text)
        print(pattern)
    def startswith_digits(self):
        pattern = re.findall(r"^6\d+\w+",self.text)
        print(pattern)

    def remove_zeros(self):
        pattern = re.sub(r"0","",self.text)
        print(pattern)
    def extracting_numbers(self):
        pattern = re.findall(r"\d{2,3}",self.text)
        print(pattern)


obj1 = Regex("Python exercises, PHP exercises, C# exercises")
obj1.substring()
obj2 = Regex("Python exercises, PHP exercises, C# exercises")
obj2.position()
obj3 = Regex("Python exercises, PHP exercises, C_ exercises")
obj3.replace()
obj4 = Regex("https:/i/www.w3resource.com/python-exercises/re/20-05-2004")
obj4.extracting_date()
obj5 = Regex("20-05-2004")
obj5.converting_date()
obj6 = Regex(" python java pilot")
obj6.starting_with_p()
obj7 = Regex("12345vijaya lakshmi 651")
obj7.extract_numbers()
obj8 = Regex("my name is anana,end with banana,amma,anna,emma")
obj8.words_startsae()
obj9 = Regex("12345vijaya.lakshmi 651")
obj9.numbers_positions()
obj10 =Regex("Vijayalakshmi651 9876689")
print(obj10.checkfor_lower_upper_digits())
obj11 = Regex("abbbbb a ab aab")
obj11.checking_for_aandb()
obj12 = Regex("abbbbb ab abb  a ab abbb")
obj12.checking_for_aandb1()
obj13 = Regex(" ba vd ab abb abbb ab a b")
obj13.checking_for_aandb2()
obj14 = Regex("a abbb ab")
obj14.checking_for_aandb3()
obj15 = Regex("a abbb abb")
obj15.checking_for_aandb4()
obj16 = Regex("vijaya_ vijaya _vijju  vijju_")
obj16.uppercase_underscore()
obj17 = Regex("Vijaya Vijaya vijju Sai")
obj17.uppercase_lowercase()
obj18 = Regex("abub ammulb  abbob abb sai vijaya ammulu hannuu")
obj18.startwith_a_endswith_b()
obj19 = Regex("vijaya is a good girl")
obj19.match_startingword()
obj20 = Regex("vijaya is a good girl")
obj20.match_endingword()
obj21 = Regex("zebraa zing amazing  amaz amazon vijaya")
obj21.word_containing_z()
obj22 = Regex("banan azanana amazing amazon zing")
obj22.word_containing_z_inmiddle()
obj23 = Regex("651vijaya 532lakshmi vijaya 651")
obj23.startswith_digits()
obj24 = Regex("25.0 34.09 0.34 10000 405")
obj24.remove_zeros()
obj25 = Regex("Exercises number 1, 12, 13, and 345 are important")
obj25.extracting_numbers()
