import alchemy


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    result_type = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {result_type}")
    result_type = alchemy.elements.create_water()
    print(f"alchemy.elements.create_water(): {result_type}")
    result_type = alchemy.elements.create_earth()
    print(f"alchemy.elements.create_earth(): {result_type}")
    result_type = alchemy.elements.create_air()
    print(f"alchemy.elements.create_air(): {result_type}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        alchemy.create_earth()
    except AttributeError as e:
        print(f"alchemy.create_earth(): {e.__class__.__name__} - not exposed")
    try:
        alchemy.create_air()
    except AttributeError as e:
        print(f"alchemy.create_air(): {e.__class__.__name__} - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
