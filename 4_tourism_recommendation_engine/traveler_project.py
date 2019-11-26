# List Declaration
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler  = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[] for i in destinations]
attractions_with_interest = []

# Functions
def get_destination_index(destination):
    for dest in destinations:
        destination_index = destinations.index(destination)
        return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    return traveler_destination

def traveler_destination_index(traveler):
    traveler_location = get_traveler_location(traveler)
    test_destination_index = get_destination_index(traveler_location)
    return test_destination_index

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
    except SyntaxError:
        return

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    #print(destination_index)
    attractions_in_city = attractions[destination_index]
    #print(attractions_in_city)
    attractions_with_interest = []

    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    #print("Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": " + str(traveler_attractions) + ", the Pike Place Market.")
    print("Hi {}, we think you'll like these places around {}: {}.".format(traveler[0], traveler_destination, str(traveler_attractions[0])))
    
# Calls           
print(destinations)
print(test_traveler)

# Print index in destinations
print("Destination Index for Los Angeles, USA : " + str(get_destination_index("Los Angeles, USA")))
print("Destination Index for Paris, France : " + str(get_destination_index("Paris, France")))

# Get destination index for traveler 
test_destination_index = traveler_destination_index(test_traveler)
print("Destination Index for " + test_traveler[0] + " is : " + str(test_destination_index) + " (" + str(test_traveler[1]) + ")")
print(attractions)

# Add attractions
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)

#find_attractions("Paris, France", 0)
la_arts = find_attractions("Los Angeles, USA",['art'])
print(la_arts)
get_attractions_for_traveler(test_traveler)


