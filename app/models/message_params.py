from pydantic import BaseModel

class MessageParams(BaseModel):
    """
    Represents the parameters for a message.

    Attributes:
        msg (str): The message content.
    """
    msg: str
