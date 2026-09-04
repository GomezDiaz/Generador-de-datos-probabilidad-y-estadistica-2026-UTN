import matplotlib.pyplot as plt


# ============================================================
# UTILIDADES
# ============================================================

def formato_numero(valor):

    if valor is None:
        return "-"

    if isinstance(valor, float):

        texto = f"{valor:.2f}"

        return texto.replace(".", ",")

    return str(valor)


def formato_lista(valores):

    if valores is None:
        return "-"

    if not isinstance(valores, list):
        valores = [valores]

    return ", ".join(
        formato_numero(valor)
        for valor in valores
    )


# ============================================================
# MENÚ
# ============================================================

def mostrar_menu():

    print()
    print("=" * 60)
    print("                 ESTADÍSTICA")
    print("=" * 60)

    print("1. Categorías")
    print("2. Mini tabla de categorías")
    print("3. Datos para armar intervalos")
    print("4. Límites del intervalo y frecuencia")

    print("=" * 60)


def seleccionar_tipo():

    while True:

        try:

            opcion = int(
                input("Seleccione una opción: ")
            )

            if opcion in (1, 2, 3, 4):
                return opcion

            print("Error: seleccione una opción entre 1 y 4.")

        except ValueError:

            print("Error: debe ingresar un número.")


# ============================================================
# RUTA
# ============================================================

def pedir_ruta_csv():

    return input(
        "\nIngrese la ruta del archivo CSV: "
    ).strip()


# ============================================================
# MOSTRAR DATOS
# ============================================================

def mostrar_datos(datos):

    print()
    print("-" * 60)
    print("DATOS")
    print("-" * 60)

    for i, dato in enumerate(datos, start=1):

        print(
            f"{i}: {dato}"
        )


# ============================================================
# MOSTRAR TABLA DE CATEGORÍAS
# ============================================================

def mostrar_mini_tabla(tabla):

    print()
    print("-" * 60)
    print("MINI TABLA DE CATEGORÍAS")
    print("-" * 60)

    for categoria, frecuencia in tabla:

        print(
            f"{categoria}: {frecuencia}"
        )


# ============================================================
# MOSTRAR INTERVALOS
# ============================================================

def mostrar_intervalos(intervalos):

    print()
    print("-" * 80)
    print("INTERVALOS")
    print("-" * 80)

    for intervalo in intervalos:

        print(
            f"[{formato_numero(intervalo['li'])} ; "
            f"{formato_numero(intervalo['ls'])}) "
            f"fi={intervalo['frecuencia']} "
            f"Xi={formato_numero(intervalo['xi'])}"
        )


# ============================================================
# RESULTADOS
# ============================================================

