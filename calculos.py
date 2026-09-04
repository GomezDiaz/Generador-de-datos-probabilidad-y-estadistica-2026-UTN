import math
from collections import Counter


# ============================================================
# FUNCIONES BÁSICAS
# ============================================================

def calcular_media(datos):
    if not datos:
        return None

    return sum(datos) / len(datos)


def calcular_moda(datos):
    if not datos:
        return None

    frecuencias = Counter(datos)
    frecuencia_maxima = max(frecuencias.values())

    if frecuencia_maxima == 1:
        return None

    modas = [
        valor
        for valor, frecuencia in frecuencias.items()
        if frecuencia == frecuencia_maxima
    ]

    modas.sort()

    if len(modas) == 1:
        return modas[0]

    return modas


def calcular_mediana(datos):
    if not datos:
        return None

    ordenados = sorted(datos)
    n = len(ordenados)

    mitad = n // 2

    if n % 2 == 0:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2

    return ordenados[mitad]


def calcular_minimo(datos):
    return min(datos) if datos else None


def calcular_maximo(datos):
    return max(datos) if datos else None


def calcular_rango(datos):
    if not datos:
        return None

    return max(datos) - min(datos)


# ============================================================
# VARIANZA Y DESVÍO ESTÁNDAR MUESTRAL
# ============================================================

def calcular_varianza(datos):
    """
    Varianza muestral:

        S² = Σ(x - x̄)² / (n - 1)

    Se utiliza n-1 porque los datos representan una muestra.
    """

    n = len(datos)

    if n < 2:
        return None

    media = calcular_media(datos)

    suma = sum((x - media) ** 2 for x in datos)

    return suma / (n - 1)


def calcular_desvio(datos):
    varianza = calcular_varianza(datos)

    if varianza is None:
        return None

    return math.sqrt(varianza)


# ============================================================
# COEFICIENTE DE VARIACIÓN
# ============================================================

def calcular_coeficiente_variacion(promedio, desvio):
    """
    Devuelve el coeficiente de variación como proporción.

    Ejemplo:
        0.14 = 14%
    """

    if promedio is None or desvio is None or promedio == 0:
        return None

    return desvio / abs(promedio)


def calcular_coeficiente_variacion_porcentaje(promedio, desvio):
    cv = calcular_coeficiente_variacion(promedio, desvio)

    if cv is None:
        return None

    return cv * 100


# ============================================================
# ASIMETRÍA
# ============================================================

def calcular_asimetria(promedio, mediana, desvio):
    """
    Coeficiente de asimetría utilizado en U2:

        As = 3(x̄ - Me) / S
    """

    if promedio is None or mediana is None or desvio is None:
        return None

    if desvio == 0:
        return 0

    return 3 * (promedio - mediana) / desvio


def clasificar_asimetria(asimetria):
    if asimetria is None:
        return "No se puede determinar"

    if asimetria == 0:
        return "Simétrica"

    if asimetria > 0:
        return "Asimetría positiva (derecha)"

    return "Asimetría negativa (izquierda)"


def interpretar_asimetria(asimetria):
    if asimetria is None:
        return "No se puede determinar la asimetría."

    if asimetria == 0:
        return (
            "La distribución es simétrica. "
            "La media y la mediana tienden a coincidir."
        )

    direccion = clasificar_asimetria(asimetria)

    if abs(asimetria) <= 0.2:
        representatividad = (
            "La media sigue siendo representativa de la distribución "
            "porque |As| <= 0,20."
        )
    else:
        representatividad = (
            "La media deja de ser representativa porque |As| > 0,20. "
            "La mediana o la moda representan mejor los datos."
        )

    return f"{direccion}. {representatividad}"


# ============================================================
# LÍMITES MEDIA ± DESVÍO
# ============================================================

def calcular_limites(promedio, desvio):
    if promedio is None or desvio is None:
        return None, None

    li = promedio - desvio
    ls = promedio + desvio

    return li, ls


# ============================================================
# CUARTILES
# MÉTODO k(n+1)/4 CON INTERPOLACIÓN
# ============================================================

