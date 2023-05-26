class Instrument:
    def play(self):
        pass


class Guitar(Instrument):
    def play(self):
        return "Playing the guitar."


class Piano(Instrument):
    def play(self):
        return "Playing the piano."


# Create instances of different instruments
instrument1 = Guitar()
instrument2 = Piano()

# Call the play method of different instruments
print(instrument1.play())  # Output: Playing the guitar.
print(instrument2.play())  # Output: Playing the piano.