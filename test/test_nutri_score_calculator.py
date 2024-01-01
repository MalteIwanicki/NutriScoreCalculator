from nutri_score_calculator import NutriScoreCalculator
# %%
def test_if_calculation_matches_example():
    
    example_values = dict(
        kilokalorien=399,
        gesaettigte_fettsaeuren=2.37,
        zucker=26.3,
        proteine=7.99,
        salz=0.82,
        ballaststoffe=4.83,
        anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele=0,
    )
    result = NutriScoreCalculator().calculate_nutri_score(**example_values)
    assert result == "Nutriscore_C"

# %%

def _extract_excel_formulars(excel_file):
    import openpyxl
    workbook = openpyxl.load_workbook(excel_file, read_only=True, )
    worksheet = workbook["allgemeiner Fall"]
    columns = {
        "A": "Produkt",
        "B": "Marke",
        "C": "None",
        "D": "Kilokalorien",
        "E": "Brennwert",
        "F": "Gesamtfett",
        "G": "gesättigte Fettsäuren",
        "H": "Zucker",
        "I": "Proteine",
        "J": "Salz",
        "K": "Ballaststoffe",
        "L": "Nährwert- einheiten",
        "M": "Anteil Obst, Gemüse, Hülsen- und Schalenfrüchte, Raps-, Walnuss- und Olivenöle",
        "N": "Natrium",
        "O": "pts_kj",
        "P": "pts_glus",
        "Q": "pts_ags",
        "R": "pts_na",
        "S": "pts_prot",
        "T": "pts_fib",
        "U": "pts_FLN",
        "V": "pts_A",
        "W": "Wert",
        "X": "Nutri-Score",
        "Y": "Farbe",
    }
    formulars = []
    for col, name in columns.items():
        cell = col + "2"
        formulars.append(f"{cell}, {name}: {worksheet[cell].value}")
    workbook.close()
    return "\n".join(formulars)


# %%

def test_if_formulars_havent_changed(file_path = "nutri-score-dt-excel-berechnungstabelle.xlsx"):
    """ Hier kann getestet werden, ob die Excel immer noch die selben FOrmeln verwendet wie am 01.01.2024. """
    current_formulars = _extract_excel_formulars(file_path)
    with open(r"test\formulars_calculation_is_based_on.txt", "r", encoding="utf-8") as f:
        orig_formulars = f.read()
    assert orig_formulars == current_formulars
