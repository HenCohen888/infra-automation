import logging
import subprocess
from pathlib import Path


class Machine:

    def __init__(self, name: str, os: str, cpu: int, ram_gb: int):
        
        if not name or len(name.strip()) == 0:
            raise ValueError("Machine name cannot be empty.")

        if cpu <= 0:
            raise ValueError("CPU must be greater than 0.")

        if ram_gb <= 0:
            raise ValueError("RAM must be greater than 0.")

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

    def install_nginx(self) -> bool:
        """
        Run scripts/install_nginx.sh using subprocess.
        Returns True on success, False on failure.
        """

        logging.info(f"Starting Nginx installation on machine '{self.name}'")

        # src/machine.py -> src/ -> project root
        project_root = Path(__file__).resolve().parents[1]
        script_path = project_root / "scripts" / "install_nginx.sh"

        logging.debug(f"Resolved install_nginx.sh path: {script_path}")

        if not script_path.is_file():
            logging.error(f"install_nginx.sh not found at {script_path}")
            return False

        try:
            result = subprocess.run(
                [str(script_path)],
                check=True,              # raise CalledProcessError if exit code != 0
                capture_output=True,
                text=True,
            )

            if result.stdout:
                logging.info("install_nginx.sh stdout:\n%s", result.stdout.strip())
            if result.stderr:
                # stderr may contain warnings, not always fatal
                logging.warning("install_nginx.sh stderr:\n%s", result.stderr.strip())

            logging.info("Nginx installation completed successfully.")
            return True

        except FileNotFoundError:
            logging.exception(
                f"Failed to execute install_nginx.sh (not found or not executable): {script_path}"
            )
            return False

        except subprocess.CalledProcessError as e:
            logging.error(
                "install_nginx.sh failed with exit code %s", e.returncode
            )
            if e.stdout:
                logging.error("Script stdout:\n%s", e.stdout.strip())
            if e.stderr:
                logging.error("Script stderr:\n%s", e.stderr.strip())
            return False

        except Exception:
            logging.exception("Unexpected error while running install_nginx.sh")
            return False
    
