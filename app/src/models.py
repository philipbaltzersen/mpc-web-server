from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class StatisticalMethod(Enum):
    INDEPENDENT_T_TEST = "independent t-test"


class DataFile(BaseModel):
    file_name: str
    is_uploaded: bool = False
    s3_name: str | None = None


class Analysis(BaseModel):
    id: str | None = None
    owners: list[str]
    data_files: list[DataFile]
    statistical_method: StatisticalMethod
    method_arguments: dict[str, str | int | float | bool] | None = None

