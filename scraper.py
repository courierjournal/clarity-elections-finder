import sys
import requests
import time

# Buffer time between requests (in seconds) so we're not flooding their server
wait_between_requests = 0.25

# Give up if not found within this many iterations
max_attempts = 4000


# Find the last election id Clarity has on file for the state
def get_recent_election(state):
    url = f"https://results.enr.clarityelections.com/{state}/elections.json"
    response = requests.get(url)
    if response.status_code == 404:
        return {
            "id": None,
            "msg": f"Could not locate manifest for {state}. Are you sure Clarity covers it?",
        }
    else:
        data = response.json()
        return {
            "id": int(data[0]["EID"]),
            "msg": f"Last election Clarity has for {state}:\n  •Date: {data[0]['Date']}\n  •Name: {data[0]['ElectionName']}\n  •URL: https://results.enr.clarityelections.com/KY/{data[0]['EID']}",
        }


# Make sure user specifies the state at run time
if len(sys.argv) == 1:
    print(
        "Must specify the state abbreviation as first argument. Ex: python scraper.py KY"
    )
    exit()

# Find out when the last election id was
state = sys.argv[1].upper()
results = get_recent_election(state)
print(results["msg"])

# If there was no election manifest found, exit
if results["id"] == None:
    exit()

# If there was an election manifest, make sure the user wants to proceed
proceed = input("Do you want to proceed with finding the next one? (y/n) ")
if proceed.lower() != "y":
    exit()

# Override the starting ID if passed in by the user
last_good_index = results["id"]
if len(sys.argv) == 3:
    last_good_index = int(sys.argv[2])

url = f"https://results.enr.clarityelections.com/{state}/"
iterator = 1
foundOne = False

while foundOne == False:
    test_id = last_good_index + iterator
    response = requests.get(url + str(test_id))
    print(f"{iterator}: trying {test_id} - response {response.status_code}", end="\r")
    if response.status_code != 404:
        foundOne = True
    else:
        iterator = iterator + 1
        time.sleep(0.25)


print("")
if foundOne == True:
    print(
        f"Found a possible match after {iterator} attempts\nhttps://results.enr.clarityelections.com/{state}/{last_good_index + iterator}"
    )
else:
    print(
        f"Could not find a match after {max_attempts} attempts\nLast id tried: {last_good_index + iterator}\nYou can try again starting at that id by supplying a second argument. Ex: python scraper.py {state} {last_good_index + iterator}"
    )

