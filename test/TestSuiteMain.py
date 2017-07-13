#!/usr/bin/env python

from TestCaseBase import TestCaseJsonCK

tcJsonCK = TestCaseJsonCK("TestCaseJSONCKExp")
TC_00_NAME = "JSONCK EXPRESSION TEST 00";
JSONCK_EXP_00 = '"method"=="Created"'
JSON_EXAMPLE_00_TRUE = '{"id": "HTTP", "method": "Created", "error": false}'
tcJsonCK.checkUseJSONCK(TC_00_NAME, JSONCK_EXP_00, JSON_EXAMPLE_00_TRUE, True)

TC_01_NAME = "JSONCK EXPRESSION TEST 01";
JSONCK_EXP_01 = '"method"=="Created" || "id"=="HTTP" || "result"==true'
JSON_EXAMPLE_011_TRUE = '{"method": "Created"}'
JSON_EXAMPLE_012_TRUE = '{"result": true}'
JSON_EXAMPLE_013_FALSE = '{"successful": true}'
tcJsonCK.checkUseJSONCK(TC_01_NAME, JSONCK_EXP_01, JSON_EXAMPLE_011_TRUE, True)
tcJsonCK.checkUseJSONCK(TC_01_NAME, JSONCK_EXP_01, JSON_EXAMPLE_012_TRUE, True)
tcJsonCK.checkUseJSONCK(TC_01_NAME, JSONCK_EXP_01, JSON_EXAMPLE_013_FALSE, False)

TC_02_NAME = "JSONCK EXPRESSION TEST 02";
JSONCK_EXP_02 = '"method"=="Created" && "id"=="HTTP" || "result"==true'
JSON_EXAMPLE_02_TRUE = '{"id": "HTTP", "method": "Created", "error": false}'
JSON_EXAMPLE_02_FALSE = '{"id": "HTTP", "method": "Updated", "error": true}'
tcJsonCK.checkUseJSONCK(TC_02_NAME, JSONCK_EXP_02, JSON_EXAMPLE_02_TRUE, True)
tcJsonCK.checkUseJSONCK(TC_02_NAME, JSONCK_EXP_02, JSON_EXAMPLE_02_FALSE, False)

TC_03_NAME = "JSONCK EXPRESSION TEST 03";
JSONCK_EXP_03 = '"error"==[true, false] && "ID"==[10, 15] && "NAME"==["OBJ010", "OBJ015"]'
JSON_EXAMPLE_03_TRUE = '[{"ID": 10, "NAME": "OBJ010", "error": true}, {"ID": 15, "NAME": "OBJ015", "error": false}]'
tcJsonCK.checkUseJSONCK(TC_03_NAME, JSONCK_EXP_03, JSON_EXAMPLE_03_TRUE, True)

TC_04_NAME = "JSONCK EXPRESSION TEST 04";
JSONCK_EXP_04 = '"status"==201 && "id"==["HTTP","HTTP.response.error.rate","web_report"] && "endpoint"==["groups","metrics","reports"] && "successful"==true'
JSON_EXAMPLE_04_TRUE = '{"items": [{"operation": {"status": 201, "successful": true, "endpoint": "groups", "type": "create", "id": "HTTP"}}, {"operation": {"status": 201, "successful": true, "endpoint": "metrics", "type": "create", "id": "HTTP.response.error.rate"}}, {"operation": {"status": 201, "successful": true, "endpoint": "reports", "type": "create", "id": "web_report"}}], "errors": false}'
JSON_EXAMPLE_04_FALSE = '{"items": [{"operation": {"status": 201, "successful": true, "endpoint": "groups", "type": "create", "id": "HTTP"}}, {"operation": {"status": 404, "successful": true, "endpoint": "metrics", "type": "create", "id": "HTTP.response.error.rate"}}, {"operation": {"status": 500, "successful": true, "endpoint": "reports", "type": "create", "id": "web_report"}}], "errors": false}'
tcJsonCK.checkUseJSONCK(TC_04_NAME, JSONCK_EXP_04, JSON_EXAMPLE_04_TRUE, True)
tcJsonCK.checkUseJSONCK(TC_04_NAME, JSONCK_EXP_04, JSON_EXAMPLE_04_FALSE, False)

print tcJsonCK

