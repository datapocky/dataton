# dataton
Repositorio oficial de Laboratorios DataPocky

::EXPLICACIÓN::
Esta visualización permite entender de un modo muy simple las sanciones entre funcionarios públicos y entidades gubernamentales. Cada nodo representa un funcionario público diferenciándolo por su género (Hombre = Magenta, Mujer = Rosa, Otro = Amarillo) o institución (en Rojo). A mayor cantidad de ligas entre nodos, mayor número de sanciones aplicadas a los funcionarios. 

Un análisis de red personas-entidades gubernamentales permite entender comunidades donde:
- Hay mayor número de sancionados por institución
- Hay menor número de sancionados
- Concentraciones y grados de importancia en la red por funcionario
- Funcionarios sancionados por más de una institución
- Toda la lista de funcionarios sancionados según institución.

La solución corre en un servidor linux con un webserver apache y escribimos una rutina en python, después de pasar los datos de un json a dataframe con la librería pandas (ver script en el repositorio de normalización y lectura de json).  Luego generamos una matrix de adyacencia que es representada mediante un plug in de análisis de redes FLOS gracias a gephi.org.

Partimos de un análisis de ciencia de redes en el que tabulamos aristas con orígen en la institicución a la que pertenece la persona sancionada y destino en el nombre y apellido de la persona. De este modo es posible advertir fácilmente aquellas personas sancionadas que han saltado de una inst a otra o inconsistencias si añadimos atributos a los nodos. Como montos de las multas u otros.

::ACCESO::
La liga de acceso es: http://34.83.81.208/network/index.html y contiene un control de búsqueda donde el usuario puede introducir nombre de funcionario o entidad gubernamental.

El diagrama de red permite al usuario visualizar la multa y el género relacionados con la persona. 
