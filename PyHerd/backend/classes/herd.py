
class Cattle:
    def __init__(self, id_cow : str, weight : float, sex : str, race : str, name="None"):
        self._id_cow = id_cow
        self._weight = weight
        self._sex = sex
        self._race = race
        self._name = name
        self._issue = "None"
    
    def newName(self, name : str):
        self._name = name

    def cattleIllness(self, ilnessName : str):
        self._issue = ilnessName
    
    def cattlecured(self):
        self._issue = "None"
    
    def status(self):
        return f"""ID: {self._id_cow} | Name: {self._name} | Sex: {self._sex} | Race: {self._race} | Sickness: {self._issue}"""

class CattleHerd:
    def __init__(self, owner : str, animal_type : str):
        self._owner = owner
        self._animal_type = animal_type
        self._herd = []
    
    def newOwner(self, new_owner : str):
        self._owner = new_owner
    
    def findCattle(self, cattle_id : int):
        for cattle in self._herd:
            if cattle["ID"] == cattle_id:
                return cattle["Animal"]
    
    def addCattle(self, cattle : Cattle):
        self._herd.insert({
            "Animal" : cattle,
            "ID" : len(self._herd)
            })
    
    def removeCattle(self, cattle_id : int):
        cattle = self.findCattle(cattle_id)
        self._herd.remove(cattle)
        limit = len(self._herd)
        for i in range(0, limit):
            self._herd[i]["ID"] = i+1
        return cattle
        
    def herdStatus(self):
        cattle_info = ""
        for cattle in self._herd:
            cattle_info += f'{cattle["ID"]}:{cattle["Animal"].status()} \n'

        resp = f"""
Herd status
Animal Type = {self._animal_type}
Owner = {self._owner}
Cattle Info:
{cattle_info}
        """
        return resp

class HerdManager:
    

    def __init__(self, location : str):
        self._location = location
        self._herds = []
        self.animal_types = [
            "Bovinos",
            "Equinos",
            "Suínos",
            "Ovinos",
            "Caprinos"
            ]
        
    def locHerd(self, id_herd : int):
        for herd in self._herds:
            if herd["ID"] == id_herd:
                return herd["Herd"]
    
    def newHerd(self):
        print("Digite o nome do dono do rebanho.")
        owner = str(input("=>> "))
        print("""
              Digite um número:
              \n1: Bovinos (Boi, Vaca, Touro)
              \n2: Equinos (Cavalo, Burro, Mula, Zebra)
              \n3: Suínos (Porco, Javali)
              \n4: Ovinos (Carneiro, Ovelha)
              \n5: Caprinos (Bode, Cabra)
              """
        )
        choice = int(input("=>> "))
        animal_type = self.animal_types[choice - 1]
        add_herd = {
            "Herd":CattleHerd(owner, animal_type),
            "ID": len(self._herds) + 1,
        }
        print(f"Note the ID!\n{add_herd}")
        self._herds.insert(add_herd)
    
    def cattleTranf(self, id_cattle : int, id_origin_herd : int, id_destination_herd : int):
        origin = self.locHerd(id_origin_herd)
        destination = self.locHerd(id_destination_herd)
        cattle = origin.removeCattle(id_cattle)
        destination.addCattle(cattle)

    def cattleDead(self, id_cattle : int, id_origin_herd : int):
        origin = self.locHerd(id_origin_herd)
        cattle = origin.removeCattle(id_cattle)
        cattle["Animal"].cattleIllness("Dead")
        print(f'RIP, {cattle["Animal"].status()}')


