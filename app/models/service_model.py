from pydantic import BaseModel

class ServiceModel(BaseModel):
    """
    Represents a service model.

    Attributes:
        msg (str): The message associated with the service model.
    """
    msg: str
    