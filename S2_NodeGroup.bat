echo ISE 201 Lab Scenario 2 Exercise 2 - Creating a Node Group via API
echo.
@echo off

:: Use variables to shorten code reuse
set baseurl="https://admin:C1sco12345@ise-pan.dcloud.local:443/api/v1/"

echo ###############################################################
echo STEP 1: Adding Node Group: ABC_LONDON_DC
echo.
curl -k -X POST "%baseurl%deployment/node-group" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"ABC_LONDON_DC\",\"description\":\"Node Group for ABCs ISE PSNs in the London Data Center\"}"
echo.
echo ###############################################################

echo STEP 2: Verifying Node Group is on ISE: ABC_LONDON_DC
echo.
curl -k -X GET "%baseurl%deployment/node-group/ABC_LONDON_DC" -H "accept: application/json"
echo.
echo ###############################################################

echo STEP 3: Adding ISE-PSN to Node Group: ABC_LONDON_DC
echo.
curl -k -X POST "%baseurl%deployment/node-group/ABC_LONDON_DC/add-node" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"hostname\":\"ise-psn\"}"
echo.
echo ###############################################################

echo STEP 4: Adding DEV-ISE22 to Node Group: ABC_LONDON_DC
echo.
curl -k -X POST "%baseurl%deployment/node-group/ABC_LONDON_DC/add-node" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"hostname\":\"dev-ise22\"}"
echo.
echo ###############################################################