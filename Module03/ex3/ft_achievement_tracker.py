#!/usr/bin/env python3
def main() -> None:
    print("=== Achievement Tracker System ===\n")
    index: int = 0
    alice: set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob: set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set = {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}
    names: list[str] = ["alice", "bob", "charlie"]
    players: list[set] = [alice, bob, charlie]
    for player in players:
        print(f"Player {names[index]} achievements: {player}")
        index += 1
    print("\n=== Achievement Analytics ===")
    shared: set[str] = alice.union(bob.union(charlie))
    unique: set[str] = alice.intersection(bob.intersection(charlie))
    wrd: set[str] = set()
    wrd = alice.difference(bob, charlie).union(bob.difference(alice, charlie),
                                               charlie.difference(alice, bob))
    print(f"All unique achievements: {shared}")
    print("Total unique achievements:", end=" ")
    print(len(shared))
    print(f"\nCommon to all players: {unique}")
    rarest_player: int = 0
    player_name: str = ""
    index = 0
    for player in players:
        for weird in wrd:
            if weird in player and player_name != names[index]:
                rarest_player += 1
                player_name = names[index]
    print(f"Rare achievements ({rarest_player} player): {wrd}")
    alice_and_bob: set = alice.intersection(bob)
    alice_unique: set = alice.difference(bob)
    bob_unique: set = bob.difference(alice)
    print(f"Alice vs Bob common: {alice_and_bob}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
