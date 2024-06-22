from abc import ABC, abstractmethod

class ServiceFactory(ABC):
    """
    Abstract base class for creating services.
    """

    @abstractmethod
    def create_service(self):
        pass
