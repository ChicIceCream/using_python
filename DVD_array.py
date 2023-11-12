class DVD:
    def __init__(self, name, release_year, director):
        self.name = name
        self.release_year = release_year
        self.director = director

    def __str__(self):
        return f"{self.name}, directed by {self.director}, released in {self.release_year}"

# Create instances of the DVD class
incredibles_dvd = DVD("The Incredibles", 2004, "Brad Bird")
finding_dory_dvd = DVD("Finding Dory", 2016, "Andrew Stanton")
lion_king_dvd = DVD("The Lion King", 2019, "Jon Favreau")

# Create a list with 15 None values
dvd_collection = [None] * 15

# Create DVD instances
incredibles_dvd = DVD("The Incredibles", 2004, "Brad Bird")
finding_dory_dvd = DVD("Finding Dory", 2016, "Andrew Stanton")
lion_king_dvd = DVD("The Lion King", 2019, "Jon Favreau")

# Add DVDs to specific positions in the collection
dvd_collection[3] = incredibles_dvd  # "The Incredibles" at index 3
dvd_collection[9] = finding_dory_dvd  # "Finding Dory" at index 9
dvd_collection[2] = lion_king_dvd     # "The Lion King" at index 2

# Print DVDs in the collection
for dvd in dvd_collection:
    if dvd is not None:
        print(dvd)
