from src.app.ports.usecases.prepare.IGetAvailableColors import IGetAvailableColors
from src.domain.values.combinations.BeadColorEnum import BeadColorEnum


class GetAvailableColors(IGetAvailableColors):
    def execute(self) -> dict[str, str]:
        return {color.name: color.value for color in BeadColorEnum}
