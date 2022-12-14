import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json

print(f"###############################################################")
print("ISE 201 Lab Scenario 2 Exercise 3 - Using APIs to Join a PSN to the Active Directory Domain\n\n")

# Variables
baseurl = "https://admin:C1sco12345@198.19.10.27:9060/ers/config/activedirectory"
payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}
adID = ""

# Step 1
print(f"###############################################################")
print("STEP 1: Determine Join Point ID of ABC-AD")
url = f"{baseurl}/name/ABC-AD"
response = requests.request("GET", url, headers=headers, data=payload, verify=False)

if response.status_code == 200:                         # Make sure we got back a 200 OK
    adJP = json.loads(response.text)                    # Load the response text
    adJP = adJP["ERSActiveDirectory"]                   # Parse the results
    print(json.dumps(adJP, indent=4, sort_keys=True))
else:
    print(f"Something went wrong!! Status Code: {response.status_code}") # Basic Error Handling
    print(response.text)
    quit()


# Step 2
print(f"###############################################################")
print("STEP 2: Parse JSON Output for ID of ABC-AD\n\n")
#adID = "/80a11f80-bc3e-11ec-9aeb-f65c9bad6277"
adID = adJP['id']
print(f"We found ABC-AD id: {adID}\n")


# Step 3
print(f"###############################################################")
print("STEP 3: Join DEV-ISE22 to ABC-AD\n\n")

newurl = f"{baseurl}/{adID}/join"
joinPayload = {
    "OperationAdditionalData" : {
        "additionalData" : [ 
            {
                "name" : "username",
                "value" : "administrator"
            },
            {
                "name" : "password",
                "value" : "C1sco12345"
            },
            {
                "name" : "node",
                "value" : "dev-ise22.dcloud.local"
            }
        ]
    }
}

payload = json.dumps(joinPayload) #Serialize Content

response = requests.request("PUT", newurl, headers=headers, data=payload, verify=False)
print(response)
print(f"###############################################################")
