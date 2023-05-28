# Fendi Racing Results Generator
#### Setup
1. Ensure you are using Python 3.10.11+
2. Clone repo fendi repo
3. Navigate to the cloned repo in your terminal and run `pip install iracingdataapi`
3. Edit the config.py file with your iRacing credentials and League info
4. Edit the `teams.py` file with pro and am teams.  If a team only has 1 driver, leave driver 2 data empty (don't delete it)
5. Run ``python sessions.py`` to get a list of the available subsession ids for the league
6. Run ``python results.py <subsession_id>`` to generate the `results/results-<subsession_id>.csv` file
