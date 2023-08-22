# English Premier League 2022-23
![image](https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/bltb58eaacf24a555bd/646fad7d995cde6fe7e3458a/EPL_Team_of_the_Season_GFX.jpg?auto=webp&format=pjpg&width=3840&quality=60) 
## *Player/Club performance analysis*

### Find:
1. who scored most goals in the season ?
2. The oldest player('s)
3. The youngest player('s)
5. The aggresive player (most yellow and red cards)

### **Phases of Analysis**
---
### 1. Extraction:
Scraped data from available websites using python
1. https://www.footballtransfers.com/en/teams/uk - Player Details

| Name | Age | Nationality | Club |
| --- | --- | --- | --- |
| Zack Steffen | 28 | United States | Manchester City |
| Ederson | 29 | Brazil | Manchester City |
| Scott Carson | 37 | England | Manchester City |
| Steffen Ortega | 30 | Germany | Manchester City |
| Aymeric Laporte | 29 | Spain | Manchester City |

`*5 rows returned*`

2. https://fbref.com/en/squads/18bb7c10/2022-2023 - Player Stats

| Player | Goals | Assists | Yellow Cards | Red Cards | Progressive Passes | Passes Recieved |
| --- | --- | --- | --- | --- | --- | --- |
| Aaron Ramsdale | 0 | 0 | 1 | 0 | 8 | 0 |
| Gabriel Dos Santos | 3 | 0 | 5 | 0 | 153 | 16 |
| Bukoya Saka | 14 | 11 | 6 | 0 | 109 | 520 |
| Martin Odegaard | 15 | 7 | 4 | 0 | 266 | 193 |
| Ben White | 2 | 5 | 5 | 0 | 249 | 124 | 

`*5 rows returned*`

### 2. Load:
1. Joined two tables and created a new table
```sql
CREATE TABLE Statistics AS
SELECT playerdata.Player, Age, Nationality, Club, 
        playerstats.Goals, 
        playerstats.Assists, 
        playerstats.YellowCards, 
        playerstats.RedCards, 
        playerstats.ProgressivePasses, 
        playerstats.PassesReceived
FROM playerdata
LEFT JOIN playerstats
ON playerdata.Player = playerstats.Player;
```
```sql
SELECT * 
FROM Statistics
```
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/360ae4ec-2472-4e23-9bde-eb08f3bc229d)

### 3. Transformation
Changed NULL to 0
```sql
SELECT Player, Age, Nationality, Club,
        COALESCE(Goals, 0) AS Goals,
        COALESCE(Assists, 0) AS Assists,
        COALESCE(YellowCards, 0) AS YellowCards,
        COALESCE(RedCards, 0) AS RedCards,
        COALESCE(ProgressivePasses, 0) AS ProgressivePasses,
        COALESCE(PassesReceived, 0) AS PassesReceived
FROM Statistics;
```

![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/5fd5f8b1-c55c-4040-9208-a22f488a0232)

Removed duplicate rows
```sql
CREATE TEMPORARY TABLE temp_table AS
SELECT DISTINCT
    Player, Age, Nationality, Club, Goals, Assists, YellowCards, RedCards, ProgressivePasses, PassesReceived
FROM Statistics;

TRUNCATE TABLE Statistics;

INSERT INTO Statistics
SELECT * FROM temp_table;
```
### Findings
---
1. Most Goals
```sql
SELECT Player, Club, max(Goals) AS Goals
FROM Statistics
GROUP BY Player, Club
ORDER BY Goals DESC;
```
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/fec0fbd7-44ba-41d4-9a46-6623b16599d0)

2. Oldest Player ('s)
```sql
SELECT Player, Club, Age
FROM Statistics
GROUP BY Player, Club, Age
ORDER BY Age DESC;
```
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/a3453d9a-41a6-43cc-8832-91d7d9caa91f)

3. Youngest Player ('s)

![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/9c182d95-4298-4954-8ff9-593ac67a11d7)

4. The aggresive player ('s)
```sql
SELECT Player, SUM(YellowCards + RedCards) AS TotalCards
FROM statistics
GROUP BY Player
ORDER BY TotalCards DESC;
```
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/9e696a27-68c4-4d68-83a8-3764dd4cc23f)

### Reflections:
---
The interesting thing about this project was it covered all the concepts I learned throughout this program. It helped me consolidate what I learned and made me feel I can do an ETL pipeline.

Here are the project outcomes for me:
* I got familiar with data scraping tools in python like BeautifulSoup and requests.
* I am now confident to load data to MySql workbench, Clean the data by dealing with NULL and Duplicate data, Transform data using JOIN function to merge two table and create a view if necessary.
* I am now better at using Github to code and document my work effectively. Markdown Cheatsheet helped me in the process.
* Every tasks had its challenges but one among them was I was not able to load the scraped data into MySql workbench eventhough it was in csv format, but later I found out it has to be in .csv(comma delimeted) format to be uploaded.
* Another issue that I faced, while I was trying to find the aggresssive player, the "Totalcards" returned a big number which I felt isn't right. The reason for it was the raws had duplicate values and it all counted. I solved it by removing those duplicates.



















