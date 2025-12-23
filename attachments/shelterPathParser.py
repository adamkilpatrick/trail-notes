import json
from datetime import date, timedelta

startDate = date(2025, 2, 14)
initPaths = json.load(open("./shelterPaths.json"))

parsedPath = []

for point in initPaths:
    parsedPoint = {
        "loc": [float(x) for x in point["gps"].split(",")],
        "label": point["name"],
        "miles": point["nobo_miles"],
        "eta": (startDate + timedelta(days=point["nobo_miles"]/12)).isoformat()
    }
    parsedPath.append(parsedPoint)

json.dump(parsedPath, open("./shelterPathParsed.json", "w"), indent=4)