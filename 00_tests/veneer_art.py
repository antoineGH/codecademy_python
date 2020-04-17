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
        for list in self.listings:
            print(list)

class Client:
    def __init__(self, name, location, is_museum, wallet):
        self.name = name
        self.wallet = wallet
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def __repr__(self):
        return ("{}, {}, Wallet: {}$.".format(self.name, self.location, self.wallet))

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_list = Listing(artwork, price, self)
            veneer.add_listing(new_list)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                art_listing = listing
            if art_listing != None:          
                self.wallet -= art_listing.price
                art_listing.art.owner.wallet += art_listing.price
                print("{} buy \"{}\" for {}$.".format(self.name, artwork.title, art_listing.price))
                print("{} credited of {}$, Total wallet {}$.".format(art_listing.art.owner.name, art_listing.price, art_listing.art.owner.wallet))
                print("{} debited of {}$, Total wallet {}$.".format(self.name, art_listing.price, self.wallet))
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)

    def add_wishlist(self, artwork, price):
        if artwork.owner != self:
            wish_list = Listing(artwork, price, self)
            wishlist.add_listing(wish_list)
            print("{} add \"{}\" to wishlist.".format(self.name, artwork.title))

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return ("{}, on sale for {}$.".format(self.art.title, self.price))

# Instantiate Marketplace
veneer = Marketplace()
wishlist = Marketplace()

# Instantiate Client
edytta = Client("Edytta Halpirt", None, False, 1000)
moma = Client("The MOMA", "New York", True, 5000)

print("-- Clients ---")
print(edytta)
print(moma)

# Instantiate Artwork
girl_with_mandolin = Art("Picasso, Pablo","Girl with a Mandolin (Fanny Tellier)", 1910,"oil on canva", edytta)
look = Art("Sebastien Tellier","Look", 1939,"oil on canva", edytta)
print("\n--- Artworks ---")
print(girl_with_mandolin)

# On sales
edytta.sell_artwork(girl_with_mandolin, 1000)
print("\n--- On Sales ---")
veneer.show_listings()

# Transactions
print("\n---Transactions ---")
moma.buy_artwork(girl_with_mandolin)

print("\n---Add To Wishlist ---")
edytta.add_wishlist(girl_with_mandolin, 0)
moma.add_wishlist(look, 0)

print("\n---All Wishlists ---")
wishlist.show_listings()