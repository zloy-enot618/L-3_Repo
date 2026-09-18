def show_games():
    print("=== Каталог настольных игр ===")
    for number, game in enumerate(games, start=1):
        print("")