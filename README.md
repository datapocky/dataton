# dataton
Repositorio oficial de Laboratorios DataPocky

Esta visualización permite entender de un modo muy simple las sanciones entre funcionarios públicos y entidades gubernamentales. Cada nodo representa un funcionario público diferenciándolo por su género (Hombre = Magenta, Mujer = Rosa). A mayor cantidad de ligas entre nodos, mayor número de sanciones aplicadas a los funcionarios. 

Un análisis de red personas-entidades gubernamentales permite entender comunidades donde:
- Hay mayor número de sancionados por institución
- Hay menor número de sancionados
- Concentraciones y grados de importancia en la red por funcionario 

La solución corre en un servidor linux con un webserver apache y escribimos una rutina en python para la generación de una matrix de adyacencia que es representada mediante un plug in de análisis de redes.
