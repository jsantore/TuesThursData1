top_games={"counter strike2": 1100,
           "DOTA2": 571,
           "PUBG:Battlegrounds":334,
           "Rust": 123,
           "Delta Force": 106,
           "Banana": 104,
           "Phantom Blade Zero":1700,
           "Stardew Valley": 81}

largest_so_far = "Rust"
for game in top_games.keys():
    current_player_count = top_games[game]
    max_players_so_far = top_games[largest_so_far]
    if current_player_count > max_players_so_far:
        largest_so_far = game
print(f"{largest_so_far} has the most players with {top_games[largest_so_far]}")
     #put your stuff here and remove pass
