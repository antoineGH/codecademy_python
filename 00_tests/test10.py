### CLASS DECLARATION

class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return ("{}. \"{}\". {}, {}. {}, {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location))

class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        self.listings.remove(expired_listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection" 

    def sell_artwork(self, artwork, price):
        if self == artwork.owner:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != artwork:
            art_listing = None
            for list in veneer.listings:
                if artwork == list.art:
                    art_listing = list
            if art_listing != None:
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)
                
class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return ("{}, {}.".format(self.art.title, self.price))
        
### OBJECT INSTANTIATION
edytta = Client("Edytta Halpirt", None, False)
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)
veneer = Marketplace()
moma = Client("The MOMA", "New York", True)

### CALLS
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
print(veneer.show_listings())