from ps7_skeleton import *

nameAdopter = 'Joe'
nameCenter = 'APipo'
centerLocation = (0, 0)
slugLocation = (2.0, 0.0)
desired_species = 'Cat Dog Krokodile'
considered_spicies = ['Wombat', 'Panda']
allergic_species = ['Snake', 'Behemot']
species_types = {'Cat' : 3, 'Snake' : 1, 'Wombat' : 1, 'Behemot' : 2}
medicine_effecitiveness = {"Snake": 0.2, "Cat": 0.5, "Behemot" : 0.5}
adoption_center = AdoptionCenter(nameCenter, species_types, centerLocation)


#init list_of_adoption_centers
ad_cen1 = AdoptionCenter(nameCenter, species_types, centerLocation)
nameCenter2 = 'BPopo2'
nameCenter3 = 'CPupo3'
species_types2 = {'Cat' : 3, 'Wombat' : 1}
species_types3 = {'Cat' : 3, 'Wombat' : 1, 'Behemot' : 2}
centerLocation2 = (1.0, 1.0)
centerLocation3 = (2.0, 2.0)
ad_cen2 = AdoptionCenter(nameCenter2, species_types2, centerLocation2)
ad_cen3 = AdoptionCenter(nameCenter3, species_types3, centerLocation3)
list_of_adoption_centers = [ad_cen1, ad_cen2, ad_cen3]

#Adopters
ad = Adopter(nameAdopter, desired_species)
allergic = AllergicAdopter(nameAdopter, desired_species, allergic_species)
allergic.get_score(adoption_center)
med_allergic = MedicatedAllergicAdopter(nameAdopter, desired_species, 
                allergic_species, medicine_effecitiveness)
med_allergic.get_score(adoption_center)
slug_adopt = SluggishAdopter(nameAdopter, desired_species, slugLocation)

#SluggishAdopter

#print slug_adopt.get_linear_distance(centerLocation)
#print slug_adopt.get_score(adoption_center)

#Order of adoption centers
print get_ordered_adoption_center_list(ad, list_of_adoption_centers)
#print get_ordered_adoption_center_list(allergic, list_of_adoption_centers)
#print get_ordered_adoption_center_list(med_allergic, list_of_adoption_centers)
#print get_ordered_adoption_center_list(slug_adopt, list_of_adoption_centers)


    
    










