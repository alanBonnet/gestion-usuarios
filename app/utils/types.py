from typing import Annotated

from pydantic import Field

# INT
INT_POSITIVE = Annotated[int, Field(ge=0)]

# TINYINT
TINYINT = Annotated[int, Field(ge=0, le=255)]

# SMALLINT
SMALLINT = Annotated[int, Field(ge=-32768, le=32767)]

SMALLINT_NULLABLE = Annotated[int, Field(ge=-32768, le=32767)]

# NVARCHAR
NVARCHAR_16 = Annotated[str, Field(max_length=16)]
NVARCHAR_50 = Annotated[str, Field(max_length=50)]

NVARCHAR_50_NULLABLE = Annotated[str | None, Field(max_length=50)]

NVARCHAR_90 = Annotated[str, Field(max_length=90)]

NVARCHAR_100_NULLABLE = Annotated[str | None, Field(max_length=100)]

NVARCHAR_150 = Annotated[str, Field(max_length=150)]
