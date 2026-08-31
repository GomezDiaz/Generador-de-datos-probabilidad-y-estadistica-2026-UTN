import csv


# ============================================================
# LECTURA GENERAL DEL CSV
# ============================================================

def leer_csv(ruta):

    """
    Lee un archivo CSV.

    Permite separador:
        ,
        ;

    Devuelve una lista de filas.
    """

    with open(
        ruta,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as archivo:

        muestra = archivo.read(
            4096
        )

        archivo.seek(0)

        try:

            dialecto = csv.Sniffer().sniff(
                muestra,
                delimiters=",;"
            )

        except csv.Error:

            dialecto = csv.excel

        lector = csv.reader(
            archivo,
            dialecto
        )

        filas = []

        for fila in lector:

            fila = [
                elemento.strip()
                for elemento in fila
            ]

            if any(
                elemento != ""
                for elemento in fila
            ):

                filas.append(fila)

    return filas


# ============================================================
# CONVERSION DE NUMEROS
# ============================================================

def convertir_numero(valor):

    """
    Convierte un texto en numero.

    Permite:

        15.5
        15,5
    """

    valor = str(
        valor
    ).strip()

    if (
        "," in valor
        and "." not in valor
    ):

        valor = valor.replace(
            ",",
            "."
        )

    return float(valor)


# ============================================================
# DETECCION DE ENCABEZADO
# ============================================================

def quitar_encabezado(
    filas,
    tipo
):

    """
    Intenta determinar si la primera fila es
    un encabezado.

    Ejemplos:

        tiempo

        categoria,frecuencia

        limite_inferior,limite_superior,frecuencia
    """

    if not filas:

        return filas

    primera_fila = filas[0]

    try:

        # ----------------------------------------------------
        # Tipo 1 y 4
        # ----------------------------------------------------

        if tipo == 1 or tipo == 4:

            convertir_numero(
                primera_fila[0]
            )

        # ----------------------------------------------------
        # Tipo 3
        # ----------------------------------------------------

        elif tipo == 3:

            convertir_numero(
                primera_fila[1]
            )

        # ----------------------------------------------------
        # Tipo 5
        # ----------------------------------------------------

        elif tipo == 5:

            convertir_numero(
                primera_fila[0]
            )

            convertir_numero(
                primera_fila[1]
            )

            convertir_numero(
                primera_fila[2]
            )

        return filas

    except (
        ValueError,
        IndexError
    ):

        return filas[1:]


# ============================================================
# OPCION 1
# DATOS TOMADOS
# ============================================================

def cargar_datos_tomados(
    filas
):

    """
    CSV esperado:

        12
        15
        12
        18
        20
    """

    datos = []

    for fila in filas:

        if not fila:
            continue

        dato = convertir_numero(
            fila[0]
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
# OPCION 2
# CATEGORIAS
# ============================================================

def cargar_categorias(
    filas
):

    """
    CSV esperado:

        Bueno
        Malo
        Bueno
        Rechazado
    """

    categorias = []

    for fila in filas:

        if not fila:
            continue

        categoria = (
            fila[0].strip()
        )

        categorias.append(
            categoria
        )

    if not categorias:

        raise ValueError(
            "No se encontraron categorias."
        )

    return categorias


def calcular_frecuencias_categorias(
    categorias
):

    """
    Cuenta las apariciones de cada categoria.
    """

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
# OPCION 3
# MINI TABLA DE CATEGORIAS
# ============================================================

def cargar_mini_tabla(
    filas
):

    """
    CSV esperado:

        Bueno,7
        Malo,3
        Rechazado,2
    """

    frecuencias = {}

    for fila in filas:

        if len(fila) < 2:
            continue

        categoria = (
            fila[0].strip()
        )

        frecuencia = int(
            convertir_numero(
                fila[1]
            )
        )

        frecuencias[
            categoria
        ] = frecuencia

    if not frecuencias:

        raise ValueError(
            "No se encontraron categorias y frecuencias."
        )

    return frecuencias


# ============================================================
# OPCION 5
# INTERVALOS YA PROPORCIONADOS
# ============================================================

def cargar_intervalos(
    filas
):

    """
    CSV esperado:

        15,17,4
        17,19,6
        19,21,16
        21,23,3
        23,25,1

    Formato:

        limite inferior
        limite superior
        frecuencia
    """

    intervalos = []

    for fila in filas:

        if len(fila) < 3:
            continue

        li = convertir_numero(
            fila[0]
        )

        ls = convertir_numero(
            fila[1]
        )

        fi = int(
            convertir_numero(
                fila[2]
            )
        )

        # Marca de clase
        xi = (
            li + ls
        ) / 2

        intervalos.append({

            "li": li,

            "ls": ls,

            "fi": fi,

            "xi": xi
        })

    if not intervalos:

        raise ValueError(
            "No se encontraron intervalos validos."
        )

    return intervalos


# ============================================================
# PROCESAMIENTO GENERAL DEL CSV
# ============================================================

def procesar_csv(
    tipo,
    ruta
):

    """
    Procesa el CSV dependiendo del tipo
    seleccionado en el menu.

    Importante:
    Esta funcion NO realiza los calculos estadisticos.
    Solamente prepara los datos.
    """

    filas = leer_csv(
        ruta
    )

    if not filas:

        raise ValueError(
            "El archivo CSV esta vacio."
        )

    filas = quitar_encabezado(
        filas,
        tipo
    )

    if not filas:

        raise ValueError(
            "No hay datos despues del encabezado."
        )

    # ========================================================
    # TIPO 1
    # ========================================================

    if tipo == 1:

        return cargar_datos_tomados(
            filas
        )

    # ========================================================
    # TIPO 2
    # ========================================================

    elif tipo == 2:

        return cargar_categorias(
            filas
        )

    # ========================================================
    # TIPO 3
    # ========================================================

    elif tipo == 3:

        return cargar_mini_tabla(
            filas
        )

    # ========================================================
    # TIPO 4
    # ========================================================

    elif tipo == 4:

        return cargar_datos_tomados(
            filas
        )

    # ========================================================
    # TIPO 5
    # ========================================================

    elif tipo == 5:

        return cargar_intervalos(
            filas
        )

    else:

        raise ValueError(
            "Tipo de carga no valido."
        )