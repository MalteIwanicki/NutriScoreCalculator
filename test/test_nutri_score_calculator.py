from nutri_score_calculator import NutriScoreCalculator, NutriScoreCategory
import hashlib
import requests

# %%
def test_if_calculation_matches_example_allgemeiner_fall():
    example_values = dict(
        category=NutriScoreCategory.ALLGEMEINER_FALL,
        kilokalorien=399,
        gesaettigte_fettsaeuren=2.37,
        zucker=26.3,
        proteine=7.99,
        salz=0.82,
        ballaststoffe=4.83,
        anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele=0,
    )
    result = NutriScoreCalculator.calculate_nutri_score(**example_values)
    assert result[0] == "Nutriscore_C"
    assert result[1] == 9


def test_if_calculation_matches_example_käse():
    example_values = dict(
        category=NutriScoreCategory.KAESE,
        kilokalorien=274,
        gesaettigte_fettsaeuren=13.9,
        zucker=0,
        proteine=21.3,
        natrium=552,
        ballaststoffe=0,
        anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele=0,
    )
    result = NutriScoreCalculator.calculate_nutri_score(
        **example_values
    )
    assert result[0] == "Nutriscore_D"
    assert result[1] == 14


def test_if_calculation_matches_example_zugesetzte_fette():
    example_values = dict(
        category=NutriScoreCategory.ZUGESETZTE_FETTE,
        kilokalorien=900,
        gesamtfett=100,
        gesaettigte_fettsaeuren=7.3,
        zucker=0,
        proteine=0,
        salz=0,
        ballaststoffe=0,
        anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele=100,
    )
    result = NutriScoreCalculator.calculate_nutri_score(**example_values)
    assert result[0] == "Nutriscore_C"
    assert result[1] == 5


def test_if_calculation_matches_example_getränke():
    example_values = dict(
        category=NutriScoreCategory.GETRAENKE,
        ist_wasser=False,
        kilokalorien=37.1,
        gesaettigte_fettsaeuren=0,
        zucker=8.67,
        proteine=0.14,
        salz=0.091,
        ballaststoffe=0,
        anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele=0,
    )
    result = NutriScoreCalculator.calculate_nutri_score(
        **example_values
    )
    assert result[0] == "Nutriscore_E"
    assert result[1] == 12


# %%


def test_if_file_hasnt_changed(
    file_path="nutri-score-dt-excel-berechnungstabelle.xlsx",
):
    """Hier kann getestet werden, ob die Excel immer noch die selbe Datei wie vom 01.01.2024 ist."""

    original_hash = "044fdc48641cba7eea0e6894bf8f9ed32efb27ab2e78a7b45b6108671989d1e1"

    url = "https://www.bmel.de/SharedDocs/Downloads/DE/_Ernaehrung/Lebensmittel-Kennzeichnung/nutri-score-dt-excel-berechnungstabelle.xlsx?__blob=publicationFile&v=6"

    response = requests.get(url)
    file_data = response.content

    sha256_hash = hashlib.sha256()
    sha256_hash.update(file_data)
    computed_hash = sha256_hash.hexdigest()

    assert computed_hash == original_hash