def calcular_cuartil(datos, k):
    """
    Método utilizado para datos sin agrupar:

        Pk = k(n + 1) / 4

    Se utiliza interpolación cuando la posición no es entera.
    """

    if not datos:
        return None

    if k not in (1, 2, 3):
        raise ValueError("El cuartil debe ser 1, 2 o 3.")

    ordenados = sorted(datos)
    n = len(ordenados)

    posicion = k * (n + 1) / 4

    # Caso inferior
    if posicion <= 1:
        return ordenados[0]

    # Caso superior
    if posicion >= n:
        return ordenados[-1]

    inferior = int(math.floor(posicion))
    decimal = posicion - inferior

    valor_inferior = ordenados[inferior - 1]
    valor_superior = ordenados[inferior]

    return valor_inferior + decimal * (
        valor_superior - valor_inferior
    )


def calcular_cuartiles(datos):
    return {
        "Q1": calcular_cuartil(datos, 1),
        "Q2": calcular_cuartil(datos, 2),
        "Q3": calcular_cuartil(datos, 3)
    }


# ============================================================
# RANGO INTERCUARTÍLICO Y OUTLIERS
# ============================================================

def calcular_iqr(q1, q3):
    if q1 is None or q3 is None:
        return None

    return q3 - q1


def calcular_limites_boxplot(q1, q3):
    """
    Límites utilizados para detectar valores atípicos:

        LI = Q1 - 1,5 * IQR
        LS = Q3 + 1,5 * IQR
    """

    iqr = calcular_iqr(q1, q3)

    if iqr is None:
        return None, None

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    return limite_inferior, limite_superior


def detectar_outliers(datos, q1, q3):
    if not datos or q1 is None or q3 is None:
        return []

    limite_inferior, limite_superior = calcular_limites_boxplot(
        q1, q3
    )

    outliers = [
        x for x in datos
        if x < limite_inferior or x > limite_superior
    ]

    return sorted(outliers)


def calcular_bigotes(datos, q1, q3):
    """
    Los bigotes no necesariamente llegan al mínimo y máximo.
    Llegan hasta los valores más extremos que todavía no son
    considerados atípicos.
    """

    if not datos:
        return None, None

    limite_inferior, limite_superior = calcular_limites_boxplot(
        q1, q3
    )

    datos_validos_inferior = [
        x for x in datos
        if x >= limite_inferior
    ]

    datos_validos_superior = [
        x for x in datos
        if x <= limite_superior
    ]

    if datos_validos_inferior:
        bigote_inferior = min(datos_validos_inferior)
    else:
        bigote_inferior = min(datos)

    if datos_validos_superior:
        bigote_superior = max(datos_validos_superior)
    else:
        bigote_superior = max(datos)

    return bigote_inferior, bigote_superior


# ============================================================
# MEDIDAS COMPLETAS PARA DATOS SIN AGRUPAR
# ============================================================

def calcular_medidas(datos):

    if not datos:
        return {}

    datos = [float(x) for x in datos]

    promedio = calcular_media(datos)
    mediana = calcular_mediana(datos)
    moda = calcular_moda(datos)

    varianza = calcular_varianza(datos)
    desvio = calcular_desvio(datos)

    cv = calcular_coeficiente_variacion(
        promedio,
        desvio
    )

    cv_porcentaje = calcular_coeficiente_variacion_porcentaje(
        promedio,
        desvio
    )

    asimetria = calcular_asimetria(
        promedio,
        mediana,
        desvio
    )

    cuartiles = calcular_cuartiles(datos)

    q1 = cuartiles["Q1"]
    q2 = cuartiles["Q2"]
    q3 = cuartiles["Q3"]

    iqr = calcular_iqr(q1, q3)

    limite_box_inferior, limite_box_superior = (
        calcular_limites_boxplot(q1, q3)
    )

    bigote_inferior, bigote_superior = calcular_bigotes(
        datos,
        q1,
        q3
    )

    outliers = detectar_outliers(
        datos,
        q1,
        q3
    )

    limite_inferior, limite_superior = calcular_limites(
        promedio,
        desvio
    )

    return {
        "n": len(datos),

        "minimo": calcular_minimo(datos),
        "maximo": calcular_maximo(datos),
        "rango": calcular_rango(datos),

        "media": promedio,
        "mediana": mediana,
        "moda": moda,

        "varianza": varianza,
        "desvio": desvio,

        "cv": cv,
        "cv_porcentaje": cv_porcentaje,

        "asimetria": asimetria,
        "clasificacion_asimetria": clasificar_asimetria(
            asimetria
        ),

        "Q1": q1,
        "Q2": q2,
        "Q3": q3,
        "IQR": iqr,

        "limite_box_inferior": limite_box_inferior,
        "limite_box_superior": limite_box_superior,

        "bigote_inferior": bigote_inferior,
        "bigote_superior": bigote_superior,

        "outliers": outliers,

        "LI": limite_inferior,
        "LS": limite_superior
    }


