import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows 

# List of URLs for different clubs
club_urls = [
    ("https://www.footballtransfers.com/en/teams/uk/man-city","Manchester City"),
    ("https://www.footballtransfers.com/en/teams/uk/arsenal","Arsenal"),
    ("https://www.footballtransfers.com/en/teams/uk/man-utd","Manchester Utd"),
    ("https://www.footballtransfers.com/en/teams/uk/newcastle-utd","Newcastle Utd"),
    ("https://www.footballtransfers.com/en/teams/uk/liverpool","liverpool"),
    ("https://www.footballtransfers.com/en/teams/uk/brighton","brighton"),
    ("https://www.footballtransfers.com/en/teams/uk/aston-villa","Aston Villa"),
    ("https://www.footballtransfers.com/en/teams/uk/tottenham","Tottenham"),
    ("https://www.footballtransfers.com/en/teams/uk/brentford","Brentford"),
    ("https://www.footballtransfers.com/en/teams/uk/fulham","Fulham"),
    ("https://www.footballtransfers.com/en/teams/uk/crystal-palace","Crystal Palace"),
    ("https://www.footballtransfers.com/en/teams/uk/chelsea","Chelsea"),
    ("https://www.footballtransfers.com/en/teams/uk/wolverhampton","Wolverhampton"),
    ("https://www.footballtransfers.com/en/teams/uk/west-ham","West-ham utd"),
    ("https://www.footballtransfers.com/en/teams/uk/bournemouth","Bournemouth"),
    ("https://www.footballtransfers.com/en/teams/uk/nottingham","Nottingham Forest"),
    ("https://www.footballtransfers.com/en/teams/uk/everton","Everton"),
    ("https://www.footballtransfers.com/en/teams/uk/leicester","Leicester"),
    ("https://www.footballtransfers.com/en/teams/uk/leeds-united","Leeds United"),
    ("https://www.footballtransfers.com/en/teams/uk/southampton","Southampton")
    ]

scraped_data = []

def scrape_club_players(url, club_name):
    # Send a GET request to fetch the HTML content
    response = requests.get(url)
    html_content = response.content
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all player rows
    player_rows = soup.find_all('tr', class_=['odd', 'even'])
    
    # Iterate through each player row and extract information
    for player_row in player_rows:
        player_name = player_row.find('a', title=True).text.strip()
        player_age = int(player_row.find('td', class_='text-right').text.strip())

        # Extract nationality from the alt attribute of the flag image within the figure
        flag_image = player_row.find('figure', class_='small-icon-image').find('img', alt=True)
        nationality = flag_image['alt'] if flag_image else "Unknown"    

        # Append scraped data as dictionary to the 'scraped_data' list
        player_data = {
            "Player Name": player_name,
            "Player Age": player_age,
            "Player Nationality": nationality,
            "Club": club_name
        }
        scraped_data.append(player_data)
# Iterate through each club URL and scrape player information
for url, club_name in club_urls:
    scrape_club_players(url, club_name)

# Create a DataFrame from the 'scraped_data' list of dictionaries
df = pd.DataFrame(scraped_data)

#Storing the data in an excel sheet
wb = Workbook()
ws = wb.create_sheet('Player Data')

for r in dataframe_to_rows(df, header=True, index=False):
    ws.append(r)
wb.remove(wb['Sheet'])

wb.save('/workspaces/1202/Project/Code/PlayerData.xlsx')