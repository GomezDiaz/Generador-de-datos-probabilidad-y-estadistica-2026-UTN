import math


# ============================================================
# CALCULOS PARA DATOS INDIVIDUALES
# ============================================================

def calcular_media(datos):

    return sum(datos) / len(datos)


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

    if frecuencia_maxima == 1:
        return []

    modas = []

    for valor, frecuencia in frecuencias.items():

        if frecuencia == frecuencia_maxima:
            modas.append(valor)

    return sorted(modas)


def calcular_mediana(datos):

    datos_ordenados = sorted(datos)

    n = len(datos_ordenados)

    posicion_central = n // 2

    if n % 2 != 0:

        return datos_ordenados[
            posicion_central
        ]

    valor1 = datos_ordenados[
        posicion_central - 1
    ]

    valor2 = datos_ordenados[
        posicion_central
    ]

    return (
        valor1 + valor2
    ) / 2


def calcular_minimo(datos):

    return min(datos)


def calcular_maximo(datos):

    return max(datos)


def calcular_rango(datos):

    return (
        calcular_maximo(datos)
        -
        calcular_minimo(datos)
    )


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


def calcular_desvio(datos):

    return math.sqrt(
        calcular_varianza(datos)
    )


# ============================================================
# NUEVO
# COEFICIENTE DE VARIACION
# ============================================================

def calcular_coeficiente_variacion(
    promedio,
    desvio
):

    """
    Coeficiente de variacion porcentual:

            S
    CV% = ----- * 100
           x_barra

    Permite expresar la dispersion de forma relativa.
    """

    # No se puede dividir por cero.
    if promedio == 0:
        return None

    return (
        desvio
        /
        abs(promedio)
    ) * 100


# ============================================================
# NUEVO
# ASIMETRIA DE PEARSON
# ============================================================

def calcular_asimetria(
    promedio,
    mediana,
    desvio
):

    """
    Segunda formula de asimetria de Pearson:

              3(x_barra - Me)
        As = -----------------
                     S

    donde:

        x_barra = media
        Me      = mediana
        S       = desvio estandar
    """

    # Si el desvio es cero, todos los datos
    # son iguales y la distribucion no presenta
    # dispersion.

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


def clasificar_asimetria(
    asimetria
):

    """
    Clasifica la distribucion de acuerdo
    con el signo de la asimetria.

    As > 0 -> asimetria positiva / derecha

    As < 0 -> asimetria negativa / izquierda

    As = 0 -> simetrica
    """

    # Se utiliza una pequeña tolerancia para evitar
    # clasificar como asimetrico un resultado como
    # 0.00000000001 causado por los decimales
    # de punto flotante.

    tolerancia = 1e-10

    if abs(asimetria) < tolerancia:

        return "Simetrica"

    elif asimetria > 0:

        return "Asimetria positiva (hacia la derecha)"

    else:

        return "Asimetria negativa (hacia la izquierda)"


# ============================================================
# CUARTILES
# ============================================================

