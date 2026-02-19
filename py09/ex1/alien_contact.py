from pydantic import BaseModel, Field, model_validator
from enum import Enum
from typing import Optional
from datetime import datetime


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == "pysical":
            raise ValueError("Physical contact must be verified")
        if self.contact_type == "telepathic" and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                " Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=================================")
    print("Valid contact report:")
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-02-19",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Messages: '{alien.message_received}'")
        print("======================================")
        print("Expected validation error:")
        alien = AlienContact(
            contact_id="AC_2024_002",
            timestamp="2026-02-19",
            location="Area 51, Nevada",
            contact_type="telepathic",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
        )
    except ValueError as e:
        for error in e.errors():
            if "at least 3" in error["msg"]:
                msg = error["msg"].split(", ")[1]
                print(msg)


if __name__ == "__main__":
    main()
