from src.view.cli.CLI import CLI


def run():
    cli = CLI()
    cli.welcome()
    cli.show_main_menu()

if __name__ == '__main__':
    run()
