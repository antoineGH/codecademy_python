# Functions

def ground_shipping(weight):
  if weight <= 2:
    cost = (weight * 1.5) + 20
  elif weight <= 6:
      cost = (weight * 3) + 20
  elif weight <= 10:
      cost = (weight * 4) + 20
  else :
      cost = (weight * 4.75) + 20
  return cost

def drone_shipping(weight):
    if weight <= 2:
        cost = weight * 4.5
    elif weight <= 6:
        cost = weight * 9
    elif weight <= 10:
        cost = weight * 10
    else :
        cost = weight * 14.25
    return cost
      
def compare_shipping(weight):
    cost_ground = ground_shipping(weight)
    cost_drone = drone_shipping(weight)

    if (cost_ground < cost_drone) and (cost_ground < cost_premium):
        print("The cheapest method if ground shipping")
        return cost_ground
    elif (cost_drone < cost_ground) and (cost_drone < cost_premium):
        print("The cheapest method if drone shipping")
        return cost_drone
    else:
        print("The cheapest method if premium shipping")
        return cost_premium

# Variables 

cost_premium = 125

# Calls
weight = float(input("Please enter package weight: "))
cost = ground_shipping(8.4)
cost = drone_shipping(1.5)
cheaper = compare_shipping(weight)
print("Total Price : "+ str(cheaper)+".")
