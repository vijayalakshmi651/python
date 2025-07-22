
import re

class regex:
	def __init__(self,text):
	    self.text = text

	def search(self):
	    pattern = re.search(r"hello",self.text)
	    print(pattern.group())

	def findall(self):
	    pattern1 = re.findall(r"[a-zA-Z]{3}",self.text)
	    pattern2 = re.findall(r"[A-Z]+",self.text)
	    pattern3 = re.findall(r"\d+",self.text)
	    print(pattern1,pattern2,pattern3)

class regex1(regex):
    def compile_(self):
	    pattern = re.compile(r"\d+")
	    print(pattern.findall(self.text))
  
    def match(self):
        pattern = re.match(r"python",self.text)
        print(pattern.group())
    
    def start_end(self):
        pattern1  = re.findall(r"\Apython",self.text)
        pattern2 = re.findall(r"python\Z",self.text)
        print(pattern1,pattern2)
  
    def boundary_nonboundary(self):
        pattern1 = re.findall(r"\bis\b",self.text)
        pattern2 = re.findall(r"\Bis\B",self.text)
        pattern3 = re.findall(r"\Bis",self.text)
        pattern4 = re.findall(r"is\B",self.text)
        pattern5 = re.findall(r"\bis",self.text)
        print(pattern1,pattern2,pattern3,pattern4,pattern5)

    def w_and_W(self):
        pattern1 = re.findall(r"\w+",self.text)
        pattern2 = re.findall(r"\W+",self.text)
        print(pattern1,pattern2)
     
    def whitespace_nonwhitespace(self):
        pattern1 = re.findall(r"\s",self.text)
        pattern2 = re.findall(r"\S+",self.text)
        print(pattern1,pattern2)


    def sub(self,text1):
        pattern1 = re.sub(r"victoria","vijju",self.text)
        pattern2 = re.sub(r"\d+","#",text1)
        print(pattern1)
        print(pattern2)
    def 

obj1=regex1("helloo vijaya lakshmi")
obj1.search()
obj2=regex1("Hii Vijaya Lakshmii651")
obj2.findall()
obj3=regex1("heyy python 123_helloo")
obj3.compile_()
obj4=regex1("python language")
obj4.match()
obj5=regex1("python Vijaya Lakshmii651")
obj5.start_end()
obj6 = regex1(" is mynameis miss ")
obj6.boundary_nonboundary()
obj7 = regex1("python\t Vijaya\n  Lakshmii651_!!@")
obj7.w_and_W()
obj7.whitespace_nonwhitespace()
obj8 = regex1("victoria is a good girl")
obj8.sub(text1 = "victoria is a good 123 girl")


