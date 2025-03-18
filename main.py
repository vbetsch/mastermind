from src.view.cli.CLIController import CLIController


def run():
    cli: CLIController = CLIController()
    cli.welcome()
    cli.main_menu()

if __name__ == '__main__':
    run()
