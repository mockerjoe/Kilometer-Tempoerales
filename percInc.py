import json
import datetime

# import json
file = open("data.json")

# returns JSON object as a dictionary
data = json.load(file)

# Parse the JSON data
parsed_data = json.loads(json.dumps(data))

# Initialize an empty list to store pace values
pace_values = []

def timeSeconds(time):
    # calculate time to seconds
    input_time = datetime.datetime.strptime(time, "%H:%M:%S")
    seconds = (input_time.minute * 60) + input_time.second
    return seconds

def pacePercentage(pace):
    valueCount = len(pace)
    oldest = pace[0]
    newest = pace[valueCount-1]

    oldestSeconds = timeSeconds(oldest)
    newestSeconds = timeSeconds(newest)

    # Formula for decreased time
    decreasedTime = ((newestSeconds - oldestSeconds)/oldestSeconds)*100

    print("Oldest: ", oldest, " in seconds: ", oldestSeconds,
          "\nNewest: " , newest, " in seconds: ", newestSeconds)
    print("Improved time by ", round(decreasedTime*-1, 2),"%")

def infoMonth(month):
    # Iterate over each run
    for run_info in parsed_data["Run_Information"]:
        distance = run_info["distance"]
        date = run_info["date"]
        pace = run_info["pace"]

        # Format date values from json
        dateStripped = datetime.datetime.strptime(date, "%Y-%m-%d")

        # check for month in date and input
        if(dateStripped.month == int(month)):
            pace_values.append(pace)
            print("Date: ", date, " Distance: ", distance, " Pace: ", pace)

    print(pace_values)

    percentage = input("Do you wanna see your improvement in percentage? y/n \n")
    if(percentage == "y"):
        pacePercentage(pace_values)
    else:
        pass


eingabe = input("Which month do you want to view?\n")

infoMonth(eingabe)