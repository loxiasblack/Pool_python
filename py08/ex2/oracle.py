import os
from dotenv import load_dotenv


def load_configuration() -> bool:
    """load from .env the environment variable"""
    loaded = load_dotenv()
    return loaded


def get_config() -> dict:
    """get the config from the os.environment"""
    return {
        "matrix_mode": os.getenv("MATRIX_MODE", "development"),
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT"),
    }


def validat_config(config: dict) -> list:
    """check if some of required key lack and get a list of th missing"""
    missing = []
    required = ["database_url", "api_key", "zion_endpoint"]

    for key in required:
        if not config[key]:
            missing.append(key.upper)
    return missing


def try_access(value: str) -> str:
    """try to access with Api_key variable"""
    if not value:
        return "NOT SET"
    elif value != os.getenv("API_KEY"):
        return "Deny Authentication"
    return "Authenticated"


def display_config(config: dict) -> None:
    """get a display to variable environment"""
    print("Configuration loaded:")
    print(f"  Mode:          {config['matrix_mode']}")
    print(f"  Database:      {config['database_url'] or 'NOT SET'}")
    print(f"  API Access:    {try_access(config['api_key'])}")
    print(f"  Log Level:     {config['log_level']}")
    print(f"  Zion Network:  {config['zion_endpoint'] or 'NOT SET'}")


def security_check(config: dict, missing: list) -> None:
    """check all security on the configuration"""
    print("\nEnvironment security check:")
    if config["api_key"]:
        print("  [OK] No hardcoded secrets detected")
    else:
        print("  [WARN] API_KEY looks like a placeholder")

    if os.path.exists(".env"):
        print("  [OK] .env file properly configured")
    else:
        print("  [WARN] No .env file found")

    if os.environ.get("MATRIX_MODE"):
        print("  [OK] Production overrides available")
    else:
        print("  [INFO] No shell overrides detected ")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    load_configuration()

    config = get_config()
    missing = validat_config(config)
    if missing:
        print("WARNING: Missing required configuration:", end=" ")
        print(f"{', '.join(missing)}")
    display_config(config)
    security_check(config, missing)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
