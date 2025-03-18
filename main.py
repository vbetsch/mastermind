from src.app.controllers.MainMenuController import MainMenuController
from src.libs.communication.Mediator import Mediator
from src.ui.cli.CLIController import CLIController


def run():
    mediator: Mediator = Mediator()
    cli: CLIController = CLIController(mediator)
    main_menu: MainMenuController = MainMenuController(mediator)
    cli.welcome()
    cli.main_menu()

if __name__ == '__main__':
    run()
