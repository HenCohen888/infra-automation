from pathlib import Path
import logging

from src.instance_io import load_instances, save_instances
from src.input_prompt import prompt_for_vm
from src.machine import Machine


def setup_logging() -> None:
    """Configure logging to write to logs/provisioning.log and console."""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "provisioning.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )

def main():

    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("=== Provisioning run started ===")
    print("=== DevOps Infra Provisioning Simulator ===")

    instances = load_instances()
    logger.info("Loaded %d existing instances.", len(instances))
    print(f"Loaded {len(instances)} existing instances.")

    vm = None

    while True:

        vm_dict = prompt_for_vm()

        try:
            vm = Machine(
                name=vm_dict["name"],
                os=vm_dict["os"],
                cpu=vm_dict["cpu"],
                ram_gb=vm_dict["ram_gb"],
            )
        except ValueError as e:
            logger.error("Validation error while creating Machine: %s", e)
            print(f"Error: {e}")
            # ask user again instead of crashing
            continue

        instances.append(vm.to_dict())
        logger.info("Added VM '%s' to instances list.", vm.name)

        another = input("add another VM? [y/N] :").strip().lower()
        if another not in ("y","yes"):
            break

    save_instances(instances)
    logger.info("Saved %d instances to configs/instances.json", len(instances))
    print(f"\nSaved {len(instances)} instances to configs/instances.json")

    if vm is not None:
        logger.info(
            "Attempting to install Nginx on last created machine '%s'.", vm.name
        )
        success = vm.install_nginx()

        if not success:
            logger.error("Nginx installation failed. Check logs for details.")
            print("Nginx installation failed. See logs/provisioning.log.")
        else:
            logger.info("Nginx installation succeeded.")
            print("Nginx installation succeeded.")

    logger.info("=== Provisioning run finished ===")

if __name__ == "__main__":
    main()