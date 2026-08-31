import carga
import calculos
import interfaz


# ============================================================
# PROCESAMIENTO
# ============================================================

def ejecutar_tipo(
    tipo,
    ruta
):

    # --------------------------------------------------------
    # CARGAR CSV
    # --------------------------------------------------------

    datos = carga.procesar_csv(
        tipo,
        ruta
    )

    # ========================================================
    # TIPO 1
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
    # TIPO 2
    # ========================================================

    elif tipo == 2:

        # ----------------------------------------------------
        # Mostrar los datos originales.
        # ----------------------------------------------------

        interfaz.mostrar_datos(
            datos
        )

        # ----------------------------------------------------
        # Obtener las frecuencias.
        # ----------------------------------------------------

        frecuencias = (
            carga.calcular_frecuencias_categorias(
                datos
            )
        )

        interfaz.mostrar_frecuencias_categorias(
            frecuencias
        )

        # ----------------------------------------------------
        # Intentar convertir las categorias a numeros.
        # ----------------------------------------------------

        try:

            datos_numericos = (
                carga.convertir_categorias_numericas(
                    datos
                )
            )

        except ValueError:

            # ------------------------------------------------
            # Si no son numericas, se trata como cualitativa.
            # ------------------------------------------------

            interfaz.mostrar_mensaje(
                "Las categorias son cualitativas."
            )

            interfaz.mostrar_mensaje(
                "No se aplican medidas cuantitativas "
                "sobre categorias de texto."
            )

            return

        # ----------------------------------------------------
        # Si las categorias son numericas:
        #
        # se calculan las medidas.
        # ----------------------------------------------------

        interfaz.mostrar_mensaje(
            "Las categorias contienen valores numericos."
        )

        interfaz.mostrar_mensaje(
            "Se calcularan las medidas estadisticas."
        )

        resultados = (
            calculos.calcular_medidas(
                datos_numericos
            )
        )

        interfaz.mostrar_resultados(
            resultados
        )

    # ========================================================
    # TIPO 3
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
    # TIPO 4
    # ========================================================

    elif tipo == 4:

        # ----------------------------------------------------
        # Mostrar datos originales.
        # ----------------------------------------------------

        interfaz.mostrar_datos(
            datos
        )

        # ----------------------------------------------------
        # Construir intervalos.
        # ----------------------------------------------------

        intervalos = (
            calculos.construir_intervalos(
                datos
            )
        )

        # ----------------------------------------------------
        # Calcular medidas agrupadas.
        # ----------------------------------------------------

        resultados = (
            calculos.calcular_medidas_agrupadas(
                intervalos
            )
        )

        # ----------------------------------------------------
        # Mostrar resultados.
        # ----------------------------------------------------

        interfaz.mostrar_resultados(
            resultados,
            agrupados=True
        )

    # ========================================================
    # TIPO 5
    # ========================================================

    elif tipo == 5:

        # ----------------------------------------------------
        # Calcular medidas agrupadas.
        # ----------------------------------------------------

        resultados = (
            calculos.calcular_medidas_agrupadas(
                datos
            )
        )

        interfaz.mostrar_resultados(
            resultados,
            agrupados=True,
            mostrar_limites=False
        )

        interfaz.mostrar_mensaje(
            "El rango mostrado corresponde "
            "al rango cubierto por los limites "
            "de los intervalos."
        )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    # --------------------------------------------------------
    # 1. Elegir tipo de problema.
    # --------------------------------------------------------

    tipo = interfaz.seleccionar_tipo()

    # --------------------------------------------------------
    # 2. Pedir CSV DESPUES de seleccionar el tipo.
    # --------------------------------------------------------

    ruta = interfaz.pedir_ruta_csv()

    # --------------------------------------------------------
    # 3. Procesar.
    # --------------------------------------------------------

    ejecutar_tipo(
        tipo,
        ruta
    )


# ============================================================
# INICIO
# ============================================================

if __name__ == "__main__":

    try:

        main()

    except FileNotFoundError:

        interfaz.mostrar_error(
            "No se encontro el archivo CSV."
        )

    except PermissionError:

        interfaz.mostrar_error(
            "No se tiene permiso para acceder "
            "al archivo."
        )

    except ValueError as error:

        interfaz.mostrar_error(
            str(error)
        )

    except Exception as error:

        interfaz.mostrar_error(
            f"Error inesperado: {error}"
        )