import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

logging.info("Hello from main.py (test log)")

from src.instance_io import load_instances, save_instances
from src.input_prompt import prompt_for_vm
from src.machine import Machine


def main():

    print("=== DevOps Infra Provisioning Simulator ===")

    instances = load_instances()
    print(f"Loaded {len(instances)} existing instances.")

    while True:

        vm_dict = prompt_for_vm()

        vm = Machine(
            name=vm_dict["name"],
            os=vm_dict["os"],
            cpu=vm_dict["cpu"],
            ram_gb=vm_dict["ram_gb"]
        )

        instances.append(vm.to_dict())

        another = input("add another VM? [y/N] :").strip().lower()
        if another not in ("y","yes"):
            break

    save_instances(instances)
    print(f"\nSaved {len(instances)} instances to configs/instances.json")

if __name__ == "__main__":
    main()