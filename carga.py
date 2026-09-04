import csv


# ============================================================
# LECTURA GENERAL
# ============================================================

def leer_archivo_texto(ruta):

    with open(
        ruta,
        "r",
        encoding="utf-8-sig"
    ) as archivo:

        return archivo.readlines()


# ============================================================
# CONVERSIÓN DE NÚMEROS
# ============================================================

def convertir_numero(valor):

    valor = str(valor).strip()

    # Quitar comillas
    valor = valor.strip('"').strip("'")

    # Decimal con coma
    if "," in valor and "." not in valor:
        valor = valor.replace(",", ".")

    # Formato tipo 1.234,56
    elif "," in valor and "." in valor:

        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")

    return float(valor)


# ============================================================
# LIMPIEZA
# ============================================================

def limpiar_linea(linea):

    return linea.strip()


def obtener_lineas_validas(lineas):

    return [
        limpiar_linea(linea)
        for linea in lineas
        if limpiar_linea(linea)
    ]


# ============================================================
# DETECTAR ENCABEZADOS
# ============================================================

def parece_encabezado(linea):

    texto = linea.lower()

    palabras = [
        "categoria",
        "categoría",
        "frecuencia",
        "dato",
        "datos",
        "valor",
        "limite",
        "límite",
        "inferior",
        "superior",
        "fi"
    ]

    return any(palabra in texto for palabra in palabras)


# ============================================================
# MÉTODO 1
# CATEGORÍAS
#
# Puede ser:
#
# 2,2
# 2,5
# 2,7
#
# o:
#
# Burbujas
# Manchas
# Costras
# ============================================================

def cargar_categorias(lineas):

    datos = []

    for linea in obtener_lineas_validas(lineas):

        if parece_encabezado(linea):
            continue

        partes = linea.split(";")

        for parte in partes:

            parte = parte.strip()

            if not parte:
                continue

            parte = parte.strip('"').strip("'")

            datos.append(parte)

    return datos


def convertir_categorias_numericas(categorias):

    datos = []

    for categoria in categorias:

        try:
            datos.append(
                convertir_numero(categoria)
            )

        except ValueError:
            return None

    return datos


# ============================================================
# MÉTODO 2
# MINI TABLA DE CATEGORÍAS
#
# "categoria";"frecuencia"
#
# Ejemplo:
#
# "A";"5"
# "B";"3"
# "C";"7"
# ============================================================

def cargar_mini_tabla(lineas):

    tabla = []

    for linea in obtener_lineas_validas(lineas):

        if parece_encabezado(linea):
            continue

        partes = list(
            csv.reader(
                [linea],
                delimiter=";"
            )
        )[0]

        if len(partes) < 2:
            continue

        categoria = partes[0].strip()

        categoria = (
            categoria
            .strip('"')
            .strip("'")
        )

        frecuencia = convertir_numero(
            partes[1]
        )

        tabla.append(
            (categoria, frecuencia)
        )

    return tabla


# ============================================================
# MÉTODO 3
# DATOS PARA ARMAR INTERVALOS
#
# Igual que el método 1, pero destinado a
# datos cuantitativos que luego serán agrupados.
# ============================================================

def cargar_datos_intervalos(lineas):

    datos = []

    for linea in obtener_lineas_validas(lineas):

        if parece_encabezado(linea):
            continue

        partes = linea.split(";")

        for parte in partes:

            parte = parte.strip()

            if not parte:
                continue

            datos.append(
                convertir_numero(parte)
            )

    return datos


# ============================================================
# MÉTODO 4
# LÍMITES + FRECUENCIA
#
# "limite inferior";"limite superior";"frecuencia"
# ============================================================

def cargar_intervalos(lineas):

    intervalos = []

    for linea in obtener_lineas_validas(lineas):

        if parece_encabezado(linea):
            continue

        partes = list(
            csv.reader(
                [linea],
                delimiter=";"
            )
        )[0]

        if len(partes) < 3:
            continue

        li = convertir_numero(partes[0])
        ls = convertir_numero(partes[1])
        frecuencia = convertir_numero(partes[2])

        xi = (li + ls) / 2

        intervalos.append({
            "li": li,
            "ls": ls,
            "frecuencia": int(frecuencia),
            "xi": xi
        })

    # Calcular frecuencias acumuladas
    n = sum(
        intervalo["frecuencia"]
        for intervalo in intervalos
    )

    acumulada = 0

    for intervalo in intervalos:

        fi = intervalo["frecuencia"]

        acumulada += fi

        hi = fi / n if n > 0 else 0

        intervalo["hi"] = hi
        intervalo["hiporcentaje"] = hi * 100

        intervalo["frecuencia_acumulada"] = acumulada

        intervalo["hi_acumulada"] = (
            acumulada / n
            if n > 0
            else 0
        )

        intervalo["hi_acumulada_porcentaje"] = (
            intervalo["hi_acumulada"] * 100
        )

    return intervalos


# ============================================================
# PROCESADOR PRINCIPAL
# ============================================================

def procesar_csv(tipo, ruta):

    lineas = leer_archivo_texto(ruta)

    if tipo == 1:

        return {
            "tipo": 1,
            "datos": cargar_categorias(lineas)
        }

    elif tipo == 2:

        return {
            "tipo": 2,
            "tabla": cargar_mini_tabla(lineas)
        }

    elif tipo == 3:

        return {
            "tipo": 3,
            "datos": cargar_datos_intervalos(lineas)
        }

    elif tipo == 4:

        return {
            "tipo": 4,
            "intervalos": cargar_intervalos(lineas)
        }

    else:

        raise ValueError(
            "El tipo de archivo debe ser 1, 2, 3 o 4."
        )