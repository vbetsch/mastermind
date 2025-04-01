from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase


class GetOrCreatePlayer(IPlayerUseCase):
    def execute(self, arg=None):
        print("Getting or creating player")
