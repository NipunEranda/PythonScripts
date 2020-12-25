import getpass
import itertools
import os

class Idcreater:
    global banner, day, month, year, splitStatus, oldNic, newNic, count, choice
    warning = '''\nWarning! : You're guessing with new nic list. This may take a lot of time. You can split file into 10 files if you like. So you can run them individually. When files being splitted, files will be named as filename0, filename1, etc'''
    banner = """

|----------------------------Created BY-------------------------------|

8888888888P                  888       .d8888b.  8888888b.           
      d88P                   888      d88P  Y88b 888   Y88b          
     d88P                    888           .d88P 888    888          
    d88P   888  888 88888b.  88888b.      8888"  888   d88P 888  888 
   d88P    888  888 888 "88b 888 "88b      "Y8b. 8888888P"  `Y8bd8P' 
  d88P     888  888 888  888 888  888 888    888 888 T88b     X88K   
 d88P      Y88b 888 888 d88P 888  888 Y88b  d88P 888  T88b  .d8""8b. 
d8888888888 "Y88888 88888P"  888  888  "Y8888P"  888   T88b 888  888 
                888 888                                              
           Y8b d88P 888                                              
            "Y88P"  888                                              

--------------------------------------------------------------------
        """
        
    def __init__(self):
        print(banner)
        self.year = 0
        self.month = 0
        self.day = 0
        self.splitStatus = 0
        self.count = 0
        oldNic = list(map("".join, itertools.product('0123456789', repeat=4)))
        newNic = list(map("".join, itertools.product('0123456789', repeat=5)))

    def setYear(self, mYear):
        self.year = mYear

    def setMonth(self, mMonth):
        self.month = mMonth

    def setDay(self, mDay):
        self.day = mDay

    def getNewNIC(self):
        return str(self.year) + str(self.dayText)

    def enterFields(self):
        self.year = str(input("Birth Year >> "))
        self.month = int(input("Birth Month >> "))
        self.day = int(input("Birth Date >> "))

    def getOldNIC(self):
        return self.year[2] + self.year[3] + str(self.dayText)

    def getStatus(self):
        return splitStatus

    def getFileName():
        return fileName

    def initiate(self):
        if (self.month > 12 or self.day > 31 or self.month < 1 or self.day < 1):
            print("Month or Day incorrect.")
            exit()
        else:
            print("\nSelect Gender")
            print("1 - Female")
            print("2 - Male")
            gender = input("\nEnter the Number >> ")

            if(self.month == 1):
                self.dayText = "0"+str(self.day)
            if(self.month == 2):
                self.dayText = "0"+str(31 + self.day)
            if(self.month == 3):
                self.dayText = "0"+str(60 + self.day)
            if(self.month == 4):
                self.dayText = 91 + self.day
                if(dayText < 100):
                    self.dayText = "0"+str(self.dayText)
            if(self.month == 5):
                self.dayText = str(121 + self.day)
            if(self.month == 6):
                self.dayText = str(152 + self.day)
            if(self.month == 7):
                self.dayText = str(182 + self.day)
            if(self.month == 8):
                self.dayText = str(213 + self.day)
            if(self.month == 9):
                self.dayText = str(244 + self.day)
            if(self.month == 10):
                self.dayText = str(274 + self.day)
            if(self.month == 11):
                self.dayText = str(305 + self.day)
            if(self.month == 12):
                self.dayText = str(335 + self.day)

            if(gender == 1):
                self.dayText = int(self.dayText) + 500

        print("\n**Select Option**")
        print("1.Output Old NIC lists.")
        print("2.Output New NIC lists.")
        self.choice = input("\nOption number >> ")
        if(self.choice == 1):
			self.oldNic = list(map("".join, itertools.product('9876543210', repeat=4)))
			for x in self.oldNic:
				self.oldNic[self.count] = self.getOldNIC() + x + "v"
				self.count += 1
		
        if(self.choice == 2):
			self.newNic = list(map("".join, itertools.product('9876543210', repeat=5)))
			for x in self.newNic:
				self.newNic[self.count] = self.getNewNIC() + x
				self.count += 1
				
	def getOldNICSet(self):
		return self.oldNic
		
	def getNewNICSet(self):
		return self.newNic
