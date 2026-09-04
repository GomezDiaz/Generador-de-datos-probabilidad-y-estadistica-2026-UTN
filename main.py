import sys

import carga
import calculos
import interfaz


# ============================================================
# MÉTODO 1
# CATEGORÍAS
# ============================================================

def ejecutar_tipo_1(ruta):

    datos_originales = carga.procesar_csv(
        1,
        ruta
    )["datos"]

    interfaz.mostrar_datos(
        datos_originales
    )

    # --------------------------------------------------------
    # Intentar determinar si las categorías son numéricas
    # --------------------------------------------------------

    datos_numericos = (
        carga.convertir_categorias_numericas(
            datos_originales
        )
    )

    if datos_numericos is None:

        # Datos cualitativos
        frecuencias = {}

        for categoria in datos_originales:

            frecuencias[categoria] = (
                frecuencias.get(categoria, 0) + 1
            )

        interfaz.mostrar_mensaje(
            "Los datos corresponden a categorías cualitativas."
        )

        interfaz.mostrar_mensaje(
            "Se calcularon las frecuencias para el gráfico de barras."
        )

        categorias = list(frecuencias.keys())
        valores = list(frecuencias.values())

        interfaz.mostrar_diagrama_barras(
            categorias,
            valores
        )

        return

    # --------------------------------------------------------
    # Datos numéricos
    # --------------------------------------------------------

    resultados = calculos.calcular_medidas(
        datos_numericos
    )

    interfaz.mostrar_resultados(
        resultados
    )

    # Para categorías numéricas utilizamos barras
    frecuencias = {}

    for dato in datos_numericos:

        frecuencias[dato] = (
            frecuencias.get(dato, 0) + 1
        )

    categorias = sorted(frecuencias.keys())

    valores = [
        frecuencias[categoria]
        for categoria in categorias
    ]

    interfaz.mostrar_diagrama_barras(
        categorias,
        valores
    )

    interfaz.mostrar_boxplot(
        datos_numericos,
        resultados
    )


# ============================================================
# MÉTODO 2
# MINI TABLA DE CATEGORÍAS
# ============================================================

def ejecutar_tipo_2(ruta):

    tabla = carga.procesar_csv(
        2,
        ruta
    )["tabla"]

    interfaz.mostrar_mini_tabla(
        tabla
    )

    categorias = [
        fila[0]
        for fila in tabla
    ]

    frecuencias = [
        fila[1]
        for fila in tabla
    ]

    # --------------------------------------------------------
    # Diagrama de barras
    # --------------------------------------------------------

    interfaz.mostrar_diagrama_barras(
        categorias,
        frecuencias
    )

    # --------------------------------------------------------
    # Si todas las categorías son numéricas,
    # calcular medidas cuantitativas.
    # --------------------------------------------------------

    categorias_numericas = (
        carga.convertir_categorias_numericas(
            categorias
        )
    )

    if categorias_numericas is None:

        interfaz.mostrar_mensaje(
            "Las categorías son cualitativas."
        )

        return

    # Crear lista expandida
    datos = calculos.expandir_frecuencias(
        zip(
            categorias_numericas,
            frecuencias
        )
    )

    resultados = calculos.calcular_medidas(
        datos
    )

    interfaz.mostrar_resultados(
        resultados
    )

    interfaz.mostrar_boxplot(
        datos,
        resultados
    )


# ============================================================
# MÉTODO 3
# DATOS PARA ARMAR INTERVALOS
# ============================================================

def ejecutar_tipo_3(ruta):

    datos = carga.procesar_csv(
        3,
        ruta
    )["datos"]

    interfaz.mostrar_datos(
        datos
    )

    # --------------------------------------------------------
    # Medidas de datos sin agrupar
    # --------------------------------------------------------

    resultados = calculos.calcular_medidas(
        datos
    )

    interfaz.mostrar_resultados(
        resultados
    )

    # --------------------------------------------------------
    # Construir intervalos
    # --------------------------------------------------------

    intervalos = calculos.construir_intervalos(
        datos
    )

    interfaz.mostrar_intervalos(
        intervalos
    )

    # --------------------------------------------------------
    # Histograma
    # --------------------------------------------------------

    interfaz.mostrar_histograma(
        intervalos
    )

    # --------------------------------------------------------
    # Boxplot
    # --------------------------------------------------------

    interfaz.mostrar_boxplot(
        datos,
        resultados
    )


# ============================================================
# MÉTODO 4
# LÍMITES DEL INTERVALO + FRECUENCIA
# ============================================================

def ejecutar_tipo_4(ruta):

    intervalos = carga.procesar_csv(
        4,
        ruta
    )["intervalos"]

    interfaz.mostrar_intervalos(
        intervalos
    )

    # --------------------------------------------------------
    # Medidas agrupadas
    # --------------------------------------------------------

    resultados = calculos.calcular_medidas_agrupadas(
        intervalos
    )

    interfaz.mostrar_resultados(
        resultados,
        agrupados=True
    )

    # --------------------------------------------------------
    # Histograma
    # --------------------------------------------------------

    interfaz.mostrar_histograma(
        intervalos
    )

    # --------------------------------------------------------
    # Boxplot aproximado
    # --------------------------------------------------------

    datos_aproximados = []

    for intervalo in intervalos:
    
        xi = intervalo["xi"]
        frecuencia = intervalo["frecuencia"]
    
        for _ in range(frecuencia):
            datos_aproximados.append(xi)
    
    interfaz.mostrar_boxplot(
        datos_aproximados,
        resultados
    )
    
    # --------------------------------------------------------
    # Advertencia
    # --------------------------------------------------------
    
    interfaz.mostrar_mensaje(
        "El boxplot es aproximado porque se construye "
        "utilizando las marcas de clase (Xi)."
    )
    
    interfaz.mostrar_mensaje(
        "Los valores estadísticos mostrados corresponden "
        "a los datos agrupados."
    )
    
    interfaz.mostrar_mensaje(
        "El boxplot exacto requiere los datos originales."
    )

# --------------------------------------------------------
# Advertencia
# --------------------------------------------------------

interfaz.mostrar_mensaje(
    "El boxplot exacto requiere los datos originales."
)


# ============================================================
# EJECUTAR
# ============================================================

def ejecutar_tipo(tipo, ruta):

    if tipo == 1:

        ejecutar_tipo_1(ruta)

    elif tipo == 2:

        ejecutar_tipo_2(ruta)

    elif tipo == 3:

        ejecutar_tipo_3(ruta)

    elif tipo == 4:

        ejecutar_tipo_4(ruta)

    else:

        raise ValueError(
            "Tipo de entrada inválido."
        )


# ============================================================
# MAIN
# ============================================================

def main():

    interfaz.mostrar_menu()

    tipo = interfaz.seleccionar_tipo()

    ruta = interfaz.pedir_ruta_csv()

    try:

        ejecutar_tipo(
            tipo,
            ruta
        )

    except FileNotFoundError:

        interfaz.mostrar_error(
            "No se encontró el archivo indicado."
        )

    except ValueError as error:

        interfaz.mostrar_error(
            f"Los datos del CSV no son válidos.\n{error}"
        )

    except Exception as error:

        interfaz.mostrar_error(
            f"Ocurrió un error inesperado:\n{error}"
        )


if __name__ == "__main__":
    main()