from app.services.service import Service

class ActiveServices:
    """
    A class representing active services.

    This class is responsible for managing and providing access to active services.
    """

    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._container = {}

    def register_factory_service(self, service_name: str, service_instance: Service):
        """
        Register a service.

        Args:
            service_name (str): The name of the service.
            service_instance (Service): An instance of the service.

        """
        self._container[service_name.lower()] = service_instance

    async def get_factory_service(self, platform: str):
        """
        Get a factory service.

        Args:
            platform (str): The platform for which the service is requested.

        Returns:
            Service: An instance of the requested service.

        Raises:
            HTTPException: If the platform is not supported.

        """
        service = self._container.get(platform.lower(), None)
        if service is None:
            raise HTTPException(status_code=400, detail="Platform not supported")
        return service
    