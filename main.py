import carga
import calculos
import interfaz


# ============================================================
# PROCESAMIENTO DE CADA TIPO
# ============================================================

def ejecutar_tipo(
    tipo,
    ruta
):

    # --------------------------------------------------------
    # CARGA DEL CSV
    # --------------------------------------------------------

    datos = carga.procesar_csv(
        tipo,
        ruta
    )

    # ========================================================
    # TIPO 1 - DATOS TOMADOS
    # ========================================================

    if tipo == 1:

        interfaz.mostrar_datos(
            datos
        )

        resultados = (
            calculos.calcular_medidas(
                datos
            )
        )

        interfaz.mostrar_resultados(
            resultados
        )

    # ========================================================
    # TIPO 2 - CATEGORIAS
    # ========================================================

    elif tipo == 2:

        interfaz.mostrar_categorias(
            datos
        )

        frecuencias = (
            carga.calcular_frecuencias_categorias(
                datos
            )
        )

        interfaz.mostrar_frecuencias_categorias(
            frecuencias
        )

        interfaz.mostrar_mensaje(
            "Las categorias son variables cualitativas."
        )

        interfaz.mostrar_mensaje(
            "No se aplican medidas cuantitativas "
            "como media, varianza o desvio "
            "sobre los nombres de las categorias."
        )

    # ========================================================
    # TIPO 3 - MINI TABLA DE CATEGORIAS
    # ========================================================

    elif tipo == 3:

        interfaz.mostrar_mini_tabla(
            datos
        )

        interfaz.mostrar_mensaje(
            "Las frecuencias fueron proporcionadas "
            "directamente en el archivo CSV."
        )

    # ========================================================
    # TIPO 4 - DATOS PARA ARMAR INTERVALOS
    # ========================================================

    elif tipo == 4:

        # Mostrar datos originales.
        interfaz.mostrar_datos(
            datos
        )

        # Construir intervalos.
        intervalos = (
            calculos.construir_intervalos(
                datos
            )
        )

        # Calcular medidas agrupadas.
        resultados = (
            calculos.calcular_medidas_agrupadas(
                intervalos
            )
        )

        # Por ahora NO mostramos la tabla de frecuencias.
        interfaz.mostrar_resultados(
            resultados,
            agrupados=True
        )

    # ========================================================
    # TIPO 5 - INTERVALOS YA DADOS
    # ========================================================

    elif tipo == 5:

        interfaz.mostrar_intervalos(
            datos
        )

        resultados = (
            calculos.calcular_medidas_agrupadas(
                datos
            )
        )

        interfaz.mostrar_resultados(
            resultados,
            agrupados=True
        )

        interfaz.mostrar_mensaje(
            "El rango mostrado corresponde al rango "
            "cubierto por los limites de los intervalos."
        )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    # --------------------------------------------------------
    # 1. Preguntar el tipo de problema
    # --------------------------------------------------------

    tipo = interfaz.seleccionar_tipo()

    # --------------------------------------------------------
    # 2. Pedir el CSV
    #
    # Esto ocurre DESPUES de seleccionar el tipo.
    # --------------------------------------------------------

    ruta = interfaz.pedir_ruta_csv()

    # --------------------------------------------------------
    # 3. Procesar
    # --------------------------------------------------------

    ejecutar_tipo(
        tipo,
        ruta
    )


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

if __name__ == "__main__":

    try:

        main()

    except FileNotFoundError:

        interfaz.mostrar_error(
            "No se encontro el archivo CSV."
        )

    except ValueError as error:

        interfaz.mostrar_error(
            str(error)
        )

    except Exception as error:

        interfaz.mostrar_error(
            f"Error inesperado: {error}"
        )