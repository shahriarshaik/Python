
import numpy as np
import matplotlib.pyplot as plt
#Map of Europe
europe_map = plt.imread('Assignment1/map.png')

#Lists of city coordinates
city_coords={"Barcelona":[2.154007, 41.390205], "Belgrade": [20.46,44.79], "Berlin": [13.40,52.52], "Brussels":[4.35,50.85],"Bucharest":[26.10,44.44], "Budapest": [19.04,47.50], "Copenhagen":[12.57,55.68], "Dublin":[-6.27,53.35], "Hamburg": [9.99, 53.55], "Istanbul": [28.98, 41.02], "Kiev": [30.52,50.45], "London": [-0.12,51.51], "Madrid": [-3.70,40.42], "Milan":[9.19,45.46], "Moscow": [37.62,55.75], "Munich": [11.58,48.14], "Paris":[2.35,48.86], "Prague":[14.42,50.07], "Rome": [12.50,41.90], "Saint Petersburg": [30.31,59.94], "Sofia":[23.32,42.70], "Stockholm": [18.06,60.33],"Vienna":[16.36,48.21],"Warsaw":[21.02,52.24]}


#Helper code for plotting plans
#First, visualizing the cities.
import csv
with open("Assignment1/european_cities.csv", "r") as f:
    data = list(csv.reader(f, delimiter=';'))
    cities = data[0]
    
fig, ax = plt.subplots(figsize=(10,10)) # set the size that you'd like (width, height)

ax.imshow(europe_map, extent=[-14.56,38.43, 37.697 +0.3 , 64.344 +2.0], aspect = "auto") # plot the image


"""
# Map (long, lat) to (x, y) for plotting
for city,location in city_coords.items():
    x, y = (location[0], location[1])
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, city, fontsize=12);
"""


#A method you can use to plot your plan on the map.
def plot_plan(city_order):
    fig, ax = plt.subplots(figsize=(10,10))
    ax.imshow(europe_map, extent=[-14.56,38.43, 37.697 +0.3 , 64.344 +2.0], aspect = "auto")

    # Map (long, lat) to (x, y) for plotting
    for index in range(len(city_order) -1):
        current_city_coords = city_coords[city_order[index]]
        next_city_coords = city_coords[city_order[index+1]]
        x, y = current_city_coords[0], current_city_coords[1]
        #Plotting a line to the next city
        next_x, next_y = next_city_coords[0], next_city_coords[1]
        plt.plot([x,next_x], [y,next_y])
        
        plt.plot(x, y, 'ok', markersize=5)
        plt.text(x, y, index, fontsize=12);
    #Finally, plotting from last to first city
    first_city_coords = city_coords[city_order[0]]
    first_x, first_y = first_city_coords[0], first_city_coords[1]
    plt.plot([next_x,first_x],[next_y,first_y])
    #Plotting a marker and index for the final city
    plt.plot(next_x, next_y, 'ok', markersize=5)
    plt.text(next_x, next_y, index+1, fontsize=12);
    plt.show();


"""
#Example usage of the plotting-method.
plan = list(city_coords.keys()) # Gives us the cities in alphabetic order
print(plan)
plot_plan(plan)
"""



# Implement the algorithm here
#program to find the shortest path between cities by brute force
import itertools
import math

def find_shortest_path(city_coords):
    # Create a list of cities
    cities = list(city_coords.keys())
    # Get the number of cities
    n = len(cities)
    # Set the minimum distance to infinity
    min_distance = float('inf')
    # Set the shortest path to None
    shortest_path = None
    # Generate all permutations of the cities (all the different possible paths)
    for path in itertools.permutations(cities):
        # Initialize the distance to 0
        distance = 0
        # Calculate distance of path
        for i in range(n-1):
            # Calculate the distance between city i and city i+1
            distance += math.sqrt((city_coords[path[i]][0] - city_coords[path[i+1]][0])**2 + (city_coords[path[i]][1] - city_coords[path[i+1]][1])**2)
        # Add distance from last city back to first city
        distance += math.sqrt((city_coords[path[-1]][0] - city_coords[path[0]][0])**2 + (city_coords[path[-1]][1] - city_coords[path[0]][1])**2)
        # Update shortest path if distance is smaller
        if distance < min_distance:
            min_distance = distance
            shortest_path = path
    return shortest_path

# Answer

