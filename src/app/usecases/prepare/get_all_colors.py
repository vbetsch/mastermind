from typing import Dict

from src.app.ports.usecases.values.IGetAllColors import IGetAllColors
from src.domain.values.combinations.BeadColorEnum import BeadColorEnum


class GetAllColors(IGetAllColors):
    def execute(self) -> Dict[str, str]:
        return {color.name: color.value for color in BeadColorEnum}
