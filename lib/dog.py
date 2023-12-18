#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed
        name_check = (isinstance(name, str) and not (len(name) < 1 or len(name) > 25))
        breed_check = breed in APPROVED_BREEDS

        if (self.name=="" or not name_check) and self.breed=="":
            print("Name must be string between 1 and 25 characters.")
        elif (not breed_check) and (self.name==""):
            print('Breed must be in list of approved breeds.')
        else:
            pass




#     def get_name(self):
#         return self._name

#     def set_name(self, name):
#         name_check = (isinstance(name, str) and not (len(name) < 1 or len(name) > 25))
#         # print(isinstance(name, str))
#         # print(len(name) < 1) 
#         # print(len(name) > 25)
#         if name_check:
#             self._name = name
#         else:
#             print("Name must be string between 1 and 25 characters.")
   

#     name = property(get_name, set_name)

#     def get_breed(self):
#         return self._breed

#     def set_breed(self, breed):
#         # print(breed in APPROVED_BREEDS)
#         breed_check = breed in APPROVED_BREEDS
#         # name_check = (isinstance(self.name, str) and not (len(self.name) < 1 or len(self.name) > 25))
#         if breed_check:
#             self._breed = breed
#         # elif name_check:
#         #     pass
#         elif False:
#             print('Breed must be in list of approved breeds.')
#         else:
#             pass

#     breed = property(get_breed, set_breed)


# # fido = Dog(name="Fido", breed="dog")
# # print(fido.name)
# # print(fido.breed)