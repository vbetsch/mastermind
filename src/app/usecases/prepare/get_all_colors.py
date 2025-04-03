from typing import Dict

from src.app.ports.usecases.prepare.IGetAllColors import IGetAllColors
from src.common.logs.Logger import Logger
from src.domain.values.combinations.BeadColorEnum import BeadColorEnum


class GetAllColors(IGetAllColors):
    def execute(self) -> Dict[str, str]:
        result = {color.name: color.value for color in BeadColorEnum}
        Logger().debug(f"All colors : {result}")
        return result
