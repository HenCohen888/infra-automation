from src.models import VMInstance
from pydantic import ValidationError


def prompt_for_vm() -> dict:
 
    while True:
        print("\n--- Define a new VM ---")

        # 1. Get raw input from the user
        name = input("VM name (start with letter, letters/numbers/hyphens only, max 30 chars): ").strip()
        os = input("Operating system (e.g. ubuntu, centos, windows): ").strip()
        cpu_raw = input("CPU cores [1-16]: ").strip()
        ram_raw = input("RAM in GB [1-64]: ").strip()

        # 2. First, make sure CPU and RAM are integers
        try:
            cpu = int(cpu_raw)
            ram_gb = int(ram_raw)
        except ValueError:
            print("CPU and RAM must be whole numbers. Please try again.\n")
            continue 

        # 3. Use Pydantic to validate all fields together
        try:
            vm = VMInstance(
                name=name,
                os=os,
                cpu=cpu,
                ram_gb=ram_gb,
            )
        except ValidationError as e:
            print("Invalid VM configuration:")
            print(e)
            print("Please try again.\n")
            continue  # invalid -> ask again

        # 4. If everything is valid, return a plain dict
        print("\n VM accepted:", vm)
        return vm.dict()
