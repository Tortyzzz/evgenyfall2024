sea_fish = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

# combined_fish = sea_fish + freshwater_fish
# combined_fish.sort(key=str.upper)
print(sorted(sea_fish + freshwater_fish, key=str.lower))