#first = {"Barcelona":[2.154007, 41.390205], "Belgrade": [20.46,44.79], "Berlin": [13.40,52.52], "Brussels":[4.35,50.85],}
timeList = []

timesToRun = 3

import time

def makeCityDict(city_coords, amount):
    first = {}
    for city in city_coords:
        if amount == 0:
            break
        first[city] = city_coords[city]
        amount -= 1
    return first

def BruteForceCalcPlot(city_coords):
    path = None
    for i in range(timesToRun - 1):
        start_time = time.time()
        #call the function
        path = find_shortest_path(makeCityDict(city_coords, i+2))
        end_time = time.time()
        timeList.append(end_time - start_time)
        plot_plan(path)
    print("The shortest path is: ", path)
    return path


def distance(path):
    distance = 0
    for i in range(len(path)-1):
        distance += math.sqrt((city_coords[path[i]][0] - city_coords[path[i+1]][0])**2 + (city_coords[path[i]][1] - city_coords[path[i+1]][1])**2)
    # Add distance from last city back to first city
    distance += math.sqrt((city_coords[path[-1]][0] - city_coords[path[0]][0])**2 + (city_coords[path[-1]][1] - city_coords[path[0]][1])**2)
    print("The total distance is: ", distance)
    return distance



#print("All the times it took using exhaustive search: ", timeList)

#print how many times longer it took in average for each city added
def timeCalc(timeList):
    for i in range(len(timeList)-1):
        try:
            print("It took ", timeList[i+1]/timeList[i], " times longer to find the shortest path with ", i+3, " cities")
        except:
            print("div by zero error")

def eachStepDistanceBrute():
    distance(BruteForceCalcPlot(makeCityDict(city_coords, timesToRun)))
    timeCalc(timeList)

"""
eachStepDistanceBrute()
"""



"""
All the times it took using exhaustive search:  [0.0, 0.0, 0.0, 0.0, 0.001500844955444336, 0.01451253890991211, 0.13611626625061035, 1.3686752319335938, 15.084447860717773, 180.0325367450714, 2478.4434514045715]

div by zero error
div by zero error
div by zero error
div by zero error
It took  9.669579030976966  times longer to find the shortest path with  7  cities
It took  9.379218005585674  times longer to find the shortest path with  8  cities
It took  10.055192297250194  times longer to find the shortest path with  9  cities
It took  11.021203210791828  times longer to find the shortest path with  10  cities
It took  11.934976898551513  times longer to find the shortest path with  11  cities
It took  13.766641831604485  times longer to find the shortest path with  12  cities


for every city added it took 9.6 times longer to find the shortest path using exhaustive search and it look like the time it takes longer also increases by 1.1 times
searching for 11 cities too 44 minutes and 38 seconds, for all 24 cities it would take 4.47e13 minues or 7.45e11 hours or 3.13e10 days or 8.5e8 years on my computer
"""

# Implement the hill climbing algorithm here
#program to find the shortest path between cities using hill climbing



import random
import math



def hill_climb(city_coords):
    cities = list(city_coords.keys())
    n = len(cities)
    # Start with a random path through the cities
    path = random.sample(cities, n)
    # Calculate the distance of the initial path
    distance = 0
    for i in range(n-1):
        distance += math.sqrt((city_coords[path[i]][0] - city_coords[path[i+1]][0])**2 + (city_coords[path[i]][1] - city_coords[path[i+1]][1])**2)
    # Add distance from last city back to first city
    distance += math.sqrt((city_coords[path[-1]][0] - city_coords[path[0]][0])**2 + (city_coords[path[-1]][1] - city_coords[path[0]][1])**2)
    while True:
        improved = False
        # Iterate over all pairs of cities
        for i in range(n-1):
            for j in range(i+1, n):
                # Swap the two cities in the path
                new_path = path[:]
                new_path[i], new_path[j] = new_path[j], new_path[i]
                # Calculate the distance of the new path
                new_distance = 0
                for k in range(n-1):
                    new_distance += math.sqrt((city_coords[new_path[k]][0] - city_coords[new_path[k+1]][0])**2 + (city_coords[new_path[k]][1] - city_coords[new_path[k+1]][1])**2)
                # Add distance from last city back to first city
                new_distance += math.sqrt((city_coords[new_path[-1]][0] - city_coords[new_path[0]][0])**2 + (city_coords[new_path[-1]][1] - city_coords[new_path[0]][1])**2)
                # If the new path is shorter, keep it
                if new_distance < distance:
                    path = new_path
                    distance = new_distance
                    improved = True
                    break
            if improved:
                break
        # If no improvement was made in the last iteration, return the current path
        if not improved:
            return path

