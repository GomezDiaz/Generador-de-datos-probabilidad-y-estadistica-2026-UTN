# ============================================================
# MENU PRINCIPAL
# ============================================================

def mostrar_menu():

    print()
    print("=" * 60)
    print("           PROGRAMA DE ESTADISTICA")
    print("=" * 60)

    print()
    print("Seleccione el tipo de problema:")
    print()

    print("1 - Datos tomados")
    print("2 - Categorias")
    print("3 - Mini tabla de categorias")
    print("4 - Datos para armar intervalos")
    print("5 - Limites de intervalo y frecuencia")

    print()
    print("=" * 60)


# ============================================================
# SELECCIONAR TIPO
# ============================================================

def seleccionar_tipo():

    mostrar_menu()

    while True:

        opcion = input(
            "Ingrese una opcion (1-5): "
        ).strip()

        if opcion in (
            "1",
            "2",
            "3",
            "4",
            "5"
        ):

            return int(
                opcion
            )

        print()
        print(
            "ERROR: debe ingresar un numero "
            "entre 1 y 5."
        )


# ============================================================
# PEDIR RUTA
# ============================================================

def pedir_ruta_csv():

    print()

    ruta = input(
        "Ingrese la ruta del archivo CSV: "
    ).strip()

    # Permite pegar una ruta entre comillas.
    ruta = ruta.strip(
        '"'
    )

    return ruta


# ============================================================
# MOSTRAR DATOS
# ============================================================

def mostrar_datos(
    datos
):

    print()
    print("=" * 60)
    print("DATOS CARGADOS")
    print("=" * 60)

    for i, dato in enumerate(
        datos,
        start=1
    ):

        print(
            f"{i:>4}: {dato}"
        )


# ============================================================
# MOSTRAR CATEGORIAS
# ============================================================

def mostrar_categorias(
    categorias
):

    print()
    print("=" * 60)
    print("CATEGORIAS")
    print("=" * 60)

    for categoria in categorias:

        print(
            categoria
        )


# ============================================================
# MOSTRAR FRECUENCIAS
# ============================================================

def mostrar_frecuencias_categorias(
    frecuencias
):

    print()
    print("=" * 60)
    print("FRECUENCIAS DE LAS CATEGORIAS")
    print("=" * 60)

    for categoria, frecuencia in (
        frecuencias.items()
    ):

        print(
            f"{categoria}: {frecuencia}"
        )


# ============================================================
# MOSTRAR MINI TABLA
# ============================================================

def mostrar_mini_tabla(
    frecuencias
):

    print()
    print("=" * 60)
    print("DATOS CARGADOS")
    print("=" * 60)

    for categoria, frecuencia in (
        frecuencias.items()
    ):

        print(
            f"{categoria}: {frecuencia}"
        )


# ============================================================
# MOSTRAR INTERVALOS
# ============================================================

def mostrar_intervalos(
    intervalos
):

    print()
    print("=" * 60)
    print("INTERVALOS CARGADOS")
    print("=" * 60)

    for intervalo in intervalos:

        li = intervalo["li"]

        ls = intervalo["ls"]

        fi = intervalo["fi"]

        xi = intervalo["xi"]

        print(
            f"[{li:.2f}, {ls:.2f})"
            f"   fi = {fi}"
            f"   Xi = {xi:.2f}"
        )


# ============================================================
# MOSTRAR RESULTADOS
# ============================================================

def mostrar_resultados(
    resultados,
    agrupados=False,
    mostrar_limites=True
):

    print()
    print("=" * 60)
    print("RESULTADOS ESTADISTICOS")
    print("=" * 60)

    if agrupados:

        print()

        print(
            "NOTA: los resultados son aproximados"
        )

        print(
            "porque se trabaja con datos agrupados."
        )

    print()

    # ========================================================
    # DATOS GENERALES
    # ========================================================

    print(
        f"Cantidad de datos (n): "
        f"{resultados['n']}"
    )

    print(
        f"Minimo:                "
        f"{resultados['minimo']:.2f}"
    )

    print(
        f"Maximo:                "
        f"{resultados['maximo']:.2f}"
    )

    print(
        f"Rango:                 "
        f"{resultados['rango']:.2f}"
    )

    # ========================================================
    # MEDIDAS DE POSICION
    # ========================================================

    print()

    print(
        "MEDIDAS DE POSICION"
    )

    print("-" * 60)

    print(
        f"Media:                 "
        f"{resultados['media']:.2f}"
    )

    # --------------------------------------------------------
    # MODA
    # --------------------------------------------------------

    moda = resultados["moda"]

    if isinstance(
        moda,
        list
    ):

        if moda:

            texto_moda = ", ".join(
                f"{x:.2f}"
                for x in moda
            )

        else:

            texto_moda = (
                "No hay moda"
            )

    else:

        texto_moda = (
            f"{moda:.2f}"
        )

    print(
        f"Moda:                  "
        f"{texto_moda}"
    )

    print(
        f"Mediana:               "
        f"{resultados['mediana']:.2f}"
    )

    # ========================================================
    # MEDIDAS DE DISPERSION
    # ========================================================

    print()

    print(
        "MEDIDAS DE DISPERSION"
    )

    print("-" * 60)

    print(
        f"Varianza:              "
        f"{resultados['varianza']:.2f}"
    )

    print(
        f"Desvio estandar:       "
        f"{resultados['desvio']:.2f}"
    )

    # --------------------------------------------------------
    # CV DECIMAL
    # --------------------------------------------------------

    cv = resultados[
        "coeficiente_variacion"
    ]

    if cv is not None:

        print(
            f"Coef. de variacion:    "
            f"{cv:.2f}"
        )

    else:

        print(
            "Coef. de variacion:    "
            "No se puede calcular"
        )

    # --------------------------------------------------------
    # CV PORCENTUAL
    # --------------------------------------------------------

    cv_porcentaje = resultados[
        "coeficiente_variacion_porcentaje"
    ]

    if cv_porcentaje is not None:

        print(
            f"Coef. de variacion %:  "
            f"{cv_porcentaje:.2f}%"
        )

    # ========================================================
    # CUARTILES
    # ========================================================

    print()

    print(
        "CUARTILES"
    )

    print("-" * 60)

    print(
        f"Q1:                    "
        f"{resultados['q1']:.2f}"
    )

    print(
        f"Q2:                    "
        f"{resultados['q2']:.2f}"
    )

    print(
        f"Q3:                    "
        f"{resultados['q3']:.2f}"
    )

    # ========================================================
    # ASIMETRIA
    # ========================================================

    print()

    print(
        "ASIMETRIA"
    )

    print("-" * 60)

    print(
        f"Coef. de asimetria:    "
        f"{resultados['asimetria']:.2f}"
    )

    print(
        f"Tipo:                  "
        f"{resultados['tipo_asimetria']}"
    )

    # ========================================================
    # LIMITES
    # ========================================================

    if mostrar_limites:

        print()

        print(
            "LIMITES"
        )

        print("-" * 60)

        print(
            f"LI:                    "
            f"{resultados['li']:.2f}"
        )

        print(
            f"LS:                    "
            f"{resultados['ls']:.2f}"
        )

    print()

    print("=" * 60)


# ============================================================
# MENSAJE
# ============================================================

def mostrar_mensaje(
    mensaje
):

    print()
    print(
        mensaje
    )


# ============================================================
# ERROR
# ============================================================

def mostrar_error(
    mensaje
):

    print()

    print(
        f"ERROR: {mensaje}"
    )