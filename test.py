import json

# Reading data from json file
file = open('data.json')
data = json.load(file)
file.close()

# Getting unique stars names from data
stars = []
for value in data:
    starcast = value['stars'].split(',')
    for star in starcast:
        stars.append(star.strip())

stars = list(dict.fromkeys(stars))

# Calculating total movies stars worked in and the average rating of all their movies
resultList = []
for star in stars:
    counter = 0
    avgRating = []
    for value in data:
        if star in value['stars']:
            counter += 1
            avgRating.append(float(value['rating']))

    # this statement will make sure to store results only for the stars who worked in more then 1 movie
    if counter > 1:
        avgR = sum(avgRating) / len(avgRating)
        lst = [star, counter, '{:.2f}'.format(round(avgR, 2))]
        resultList.append(lst)

# Sorting the list based on number of movies the stars worked in
resultList = sorted(resultList, key = lambda x: x[1])

# print the results
for values in resultList:
    print(f"Star Name: {values[0]:22} | Movies: {values[1]: 1} | Avg. Rating: {values[2]}")