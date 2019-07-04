

# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
# cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
# plain_text = cipher_suite.decrypt(cipher_text)




class ionor():

    from os import path
    from cryptography.fernet import Fernet
    import getpass, os,json
    prime_key = 'wzaU_Rwyt2hXmXfGgdEIZu1aRSQYcpAAlUFMAhsQhOE='

    def __init__(self):
        #here we check for dirs and files
        if self.checkDir("C:\\users\\" + self.getpass.getuser() + "\\Documents\\ionor")["status"] == False:
            self.os.mkdir("C:\\users\\" + self.getpass.getuser() + "\\Documents\\ionor")
            init_Dict = {self.encryptr(msg="records", key=self.prime_key)["msg"] :[],
                        self.encryptr(msg="key", key=self.prime_key)["msg"]: self.prime_key}
            tmp = open("C:\\users\\" + self.getpass. getuser() + "\\Documents\\ionor\\iodata.pyz","w")
            tmp.write(self.json.dumps(init_Dict))
            tmp.close()
        elif self.checkDir("C:\\users\\" + self.getpass.getuser() + "\\Documents\\ionor")["status"] == True:
            if self.checkFile("C:\\users\\" + self.getpass.getuser() + "\\Documents\\ionor\\iodata.pyz")["status"] == False:
                init_Dict = {self.encryptr(msg="records", key=self.prime_key)["msg"] :[],
                            self.encryptr(msg="key", key=self.prime_key)["msg"]: self.prime_key}
                tmp = open("C:\\users\\" + self.getpass. getuser() + "\\Documents\\ionor\\iodata.pyz","w")
                tmp.write(self.json.dumps(init_Dict))
                tmp.close()

    def checkDir(self,dir):
        #returns a dict with two keys [boolean]['status'] and [string]['msg']
        #[boolean]['status'] is either True or False with respect to if the directory exists
        #not to be used out of the class
        status, internal_msg = None, "function did not terminate"
        if self.path.isdir(dir): status, internal_msg = True, "{} exists".format(dir)
        elif not self.path.isdir(dir):status, internal_msg = False, "{} do not exists".format(dir)
        return {"status":status,"msg":internal_msg}

    def checkFile(self,dir):
        #returns a dict with two keys [boolean]['status'] and [string]['msg']
        #[boolean]['status'] is either True or False with respect to if the file exists
        #not to be used out of this class
        status, internal_msg = None, "function did not terminate"
        if self.path.exists(dir): status, internal_msg = True, "{} exists".format(dir)
        elif not self.path.exists(dir):status, internal_msg = False, "{} do not exists".format(dir)
        return {"status":status,"msg":internal_msg}

    def file(self,mode): return open("C:\\users\\" + self.getpass. getuser() + "\\Documents\\ionor\\iodata.json",mode)

    def addr(self,**kwargs):
        rkwargs, tmpdict,filer = {"platform","login","password"}, dict(), self.file("r") #required keywords
        iodata = self.json.loads(filer.read())
        filer.close()
        if rkwargs == set(kwargs.keys()):
            for kw in kwargs:
                tmpdict[self.encryptr(msg=kw,key=self.prime_key)["msg"]] = self.encryptr(msg=kwargs[kw], key=self.prime_key)["msg"]
            for kw in iodata:
                if self.decryptr(msg=kw, key=self.prime_key)["msg"] == "records":
                     filew = self.file("w")
                     iodata[kw].append(tmpdict)
                     filew.write(self.json.dumps(iodata))
                     filew.close()
                     print("done")

    def readr(self):#TAKAM ALEX CHRISTIAN and takam Bonlong glory
    # def readr (self)
        data,status,internal_msg = None, None, ""
        filedr = self.openDeepStore("r")
        deepCont = filedr.read()
        jsonCryptedCont = self.decryptr(key=self.prime_key, msg=deepCont)
        return {"data": data}
    def update(self):
        pass

    def delr(self):
        pass

    def encryptr(self,**kwargs): # takes string data as parameter and outputs string data
        rkwargs = {"key","msg"}
        if set(kwargs.keys()) == rkwargs:
            fernet = self.Fernet(bytes(kwargs["key"],'utf-8'))
            msg = fernet.encrypt(bytes(kwargs['msg'],'utf-8'))
            msg = msg.decode('utf-8')

        return {"msg": msg,"key": kwargs["key"]}

    def decryptr(self, **kwargs): #takes string data and ouputs string data
        rkwargs = {'key','msg'}
        if set(kwargs.keys()) == rkwargs:
            fernet = self.Fernet(bytes(kwargs["key"],"utf-8"))
            msg = fernet.decrypt(bytes(kwargs["msg"], "utf-8"))
            msg = msg.decode("utf-8")

        return {"msg": msg, "key": kwargs["key"]}
    def checkDeepStore(self):
        status, internal_msg, n = False, "", 0
        if self.checkDir("C:\\users\\" + self.getpass.getuser() + "\\Documents\\ionor\\deep")["status"] == False:
            internal_msg, n = str(n + 1) + "deep dir do not exist \n ", n + 1
            self.os.mkdir("C:\\users\\" + self.getpass.getuser() + "\\Documents\\ionor\\deep")
            internal_msg, n = internal_msg + str(n + 1) + "deep dir was created successfully \n ", n + 1
            open("C:\\users\\" + self.getpass. getuser() + "\\Documents\\ionor\\deep\\iodata.txt","w").close()
            internal_msg, n = internal_msg + str(n + 1) + "deep iodata do not exist and was created success fully \n", n + 1
            status = True
        elif self.checkDir("C:\\users\\" + self.getpass.getuser() + "\\Documents\\ionor\\deep")["status"] == True:
            internal_msg, n = str(n + 1) + "deep dir exist \n", n + 1
            if self.checkFile("C:\\users\\" + self.getpass.getuser() + "\\Documents\\ionor\\deep\\iodata.txt")["status"] == False:
                internal_msg, n = str(n + 1) + "deep iodata not exist \n", n + 1
                open("C:\\users\\" + self.getpass. getuser() + "\\Documents\\ionor\\deep\\iodata.txt","w").close()
                internal_msg, n = str(n + 1) + "deep iodata file was created \n", n + 1
                status = True
            else: status = False
        else: status, internal_msg = True, "deep iodata is okay"

        return {"status": status, "msg": internal_msg}
    def openDeepStore(self, mode):# return the opened deep file.
        #should only be called by other methods in this class
        #should not be called from out of this class, ionor
        if self.checkDeepStore()["status"] == True:
            file = open("C:\\users\\" + self.getpass. getuser() + "\\Documents\\ionor\\deep\\iodata.txt", mode)
        else:
            file =  open("C:\\users\\" + self.getpass. getuser() + "\\Documents\\ionor\\deep\\iodata.txt", mode)
        return file
    def upDateDeepStore(self): #takes the content in iodata.json and encrypts it and stores it in deep/iodata.txt
        #this method should be called, at the end of the program. each time
        filer,filed = self.file("r"), self.openDeepStore("w")
        status, internal_msg = None, ""
        jsoncont = filer.read()
        filed.write(self.encryptr(msg=jsoncont, key= self.prime_key)["msg"])
        filed.close()
        filew = self.file("w")
        init_Dict = {self.encryptr(msg="records", key=self.prime_key)["msg"] :[],
                    self.encryptr(msg="key", key=self.prime_key)["msg"]: self.prime_key}
        filew.write(self.json.dumps(init_Dict))
        return {"status": status,"msg":internal_msg}

    def jsonFromDeep(self): #decryptes the data in deep/iodata.txt, to obtain the json of crypted entries
        #this method should always be called, before working with the json file
        status, internal_msg = None, ""
        filedr,filew= self.openDeepStore("r"), self.file("w")
        deepCont = filedr.read()
        filew.write(self.decryptr(key=self.prime_key,msg=deepCont)["msg"])
        status, internal_msg= True, "Done"
        return{"status": status, "msg":internal_msg}
