import csv


# ============================================================
# LECTURA GENERAL DEL ARCHIVO
# ============================================================

def leer_archivo_texto(
    ruta
):

    """
    Lee el archivo linea por linea.

    NO utiliza la coma como separador.

    Esto permite que:

        2,2

    sea interpretado como un unico dato.
    """

    with open(
        ruta,
        "r",
        encoding="utf-8-sig"
    ) as archivo:

        lineas = archivo.readlines()

    return lineas


# ============================================================
# CONVERTIR TEXTO A NUMERO
# ============================================================

def convertir_numero(
    valor
):

    """
    Convierte:

        2,2  -> 2.2
        2.2  -> 2.2
        3    -> 3.0

    Tambien elimina espacios y comillas.
    """

    valor = str(
        valor
    ).strip()

    valor = valor.strip(
        '"'
    )

    valor = valor.strip(
        "'"
    )

    valor = valor.strip()

    if not valor:

        raise ValueError(
            "Se encontro un valor numerico vacio."
        )

    # --------------------------------------------------------
    # Si utiliza coma decimal:
    #
    # 2,2 -> 2.2
    # --------------------------------------------------------

    if (
        ","
        in valor
        and "."
        not in valor
    ):

        valor = valor.replace(
            ",",
            "."
        )

    # --------------------------------------------------------
    # Si por alguna razon aparece:
    #
    # 1.234,56
    #
    # se interpreta como 1234.56
    # --------------------------------------------------------

    elif (
        ","
        in valor
        and "."
        in valor
    ):

        valor = valor.replace(
            ".",
            ""
        )

        valor = valor.replace(
            ",",
            "."
        )

    try:

        return float(
            valor
        )

    except ValueError:

        raise ValueError(
            f"'{valor}' no es un numero valido."
        )


# ============================================================
# LIMPIAR LINEA
# ============================================================

def limpiar_linea(
    linea
):

    linea = linea.strip()

    # Ignorar lineas vacias.
    if not linea:

        return None

    # Ignorar comentarios.
    if linea.startswith("#"):

        return None

    return linea


# ============================================================
# DETECTAR ENCABEZADO NUMERICO
# ============================================================

def es_encabezado_tipo_1_2_4(
    linea
):

    """
    Para tipos 1, 2 y 4.

    Si la primera linea es:

        Tiempo

    no es numerica y se considera encabezado.

    Si es:

        2,2

    es un dato y NO se elimina.
    """

    try:

        # Si contiene ';', puede haber
        # varios datos en una misma linea.

        partes = linea.split(";")

        for parte in partes:

            convertir_numero(
                parte
            )

        return False

    except ValueError:

        return True


# ============================================================
# TIPO 1
# DATOS TOMADOS/ esto quedo resagado ya que tipo 2 cumple esta funcion
# ============================================================

def cargar_datos_tomados(
    lineas
):

    datos = []

    for linea in lineas:

        linea = limpiar_linea(
            linea
        )

        if linea is None:
            continue

        # ----------------------------------------------------
        # Una linea puede contener:
        #
        # 2,2
        #
        # o:
        #
        # 2,2;2,5;2,7
        # ----------------------------------------------------

        partes = linea.split(
            ";"
        )

        for parte in partes:

            if not parte.strip():
                continue

            dato = convertir_numero(
                parte
            )

            datos.append(
                dato
            )

    if not datos:

        raise ValueError(
            "No se encontraron datos numericos."
        )

    return datos


# ============================================================
# TIPO 2
# CATEGORIAS
# ============================================================

def cargar_categorias(
    lineas
):

    categorias = []

    for linea in lineas:

        linea = limpiar_linea(
            linea
        )

        if linea is None:
            continue

        # ----------------------------------------------------
        # Cada salto de linea es un dato.
        #
        # ';' permite varios datos en una linea.
        # ----------------------------------------------------

        partes = linea.split(
            ";"
        )

        for parte in partes:

            categoria = (
                parte
                .strip()
                .strip('"')
                .strip("'")
                .strip()
            )

            if categoria:

                categorias.append(
                    categoria
                )

    if not categorias:

        raise ValueError(
            "No se encontraron categorias."
        )

    return categorias


# ============================================================
# FRECUENCIAS DE CATEGORIAS
# ============================================================

def calcular_frecuencias_categorias(
    categorias
):

    frecuencias = {}

    for categoria in categorias:

        if categoria in frecuencias:

            frecuencias[
                categoria
            ] += 1

        else:

            frecuencias[
                categoria
            ] = 1

    return frecuencias


# ============================================================
# CONVERTIR CATEGORIAS NUMERICAS
# ============================================================

def convertir_categorias_numericas(
    categorias
):

    datos = []

    for categoria in categorias:

        try:

            datos.append(
                convertir_numero(
                    categoria
                )
            )

        except ValueError:

            raise ValueError(
                "Las categorias contienen "
                "al menos un valor no numerico."
            )

    return datos


# ============================================================
# TIPO 3
# MINI TABLA DE CATEGORIAS
# ============================================================

