import math


# ============================================================
# MEDIDAS PARA DATOS INDIVIDUALES
# ============================================================

def calcular_media(datos):

    return sum(datos) / len(datos)


# ============================================================
# MODA
# ============================================================

def calcular_moda(datos):

    frecuencias = {}

    for dato in datos:

        if dato in frecuencias:
            frecuencias[dato] += 1

        else:
            frecuencias[dato] = 1

    frecuencia_maxima = max(
        frecuencias.values()
    )

    # Si todos aparecen una sola vez,
    # no existe moda.
    if frecuencia_maxima == 1:

        return []

    modas = []

    for valor, frecuencia in frecuencias.items():

        if frecuencia == frecuencia_maxima:

            modas.append(
                valor
            )

    return sorted(
        modas
    )


# ============================================================
# MEDIANA
# ============================================================

def calcular_mediana(datos):

    datos_ordenados = sorted(
        datos
    )

    n = len(
        datos_ordenados
    )

    posicion_central = n // 2

    # Cantidad impar
    if n % 2 != 0:

        return datos_ordenados[
            posicion_central
        ]

    # Cantidad par
    valor1 = datos_ordenados[
        posicion_central - 1
    ]

    valor2 = datos_ordenados[
        posicion_central
    ]

    return (
        valor1 + valor2
    ) / 2


# ============================================================
# MINIMO
# ============================================================

def calcular_minimo(datos):

    return min(
        datos
    )


# ============================================================
# MAXIMO
# ============================================================

def calcular_maximo(datos):

    return max(
        datos
    )


# ============================================================
# RANGO
# ============================================================

def calcular_rango(datos):

    return (
        calcular_maximo(datos)
        -
        calcular_minimo(datos)
    )


# ============================================================
# VARIANZA
# ============================================================

def calcular_varianza(datos):

    promedio = calcular_media(
        datos
    )

    suma = 0

    for dato in datos:

        suma += (
            dato - promedio
        ) ** 2

    return (
        suma / len(datos)
    )


# ============================================================
# DESVIO ESTANDAR
# ============================================================

def calcular_desvio(datos):

    return math.sqrt(
        calcular_varianza(datos)
    )


# ============================================================
# COEFICIENTE DE VARIACION
# ============================================================

def calcular_coeficiente_variacion(
    promedio,
    desvio
):

    """
    Coeficiente de variacion:

              S
        CV = ---
              X

    """

    if promedio == 0:

        return None

    return (
        desvio
        /
        abs(promedio)
    )


def calcular_coeficiente_variacion_porcentaje(
    promedio,
    desvio
):

    """
    Coeficiente de variacion porcentual:

               S
        CV% = --- * 100
               X
    """

    cv = calcular_coeficiente_variacion(
        promedio,
        desvio
    )

    if cv is None:

        return None

    return cv * 100


# ============================================================
# ASIMETRIA DE PEARSON
# ============================================================

def calcular_asimetria(
    promedio,
    mediana,
    desvio
):

    """
    As = 3(media - mediana) / S
    """

    if desvio == 0:

        return 0

    return (
        3
        *
        (
            promedio
            -
            mediana
        )
        /
        desvio
    )


# ============================================================
# CLASIFICACION DE ASIMETRIA
# ============================================================

def clasificar_asimetria(
    asimetria
):

    tolerancia = 1e-10

    if abs(asimetria) < tolerancia:

        return "Simetrica"

    elif asimetria > 0:

        return (
            "Asimetria positiva (derecha)"
        )

    else:

        return (
            "Asimetria negativa (izquierda)"
        )


# ============================================================
# LIMITES ASOCIADOS A LA MEDIA
# ============================================================

def calcular_limites(
    promedio,
    desvio
):

    """
    Calcula:

        LI = media - desvio

        LS = media + desvio

    """

    limite_inferior = (
        promedio - desvio
    )

    limite_superior = (
        promedio + desvio
    )

    return (
        limite_inferior,
        limite_superior
    )


# ============================================================
# CUARTILES
# ============================================================

def calcular_cuartil(
    datos,
    k
):

    """
    Posicion:

              k(n + 1)
        P = -----------
                  4

    k = 1 -> Q1
    k = 2 -> Q2
    k = 3 -> Q3

    Se realiza interpolacion.
    """

    datos_ordenados = sorted(
        datos
    )

    n = len(
        datos_ordenados
    )

    posicion = (
        k * (n + 1)
    ) / 4

    # Posicion inferior al primer dato.
    if posicion <= 1:

        return datos_ordenados[0]

    # Posicion superior al ultimo dato.
    if posicion >= n:

        return datos_ordenados[-1]

    posicion_inferior = math.floor(
        posicion
    )

    parte_decimal = (
        posicion
        -
        posicion_inferior
    )

    valor_inferior = datos_ordenados[
        posicion_inferior - 1
    ]

    valor_superior = datos_ordenados[
        posicion_inferior
    ]

    return (
        valor_inferior
        +
        parte_decimal
        *
        (
            valor_superior
            -
            valor_inferior
        )
    )


