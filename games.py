import time
def show_games(games):
    print("=== Каталог настольных игр ===")
    for number, game in enumerate(games, start=1):
        print(f"{number}. Название: {game['name']}\n[!] Жанр: {game['genre']}\n")

        time.sleep(0.3)