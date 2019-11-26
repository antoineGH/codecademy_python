# Lists

# Destinations List
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# Traveler Lest [ String Name, String Location, List[ String Tag1, String Tag2 ]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# List of list declaration [[], [], [], [], []]
attractions = [[] for i in range(5)] 

# Functions

# Get List index from Destination List
def get_destination_index(destination):
    # 2 = destinations.index("Los Angeles, USA")
    # 0 = destinations.index("Paris, France")
    destination_index = destinations.index(destination)
    return destination_index

# Get Traveler index from Destination List
def get_traveler_location(traveler):
    
    # Get traveler location list[1]
    # 'Shanghai, China' = test_traveler[1]
    traveler_destination = traveler[1]
    
    # Get destination index for traveler location in destination list
    # 1 = get_destination_index(Shanghai, China)
    traveler_destination_index = get_destination_index(traveler_destination)
    
    # return 1
    return traveler_destination_index

# This function add the attraction in the destination index in list attraction
def add_attraction(destination, attraction):
    try:
        # Get List index from Destination List
        # 2 = destinations.index("Los Angeles, USA")
        destination_index = get_destination_index(destination)

        # Add attraction in attractions list in the destination index
        attractions_for_destination = attractions[destination_index].append(attraction)
    except SyntaxError:
        return

# Find attraction according to the interests tag list and the destination provided
def find_attractions(destination, interests):
    # Get traveler location list[1]
    # 'Shanghai, China' = test_traveler[1]
    destination_index = get_destination_index(destination)

    # Load attractions_in_city with attraction in destination index from attraction list
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    
    # Loop through attractions_in_city and get possible attration[0] gets only the attraction (not the tags)
    for attraction in attractions_in_city:
        possible_attraction = attraction[0]
        # Collect the attraction tag
        attraction_tags = attraction[1]

        # Loop through interests and get interests if the interest match with the attraction tag append in attractions_with_interest
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction)

    return attractions_with_interest
       
# Get attraction for traveler
def get_attractions_for_traveler(traveler):  
    # Extract traveler destination (string)
    # 'Shanghai, China'
    traveler_destination = traveler[1]

    # Extract traveler interest (list)
    # ['historical site', 'art']
    traveler_interests = traveler[2]

    # Find attraction for traveler destination, and traveler interests
    # find_attractions('Shanghai, China', ['historical site', 'art'])
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    # "string".format() result for display using Traveler's name : traveler[0], Traveler's destination : traveler_destination, Traveler's attraction : traveler_attractions
    interests_string = "Hi {}, we think you'll like these places around {}: {}.".format(traveler[0], traveler_destination, traveler_attractions[0] )
    return interests_string

# Calls
# Get index for "Los Angeles, USA" in destination list = 2 (int)
get_destination_index("Los Angeles, USA")

# Get traveler's location for test_traveler = 'Shanghai, China' (string)
get_traveler_location(test_traveler)

# Add attraction to the application add_attraction("destination"(string), tags ['Venice Beach', ['beach'] (list)]
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

# Print attraction in "Los Angeles, USA" matching tag ['art']
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)

# Get attractions for differents travelers and print result
get_attractions_for_traveler(test_traveler)
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
ratat_egypt = get_attractions_for_traveler(['Antoine Ratat', 'Cairo, Egypt', ['historical site']])
mollaret_USA = get_attractions_for_traveler(['Sebastien Mollaret', 'Los Angeles, USA', ['museum']])
print(smills_france)
print(ratat_egypt)
print(mollaret_USA)