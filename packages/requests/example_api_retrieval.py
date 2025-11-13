# This example is used to examine the JSON response of a 3rd-party API

import requests
import sys
import json

limit_count = 2

# Minimum data checking used.  Just need a string passed on the python command line.
if len(sys.argv) != 2:
    sys.exit("USAGE ERROR: Wrong number of arguments.")

# This URL was supplied in an online class.
# It's a good example, easy to use, and returns JSON for further experimentation.
url = f"https://itunes.apple.com/search?entity=song&limit={limit_count}&term={sys.argv[1]}"

response = requests.get( url )
response_json = response.json()

#Prettify the response for human inspection...
print(json.dumps(response_json, indent=2))

# Extract something interesting from each dictionary...
for result in response_json["results"]:
    print(result["trackName"])
 