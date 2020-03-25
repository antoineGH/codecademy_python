### FUNCTIONS

def rectangle_surface(width, length):
     rectangle_surface = (width * length)
     return rectangle_surface

def price_surface(price_tile, surface):
    price_surface = (price_tile * surface)
    return price_surface
    
def calculate_surface_price(width, length, price_tile):
        surface = rectangle_surface(width, length)
        price = price_surface(price_tile, surface)
        return surface, price

### CALLS

width = input("Rectangle width: ")
length = input("Rectangle length: ")
price_tile = input("Price per tile: ")
surface_price = calculate_surface_price(int(width), int(length), int(price_tile))
surface = surface_price[0]
price = surface_price[1]

print("Rectangle of {}x{} needs {} tiles : {}RMB ({}RMB/tile)".format(width, length, surface, price, price_tile))