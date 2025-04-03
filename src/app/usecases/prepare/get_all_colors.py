from src.app.ports.usecases.prepare.IGetAllColors import IGetAllColors
from src.domain.values.combinations.BeadColorEnum import BeadColorEnum


class GetAllColors(IGetAllColors):
    def execute(self) -> dict[str, str]:
        return {color.name: color.value for color in BeadColorEnum}
