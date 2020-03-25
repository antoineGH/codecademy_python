### CLASS DECLARATION

class Art:
    def __init__(self, artist, title, medium, year):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year

    def __repr__(self):
        return ("{}. \"{}\". {}, {}.".format(self.artist, self.title, self.year, self.medium))

### OBJECT INSTANTIATION

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas")
print(girl_with_mandolin)
