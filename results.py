from iracingdataapi.client import irDataClient
import pprint
import csv
import sys
import teams
import config

pp = pprint.PrettyPrinter(indent=4)
idc = irDataClient(username=config.username, password=config.password)

max_points = 300
min_points = 10
decrement = 10

classes = teams.classes
pro_teams = teams.pro_teams
am_teams = teams.am_teams

# pp.pprint(teams)
# quit()

try:
    subsession_id = sys.argv[1]
except:
    print('---------------------------------')
    print("Please provide a subsession id.")
    print('---------------------------------')
    sys.exit(2)

results = idc.result(subsession_id)

def calculate(team):
    current_class = ""
    for result in results['session_results']:
        if result['simsession_name'] == 'RACE':
            for car_class in classes:
                if current_class != car_class:
                    count = 1
                    current_class = car_class
                for race_result in result['results']:
                    if current_class == race_result['car_class_short_name']:
                        try:
                            i = next((i for i, item in enumerate(team) if item["driver_1_id"] == race_result['cust_id']), None)
                            if i != None:
                                team[i]["driver_1_finish_pos"] = count
                                team[i]["driver_1_points"] = max_points - ((count-1)*decrement)
                                team[i]["class"] = race_result['car_class_short_name']
                                count = count+1
                            i = next((i for i, item in enumerate(team) if item["driver_2_id"] == race_result['cust_id']), None)
                            if i != None:
                                team[i]["driver_2_finish_pos"] = count
                                team[i]["driver_2_points"] = max_points - ((count-1)*decrement)
                                team[i]["class"] = race_result['car_class_short_name']
                                count = count+1
                        except KeyError:
                            print(race_result)

    return team

am_results = calculate(am_teams)
pro_results = calculate(pro_teams)

with open('results/results-' + str(subsession_id) + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Team Name', 'Driver 1 Name', 'Driver 1 Position', 'Driver 1 Points', 'Driver 2 Name', 'Driver 2 Position', 'Driver 2 Points', 'PRO / AM', 'Car Class'])
    for result in am_results:
        writer.writerow([result['team_name'], result['driver_1'], result['driver_1_finish_pos'], result['driver_1_points'], result['driver_2'], result['driver_2_finish_pos'], result['driver_2_points'], 'AM', result['class']])
    for result in pro_results:
        writer.writerow([result['team_name'], result['driver_1'], result['driver_1_finish_pos'], result['driver_1_points'], result['driver_2'], result['driver_2_finish_pos'], result['driver_2_points'], 'PRO', result['class']])
