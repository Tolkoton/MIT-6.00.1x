from ps7_skeleton import *

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
print get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])
print get_ordered_adoption_center_list(adopter5, [ac,ac2,ac3,ac4,ac5,ac6])                            
print get_ordered_adoption_center_list(adopter6, [ac,ac2,ac3,ac4,ac5,ac6])                            
                            
# you can print the name and score of each item in the list returned
