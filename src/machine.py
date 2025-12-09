import logging



class Machine:

    def __init__(self, name: str, os: str, cpu: int, ram_gb: int):
        
        self.name = name
        self.os =  os
        self.cpu = cpu
        self.ram_gb = ram_gb

        logging.info(
            f"Created Machine(name={name}, os={os}, cpu={cpu}, ram_gb={ram_gb})"
        )


    def to_dict(self) -> dict:

        logging.info(
            f"Converting Machine '{self.name}' to dict"
            )

        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram_gb": self.ram_gb
        }

    
