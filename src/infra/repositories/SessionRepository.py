from src.app.ports.IRepository import IRepository


class SessionRepository(IRepository):
    def create(self):
        print("Creating a new session...")
