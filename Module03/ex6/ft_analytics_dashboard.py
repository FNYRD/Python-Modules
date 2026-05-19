#!/usr/bin/env python3
from advanced_data_helper import AdvancedDataHelper


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    data = AdvancedDataHelper()
    players: list[str] = [x for x in data.player_names][:6]
    scores: list[int] = [x for x in
                         data.generate_complex_scores()[:len(players)]]
    game_db: dict[str, int] = {players[i]: scores[i]
                               for i in range(len(players))}
    high_scores_players: list[str] = [x for x, y in game_db.items()
                                      if y > 1000]
    scores_doubled: list[int] = [x * 2 for x in scores]

    print(f"High scorers (>1200): {high_scores_players}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {players}")
    print("\n=== Dict Comprehension Examples ===")
    ranges_scores: dict = {
                            "high": len([h for h in scores
                                         if h > max(scores) * 0.6]),
                            "medium": len([m for m in scores
                                           if m > max(scores) * 0.4
                                           and m <= max(scores) * 0.6]),
                            "low": len([low for low in scores if
                                        low <= max(scores) * 0.4]),
                          }
    print(f"Player scores: {game_db}")
    print(f"Score categories: {ranges_scores}")
    achiev: list[dict] = [x for x in
                          data.generate_achievement_network().values()][:6]
    players_achievments: dict = {players[i]: len(achiev[i])
                                 for i in range(len(players))}
    print(f"Achievement counts: {players_achievments}")
    print("\n=== Set Comprehension Examples ===")
    unique_achievement: set = {achievement for dictionary in achiev
                               for achievement in dictionary}
    print(f"Unique achievements: {unique_achievement}")
    inv = data.generate_nested_inventory()
    all_items: set = {item for p in inv["players"].values()
                      for item in p["items"]}
    print(f"Unique items in inventories: {all_items}")
    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievement)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    top_list: list[str] = [x for x, y in game_db.items() if y == max(scores)]
    top_perfm: str = top_list[0]
    print(f"Top performer: {top_perfm} ({max(scores)} points, "
          f"{players_achievments[top_perfm]} achievements)")


if __name__ == "__main__":
    main()
