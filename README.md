# English Premier League 2022-23
![image](https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/bltb58eaacf24a555bd/646fad7d995cde6fe7e3458a/EPL_Team_of_the_Season_GFX.jpg?auto=webp&format=pjpg&width=3840&quality=60) 
## Player/Club performance analysis

### Find:
1. who scored most goals in the season ?
2. The oldest player('s)
3. The youngest player('s)
5. The aggresive player (most yellow and red cards)

### Extraction:
Scraped data from available websites using python
1. https://www.footballtransfers.com/en/teams/uk - Player Details
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/ecc93b45-facc-4a8d-8e84-f92d62a3a2b2)


3. https://fbref.com/en/squads/18bb7c10/2022-2023 - Player Stats
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/ade87104-2239-4946-9707-6a3fe7f64190)

### Load:
1. Joined two tables and created a view
```sql
CREATE VIEW PlayerStatsView AS
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
FROM PlayerStatsView
```
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/360ae4ec-2472-4e23-9bde-eb08f3bc229d)

### Transformation
Changed NULL to 0
```sql
SELECT Player, Age, Nationality, Club,
        COALESCE(Goals, 0) AS Goals,
        COALESCE(Assists, 0) AS Assists,
        COALESCE(YellowCards, 0) AS YellowCards,
        COALESCE(RedCards, 0) AS RedCards,
        COALESCE(ProgressivePasses, 0) AS ProgressivePasses,
        COALESCE(PassesReceived, 0) AS PassesReceived
FROM playerstatsview;
```

![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/5fd5f8b1-c55c-4040-9208-a22f488a0232)

### Findings
1. Most Goals
```sql
SELECT Player, Club, max(Goals) AS Goals
FROM playerstatsview
GROUP BY Player, Club
ORDER BY Goals DESC;
```
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/fec0fbd7-44ba-41d4-9a46-6623b16599d0)

2. Oldest Player ('s)
```sql
SELECT Player, Club, Age
FROM playerstatsview
GROUP BY Player, Club, Age
ORDER BY Age DESC;
```
![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/a3453d9a-41a6-43cc-8832-91d7d9caa91f)

3. Youngest Player ('s)

![image](https://github.com/Paulsh3rin/Project1202/assets/114738504/9c182d95-4298-4954-8ff9-593ac67a11d7)

4. The aggresive player

















