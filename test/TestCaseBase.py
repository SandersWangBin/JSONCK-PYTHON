#!/usr/bin/env python

import re
import sys
sys.path.append('../src/')
from JsonCK import JsonCK

class TestCaseJsonCK:
    TC_DETAIL_INDENT = "    "
    TC_NEWLINE = "\n"
    TC_HEADER = "> TESTCASE: %s" + TC_NEWLINE
    TC_SUM = "==== TEST SUITE (%s) RESULT: SUCCESS (%d/%d => %s%%), FAIL (%d/%d)" + TC_NEWLINE

    def __init__(self, name):
        self.tsName = name
        self.tcList = list()

    def genResult(self, tcName, description, status):
        return self.TC_HEADER % (tcName) + description + \
               self.TC_DETAIL_INDENT + "====> TEST CASE RESULT: " + str(status) + self.TC_NEWLINE + self.TC_NEWLINE

    def genDescription(self, texts):
        result = ''
        for text in texts: result += self.TC_DETAIL_INDENT + text + self.TC_NEWLINE
        return result

    def addTcResult(self, tcName, jsonExp, text, expect, result):
        self.tcList.append((self.genResult(tcName, \
                            self.genDescription(["JSONCK REGEXP EXPRESSION: " + jsonExp, \
                                                 "CHECKED TEXT            : " + text, \
                                                 "JSONCK EXECUTE RESULT   : " + str(result)]), \
                            (result==expect)), 
                            (result==expect)))

    def addTcExcption(self, tcName, e):
        self.tcList.append((self.genResult(tcName, str(e), False), False))

    def checkUseJSONCK(self, tcName, jsonExp, text, expect):
        try:
            j = JsonCK(jsonExp)
            r = j.check(text)
            self.addTcResult(tcName, jsonExp, text, expect, r)
        except Exception as e:
            self.addTcExcption(tcName, str(e))

    def __str__(self):
        result = ''
        total = len(self.tcList)
        success = 0
        fail = 0
        for tc in self.tcList:
            result += tc[0]
            if tc[1]: success += 1
            else: fail += 1
        return self.TC_SUM % (self.tsName, success, total, success*1.0/total*100, fail, total) + \
               result