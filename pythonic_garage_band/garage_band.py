from abc import ABC, ABCMeta, abstractmethod

###########################################    
class Band(ABC):
    bands = []
    def __init__(self, name, members = []):
        self.name = name
        self.members = members
        Band.bands.append(self)
        print(Band.bands)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return(solos)

    @classmethod            
    def to_list(cls):
        return (cls.bands)

    def __repr__(self):
        return (f"{self.name}")

    def __str__(self):
        return (f"{self.name}")

###########################################    
class Musician:
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        return self.instrument

    @abstractmethod
    def play_solo(self):
        pass  

    def __repr__(self):
        if (self.instrument).lower() == "guitar":
            class_name = "Guitarist"
        elif (self.instrument).lower() == "bass":
            class_name = "Bassist"
        elif (self.instrument).lower() == "drums":
            class_name = "Drummer"
        return (f"{class_name} instance. Name = {self.name}")

    def __str__(self):
        return (f"My name is {self.name} and I play {(self.instrument)}")

###########################################    
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = "guitar"

    def play_solo(self):
        return("face melting guitar solo")
    
###########################################    
class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = "bass"
    
    def play_solo(self):
        return("bom bom buh bom")
    
###########################################    
class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = "drums"

    def play_solo(self):
        return("rattle boom crash")

###########################################    
###########################################    
if __name__ == "__main__":
    my_band = Band("Blue", ["mark", "john", "oliver"])
    your_band = Band("Back", ["mark", "john", "oliver"])