def calcular_cuartiles(datos):

    q1 = calcular_cuartil(
        datos,
        1
    )

    q2 = calcular_cuartil(
        datos,
        2
    )

    q3 = calcular_cuartil(
        datos,
        3
    )

    return (
        q1,
        q2,
        q3
    )


# ============================================================
# MEDIDAS COMPLETAS PARA DATOS INDIVIDUALES
# ============================================================

def calcular_medidas(datos):

    promedio = calcular_media(
        datos
    )

    mediana = calcular_mediana(
        datos
    )

    desvio = calcular_desvio(
        datos
    )

    q1, q2, q3 = calcular_cuartiles(
        datos
    )

    asimetria = calcular_asimetria(
        promedio,
        mediana,
        desvio
    )

    limite_inferior, limite_superior = (
        calcular_limites(
            promedio,
            desvio
        )
    )

    return {

        "n":
            len(datos),

        "minimo":
            calcular_minimo(datos),

        "maximo":
            calcular_maximo(datos),

        "rango":
            calcular_rango(datos),

        "media":
            promedio,

        "moda":
            calcular_moda(datos),

        "mediana":
            mediana,

        "varianza":
            calcular_varianza(datos),

        "desvio":
            desvio,

        "coeficiente_variacion":
            calcular_coeficiente_variacion(
                promedio,
                desvio
            ),

        "coeficiente_variacion_porcentaje":
            calcular_coeficiente_variacion_porcentaje(
                promedio,
                desvio
            ),

        "asimetria":
            asimetria,

        "tipo_asimetria":
            clasificar_asimetria(
                asimetria
            ),

        "q1":
            q1,

        "q2":
            q2,

        "q3":
            q3,

        "li":
            limite_inferior,

        "ls":
            limite_superior
    }


# ============================================================
# CONSTRUCCION DE INTERVALOS
# ============================================================

def construir_intervalos(datos):

    minimo = min(
        datos
    )

    maximo = max(
        datos
    )

    n = len(
        datos
    )

    rango = (
        maximo - minimo
    )

    # Todos los datos son iguales.
    if rango == 0:

        return [
            {
                "li": minimo,
                "ls": maximo,
                "fi": n,
                "xi": minimo
            }
        ]

    # --------------------------------------------------------
    # STURGES
    # --------------------------------------------------------

    cantidad_intervalos = (
        1
        +
        3.3
        *
        math.log10(n)
    )

    cantidad_intervalos = math.ceil(
        cantidad_intervalos
    )

    # --------------------------------------------------------
    # AMPLITUD
    # --------------------------------------------------------

    amplitud_exacta = (
        rango
        /
        cantidad_intervalos
    )

    if amplitud_exacta >= 1:

        decimales = 0

    elif amplitud_exacta >= 0.1:

        decimales = 1

    elif amplitud_exacta >= 0.01:

        decimales = 2

    else:

        decimales = 3

    factor = (
        10 ** decimales
    )

    amplitud = (
        math.ceil(
            amplitud_exacta
            *
            factor
        )
        /
        factor
    )

    # --------------------------------------------------------
    # CREAR INTERVALOS
    # --------------------------------------------------------

    intervalos = []

    limite_inferior = minimo

    for i in range(
        cantidad_intervalos
    ):

        limite_superior = (
            limite_inferior
            +
            amplitud
        )

        if (
            i == cantidad_intervalos - 1
            and
            limite_superior < maximo
        ):

            limite_superior = maximo

        if i == cantidad_intervalos - 1:

            frecuencia = sum(
                limite_inferior
                <= dato
                <= limite_superior
                for dato in datos
            )

        else:

            frecuencia = sum(
                limite_inferior
                <= dato
                <
                limite_superior
                for dato in datos
            )

        xi = (
            limite_inferior
            +
            limite_superior
        ) / 2

        intervalos.append(
            {
                "li": limite_inferior,
                "ls": limite_superior,
                "fi": frecuencia,
                "xi": xi
            }
        )

        limite_inferior = (
            limite_superior
        )

    return intervalos


# ============================================================
# MEDIDAS PARA DATOS AGRUPADOS
# ============================================================

