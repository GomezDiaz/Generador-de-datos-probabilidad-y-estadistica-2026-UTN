programa desarrollado en Python para facilitar el análisis descriptivo de conjuntos de datos a partir de archivos .csv.

El programa está pensado para trabajar con los distintos tipos de ejercicios estadísticos planteados en la materia. Dependiendo de cómo estén presentados los datos, el usuario selecciona uno de cinco métodos de carga y posteriormente proporciona el archivo .csv correspondiente.

A partir de los datos cargados, el programa puede realizar distintos cálculos de estadística descriptiva, entre ellos:

Media.
Moda.
Mediana.
Varianza.
Desvío estándar.
Rango.
Cuartiles \(Q_1\), \(Q_2\) y \(Q_3\).
Coeficiente de variación.
Coeficiente de asimetría.
Identificación del tipo de asimetría.

Los resultados se muestran mediante una interfaz gráfica sencilla, organizada por grupos de medidas para facilitar su lectura.
/////////////////////////////////////////////////////////////////////
Tipos de archivos .csv admitidos

Antes de seleccionar el archivo, el programa solicita indicar qué tipo de problema se desea resolver.

Existen cinco opciones:

1 - Datos tomados
2 - Categorías
3 - Mini tabla de categorías
4 - Datos para armar intervalos
5 - Límites de intervalo y frecuencia

La estructura esperada del .csv depende de la opción seleccionada.

2.1. Tipo 1 — Datos tomados

Esta opción se utiliza cuando se dispone directamente de una serie de observaciones cuantitativas.

Por ejemplo:

15.2
16.7
18.3
17.5
20.1
16.7
19.4

También se puede utilizar coma decimal:

15,2
16,7
18,3
17,5
20,1
16,7
19,4

Cada fila representa un dato individual.

A partir de estos datos se pueden calcular directamente las principales medidas descriptivas.

///////////////////////////////////////////////////////////
2.2. Tipo 2 — Categorías

Esta opción se utiliza cuando los datos corresponden a categorías cualitativas.

Por ejemplo:

Bueno
Malo
Bueno
Regular
Bueno
Malo
Regular

En este caso el programa conserva los datos y determina cuántas veces aparece cada categoría.

Por ejemplo:

Bueno:    3
Malo:     2
Regular:  2

Al tratarse de categorías cualitativas, no se calculan medidas como media, mediana, varianza o desvío estándar sobre los nombres de las categorías.
//////////////////////////////////////////////////////////
2.3. Tipo 3 — Mini tabla de categorías

Esta opción se utiliza cuando el archivo ya proporciona directamente la categoría y la cantidad de veces que aparece.

Por ejemplo:

Bueno,7
Malo,3
Regular,5

La primera columna corresponde a la categoría y la segunda a su frecuencia.

En este caso el programa no necesita contar nuevamente las categorías, ya que las frecuencias vienen dadas directamente.

La información cargada se interpreta como:

Bueno     → 7
Malo      → 3
Regular   → 5
//////////////////////////////////////////////////////////////////////
2.4. Tipo 4 — Datos para armar intervalos

Esta opción se utiliza cuando se dispone de datos cuantitativos individuales, pero el ejercicio requiere agruparlos posteriormente en intervalos.

El .csv tiene el mismo principio que el Tipo 1:

15.2
16.7
18.3
17.5
20.1
16.7
19.4

La diferencia está en el tratamiento posterior.

El programa toma los datos individuales y calcula, entre otros elementos:

Cantidad de datos.
Mínimo.
Máximo.
Rango.
Cantidad de intervalos mediante la regla de Sturges.
Amplitud de los intervalos.
Frecuencia de cada intervalo.
Marca de clase.

Posteriormente utiliza los intervalos para realizar los cálculos correspondientes a datos agrupados.

Los resultados obtenidos a partir de los intervalos son aproximados, debido a que se utiliza la marca de clase como representación de los datos pertenecientes a cada intervalo.
///////////////////////////////////////////////////////////////////////////////////
2.5. Tipo 5 — Límites de intervalo y frecuencia

Esta opción se utiliza cuando el ejercicio ya proporciona los intervalos y sus frecuencias.

El .csv debe contener tres columnas:

Límite inferior,Límite superior,Frecuencia

Por ejemplo:

15,17,4
17,19,6
19,21,16
21,23,3
23,25,1

El programa interpreta cada fila como:

Límite inferior | Límite superior | Frecuencia
       15       |       17        |     4
       17       |       19        |     6
       19       |       21        |     16
       21       |       23        |     3
       23       |       25        |     1
