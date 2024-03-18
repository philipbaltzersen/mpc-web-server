from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class StatisticalMethod(Enum):
    INDEPENDENT_T_TEST = "independent t-test"


class Analysis(BaseModel):
    id: str | None = None
    owners: list[str]
    file_names: list[str]
    statistical_method: StatisticalMethod
    method_arguments: dict[str, str | int | float | bool] | None = None

