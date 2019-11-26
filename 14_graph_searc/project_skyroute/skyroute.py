import graph_search
from graph_search import bfs, dfs
import vc_metro
from vc_metro import vc_metro
import vc_landmarks
from vc_landmarks import vc_landmarks
import landmark_choices
from landmark_choices import landmark_choices
import datetime

landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += "{} - {}\n".format(letter, landmark)

stations_under_construction = ['Lansdowne']

def greet_menu():
    now = datetime.datetime.now()
    print("\n--- Vancouvers Metro System ---".upper())
    print(now.strftime("   --- %Y-%m-%d %H:%M ---\n"))

    print("PRESS 1. Print Current Stations")
    print("PRESS 2. Find Shortest Way")
    print("PRESS 3. Add Station Under Construction")
    print("PRESS 4. Remove Station Under Construction")
    print("PRESS 0. QUIT")

    choice = int(input("\nPlease select : "))
    if choice == 0:
        return
    elif choice < 1 or choice > 4:
        print("Please select from 1 to 5")
        greet_menu()
    else:
        if choice == 1:
            display_station_under_contruction(stations_under_construction)
            greet_menu()
        elif choice == 2:
            skyroute()
            greet_menu()
        elif choice == 3:
            add_station_under_construction(stations_under_construction)
            greet_menu()
        elif choice == 4:
            remove_station_under_construction(stations_under_construction)
            greet_menu

def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
    greet()
    new_route()
    goodbye()

def set_start_and_end(start_point, end_point):
    # handle setting the selected origin and destination points
    if start_point:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
        if change_point == "b":
            get_start()
            get_end()
        elif change_point == "o":
            get_start()
        elif change_point == "d":
            get_end()
        else:
            print("Oops, that isn't 'o', 'd', or 'b'...")
            set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()
    if start_point != end_point:
        return start_point, end_point
    else:
        print("Oops, Origin and destination are the same...")
        set_start_and_end(start_point, end_point)

def get_start():
    # request an origin from the user
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices.keys():
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_start()

def get_end():
    # request a destination from the user
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices.keys():
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_end()

def new_route(start_point = None, end_point = None):
    # get and set the origin and destination, call search to get the recommended route, search for another route
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    
    if shortest_route is not None:
        shortest_route_string = "\n".join(shortest_route)
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    else:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))

    again = input("Would you like to see another route? Enter y/n: ")
    if again == "y":
        show_landmarks()
        new_route(start_point, end_point)

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)
                if not possible_route:
                    return None
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)
    shortest_route = min(routes, key=len)
    return shortest_route

def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks == "y":
        print(landmark_string)

def goodbye():
    # Print Gooodbye
    print("Thanks for using SkyRoute!")

def get_active_stations():
    updated_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station]= set([])
    return updated_metro 

def display_station_under_contruction(stations_under_construction):
    i = 0   
    print("\nCURRENT STATIONS")
    metro_list=list(vc_metro.keys())
    for station in metro_list:
        print("{}. {}".format(i, station))
        i += 1
    print("\nCURRENT STATIONS UNDER CONSTRUCTION")
    print(stations_under_construction)
    return metro_list

def remove_station_under_construction(stations_under_construction):
    print("\nCurrent stations under construction :")
    i = 0
    for station_under_construction in stations_under_construction:
        print("{}. {}".format(i, station_under_construction))
        i += 1

    station_to_remove = int(input("\nPlease select the station to set as normal (0 to QUIT) : "))
    if station_to_remove == 0:
        return stations_under_construction
    elif (station_to_remove > 0) and (station_to_remove < len(stations_under_construction)-1):
        print("\nRemoving {} to Stations under construction.".format(station_to_remove))
        stations_under_construction.remove(stations_under_construction[station_to_remove])
        print("Station under construction : {}".format(stations_under_construction))
        return stations_under_construction
    else:
        print("Oops, please select a station under construction")
        remove_station_under_construction(stations_under_construction)

def add_station_under_construction(stations_under_construction):
    metro_list = display_station_under_contruction(stations_under_construction)
    index = input("Please select the station to set as under construction : ")
    index = int(index)

    if (index < 0) or (index > (len(metro_list)-1)):
        print("Index out of range, please select from 0 to {}.".format(len(metro_list)-1))
        add_station_under_construction(stations_under_construction)
    else:
        station_to_add = metro_list[index]
        if station_to_add not in stations_under_construction:
            print("\nAdding {} to Stations under construction.".format(station_to_add))
            stations_under_construction.append(station_to_add)
            print("Station under construction : {}".format(stations_under_construction))
        return stations_under_construction

greet_menu()