def cargar_mini_tabla(
    lineas
):

    """
    Formato:

        "categoria";"frecuencia"

    Ejemplo:

        "2,2";"3"
        "2,5";"1"
        "2,7";"3"
    """

    frecuencias = {}

    for linea in lineas:

        linea = limpiar_linea(
            linea
        )

        if linea is None:
            continue

        # ----------------------------------------------------
        # El separador del tipo 3 es ';'
        # ----------------------------------------------------

        partes = linea.split(
            ";"
        )

        partes = [
            parte.strip()
            .strip('"')
            .strip("'")
            for parte in partes
        ]

        if len(partes) < 2:

            raise ValueError(
                "El tipo 3 debe tener "
                "categoria;frecuencia."
            )

        categoria = partes[0]

        frecuencia = int(
            convertir_numero(
                partes[1]
            )
        )

        if frecuencia < 0:

            raise ValueError(
                "Las frecuencias no pueden "
                "ser negativas."
            )

        frecuencias[
            categoria
        ] = frecuencia

    if not frecuencias:

        raise ValueError(
            "No se encontraron datos "
            "en la mini tabla."
        )

    return frecuencias


# ============================================================
# TIPO 5
# INTERVALOS + FRECUENCIA
# ============================================================

def cargar_intervalos(
    lineas
):

    """
    Formato:

        "limite inferior";"limite superior";"frecuencia"

    Ejemplo:

        "15";"17";"4"
        "17";"19";"6"
        "19";"21";"16"
    """

    intervalos = []

    for linea in lineas:

        linea = limpiar_linea(
            linea
        )

        if linea is None:
            continue

        partes = linea.split(
            ";"
        )

        partes = [
            parte.strip()
            .strip('"')
            .strip("'")
            for parte in partes
        ]

        if len(partes) < 3:

            raise ValueError(
                "El tipo 5 debe tener "
                "limite inferior;limite superior;frecuencia."
            )

        li = convertir_numero(
            partes[0]
        )

        ls = convertir_numero(
            partes[1]
        )

        fi = int(
            convertir_numero(
                partes[2]
            )
        )

        if ls <= li:

            raise ValueError(
                "El limite superior debe ser "
                "mayor que el limite inferior."
            )

        if fi < 0:

            raise ValueError(
                "Las frecuencias no pueden "
                "ser negativas."
            )

        xi = (
            li + ls
        ) / 2

        intervalos.append({

            "li":
                li,

            "ls":
                ls,

            "fi":
                fi,

            "xi":
                xi
        })

    if not intervalos:

        raise ValueError(
            "No se encontraron intervalos validos."
        )

    return intervalos


# ============================================================
# PROCESAMIENTO GENERAL
# ============================================================

def procesar_csv(
    tipo,
    ruta
):

    lineas = leer_archivo_texto(
        ruta
    )

    if not lineas:

        raise ValueError(
            "El archivo CSV esta vacio."
        )

    # ========================================================
    # TIPO 1
    # ========================================================

    if tipo == 1:

        # ----------------------------------------------------
        # Detectar encabezado.
        # ----------------------------------------------------

        primera_linea = None

        for linea in lineas:

            linea = limpiar_linea(
                linea
            )

            if linea is not None:

                primera_linea = linea

                break

        if primera_linea is not None:

            if es_encabezado_tipo_1_2_4(
                primera_linea
            ):

                lineas = lineas[
                    lineas.index(
                        next(
                            x for x in lineas
                            if limpiar_linea(x)
                            is not None
                        )
                    ) + 1:
                    ]

        return cargar_datos_tomados(
            lineas
        )

    # ========================================================
    # TIPO 2
    # ========================================================

    elif tipo == 2:

        primera_linea = None

        for linea in lineas:

            linea = limpiar_linea(
                linea
            )

            if linea is not None:

                primera_linea = linea

                break

        if primera_linea is not None:

            if es_encabezado_tipo_1_2_4(
                primera_linea
            ):

                lineas = lineas[
                    lineas.index(
                        next(
                            x for x in lineas
                            if limpiar_linea(x)
                            is not None
                        )
                    ) + 1:
                    ]

        return cargar_categorias(
            lineas
        )

    # ========================================================
    # TIPO 3
    # ========================================================

    elif tipo == 3:

        return cargar_mini_tabla(
            lineas
        )

    # ========================================================
    # TIPO 4
    # ========================================================

    elif tipo == 4:

        primera_linea = None

        for linea in lineas:

            linea = limpiar_linea(
                linea
            )

            if linea is not None:

                primera_linea = linea

                break

        if primera_linea is not None:

            if es_encabezado_tipo_1_2_4(
                primera_linea
            ):

                lineas = lineas[
                    lineas.index(
                        next(
                            x for x in lineas
                            if limpiar_linea(x)
                            is not None
                        )
                    ) + 1:
                    ]

        return cargar_datos_tomados(
            lineas
        )

    # ========================================================
    # TIPO 5
    # ========================================================

    elif tipo == 5:

        return cargar_intervalos(
            lineas
        )

    else:

        raise ValueError(
            "Tipo de carga invalido."
        )