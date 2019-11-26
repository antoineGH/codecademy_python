#### CLASS DEFINITION

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        if is_museum:
            self.location = location
        else :
            self.location = "Private Collection"  
            
    def __str__(self):
        return "{}, {}.".format(self.name, self.location)

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != artwork:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork:
                    art_listing = listing
            if art_listing != None:
                art_listing.art.owner= self
                veneer.remove_listing(art_listing)

class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __str__(self):
        return "\nartist : {}\ntitle : {}\nyear: {}\nmedium: {}\nowner: {}\nlocation: {}\n".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

class MarketPlace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        self.listings.remove(expired_listing)

    def show_listings(self):
        for list in self.listings:
            print(list)

class Listing:
    def __init__(self, art, price, seller):
        self.art = art 
        self.price = price
        self.seller = seller

    def __str__(self):
        return "{}, {}.".format(self.art.title, self.price)

#### CLASS INSTANTIATION

veneer = MarketPlace()
edytta = Client("Edytta Halpirt", None, False)
moma = Client("The MOMA", "New York", True)
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

#### CALLS

edytta.sell_artwork(girl_with_mandolin, "2USD")
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
veneer.show_listings()
print(girl_with_mandolin)

