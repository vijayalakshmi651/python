import os

class os_py:

    def mk_dir(self):
        os.mkdir("vicky1")
        return "vicky1"

    def mk_dirs(self):
        os.makedirs("child1/parent/grandfather")
        return "child1/parent/grandfather"
    def rmdir(self):
        os.mkdir("vijaya")
        os.rmdir("vijaya")
        return "vijaya"
    def remove(self):
        file=open("file.txt","w")
        file.write("this is a new file")
        file.close()
        os.remove("file.txt")
        return "file.txt"
    def rename(self):
        file=open("text.txt","w")
        file.write("file created")
        file.close()
        os.rename("text.txt","newtext.txt")
        return "newtext.txt"

    def listdir(self):
        contents=os.listdir()
        return "contents"
        
    def getcwd(self):
        new_directory=os.getcwd()
        return "new_directory"

    def chdir(self):
        #os.mkdir("sam")
        os.chdir("vicky1")
        result = os.getcwd()
        print(result)
    
    def pathjoin(self):
        os.mkdir("new_directory")
        text=os.path.join("new_directory","newtext.txt")
        print(text)
    def pathexists(self):
        if os.path.exists("/media/besquare/besquare/vijayalakshmi/os_python"):
            print("file exist")
        else:
            print("not exist")
    
    def isfile(self):
        print(os.path.isfile("/media/besquare/besquare/vijayalakshmi/os_python/newtext.txt"))
    def isdirectory(self):
        print(os.path.isdir("/media/besquare/besquare/vijayalakshmi/os_python"))



'''obj = os_cmd()
obj.mk_dir()
obj.mk_dirs()
obj.rmdir()
obj.remove()
obj.rename()
obj.listdir()
obj.getcwd()
obj.chdir()
obj.pathjoin()
obj.pathexists()
obj.isfile()
obj.isdirectory()'''
