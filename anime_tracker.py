anime_title = input("Как называется анимэ?\n")
anime_episodes_total = input("Сколько всего эпизодов?\n")
anime_episodes_watched = input("Сколько эпизодов просмотрено?\n")
anime_my_score = int(input("Какая оценка?\n"))
anime_genres_str = input("Какие жанры?(через запятую)\n")

print(
    f"Анимэ: {anime_title}, просмотрено: {anime_episodes_watched}/{anime_episodes_total}, моя оценка: {anime_my_score}, жанры: {anime_genres_str}")
