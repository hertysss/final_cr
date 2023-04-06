import csv
import sqlite3

db = input()
table_name = input()
title = input()
max_num = int(input())
con = sqlite3.connect(db)
res = con.cursor().execute(f"""SELECT colonies.id, colonies.leader, planets.planet, 
stars.name, colonies.number, planets.life_zone from colonies
INNER JOIN stars ON stars.id = planets.star_id
INNER JOIN planets ON planets.id = colonies.planet_id
WHERE {table_name}.{title} <= {max_num}
ORDER BY planets.planet, colonies.leader""").fetchall()
con.close()
with open("response.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=':', quotechar='"')
    header = ("colony_id", "leader", "planet_name", "star_name", "number", "life_zone")
    writer.writerow(header)
    for i in res:
        writer.writerow(i)