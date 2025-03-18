from src.libs.options.values.MenuOption import MenuOption


class MainMenuOptionsList:
    CREATE_A_GAME = MenuOption("CREATE_A_GAME", "Create a game")
    CONTINUE_A_GAME = MenuOption("CONTINUE_A_GAME", "Continue a game")
    SHOW_LEADERBOARD = MenuOption("SHOW_LEADERBOARD", "Show leaderboard")
    QUIT = MenuOption("QUIT", "Quit")

    @classmethod
    def all_options(cls):
        return [cls.CREATE_A_GAME, cls.CONTINUE_A_GAME, cls.SHOW_LEADERBOARD, cls.QUIT]
