unidades = {
    "ohm": r"\Omega",
    "siemens": r"\mbox{S}",
    "ampere": r"\mbox{A}",
    "volt": r"\mbox{V}",
}

calcular = {
    "corriente": {
        "texto": "las corrientes",
        "variable": "i",
        "A": {"unidad": unidades["ohm"],
              "unidad_inversa": unidades["siemens"],
              "formato": "{:.4g}"},
        "X": {"unidad": unidades["ampere"],
              "formato": "{:.4g}"},
        "b": {"unidad": unidades["volt"],
              "formato": "{:.4g}"}
    },
    "tension": {
        "texto": "las tensiones",
        "variable": "v",
        "A": {"unidad": unidades["ohm"],
              "unidad_inversa": unidades["siemens"],
              "formato": "{:.4g}"},
        "X": {"unidad": unidades["volt"],
              "formato": "{:.4e}"},
        "b": {"unidad": unidades["ampere"],
              "formato": "{:.4e}"},
    }
}
