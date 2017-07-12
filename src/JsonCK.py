#!/usr/bin/env python

from JsonCKExp import JsonCKExp
from PULL.PullChain import PullChain

class JsonCK:
    SEPERATOR_OR = "||";
    SEPERATOR_AND = "&&"
    SYMBOL_NEWLINE = "\n"
    SYMBOL_OR = "||"
    SYMBOL_AND = "&&"

    FORMAT_JSONCK_EXP_NAME = "JSONCK_EXP_%s"
    JSONCK_EXP_ALL = "ALL"
    JSONCK_EXP_IND = 0

    def __init__(self, jsonCKExpLine):
        self.jsonCKExpList = list()
        self.genJsonCKExpList(jsonCKExpLine)
        self.pullExp = self.genPullExp()
        result = False

    def genJsonCKExpList(self, jsonCKExpLine):
        for subLine in jsonCKExpLine.split(self.SEPERATOR_AND):
            op = self.SYMBOL_AND
            for exp in subLine.split(self.SEPERATOR_OR):
                self.jsonCKExpList.append(JsonCKExp(\
                self.FORMAT_JSONCK_EXP_NAME % self.JSONCK_EXP_IND, \
                op, exp))
                op = self.SYMBOL_OR
                self.JSONCK_EXP_IND += 1
            op = self.SYMBOL_AND

    def genPullExpRef(self):
        return self.FORMAT_JSONCK_EXP_NAME % (self.JSONCK_EXP_ALL)

    def genPullExp(self):
        result = "m\'"
        for jExp in self.jsonCKExpList: result += str(jExp.getPullExp()) + self.SYMBOL_NEWLINE
        result += self.genPullExpRef() + ": "
        for jExp in self.jsonCKExpList: result += jExp.getName() + ' + '
        if result.endswith(' + '): result = result[:-3]
        result += "\'.PULL(" + self.genPullExpRef() + ")"
        return result

    def calculateBoolean(self, first, op, second):
        if op == self.SYMBOL_AND: return first and second
        elif op == self.SYMBOL_OR: return first or second
        else: return False

    def getOpFromExpList(self, expName):
        for exp in self.jsonCKExpList:
            if exp.getName() == expName:
                return exp.getOperator()
        return None

    def check(self, text):
        localResult = True
        pChain = PullChain(self.pullExp)
        pChain.check(text)
        for obj in pChain.getPullChainCurrent().getChildren():
            localResult = self.calculateBoolean(localResult, \
            self.getOpFromExpList(obj.getName()), obj.getResult())
        self.result = localResult
        return self.result

    def __str__(self):
        result  = "==== JSONCK INFO ====\n"
        result += self.pullExp + "\n"
        return result