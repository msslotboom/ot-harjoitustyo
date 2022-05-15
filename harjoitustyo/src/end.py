import highscores.highscore_handler

class EndMenu:
    def __init__(self, level, name, score) -> None:
        handler = highscores.highscore_handler.Highscores(level)
        handler.add_score(name,score)
        topscores = handler.find_top(10)
        for row in topscores:
            print(row["name"], row["score"])
       