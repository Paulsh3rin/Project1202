import requests
from bs4 import BeautifulSoup
import pandas as pd 
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows 

urls = [
    "https://fbref.com/en/squads/18bb7c10/2022-2023/Arsenal-Stats",
    "https://fbref.com/en/squads/b8fd03ef/2022-2023/Manchester-City-Stats",
    "https://fbref.com/en/squads/19538871/2022-2023/Manchester-United-Stats",
    "https://fbref.com/en/squads/b2b47a98/2022-2023/Newcastle-United-Stats",
    "https://fbref.com/en/squads/b2b47a98/2022-2023/Newcastle-United-Stats",
    "https://fbref.com/en/squads/822bd0ba/2022-2023/Liverpool-Stats",
    "https://fbref.com/en/squads/d07537b9/2022-2023/Brighton-and-Hove-Albion-Stats",
    "https://fbref.com/en/squads/8602292d/2022-2023/Aston-Villa-Stats",
    "https://fbref.com/en/squads/361ca564/2022-2023/Tottenham-Hotspur-Stats",
    "https://fbref.com/en/squads/cd051869/2022-2023/Brentford-Stats",
    "https://fbref.com/en/squads/fd962109/2022-2023/Fulham-Stats",
    "https://fbref.com/en/squads/47c64c55/2022-2023/Crystal-Palace-Stats",
    "https://fbref.com/en/squads/cff3d9bb/2022-2023/Chelsea-Stats",
    "https://fbref.com/en/squads/8cec06e1/2022-2023/Wolverhampton-Wanderers-Stats",
    "https://fbref.com/en/squads/7c21e445/2022-2023/West-Ham-United-Stats",
    "https://fbref.com/en/squads/4ba7cbea/2022-2023/Bournemouth-Stats",
    "https://fbref.com/en/squads/e4a775cb/2022-2023/Nottingham-Forest-Stats",
    "https://fbref.com/en/squads/d3fd31cc/2022-2023/Everton-Stats",
    "https://fbref.com/en/squads/a2d435b3/2022-2023/Leicester-City-Stats",
    "https://fbref.com/en/squads/5bfb9659/2022-2023/Leeds-United-Stats",
    "https://fbref.com/en/squads/33c895d4/2022-2023/Southampton-Stats"
    ]

scraped_data = []

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        rows = soup.find("div", class_ ="table_wrapper tabbed").find_all("tr")# Find all rows in the table
        exclude_names = ["Squad Total", "Opponent Total"]
        for row in rows[2:]:
            player = row.find("th", {"data-stat": "player"})  # Find player name
            if player:
                player_name = player.text.strip()
                
                if player_name not in exclude_names:
                    goals_element = row.find("td", {"data-stat": "goals"})
                    goals = goals_element.text.strip() if goals_element else "None"

                    assists_element = row.find("td", {"data-stat": "assists"})
                    assists = assists_element.text.strip() if assists_element else "None"

                    cards_yellow_element = row.find("td", {"data-stat": "cards_yellow"})
                    cards_yellow = cards_yellow_element.text.strip() if cards_yellow_element else "None"

                    cards_red_element = row.find("td", {"data-stat": "cards_red"})
                    cards_red = cards_red_element.text.strip() if cards_red_element else "None"

                    prog_passes_element = row.find("td", {"data-stat": "progressive_passes"})
                    progressive_passes = prog_passes_element.text.strip() if prog_passes_element else "None"

                    passes_received_element = row.find("td", {"data-stat": "progressive_passes_received"})
                    passes_received = passes_received_element.text.strip() if passes_received_element else "None"

                    player_stats={
                        "Player": player_name,
                        "Goals": goals,
                        "Assists": assists,
                        "Yellow Cards": cards_yellow,
                        "Red Cards": cards_red,
                        "Progressive Passes": progressive_passes,
                        "Passes Received": passes_received
                    }
                    scraped_data.append(player_stats)
                

df = pd.DataFrame(scraped_data)
wb = Workbook()
ws = wb.create_sheet('Player Stats')

for r in dataframe_to_rows(df, header=True, index=False):
    ws.append(r)
wb.remove(wb['Sheet'])

wb.save('/workspaces/1202/Project/Code/PlayeStats.xlsx')