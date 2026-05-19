try:
    from enum import Enum
    from pydantic import BaseModel, Field, model_validator
    from datetime import datetime
    from typing import Optional
    from typing_extensions import Self
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def id_validator(self) -> Self:
        if self.contact_id[0] != "A" or self.contact_id[1] != "C":
            raise ValueError("All id's must start with "
                             f"'AC'. Error: {self.contact_id}")
        return self

    @model_validator(mode='after')
    def contact_validator(self) -> Self:
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError("Telepathic contacts must have "
                             "at least 3 witnesses")
        return self

    @model_validator(mode='after')
    def signal_validator(self) -> Self:
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must "
                             "include a received messages")
        return self