timesToRun = 3
timeList = []

def HillClimbCalcPlot(timesToRun, timeList):
    path = None
    for i in range(timesToRun - 1):
        start_time = time.time()
        #call the function
        path = hill_climb(makeCityDict(city_coords, i+2))
        end_time = time.time()
        timeList.append(end_time - start_time)
        plot_plan(path)
    print("The shortest path is: ", path)
    return path

#method that takes in path and sums the distance between each city

def eachStepDistanceHill():
    distance(HillClimbCalcPlot(timesToRun, timeList))
    timeCalc(timeList)


def bestOutOf(amounts):
    shortest = 0
    shortestpath = None
    for i in range(amounts):
        path = hill_climb(makeCityDict(city_coords, timesToRun))
        if i == 0:
            shortest = distance(path)
        else:
            if distance(path) < shortest:
                shortest = distance(path)
                shortestpath = path
    print("The shortest distance was: ", shortest, " \nand the path was: ", shortestpath)



#eachStepDistanceHill()
#bestOutOf(100)

#function that uses genetic algorithm to find the shortest path between cities

def ShortestPathGenetic(city_coords, population_size=50, mutation_rate=0.1, generations=100):
    cities = list(city_coords.keys())
    n = len(cities)
    # Generate initial population of random paths
    population = [random.sample(cities, n) for i in range(population_size)]
    for generation in range(generations):
        # Calculate fitness of each path
        fitness = [1 / distance1(city_coords, path) for path in population]
        # Normalize fitness values
        fitness_sum = sum(fitness)
        fitness = [f / fitness_sum for f in fitness]
        # Create new population
        new_population = []
        # Select the best individual from the current population
        best_individual = population[fitness.index(max(fitness))]
        for i in range(population_size):
            # Select two random paths
            path1 = random.choices(population, fitness)[0]
            path2 = random.choices(population, fitness)[0]
            # Perform crossover
            path = crossover(path1, path2)
            # Perform mutation
            if random.random() < mutation_rate:
                path = mutate(path)
            # Add new path to new population
            new_population.append(path)
        # Compare the best individual with the worst individual in the new population
        worst_fitness = min([1 / distance1(city_coords, path) for path in new_population])
        if 1 / distance1(city_coords, best_individual) > worst_fitness:
            new_population[new_population.index(min(new_population, key=lambda x: 1 / distance1(city_coords, x)))] = best_individual
        population = new_population
    # Return best path
    best_path = population[0]
    best_distance = distance1(city_coords, best_path)
    for path in population:
        path_distance = distance1(city_coords, path)
        if path_distance < best_distance:
            best_path = path
            best_distance = path_distance
    return best_path


def crossover(path1, path2):
    n = len(path1)
    # Select random crossover point
    crossover_point = random.randint(0, n-1)
    # Create new path
    path = path1[:crossover_point]
    for city in path2:
        if city not in path:
            path.append(city)
    return path

def mutate(path):
    n = len(path)
    # Select two random cities
    city1 = random.randint(0, n-1)
    city2 = random.randint(0, n-1)
    # Swap the two cities in the path
    path[city1], path[city2] = path[city2], path[city1]
    return path

def distance1(city_coords, path):
    distance = 0
    n = len(path)
    for i in range(n-1):
        distance += math.sqrt((city_coords[path[i]][0] - city_coords[path[i+1]][0])**2 + (city_coords[path[i]][1] - city_coords[path[i+1]][1])**2)
    # Add distance from last city back to first city
    distance += math.sqrt((city_coords[path[-1]][0] - city_coords[path[0]][0])**2 + (city_coords[path[-1]][1] - city_coords[path[0]][1])**2)
    return distance



timesToRun = 20
timeList = []

def geneticCalcPlot(timesToRun, timeList):
    path = None
    for i in range(timesToRun - 1):
        start_time = time.time()
        #call the function
        path = ShortestPathGenetic(makeCityDict(city_coords, i+2))
        end_time = time.time()
        timeList.append(end_time - start_time)
        plot_plan(path)
    print("The shortest path is: ", path)
    return path

#method that takes in path and sums the distance between each city

distance(geneticCalcPlot(timesToRun, timeList))




timeCalc(timeList)

