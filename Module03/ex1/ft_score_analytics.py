#!/usr/bin/env python3
import sys


def main() -> None:
    scores: list[int] = []
    for arg in sys.argv:
        if arg == sys.argv[0]:
            pass
        else:
            try:
                scores.append(int(arg))
            except ValueError:
                print(f"OOPS! you write {arg} as a number,"
                      " did you go to school? ")
    if len(scores) >= 1:
        print("=== Player Score Analytics ===")
        print("_____  _____ ____  _____  ______  _____\n"
              "/ ____|/ ____/ __ \\|  __ \\|  ____|/ ____|\n"
              "| (___ | |   | |  | | |__) | |__  | (___ \n"
              "\\___ \\| |   | |  | |  _  /|  __|  \\___ \\\n"
              "____) | |___| |__| | | \\ \\| |____ ____) |\n"
              "|_____/ \\_____\\____/|_|  \\_\\______|_____/ ")
        print("\n_____  _____ ____  _____  ______  _____\n")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
