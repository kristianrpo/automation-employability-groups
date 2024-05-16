from app.services.message_service import MessageService

class ServiceRegistry:
    def __init__(self):
        self._container = {}

    def register_service(self, service_name: str, service_instance: MessageService):
        self._container[service_name.lower()] = service_instance

    def get_service(self, service_name: str) -> MessageService:
        return self._container.get(service_name.lower(), None)
