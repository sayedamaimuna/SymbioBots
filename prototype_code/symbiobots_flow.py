# SymbioBots Communication Flow (Pseudo-code)
# Created by: Sayeda Maimuna Muna

# Define the main ecosystem components
class SeedSwarmDrone:
    def scan(self, area):
        print(f"Scanning area {area} for planting conditions...")

    def find_suitable_soil(self):
        # Example condition
        return True

    def plant_seed(self, area):
        print(f"Planting seeds in {area}...")

    def collect_data(self):
        return {"soil_moisture": 68, "temperature": 29, "CO2_level": 410}


class GuardianGroundBot:
    def check_moisture(self):
        print("Checking soil moisture levels...")

    def water_if_needed(self):
        print("Watering plants as required...")

    def send_status_to(self, biohub):
        biohub.receive_status("GroundBot status: healthy and active")


class BioHub:
    def __init__(self):
        self.database = []

    def store(self, data):
        self.database.append(data)
        print("Data stored in BioHub:", data)

    def receive_status(self, status):
        print("Received:", status)


# --- Simulation ---
drones = [SeedSwarmDrone() for _ in range(2)]
ground_bots = [GuardianGroundBot() for _ in range(2)]
biohub = BioHub()

for area in ["Zone A", "Zone B"]:
    for drone in drones:
        drone.scan(area)
        if drone.find_suitable_soil():
            drone.plant_seed(area)
            data = drone.collect_data()
            biohub.store(data)

for bot in ground_bots:
    bot.check_moisture()
    bot.water_if_needed()
    bot.send_status_to(biohub)
