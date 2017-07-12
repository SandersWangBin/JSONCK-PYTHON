#!/usr/bin/env python

import re

class JsonCKExp:
    REG_JSONCK_EXPRESS = r"""\s*(".*")\s*([!<=>]+)\s*(.*)\s*"""
    REG_JSONCK_VAR_TYPE_INTEGER = r"^\d+$|\[\s*\d+(\s*,\s*\d+)*\]"

    FORMAT_PULL_EXP_STRING  = """%s: r'%s\s*:\s*"([a-zA-Z0-9\\._-]+)"\s*'.PULL({0}%s)"""
    FORMAT_PULL_EXP_INTEGER = """%s: r'%s\s*:\s*([0-9]+)\s*'.PULL({0}%s)"""
    FORMAT_PULL_EXP_BOOLEAN = """%s: r'%s\s*:\s*([a-zA-Z]+)\s*'.PULL({0}%s)"""

    TYPE_STRING = "STRING"
    TYPE_INTEGER = "INTEGER"
    TYPE_BOOLEAN = "BOOLEAN"
    BOOLEAN_TRUE = "true"
    BOOLEAN_FALSE = "false"

    def __init__(self, name, operator, expression):
        self.name = name.strip()
        self.operator = operator.strip()
        self.expression = expression.strip()
        self.expVar = ""
        self.expOp = ""
        self.expValue = ""
        self.expType = ""
        self.parserJsonCKExp(self.expression)
        self.pullExp = self.genPullExp()

    def getType(self, value):
        if re.search(self.REG_JSONCK_VAR_TYPE_INTEGER, value): return self.TYPE_INTEGER
        elif value == self.BOOLEAN_TRUE or value == self.BOOLEAN_FALSE: return self.TYPE_BOOLEAN
        else: return self.TYPE_STRING

    def parserJsonCKExp(self, expression):
        m = re.search(self.REG_JSONCK_EXPRESS, expression)
        if m:
            self.expVar = m.group(1).strip()
            self.expOp = m.group(2).strip()
            self.expValue = m.group(3).strip()
            self.expType = self.getType(self.expValue)

    def genPullExp(self):
        if self.expType == self.TYPE_STRING: return self.FORMAT_PULL_EXP_STRING % (self.name, self.expVar, self.expOp+self.expValue)
        elif self.expType == self.TYPE_INTEGER: return self.FORMAT_PULL_EXP_INTEGER % (self.name, self.expVar, self.expOp+self.expValue)
        elif self.expType == self.TYPE_BOOLEAN: return self.FORMAT_PULL_EXP_BOOLEAN % (self.name, self.expVar, self.expOp+self.expValue)
        else: return ""

    def getPullExp(self): return self.pullExp
    def getName(self): return self.name
    def getOperator(self): return self.operator

    def __str__(self):
        result  = "==== JSONCK EXPRESSION INFO ====\n"
        result += "name     : " + self.name + "\n"
        result += "operator : " + self.operator + "\n"
        result += "PULL exp : " + self.pullExp + "\n"
        return result