#!/usr/bin/env python3

from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation import philosophers_stone, elixir_of_life
import alchemy


def main() -> None:
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}\n")

    print("Testing Relative Imports (from advanced.py):")
    print(f"philisophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}\n")

    print("Testing Package Access:")
    result_type = alchemy.transmutation.lead_to_gold()
    print(
        f"alchemy.transmutation.lean_to_gold(): {result_type}"
    )
    result_type = alchemy.transmutation.philosophers_stone()
    print(
        f"alchemy.transmutation.philosophers_stone(): {result_type}\n"
    )
    print("Both pathways work! Absolute: clear, Realtive: concise")


if __name__ == "__main__":
    main()
