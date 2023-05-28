from iracingdataapi.client import irDataClient
import config
import pprint

pp = pprint.PrettyPrinter(indent=4)

idc = irDataClient(username=config.username, password=config.password)

results = idc.league_season_sessions(config.league_id, config.season_id)
for result in results['sessions']:
    if result['race_length'] > 0:
        if 'subsession_id' in result:
            pp.pprint(str(result['subsession_id']) + ' ' + str(result['track']['track_name']) + ' ' + str(result['launch_at']))