def calcular_medidas_agrupadas(
    intervalos
):

    n = sum(
        intervalo["fi"]
        for intervalo in intervalos
    )

    if n == 0:

        raise ValueError(
            "La suma de las frecuencias debe ser mayor que cero."
        )

    # --------------------------------------------------------
    # MEDIA
    # --------------------------------------------------------

    suma_xifi = 0

    for intervalo in intervalos:

        suma_xifi += (
            intervalo["xi"]
            *
            intervalo["fi"]
        )

    promedio = (
        suma_xifi / n
    )

    # --------------------------------------------------------
    # FRECUENCIA ACUMULADA
    # --------------------------------------------------------

    frecuencia_acumulada = []

    acumulada = 0

    for intervalo in intervalos:

        acumulada += (
            intervalo["fi"]
        )

        frecuencia_acumulada.append(
            acumulada
        )

    # --------------------------------------------------------
    # MODA
    # --------------------------------------------------------

    indice_modal = max(
        range(
            len(intervalos)
        ),
        key=lambda i:
            intervalos[i]["fi"]
    )

    intervalo_modal = (
        intervalos[
            indice_modal
        ]
    )

    if indice_modal > 0:

        frecuencia_anterior = (
            intervalos[
                indice_modal - 1
            ]["fi"]
        )

    else:

        frecuencia_anterior = 0

    if (
        indice_modal
        <
        len(intervalos) - 1
    ):

        frecuencia_siguiente = (
            intervalos[
                indice_modal + 1
            ]["fi"]
        )

    else:

        frecuencia_siguiente = 0

    delta1 = (
        intervalo_modal["fi"]
        -
        frecuencia_anterior
    )

    delta2 = (
        intervalo_modal["fi"]
        -
        frecuencia_siguiente
    )

    amplitud = (
        intervalo_modal["ls"]
        -
        intervalo_modal["li"]
    )

    if (
        delta1 + delta2
        != 0
    ):

        moda = (
            intervalo_modal["li"]
            +
            amplitud
            *
            delta1
            /
            (
                delta1
                +
                delta2
            )
        )

    else:

        moda = (
            intervalo_modal["xi"]
        )

    # --------------------------------------------------------
    # CUARTILES AGRUPADOS
    # --------------------------------------------------------

    def calcular_cuartil_agrupado(
        k
    ):

        posicion = (
            k * n
        ) / 4

        indice = 0

        for i, frecuencia in enumerate(
            frecuencia_acumulada
        ):

            if frecuencia >= posicion:

                indice = i

                break

        intervalo = (
            intervalos[
                indice
            ]
        )

        if indice > 0:

            frecuencia_anterior = (
                frecuencia_acumulada[
                    indice - 1
                ]
            )

        else:

            frecuencia_anterior = 0

        fi = (
            intervalo["fi"]
        )

        amplitud = (
            intervalo["ls"]
            -
            intervalo["li"]
        )

        return (
            intervalo["li"]
            +
            amplitud
            *
            (
                posicion
                -
                frecuencia_anterior
            )
            /
            fi
        )

    q1 = calcular_cuartil_agrupado(
        1
    )

    q2 = calcular_cuartil_agrupado(
        2
    )

    q3 = calcular_cuartil_agrupado(
        3
    )

    mediana = q2

    # --------------------------------------------------------
    # VARIANZA
    # --------------------------------------------------------

    suma_varianza = 0

    for intervalo in intervalos:

        suma_varianza += (
            (
                intervalo["xi"]
                -
                promedio
            ) ** 2
            *
            intervalo["fi"]
        )

    varianza = (
        suma_varianza
        /
        n
    )

    # --------------------------------------------------------
    # DESVIO
    # --------------------------------------------------------

    desvio = math.sqrt(
        varianza
    )

    # --------------------------------------------------------
    # ASIMETRIA
    # --------------------------------------------------------

    asimetria = calcular_asimetria(
        promedio,
        mediana,
        desvio
    )

    # --------------------------------------------------------
    # COEFICIENTE DE VARIACION
    # --------------------------------------------------------

    cv = calcular_coeficiente_variacion(
        promedio,
        desvio
    )

    cv_porcentaje = (
        calcular_coeficiente_variacion_porcentaje(
            promedio,
            desvio
        )
    )

    # --------------------------------------------------------
    # RANGO DE LOS INTERVALOS
    # --------------------------------------------------------

    rango = (
        intervalos[-1]["ls"]
        -
        intervalos[0]["li"]
    )

    return {

        "n":
            n,

        "minimo":
            intervalos[0]["li"],

        "maximo":
            intervalos[-1]["ls"],

        "rango":
            rango,

        "media":
            promedio,

        "moda":
            moda,

        "mediana":
            mediana,

        "varianza":
            varianza,

        "desvio":
            desvio,

        "coeficiente_variacion":
            cv,

        "coeficiente_variacion_porcentaje":
            cv_porcentaje,

        "asimetria":
            asimetria,

        "tipo_asimetria":
            clasificar_asimetria(
                asimetria
            ),

        "q1":
            q1,

        "q2":
            q2,

        "q3":
            q3,

        "li":
            promedio - desvio,

        "ls":
            promedio + desvio
    }