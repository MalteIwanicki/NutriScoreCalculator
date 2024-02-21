
[![Algorithm is up to date and unittest succeedes](https://github.com/MalteIwanicki/NutriScoreCalculator/actions/workflows/main.yml/badge.svg)](https://github.com/MalteIwanicki/NutriScoreCalculator/actions/workflows/main.yml)

# NutriScoreCalculator

The goal of this project is to provide a simple package that can calculate the Nutri-Score based on the formula of 2024.

<p align="center">
  <img width="568" height="307" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Nutri-score-E.svg/1920px-Nutri-score-E.svg.png" alt="Nutri Score logo">
</p>


## What is the Nutri-Score?

The Nutri-Score is a nutrition label that converts the nutritional value of products into a simple code consisting of 5 letters, each with its own color. Each product is awarded a score based on a scientific algorithm. This formula takes into account the nutrients to avoid (energy value and the amount of sugars, saturated fats, and salt) and the positive ones (the amount of fiber, protein, fruit, vegetables, and nuts). You can therefore see at a glance which products are recommended and which should be avoided.

> The formulars are sourced from: https://www.bmel.de/SharedDocs/Downloads/DE/_Ernaehrung/Lebensmittel-Kennzeichnung/nutri-score-dt-excel-berechnungstabelle.html

> more information here: https://www.bmel.de/DE/themen/ernaehrung/lebensmittel-kennzeichnung/freiwillige-angaben-und-label/nutri-score/nutri-score_node.html
## Where to get it

The source code is currently hosted on GitHub at: https://github.com/MalteIwanicki/NutriScoreCalculator

## Usage

Install:

```bash
cd {projects folder with setup.py}
pip install .
```

## Calculate the Nutri-Score:

```Python
from nutri_score_calculator import NutriScoreCalculator, NutriScoreCategory

result = NutriScoreCalculator.calculate_nutri_score(
    category=NutriScoreCategory.ALLGEMEINER_FALL,
    kilokalorien=0,
    gesaettigte_fettsaeuren=4,
    zucker=60,
    proteine=2,
    salz=2,
    ballaststoffe=500,
    anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele=10,
)
print(result) # result: "Nutriscore_D"
```
## License
MIT

## Contribution
Feel free to add suggestions, PRs, comments, and bug reports.

## Authors
Malte Iwanicki (malteiwa@gmail.com)
