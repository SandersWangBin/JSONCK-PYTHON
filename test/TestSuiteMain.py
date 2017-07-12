#!/usr/bin/env python

from TestCaseBase import TestCaseJsonCK

tcJsonCK = TestCaseJsonCK("TestCaseJSONCKExp")
TC_01_NAME = "PULL REGEXP EXPRESSION TEST 01";
JSONCK_EXP_01 = '"method"=="Created" || "id"=="HTTP" || "result"==true'
JSON_EXAMPLE_011_TRUE = '{"method": "Created"}'
JSON_EXAMPLE_012_TRUE = '{"result": true}'
JSON_EXAMPLE_013_FALSE = '{"successful": true}'
tcJsonCK.checkUseJSONCK(TC_01_NAME, JSONCK_EXP_01, JSON_EXAMPLE_011_TRUE, True)
tcJsonCK.checkUseJSONCK(TC_01_NAME, JSONCK_EXP_01, JSON_EXAMPLE_012_TRUE, True)
tcJsonCK.checkUseJSONCK(TC_01_NAME, JSONCK_EXP_01, JSON_EXAMPLE_013_FALSE, False)

print tcJsonCK

