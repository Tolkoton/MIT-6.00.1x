# -*- coding: utf-8 -*-
import random 
import string
import math
import operator

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location
    
    def get_number_of_species(self, animal):
        return self.species_types[animal]
         
    def get_location(self):
        float_location = ()
        
        for i in self.location:
            float_location += (float(i), )
            
        return float_location
        
    
    def get_species_count(self):
        species_count = self.species_types.copy()
        del_species = []
        
        for species in species_count:
            if species_count[species] == 0:
                del_species.append(species)
        
        for species in del_species:       
            del species_count[species]                        
        
        return species_count
   
    def get_name(self):
        return self.name
        
    def adopt_pet(self, species):
        if self.species_types > 0:
            self.species_types[species] -= 1
        
        


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
        
         
    def get_name(self):
        return self.name
         
    def get_desired_species(self):
        return self.desired_species
        
    def get_score(self, adoption_center):
        desired_list = []
        score = 0
        
        desired_list = self.desired_species.split()
        for i in desired_list:
            if i in adoption_center.species_types:
                score += adoption_center.species_types[i]
               
        return float(score)



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        self.name = name
        self.desired_species = desired_species
        self. considered_species = considered_species
        
    def get_score(self, adoption_center):
        num_other = 0
        ad = Adopter(self.name, self.desired_species)
        adopter_score = ad.get_score(adoption_center)
        
        for i in self.considered_species:
            if i in adoption_center.species_types:
                num_other += adoption_center.species_types[i]
        
        score = adopter_score + 0.3 * num_other              
        return float(score)

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        self.name = name
        self.desired_species = desired_species
        self.feared_species = feared_species

    def get_score(self, adoption_center):
       # num_other = 0
        num_feared = 0
        ad = Adopter(self.name, self.desired_species)
        adopter_score = ad.get_score(adoption_center)
        
        feared_list = self.feared_species.split()
        
        for i in feared_list:
            if i in adoption_center.species_types:
                num_feared += adoption_center.species_types[i]
        
        score = adopter_score - 0.3 * num_feared              
        
        if score < 0:
            score = 0
            
        return float(score)

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species
        
    def get_score(self, adoption_center):
        score = 0.0
        
        #if allergic species present - return 0
        for i in self.allergic_species:
            if i in adoption_center.species_types:
                score = 0.0
                return score
        
        ad = Adopter(self.name, self.desired_species)
        score = ad.get_score(adoption_center)
        return score
        
class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species
        self.medicine_effectiveness = medicine_effectiveness
    
    def get_score(self, adoption_center):
        score = 0.0
        mult = 1
        
         #get smallest allergy resisistance       
        
        for i in self.allergic_species:
            if i in adoption_center.species_types:
                if i in self.medicine_effectiveness.keys():
                    if self.medicine_effectiveness[i] < mult:
                        mult = self.medicine_effectiveness[i]
                else:
                    mult = 0
     
        '''           
        #find out if there allergic species in adoption center
        for i in self.allergic_species:
            if i in adoption_center.species_types:
                mult = 0
         '''
          
        #Adoption center score
        ad = Adopter(self.name, self.desired_species)
        score = ad.get_score(adoption_center)
        score *= mult
        return score
    



class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, location):
        self.name = name
        self.desired_species = desired_species
        self.location = location
        
    def get_score(self, adoption_center):
        score = 0
        to_location = adoption_center.get_location()        
        distance = self.get_linear_distance(to_location)
        #print 'distance =', distance 
        
        ad = Adopter(self.name, self.desired_species)
        the_number_of_desired_species = ad.get_score(adoption_center) 
        #print 'the_number_of_desired_species', the_number_of_desired_species
        
        if distance < 1:
            score = the_number_of_desired_species
        elif distance >= 1 and distance < 3:
            score = the_number_of_desired_species * random.uniform(0.7, 0.9)
        elif distance >= 3 and distance < 5:
            score = the_number_of_desired_species * random.uniform(0.5, 0.7)
        elif distance >= 5:
            score = the_number_of_desired_species * random.uniform(0.1, 0.5)
            
        
        return score
        
    def get_linear_distance(self, to_location):
        distance = 0
        distance = math.sqrt((self.location[0] - to_location[0])**2 + (self.location[1] - to_location[1])**2)
        return distance
        
    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    
    adoption_centers_dic = {}
    adoption_centers_list_with_scores = []
    score_list = []
    adoption_centers_sorted = []
    score = 0
    adoption_center = ''
    index = 0
    
    
    #Додати adoption center score в score_list i unsorted_centers
    for center in list_of_adoption_centers:
        score = adopter.get_score(center)
        score_list.append(score)
        adoption_centers_dic[center] = score
        
    #sorting
    adoption_centers_list_with_scores = adoption_centers_dic.items()
    #adoption_centers_list_with_scores = sorted(adoption_centers_list_with_scores, key = lambda x: x[0].get_name(), reverse = True)
    adoption_centers_list_with_scores.sort(key = lambda tup: tup[1])
    adoption_centers_list_with_scores.reverse()
    
    
    #print adoption_centers_list_with_scores
   
    adoption_centers_sorted = [i[0] for i in adoption_centers_list_with_scores]
    #print adoption_centers_sorted  
            
    return adoption_centers_sorted       

    

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    score = 0
    score_list = []
    adopters_dic = {}
    ordered_adopters_list = []
    final_list = []
    
    if len(list_of_adopters) < n:
        n = len(list_of_adopters)
    
    
    for i in range(n):
        score = list_of_adopters[i].get_score(adoption_center)
        score_list.append(score)
        adopters_dic[list_of_adopters[i]] = score
        
    #sorting
    ordered_adopters_list = adopters_dic.items()
    ordered_adopters_list = sorted(ordered_adopters_list, key = lambda x: x[0].get_name(), reverse = True)
    ordered_adopters_list.sort(key = lambda score: score[1])
    ordered_adopters_list.reverse()
    
    final_list = [i[0] for i in ordered_adopters_list]
   
    return final_list
    
    
    
    
    #test
    
rand = 0
adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": random.random()})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": random.randint(20, 50), "Dog": random.randint(1, 10)}, (-2,10))

print get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)



    