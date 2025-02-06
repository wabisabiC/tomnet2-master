from . import simulated_data_handler as sd

class DataManager:
    """
    Factory class that manages the creation of the data handler class
    depending on the parsed args human or simulation command. This will 
    handle the instantiated data handler
    """

    def handle_data(self, data_type): 
        if data_type == "human":
            return hd.HumanDataHandler()

        elif data_type == "simulation":
            return sd.SimulatedDataHandler()