def calcular_cuartil(
    datos,
    k
):

    datos_ordenados = sorted(
        datos
    )

    n = len(
        datos_ordenados
    )

    posicion = (
        k * (n + 1)
    ) / 4

    if posicion <= 1:

        return datos_ordenados[0]

    if posicion >= n:

        return datos_ordenados[-1]

    posicion_inferior = math.floor(
        posicion
    )

    decimal = (
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

    resultado = (
        valor_inferior
        +
        decimal
        *
        (
            valor_superior
            -
            valor_inferior
        )
    )

    return resultado


def calcular_cuartiles(
    datos
):

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

    return q1, q2, q3


# ============================================================
# TODAS LAS MEDIDAS PARA DATOS INDIVIDUALES
# ============================================================

def calcular_medidas(
    datos
):

    minimo = calcular_minimo(
        datos
    )

    maximo = calcular_maximo(
        datos
    )

    rango = calcular_rango(
        datos
    )

    promedio = calcular_media(
        datos
    )

    moda = calcular_moda(
        datos
    )

    mediana = calcular_mediana(
        datos
    )

    varianza = calcular_varianza(
        datos
    )

    desvio = calcular_desvio(
        datos
    )

    q1, q2, q3 = calcular_cuartiles(
        datos
    )

    # --------------------------------------------------------
    # NUEVO
    # ASIMETRIA
    # --------------------------------------------------------

    asimetria = calcular_asimetria(
        promedio,
        mediana,
        desvio
    )

    tipo_asimetria = (
        clasificar_asimetria(
            asimetria
        )
    )

    # --------------------------------------------------------
    # NUEVO
    # COEFICIENTE DE VARIACION
    # --------------------------------------------------------

    coeficiente_variacion = (
        calcular_coeficiente_variacion(
            promedio,
            desvio
        )
    )

    resultados = {

        "n": len(datos),

        "minimo": minimo,

        "maximo": maximo,

        "rango": rango,

        "media": promedio,

        "moda": moda,

        "mediana": mediana,

        "varianza": varianza,

        "desvio": desvio,

        "coeficiente_variacion":
            coeficiente_variacion,

        "asimetria":
            asimetria,

        "tipo_asimetria":
            tipo_asimetria,

        "q1": q1,

        "q2": q2,

        "q3": q3
    }

    return resultados


# ============================================================
# CONSTRUCCION DE INTERVALOS
# ============================================================

def construir_intervalos(
    datos
):

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
    # REGLA DE STURGES
    #
    # Ni = 1 + 3,3 log(n)
    # --------------------------------------------------------

    Ni = (
        1
        +
        3.3
        *
        math.log10(n)
    )

    Ni = math.ceil(
        Ni
    )

    # --------------------------------------------------------
    # AMPLITUD
    # --------------------------------------------------------

    amplitud_exacta = (
        rango / Ni
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
    # INTERVALOS
    # --------------------------------------------------------

    intervalos = []

    limite_inferior = minimo

    for i in range(Ni):

        limite_superior = (
            limite_inferior
            +
            amplitud
        )

        if (
            i == Ni - 1
            and
            limite_superior < maximo
        ):

            limite_superior = maximo

        if i == Ni - 1:

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
    # MODA AGRUPADA
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

    def cuartil_agrupado(
        k
    ):

        posicion = (
            k * n
        ) / 4

        indice = 0

        for i, F in enumerate(
            frecuencia_acumulada
        ):

            if F >= posicion:

                indice = i
                break

        intervalo = (
            intervalos[
                indice
            ]
        )

        if indice > 0:

            Fa = (
                frecuencia_acumulada[
                    indice - 1
                ]
            )

        else:

            Fa = 0

        fi = (
            intervalo["fi"]
        )

        c = (
            intervalo["ls"]
            -
            intervalo["li"]
        )

        resultado = (
            intervalo["li"]
            +
            c
            *
            (
                posicion
                -
                Fa
            )
            /
            fi
        )

        return resultado

    q1 = cuartil_agrupado(
        1
    )

    q2 = cuartil_agrupado(
        2
    )

    q3 = cuartil_agrupado(
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
    # NUEVO
    # ASIMETRIA DE PEARSON
    # --------------------------------------------------------

    asimetria = (
        calcular_asimetria(
            promedio,
            mediana,
            desvio
        )
    )

    tipo_asimetria = (
        clasificar_asimetria(
            asimetria
        )
    )

    # --------------------------------------------------------
    # NUEVO
    # COEFICIENTE DE VARIACION
    # --------------------------------------------------------

    coeficiente_variacion = (
        calcular_coeficiente_variacion(
            promedio,
            desvio
        )
    )

    # --------------------------------------------------------
    # RANGO CUBIERTO
    # --------------------------------------------------------

    rango = (
        intervalos[-1]["ls"]
        -
        intervalos[0]["li"]
    )

    return {

        "n": n,

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
            coeficiente_variacion,

        "asimetria":
            asimetria,

        "tipo_asimetria":
            tipo_asimetria,

        "q1":
            q1,

        "q2":
            q2,

        "q3":
            q3
    }