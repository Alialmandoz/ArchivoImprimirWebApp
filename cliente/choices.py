TIPO_TRABAJO = (
    (1, ("Imprenta")),
    (2, ("Gran Formato"))
)


SOPORTE = (
    ("a", "Obra 80"),
    ("c", "Ilustracion 130"),
    ("e", "Ilustracion 250/300"),
    ("g", "Vegetal / Rives"),
    ("h", "auto-adhesivo ilustracion/obra"),
    ("i", "auto-adhesivo + corte"),
)


def traducir_soporte(material):
    if material == "a":
        material = "Obra 80"
    elif material == "c":
        material = "Ilustracion 130"
    elif material == "e":
        material = "Ilustracion 250/300"
    elif material == "g":
        material = "Vegetal / Rives"
    elif material == "h":
        material = "auto-adhesivo ilustracion/obra"
    else:
        material = "auto-adhesivo + corte"
    return material

CANTIDADES = (
    ("1 a 4", 1),
    ("5 a 10", 2),
    ("11 a 50", 3),
    ("51 a 100", 4),
    ("101 a 250", 5),
    ("251 a 500", 6),


)

HOJA = (
    ("1", "Simple Faz"),
    ("2", "Doble Faz"),
)


def traducir_cara(cara):
    if cara == "1":
        cara = "Simple Faz"
    else:
        cara = "Doble Faz"
    return cara


BYN = (
    (True, "Blanco y Negro"),
)






