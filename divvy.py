#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 3: Divvy Bike Problem
import math

import json
try:
    from urllib.request import urlopen

    webservice_url = "http://www.divvybikes.com/stations/json"
    data = urlopen(webservice_url).read().decode("utf8")
    result = json.loads(data)
    stations = result['stationBeanList']

    #set latitude and longitude for Young
    distances = []
    young_lat = 41.793414
    young_long = -87.600915

    #calculate distances between Young and each station using latitude and longitude
    for i in range(len(stations)):
        distances.append(math.sqrt((stations[i]['latitude']-young_lat)**2 + (stations[i]['longitude']-young_long)**2))
        
    #associate each distance with an ID in a dictionary
    distances_dict = {}

    for i in range(len(stations)):
        distances_dict.update({i : distances[i]})

    #sort list of distances to identify the shortest
    distances.sort()

    #iterate through distances_dict to identify the station with shortest distance to Young
    for i, j in distances_dict.items():
        if distances_dict[i] == distances[0]:
            print("\nThe station closest to Young is:", stations[i]['stationName'])
            if int(stations[i]['availableBikes']) == 1:
                print("\nThere is", stations[i]['availableBikes'], "bike currently available.")
            else:
                print("\nThere are", stations[i]['availableBikes'], "bikes currently available.")

except:
    print("There was an unexpected error. Please try again.")


