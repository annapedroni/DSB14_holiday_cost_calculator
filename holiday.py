'''calculate the user's holiday cost, once they have chosen
- the destination (flight)
- the number of nights for the hotel
- the number of days they want to rent a car for'''

# check the user input, and output
# - the input as a valid city or an integer,
# - the value for the variable choice (quit or not)
# - error if invalid input
def check_input(user_input, desired_input_type):

    if user_input.lower() == "q":    
        return None, "q"
    
    elif desired_input_type == "integer":
        user_input = int(user_input)
        return user_input, ""
        
    else:
        user_input = user_input.strip().capitalize()
        if user_input in city_list:
            return user_input, "" 
        else:
            raise Exception

# calculate the cost: hotel, rental, holiday
# retrieve the flight cost
def hotel_cost(num_nights):
    return night_cost_by_city[city_flight] * num_nights

def plane_cost(city_flight):
    return flight_cost[city_flight]

def rental_cost(rental_days):
    return daily_vehicle_cost_by_city[city_flight][0] * rental_days

def holiday_cost(num_nights, city_flight, rental_days):
    hotel = hotel_cost(num_nights)
    flight = plane_cost(city_flight)
    vehicle = rental_cost(rental_days)
    return hotel + flight + vehicle





# available destination, flight cost, hotel cost per night, vehicle cost per day
city_list = ["Rome", "Milan", "Siena", "Naples", "Venice"]

flight_cost = {"Rome" : 150,
               "Milan" : 140,
               "Siena" : 160,
               "Naples" : 190,
               "Venice" : 150}

night_cost_by_city = {"Rome" : 120,
                      "Milan" : 130,
                      "Siena" : 110,
                      "Naples" : 100,
                      "Venice" : 130}

daily_vehicle_cost_by_city = {"Rome" : (20, "car"),
                      "Milan" : (25, "car"),
                      "Siena" : (17, "car"),
                      "Naples" : (19, "car"),
                      "Venice" : (50, "motorboat")}


# display greeting and instructions
print("\nHello! Are you thinking of a city break?")
print("Here are the options (prices in EUR):\n")

print("CITY\t\tFLIGHT\tHOTEL (1 night)\t\tVEHICLE (1 day/type)")
for city in city_list:
    print(f"{city}\t\t{flight_cost[city]}\t\t{night_cost_by_city[city]}\t\t{daily_vehicle_cost_by_city[city][0]}/{daily_vehicle_cost_by_city[city][1]}")

start_message = """\nTo calculate the cost of your holiday, enter
- the city you would like to visit,
- the number of night you would like to spend there,
- how many days you would like to rent a car for (N.B.: motorboat in Venice).
Let's begin!
('q' to quit the program)\n"""
print(start_message)

# get the user input and check it
choice = ""
city_flight = ""
num_nights = 0
rental_days = 0

while choice != "q":
    print("Available cities:")
    print(', '.join(city_list))       # https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
    city = input("City: ")

    try:
        city_flight, choice = check_input(city, "string")
        break
    except:
        print("Choose a city from the list, or 'q' to quit")


while choice != "q":
    nights = input("Number of nights: ")
    try:
        num_nights, choice = check_input(nights, "integer")
        break
    except:
        print("Please, enter a valid number")


while choice != "q":
    days = input("Number of days (vehicle): ")
    try:
        rental_days, choice = check_input(days, "integer")
        break
    except:
        print("Please, enter a valid number")


if choice != "q":
    result_message = f"""\nCOST OF YOUR HOLIDAY
- flight to {city_flight.upper()}:\t\t{plane_cost(city_flight)} EUR
- hotel stay ({num_nights} nights):\t{hotel_cost(num_nights)} EUR
- {daily_vehicle_cost_by_city[city_flight][1]} rental ({rental_days} day(s)):\t{rental_cost(rental_days)} EUR.
\n- TOTAL COST:\t\t\t{holiday_cost(num_nights, city_flight, rental_days)} EUR"""
    print(result_message)


print("\nGoodbye!\n")