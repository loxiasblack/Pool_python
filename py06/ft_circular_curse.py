from alchemy.grimoire import validate_ingredients, record_spell


def main():
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    result_type = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {result_type}')
    result_type = validate_ingredients("dragon scales")
    print(
        f'validate_ingredients("dragon scales"): {result_type}\n'
    )
    print("Testing spell recording with validation:")
    result_type = record_spell("Fireball", "fire air")
    print(
        f'record_spell("Fireball", "fire air"): {result_type}'
    )
    result_type = record_spell("Dark Magic", "shadow")
    print(
        f'record_spell("Dark Magic", "shadow"): {result_type}\n'
    )
    print("Testing late import technique:")
    record_type = record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {record_type}\n')
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
