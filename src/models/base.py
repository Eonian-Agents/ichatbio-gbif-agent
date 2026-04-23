from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import Optional


class ProductionBaseModel(BaseModel):
    """Base model with production-ready settings for all GBIF models (immutable, strict validation)."""

    model_config = ConfigDict(
        frozen=True,  # Models are immutable
        extra="forbid",  # Forbid extra fields not in the model
        validate_assignment=True,  # Validate when values are assigned
        from_attributes=True,  # Allow loading from objects with attributes
        populate_by_name=True,  # Allow population by field name OR alias
        validate_default=True,  # Validate default values
    )


class EntrypointBaseModel(ProductionBaseModel):
    """Base model for all entrypoint parameters."""
    query_start: Optional[str] = Field(
        None, description="ISO-8601 wall-clock time (UTC) when the user query started"
    )
