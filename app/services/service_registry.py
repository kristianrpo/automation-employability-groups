from app.services.message_service import MessageService

class ServiceRegistry:
    """
    A class that represents a service registry.

    The service registry is responsible for registering and retrieving service instances based on their names.

    Attributes:
        _container (dict): A dictionary that stores the registered services.

    Methods:
        register_service: Registers a service instance with a given name.
        get_message_service: Retrieves a message service instance based on the platform.

    """

    def __init__(self):
        self._container = {}

    def register_service(self, service_name: str, service_instance: MessageService):
        """
        Registers a service instance with a given name.

        Args:
            service_name (str): The name of the service.
            service_instance (MessageService): The instance of the service.

        """
        self._container[service_name.lower()] = service_instance

    async def get_message_service(self, platform: str) -> MessageService:
        """
        Retrieves a message service instance based on the platform.

        Args:
            platform (str): The platform for which the message service is requested.

        Returns:
            MessageService: The instance of the message service.

        Raises:
            HTTPException: If the platform is not supported.

        """
        service = self._container.get(platform.lower(), None)
        if service is None:
            raise HTTPException(status_code=400, detail="Platform not supported")
        return service