# ============================================================
# CONSTRUCCIÓN DE INTERVALOS
# ============================================================

def construir_intervalos(datos):

    if not datos:
        return []

    datos = sorted(float(x) for x in datos)

    n = len(datos)

    minimo = min(datos)
    maximo = max(datos)

    if minimo == maximo:
        return [{
            "li": minimo,
            "ls": maximo,
            "frecuencia": n,
            "hi": 1,
            "hiporcentaje": 100,
            "xi": minimo,
            "frecuencia_acumulada": n,
            "hi_acumulada": 1,
            "hi_acumulada_porcentaje": 100
        }]

    # Regla de Sturges
    cantidad_intervalos = math.ceil(
        1 + 3.3 * math.log10(n)
    )

    amplitud = (maximo - minimo) / cantidad_intervalos

    # Redondeo hacia arriba para obtener intervalos sencillos
    if amplitud >= 1:
        amplitud = math.ceil(amplitud)

    elif amplitud >= 0.1:
        amplitud = math.ceil(amplitud * 10) / 10

    elif amplitud >= 0.01:
        amplitud = math.ceil(amplitud * 100) / 100

    else:
        amplitud = math.ceil(amplitud * 1000) / 1000

    intervalos = []

    li = minimo

    for i in range(cantidad_intervalos):

        ls = li + amplitud

        if i == cantidad_intervalos - 1:
            ls = max(ls, maximo)

        frecuencia = 0

        for valor in datos:

            if i == cantidad_intervalos - 1:
                if li <= valor <= ls:
                    frecuencia += 1

            else:
                if li <= valor < ls:
                    frecuencia += 1

        xi = (li + ls) / 2

        intervalos.append({
            "li": li,
            "ls": ls,
            "frecuencia": frecuencia,
            "xi": xi
        })

        li = ls

    # Frecuencias acumuladas
    acumulada = 0

    for intervalo in intervalos:

        fi = intervalo["frecuencia"]

        hi = fi / n

        acumulada += fi

        intervalo["hi"] = hi
        intervalo["hiporcentaje"] = hi * 100

        intervalo["frecuencia_acumulada"] = acumulada
        intervalo["hi_acumulada"] = acumulada / n
        intervalo["hi_acumulada_porcentaje"] = (
            acumulada / n
        ) * 100

    return intervalos


# ============================================================
# MEDIDAS PARA DATOS AGRUPADOS
# ============================================================

def calcular_media_agrupada(intervalos):

    n = sum(i["frecuencia"] for i in intervalos)

    if n == 0:
        return None

    suma = sum(
        i["xi"] * i["frecuencia"]
        for i in intervalos
    )

    return suma / n


def encontrar_intervalo_posicion(intervalos, posicion):

    for intervalo in intervalos:

        if intervalo["frecuencia_acumulada"] >= posicion:
            return intervalo

    return intervalos[-1]


def calcular_mediana_agrupada(intervalos):

    n = sum(i["frecuencia"] for i in intervalos)

    if n == 0:
        return None

    posicion = n / 2

    intervalo = encontrar_intervalo_posicion(
        intervalos,
        posicion
    )

    indice = intervalos.index(intervalo)

    frecuencia_anterior = 0

    if indice > 0:
        frecuencia_anterior = (
            intervalos[indice - 1]["frecuencia_acumulada"]
        )

    frecuencia_intervalo = intervalo["frecuencia"]

    amplitud = intervalo["ls"] - intervalo["li"]

    if frecuencia_intervalo == 0:
        return intervalo["li"]

    return (
        intervalo["li"]
        + amplitud
        * (
            (posicion - frecuencia_anterior)
            / frecuencia_intervalo
        )
    )


