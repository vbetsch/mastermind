from src.common.communication.events.cli.menu.MenuOption import MenuOption


class MainMenuOptions:
    CREATE_A_SESSION = MenuOption("CREATE_A_SESSION", "Create a game")
    SHOW_SESSIONS = MenuOption("LIST_SESSIONS", "Show games")
    CONTINUE_A_SESSION = MenuOption("CONTINUE_A_SESSION", "Continue a game")
    QUIT = MenuOption("QUIT", "Quit")

    @classmethod
    def all_options(cls):
        return [cls.CREATE_A_SESSION, cls.SHOW_SESSIONS, cls.CONTINUE_A_SESSION, cls.QUIT]