def mostrar_resultados(
    resultados,
    agrupados=False
):

    print()
    print("=" * 60)
    print("RESULTADOS ESTADÍSTICOS")
    print("=" * 60)

    # --------------------------------------------------------
    # DATOS GENERALES
    # --------------------------------------------------------

    print()
    print("DATOS GENERALES")
    print("-" * 60)

    print(
        f"N: {resultados.get('n', '-')}"
    )

    print(
        f"Mínimo: {formato_numero(resultados.get('minimo'))}"
    )

    print(
        f"Máximo: {formato_numero(resultados.get('maximo'))}"
    )

    print(
        f"Rango: {formato_numero(resultados.get('rango'))}"
    )

    # --------------------------------------------------------
    # MEDIDAS DE POSICIÓN
    # --------------------------------------------------------

    print()
    print("MEDIDAS DE POSICIÓN")
    print("-" * 60)

    print(
        f"Media (X): "
        f"{formato_numero(resultados.get('media'))}"
    )

    print(
        f"Mediana: "
        f"{formato_numero(resultados.get('mediana'))}"
    )

    print(
        f"Moda: "
        f"{formato_lista(resultados.get('moda'))}"
    )

    # --------------------------------------------------------
    # DISPERSIÓN
    # --------------------------------------------------------

    print()
    print("MEDIDAS DE DISPERSIÓN")
    print("-" * 60)

    print(
        f"Varianza: "
        f"{formato_numero(resultados.get('varianza'))}"
    )

    print(
        f"S, Desvío: "
        f"{formato_numero(resultados.get('desvio'))}"
    )

    print(
        f"Cv: "
        f"{formato_numero(resultados.get('cv'))}"
    )

    print(
        f"Cv%: "
        f"{formato_numero(resultados.get('cv_porcentaje'))}%"
    )

    # --------------------------------------------------------
    # CUARTILES
    # --------------------------------------------------------

    print()
    print("CUARTILES")
    print("-" * 60)

    print(
        f"Q1: "
        f"{formato_numero(resultados.get('Q1'))}"
    )

    print(
        f"Q2: "
        f"{formato_numero(resultados.get('Q2'))}"
    )

    print(
        f"Q3: "
        f"{formato_numero(resultados.get('Q3'))}"
    )

    print(
        f"IQR: "
        f"{formato_numero(resultados.get('IQR'))}"
    )

    # --------------------------------------------------------
    # ASIMETRÍA
    # --------------------------------------------------------

    print()
    print("ASIMETRÍA")
    print("-" * 60)

    print(
        f"As: "
        f"{formato_numero(resultados.get('asimetria'))}"
    )

    print(
        resultados.get(
            "clasificacion_asimetria",
            "-"
        )
    )

    # --------------------------------------------------------
    # LÍMITES MEDIA ± DESVÍO
    # --------------------------------------------------------

    print()
    print("LÍMITES MEDIA ± DESVÍO")
    print("-" * 60)

    print(
        f"LI: "
        f"{formato_numero(resultados.get('LI'))}"
    )

    print(
        f"LS: "
        f"{formato_numero(resultados.get('LS'))}"
    )

    # --------------------------------------------------------
    # BOX PLOT
    # --------------------------------------------------------

    if not agrupados:

        print()
        print("BOX PLOT")
        print("-" * 60)

        print(
            f"Límite inferior boxplot: "
            f"{formato_numero(resultados.get('limite_box_inferior'))}"
        )

        print(
            f"Límite superior boxplot: "
            f"{formato_numero(resultados.get('limite_box_superior'))}"
        )

        print(
            f"Bigote inferior: "
            f"{formato_numero(resultados.get('bigote_inferior'))}"
        )

        print(
            f"Bigote superior: "
            f"{formato_numero(resultados.get('bigote_superior'))}"
        )

        outliers = resultados.get(
            "outliers",
            []
        )

        if outliers:

            print(
                f"Valores atípicos: "
                f"{formato_lista(outliers)}"
            )

        else:

            print(
                "Valores atípicos: Ninguno"
            )


# ============================================================
# DIAGRAMA DE BARRAS
# ============================================================

def mostrar_diagrama_barras(categorias, frecuencias):

    plt.figure(figsize=(8, 5))

    posiciones = range(len(categorias))

    plt.bar(
        posiciones,
        frecuencias
    )

    plt.xticks(
        posiciones,
        [str(c) for c in categorias],
        rotation=45,
        ha="right"
    )

    plt.xlabel("Categoría")
    plt.ylabel("Frecuencia absoluta")
    plt.title("Diagrama de barras")

    plt.tight_layout()

    plt.show()


# ============================================================
# HISTOGRAMA
# ============================================================

def mostrar_histograma(intervalos):

    if not intervalos:
        return

    limites = [
        intervalo["li"]
        for intervalo in intervalos
    ]

    limites.append(
        intervalos[-1]["ls"]
    )

    frecuencias = [
        intervalo["frecuencia"]
        for intervalo in intervalos
    ]

    plt.figure(figsize=(9, 5))

    # width se calcula a partir de cada intervalo
    for i, intervalo in enumerate(intervalos):

        ancho = (
            intervalo["ls"]
            - intervalo["li"]
        )

        plt.bar(
            intervalo["li"],
            intervalo["frecuencia"],
            width=ancho,
            align="edge",
            edgecolor="black"
        )

    plt.xlabel("Intervalos")
    plt.ylabel("Frecuencia absoluta")
    plt.title("Histograma")

    plt.xticks(limites)

    plt.tight_layout()

    plt.show()


# ============================================================
# BOXPLOT
# ============================================================

def mostrar_boxplot(datos, resultados):

    if not datos:
        return

    plt.figure(figsize=(7, 5))

    plt.boxplot(
        datos,
        vert=False
    )

    plt.title("Diagrama de cajas y bigotes")
    plt.xlabel("Valores")

    # Mostrar límites de detección de outliers
    limite_inferior = resultados.get(
        "limite_box_inferior"
    )

    limite_superior = resultados.get(
        "limite_box_superior"
    )

    if limite_inferior is not None:
        plt.axvline(
            limite_inferior,
            linestyle="--"
        )

    if limite_superior is not None:
        plt.axvline(
            limite_superior,
            linestyle="--"
        )

    plt.tight_layout()

    plt.show()


# ============================================================
# MENSAJES
# ============================================================

def mostrar_mensaje(mensaje):

    print()
    print(mensaje)


def mostrar_error(error):

    print()
    print("=" * 60)
    print("ERROR")
    print("=" * 60)
    print(error)