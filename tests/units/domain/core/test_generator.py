import pytest
from unittest.mock import patch
from src.domain.core.Generator import Generator
from src.domain.values.combinations.Bead import Bead
from src.domain.values.combinations.BeadColorEnum import BeadColorEnum
from src.domain.values.combinations.Combination import Combination


class TestGenerator:
    @pytest.fixture
    def generator(self):
        return Generator()

    def test_generate_bead(self, generator):
        with patch.object(generator, '_generate_bead', return_value=Bead(BeadColorEnum.R)) as mock_generate:
            bead = generator._generate_bead()
            assert isinstance(bead, Bead)
            assert bead.get_color() == BeadColorEnum.R.value
            mock_generate.assert_called_once()

    def test_generate_combination(self, generator):
        combination = generator.generate_combination()
        assert isinstance(combination, Combination)
        assert len(combination._beads) == generator.nb_beads

    def test_generate_combination_randomness(self, generator):
        with patch('src.domain.core.Generator.choice', return_value=BeadColorEnum.R):
            combination1 = generator.generate_combination()
            with patch('src.domain.core.Generator.choice', return_value=BeadColorEnum.G):
                combination2 = generator.generate_combination()

            assert combination1 != combination2
