class NutriScoreCalculator:
    """
    Dieser Nutri-Score Rechner nutzt die Formeln aus der Nutri-Score Berechnungs Excel Tablle des BMEL von: https://www.bmel.de/SharedDocs/Downloads/DE/_Ernaehrung/Lebensmittel-Kennzeichnung/nutri-score-dt-excel-berechnungstabelle.html bezogen am 01.01.2024.
    Lediglich der Allgemeine Fall wird ausgerechnet.
    """

    @staticmethod
    def _calculate_brennwert(kilokalorien):
        return round(kilokalorien * 4.184, 0)

    @staticmethod
    def _calculate_natrium(salz):
        return round(salz / 2.5 * 1000, 0)

    @staticmethod
    def _calculate_pts_kj(brennwert):
        if brennwert is None:
            return " "
        brennwert = round(brennwert, 1)
        if brennwert <= 335:
            return 0
        elif brennwert <= 670:
            return 1
        elif brennwert <= 1005:
            return 2
        elif brennwert <= 1340:
            return 3
        elif brennwert <= 1675:
            return 4
        elif brennwert <= 2010:
            return 5
        elif brennwert <= 2345:
            return 6
        elif brennwert <= 2680:
            return 7
        elif brennwert <= 3015:
            return 8
        elif brennwert <= 3350:
            return 9
        else:
            return 10

    @staticmethod
    def _calculate_pts_glus(zucker):
        if zucker is None:
            return None
        zucker = round(zucker, 2)
        if zucker <= 4.5:
            return 0
        elif zucker <= 9:
            return 1
        elif zucker <= 13.5:
            return 2
        elif zucker <= 18:
            return 3
        elif zucker <= 22.5:
            return 4
        elif zucker <= 27:
            return 5
        elif zucker <= 31:
            return 6
        elif zucker <= 36:
            return 7
        elif zucker <= 40:
            return 8
        elif zucker <= 45:
            return 9
        else:
            return 10

    @staticmethod
    def _calculate_pts_ags(gesaettigte_fettsaeuren):
        if gesaettigte_fettsaeuren is None:
            return None
        gesaettigte_fettsaeuren = round(gesaettigte_fettsaeuren, 1)
        if gesaettigte_fettsaeuren <= 1:
            return 0
        elif gesaettigte_fettsaeuren <= 2:
            return 1
        elif gesaettigte_fettsaeuren <= 3:
            return 2
        elif gesaettigte_fettsaeuren <= 4:
            return 3
        elif gesaettigte_fettsaeuren <= 5:
            return 4
        elif gesaettigte_fettsaeuren <= 6:
            return 5
        elif gesaettigte_fettsaeuren <= 7:
            return 6
        elif gesaettigte_fettsaeuren <= 8:
            return 7
        elif gesaettigte_fettsaeuren <= 9:
            return 8
        elif gesaettigte_fettsaeuren <= 10:
            return 9
        else:
            return 10

    @staticmethod
    def _calculate_pts_na(natrium):
        if natrium is None:
            return None
        natrium = round(natrium, 1)
        if natrium <= 90:
            return 0
        elif natrium <= 180:
            return 1
        elif natrium <= 270:
            return 2
        elif natrium <= 360:
            return 3
        elif natrium <= 450:
            return 4
        elif natrium <= 540:
            return 5
        elif natrium <= 630:
            return 6
        elif natrium <= 720:
            return 7
        elif natrium <= 810:
            return 8
        elif natrium <= 900:
            return 9
        else:
            return 10

    @staticmethod
    def _calculate_pts_prot(protein):
        if protein is None:
            return None
        protein = round(protein, 2)
        if protein <= 1.6:
            return 0
        elif protein <= 3.2:
            return 1
        elif protein <= 4.8:
            return 2
        elif protein <= 6.4:
            return 3
        elif protein <= 8:
            return 4
        else:
            return 5

    @staticmethod
    def _calculate_pts_fib(ballaststoffe):
        if ballaststoffe is None:
            return None
        ballaststoffe = round(ballaststoffe, 2)
        if ballaststoffe <= 0.9:
            return 0
        elif ballaststoffe <= 1.9:
            return 1
        elif ballaststoffe <= 2.8:
            return 2
        elif ballaststoffe <= 3.7:
            return 3
        elif ballaststoffe <= 4.7:
            return 4
        else:
            return 5

    @staticmethod
    def _calculate_pts_FLN(
        anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele,
    ):
        anteile = anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele
        if anteile is None:
            return None
        anteile = round(
            anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele, 1
        )
        if anteile <= 40:
            return 0
        elif anteile <= 60:
            return 1
        elif anteile <= 80:
            return 2
        else:
            return 5

    @staticmethod
    def _calculate_pts_A(
        pts_kj,
        pts_glus,
        pts_ags,
        pts_na,
    ):
        if any(
            v is None
            for v in [
                pts_kj,
                pts_glus,
                pts_ags,
                pts_na,
            ]
        ):
            return None
        return pts_kj + pts_glus + pts_ags + pts_na

    @staticmethod
    def _calculate_wert(pts_A, pts_prot, pts_fib, pts_FLN):
        if any(v is None for v in [pts_A, pts_prot, pts_fib, pts_FLN]):
            return None
        if 0 <= pts_A < 11:
            return pts_A - (pts_prot + pts_fib + pts_FLN)
        elif pts_A >= 11 and pts_FLN == 5:
            return pts_A - (pts_prot + pts_fib + pts_FLN)
        else:
            return pts_A - pts_FLN - pts_fib

    @staticmethod
    def _calculate_rating(wert):
        if wert is None:
            return "fehlende_Daten"
        if wert < 0:
            return "Nutriscore_A"
        elif wert < 3:
            return "Nutriscore_B"
        elif wert < 11:
            return "Nutriscore_C"
        elif wert < 19:
            return "Nutriscore_D"
        else:
            return "Nutriscore_E"

    @classmethod
    def calculate_nutri_score(
        cls,
        kilokalorien,
        gesaettigte_fettsaeuren,
        zucker,
        proteine,
        salz,
        ballaststoffe,
        anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele,
    ):
        natrium = cls._calculate_natrium(salz)
        brennwert = cls._calculate_brennwert(kilokalorien)
        pts_kj = cls._calculate_pts_kj(brennwert)
        pts_glus = cls._calculate_pts_glus(zucker)
        pts_ags = cls._calculate_pts_ags(gesaettigte_fettsaeuren)
        pts_na = cls._calculate_pts_na(natrium)
        pts_prot = cls._calculate_pts_prot(proteine)
        pts_fib = cls._calculate_pts_fib(ballaststoffe)
        pts_FLN = cls._calculate_pts_FLN(
            anteil_obst_gemuese_huelsen_schalen_raps_walnuss_und_olivenoele
        )
        pts_A = cls._calculate_pts_A(
            pts_kj,
            pts_glus,
            pts_ags,
            pts_na,
        )

        wert = cls._calculate_wert(pts_A, pts_prot, pts_fib, pts_FLN)
        rating = cls._calculate_rating(wert)
        return rating