def calcular_moda_agrupada(intervalos):

    if not intervalos:
        return None

    intervalo_modal = max(
        intervalos,
        key=lambda x: x["frecuencia"]
    )

    indice = intervalos.index(intervalo_modal)

    frecuencia_modal = intervalo_modal["frecuencia"]

    frecuencia_anterior = 0
    frecuencia_siguiente = 0

    if indice > 0:
        frecuencia_anterior = (
            intervalos[indice - 1]["frecuencia"]
        )

    if indice < len(intervalos) - 1:
        frecuencia_siguiente = (
            intervalos[indice + 1]["frecuencia"]
        )

    delta1 = frecuencia_modal - frecuencia_anterior
    delta2 = frecuencia_modal - frecuencia_siguiente

    amplitud = intervalo_modal["ls"] - intervalo_modal["li"]

    denominador = delta1 + delta2

    if denominador == 0:
        return intervalo_modal["xi"]

    return (
        intervalo_modal["li"]
        + amplitud * delta1 / denominador
    )


def calcular_cuartil_agrupado(intervalos, k):

    n = sum(i["frecuencia"] for i in intervalos)

    if n == 0:
        return None

    posicion = k * n / 4

    intervalo = encontrar_intervalo_posicion(
        intervalos,
        posicion
    )

    indice = intervalos.index(intervalo)

    frecuencia_anterior = 0

    if indice > 0:
        frecuencia_anterior = (
            intervalos[indice - 1]["frecuencia_acumulada"]
        )

    frecuencia_intervalo = intervalo["frecuencia"]

    amplitud = intervalo["ls"] - intervalo["li"]

    if frecuencia_intervalo == 0:
        return intervalo["li"]

    return (
        intervalo["li"]
        + amplitud
        * (
            (posicion - frecuencia_anterior)
            / frecuencia_intervalo
        )
    )


def calcular_varianza_agrupada(intervalos, media):

    n = sum(i["frecuencia"] for i in intervalos)

    if n < 2:
        return None

    suma = sum(
        i["frecuencia"] * (i["xi"] - media) ** 2
        for i in intervalos
    )

    return suma / (n - 1)


def calcular_medidas_agrupadas(intervalos):

    if not intervalos:
        return {}

    n = sum(i["frecuencia"] for i in intervalos)

    if n == 0:
        return {}

    media = calcular_media_agrupada(intervalos)

    mediana = calcular_mediana_agrupada(intervalos)

    moda = calcular_moda_agrupada(intervalos)

    varianza = calcular_varianza_agrupada(
        intervalos,
        media
    )

    desvio = (
        math.sqrt(varianza)
        if varianza is not None
        else None
    )

    q1 = calcular_cuartil_agrupado(intervalos, 1)
    q2 = calcular_cuartil_agrupado(intervalos, 2)
    q3 = calcular_cuartil_agrupado(intervalos, 3)

    iqr = calcular_iqr(q1, q3)

    cv = calcular_coeficiente_variacion(
        media,
        desvio
    )

    cv_porcentaje = calcular_coeficiente_variacion_porcentaje(
        media,
        desvio
    )

    asimetria = calcular_asimetria(
        media,
        mediana,
        desvio
    )

    # Para datos agrupados no conocemos exactamente
    # el mínimo y máximo originales.
    minimo = intervalos[0]["li"]
    maximo = intervalos[-1]["ls"]

    rango = maximo - minimo

    li, ls = calcular_limites(
        media,
        desvio
    )

    return {
        "n": n,

        "minimo": minimo,
        "maximo": maximo,
        "rango": rango,

        "media": media,
        "mediana": mediana,
        "moda": moda,

        "varianza": varianza,
        "desvio": desvio,

        "cv": cv,
        "cv_porcentaje": cv_porcentaje,

        "asimetria": asimetria,
        "clasificacion_asimetria": clasificar_asimetria(
            asimetria
        ),

        "Q1": q1,
        "Q2": q2,
        "Q3": q3,
        "IQR": iqr,

        "LI": li,
        "LS": ls
    }


# ============================================================
# EXPANDIR UNA MINI TABLA
# ============================================================

def expandir_frecuencias(frecuencias):

    datos = []

    for categoria, frecuencia in frecuencias:

        frecuencia = int(frecuencia)

        for _ in range(frecuencia):
            datos.append(categoria)

    return datos