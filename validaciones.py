def validar_nom_cognom(nom, cognom):
    return nom.isalpha() and cognom.isalpha()

def validar_telefon(telefon):
    return telefon.isdigit() and len(telefon) >= 5 and len(telefon) <= 9

def validar_quantitat_diners(quantitatDiners):
    try:
        quantitatDiners_float = float(quantitatDiners)
        return quantitatDiners_float >= 0
    except ValueError:
        return False
