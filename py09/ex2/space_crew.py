from enum import Enum
from pydantic import BaseModel, model_validator, Field
from datetime import datetime
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        if not any(
            m.rank in (Rank.captain, Rank.commander) for m in self.crew
        ):
            raise ValueError("Must have at least one Commander or Captain")
        experienced = sum(1 for m in self.crew if m.years_experience >= 5)
        ratio = experienced / len(self.crew)
        if self.duration_days > 365 and ratio < 0.5:
            raise ValueError('Long missions need 50"%" experienced crew')
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-01-01T00:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=45,
                specialization="Mission Command",
                years_experience=20,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=10,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=5,
            ),
        ],
    )
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
        )
    print("=========================================")
    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Failed Mission",
            destination="Moon",
            launch_date="2024-01-01",
            duration_days=30,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob",
                    rank=Rank.cadet,
                    age=22,
                    specialization="Cleaning",
                    years_experience=0,
                )
            ],
        )
    except ValueError as e:
        print("Expected validation error:")
        for error in e.errors():
            if "Commander or Captain" in error["msg"]:
                msg = error["msg"].split(", ")[1]
                print(msg)


if __name__ == "__main__":
    main()
