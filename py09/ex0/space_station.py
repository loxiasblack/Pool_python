from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": "6",
        "power_level": "85.5",
        "oxygen_level": "92.3",
        "last_maintenance": "2025-01-25",
        "is_operational": "True",
    }
    space_station = SpaceStation(**data)
    print(f"ID: {space_station.station_id}")
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size} peolple")
    print(f"Power: {space_station.power_level}")
    print(f"Oxygen: {space_station.oxygen_level}")
    operation = (
        "Operational" if space_station.is_operational else "not Operational"
    )
    print(f"Status: {operation}")
    print("========================================")
    try:
        data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": "21",
            "power_level": "85.5",
            "oxygen_level": "92.3",
            "last_maintenance": "2025-01-25",
            "is_operational": "True",
        }
        space_station = SpaceStation(**data)

    except ValidationError as e:
        for error in e.errors():
            if "less than" in error["msg"] and "20" in error["msg"]:
                print(f"{error['msg']}")


if __name__ == "__main__":
    main()
