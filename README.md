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
Formato de los archivos CSV

El programa acepta cinco formas diferentes de organizar los datos.
Antes de cargar el archivo .csv, se debe seleccionar la opción correspondiente al formato utilizado.

Importante: en los tipos 1, 2 y 4, la coma , puede utilizarse como separador decimal. Por este motivo, la separación entre datos se realiza mediante saltos de línea. También se permite utilizar ; para colocar varios datos en una misma línea.

Tipo 1 — Datos tomados

Se utiliza cuando se tienen los datos cuantitativos directamente.

Ejemplo con punto decimal
1.68
1.76
1.76
2.00
2.16
2.50
2.75
3.10
3.25
Ejemplo con coma decimal
1,68
1,76
1,76
2,00
2,16
2,50
2,75
3,10
3,25
También se pueden colocar varios datos utilizando ;
1,68;1,76;1,76
2,00;2,16;2,50
2,75;3,10;3,25

El programa interpreta cada valor como un dato independiente.

Por ejemplo:

1,68;1,76;1,76

se interpreta como:

1.68
1.76
1.76
Tipo 2 — Categorías

Se utiliza cuando los datos vienen representados como categorías que pueden repetirse.

Las categorías pueden ser texto o números.

Ejemplo con categorías de texto
Bueno
Malo
Bueno
Regular
Bueno
Malo
Regular

El programa obtiene las frecuencias:

Bueno:    3
Malo:     2
Regular:  2
Ejemplo con categorías numéricas
2,2
2,2
2,5
2,7
2,7
2,7
2,8
2,9
2,9
2,9
2,9
3
3,1
3,1
3,1
3,2
3,3
3,4
3,7
3,7

En este caso, aunque se haya seleccionado Categorías, los valores son numéricos. Por lo tanto, el programa puede utilizarlos para realizar los cálculos estadísticos.

Por ejemplo:

2,2 → 2.2
2,5 → 2.5
2,7 → 2.7
3   → 3.0
3,1 → 3.1

También se permite utilizar ; para separar varios datos:

2,2;2,5;2,7
2,7;2,8;2,9
3;3,1;3,2
Tipo 3 — Mini tabla de categorías

En este caso el archivo ya contiene la categoría y la frecuencia.

El separador utilizado es ;.

El formato es:

"categoria";"frecuencia"

La categoría puede ser texto o un número.

Ejemplo con categorías de texto
"Bueno";"7"
"Malo";"3"
"Regular";"5"

El programa interpreta:

Bueno     → 7
Malo      → 3
Regular   → 5
Ejemplo con categorías numéricas
"2,2";"3"
"2,5";"1"
"2,7";"4"
"2,9";"6"
"3,1";"3"

Aquí:

Primera columna → categoría.
Segunda columna → cantidad de veces que se repite.

Por ejemplo:

"2,9";"6"

significa que la categoría 2,9 aparece 6 veces.

Tipo 4 — Datos para armar intervalos

Se utiliza cuando se proporcionan los datos individuales, pero el ejercicio requiere posteriormente agruparlos en intervalos.

El formato de entrada es igual al Tipo 1.

Ejemplo con punto decimal
1.68
1.76
1.76
2.00
2.16
2.50
2.75
3.10
3.25
3.50
3.75
4.00
Ejemplo con coma decimal
1,68
1,76
1,76
2,00
2,16
2,50
2,75
3,10
3,25
3,50
3,75
4,00

También se acepta:

1,68;1,76;1,76
2,00;2,16;2,50
2,75;3,10;3,25
3,50;3,75;4,00

A diferencia del Tipo 1, el programa posteriormente utilizará estos datos para construir los intervalos y calcular las medidas correspondientes a datos agrupados.

Tipo 5 — Límites del intervalo y frecuencia

En este caso los intervalos ya están definidos, por lo que el archivo debe proporcionar:

Límite inferior ; Límite superior ; Frecuencia

El separador es ;.

Ejemplo
"15";"17";"4"
"17";"19";"6"
"19";"21";"16"
"21";"23";"3"
"23";"25";"1"