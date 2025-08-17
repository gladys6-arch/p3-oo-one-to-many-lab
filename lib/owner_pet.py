class Pet:

    PET_TYPES= ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type '{pet_type}'.Allowed types: {Pet.PET_TYPES}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        owner_name = self.owner.name if self.owner else "None"
        return f"Pet(name={self.name}, pet_type={self.pet_type}, owner={owner_name})"
    

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError(f"Expected Pet instance, got {type(pet).__name__}")
        pet.owner = self

    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    


pet = Pet("Fido", "dog",)
owner = Owner("Jim")