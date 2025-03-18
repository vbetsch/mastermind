from src.app.controllers.MainMenuController import MainMenuController
from src.common.communication.Mediator import Mediator
from src.ui.cli.CLIController import CLIController


def inject() -> CLIController:
    mediator: Mediator = Mediator()
    cli: CLIController = CLIController(mediator)
    main_menu: MainMenuController = MainMenuController(mediator)
    return cli


def run():
    cli: CLIController = inject()
    cli.welcome()
    cli.main_menu()

if __name__ == '__main__':
    run()
