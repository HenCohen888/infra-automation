from pydantic import BaseModel, conint, constr


class VMInstance(BaseModel):
    """
    Represents a single VM definition with validation rules.
    """
    # VM name: must start with a letter, then letters/numbers/hyphens, max 30 chars
    name: constr(regex=r"^[A-Za-z][A-Za-z0-9\-]{0,29}$")

    # OS: free text for now
    os: str

    # CPU cores: integer between 1 and 16
    cpu: conint(ge=1, le=16)

    # RAM in GB: integer between 1 and 64
    ram_gb: conint(ge=1, le=64)
