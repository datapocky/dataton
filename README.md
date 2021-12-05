# dataton
Repositorio oficial de Laboratorios DataPocky

Esta visualización permite entender de un modo muy simple las sanciones entre funcionarios públicos y entidades gubernamentales. Cada nodo representa un funcionario público diferenciándolo por su género (Hombre = Magenta, Mujer = Rosa, Otro = Amarillo) o institución (en Rojo). A mayor cantidad de ligas entre nodos, mayor número de sanciones aplicadas a los funcionarios. 

Un análisis de red personas-entidades gubernamentales permite entender comunidades donde:
- Hay mayor número de sancionados por institución
- Hay menor número de sancionados
- Concentraciones y grados de importancia en la red por funcionario
- Funcionarios sancionados por más de una institución
- Toda la lista de funcionarios sancionados según institución.

La solución corre en un servidor linux con un webserver apache y escribimos una rutina en python para la generación de una matrix de adyacencia que es representada mediante un plug in de análisis de redes FLOS.


La liga de acceso es: http://34.83.81.208/network/index.html y contiene un control de búsqueda donde el usuario puede introducir nombre de funcionario o entidad gubernamental.

El diagrama de red permite al usuario visualizar la multa y el género relacionados con la persona. 
