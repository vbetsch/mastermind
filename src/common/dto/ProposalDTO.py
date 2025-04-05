from .IDto import IDto


class ProposalDTO(IDto):
    def __init__(self, proposal: str) -> None:
        self.proposal: str = proposal
