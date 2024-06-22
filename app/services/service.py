from abc import ABC, abstractmethod

class Service(ABC):
    """
    Abstract base class for services.
    """

    def __init__(self, msg:str, params):
        self.msg = msg
        self.params = params

    @abstractmethod
    async def send_message(self):
        pass
