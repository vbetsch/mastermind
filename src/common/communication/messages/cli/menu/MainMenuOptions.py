from src.common.communication.messages.cli.menu.MenuOption import MenuOption


class MainMenuOptions:
    CREATE_A_GAME = MenuOption("CREATE_A_GAME", "Create a game")
    SHOW_LEADERBOARD = MenuOption("LIST_SESSIONS", "Show games")
    CONTINUE_A_GAME = MenuOption("CONTINUE_A_GAME", "Continue a game")
    QUIT = MenuOption("QUIT", "Quit")

    @classmethod
    def all_options(cls):
        return [cls.CREATE_A_GAME, cls.SHOW_LEADERBOARD, cls.CONTINUE_A_GAME, cls.QUIT]
