![zodiac](https://github.com/Guilliu/zodiac/blob/main/imagen.jpg)
# Zodiac:

**Zodiac** presenta un nuevo marco astrológico basado en técnicas de `aprendizaje no supervisado`.

## <b>Contexto</b>

Todos conocemos los 12 signos del Zodíaco, bueno, quizá no los 12 pero al menos cada uno conoce el suyo 😅.

De acuerdo con la astrología clásica, los fenómenos celestes reflejan o rigen las actividades humanas de forma que los doce signos del Zodíaco representan doce personalidades básicas o modelos de expresión característicos.

El orden de los doce signos tradicionales es:

<p align="center">Aries, Tauro, Géminis, Cáncer, Leo, Virgo, Libra, Escorpio, Sagitario, Capricornio, Acuario, Piscis</p>

Pertenecer a un signo u otro atiende exclusivamente a una cuestión temporal, la época del año en la que naciste. Es decir, la `clasificación zodiacal` se hace fijando 11 puntos de corte (normalmente un día entre el 20 y el 24 de cada mes) que determinan a los 12 grupos disjuntos. Esta teoría ha dado de comer a mucha gente: tarotistas, adivinos, revistas de prensa rosa, aplicaciones de citas... Incluso parece estar cogiendo mucha fuerza entre los más jovenes!

<p align="center"><i>Es normal... Un Géminis y un Escorpio ya se sabe... No puede salir bien...</i></p>

De hecho, seguro que alguna vez nos hemos sentido identificados con nuestro signo leyendo algo al respecto.... Hasta puede que nos encajen ciertos comportamientos de conocidos en base a su teórico signo zodiacal o si no en base al de alguno de sus familiares, o en base al de su perro, o en base a su signo ascendente en función de la hora el minuto y el milisegundo en el que vino a este mundo!

Yo no sé si habrá algo de verdad en esto, pero en estos mundos místicos es mejor no pecar de ingenuo y no olvidar que el ser humano tiende, por naturaleza, a reconocer patrones donde quizá solo hay casualidad...

## <b>Idea</b>
Esto de que tu personalidad se catalogue en uno de estos 12 grupos en función de tu fecha de nacimiento es demasiado determinista, ¿no?... Vale sí, tiene gancho estoy de acuerdo, pero usar como única variable el momento de tu llegada al mundo no parece demasiado convincente...

¿Y si intentamos, en base a una muestra REAL de personas, buscar `patrones de comportamiento`? Podríamos tratar de recoger/caracterizar esa personalidad en base a las respuestas de un cuestionario con preguntas variadas... Además, si esas preguntas tuvieran distintas opciones que tuvieras que ordenar de mayor a menor preferencia... Mmmmm... Así, podríamos usar una técnica de aprendizaje no supervisado como el `clustering` para encontrar esos nuevos grupos de personalidades innatas... Sounds good? 🤔

Esto es EXACTAMENTE lo que hemos desarrollado en el proyecto Zodiac. Durante dos periodos temporales distintos (jun2020 y jan2021) se recogieron `dos muestras independientes` de personas que respondieron al siguiente cuestionario, diseñado a medida para este estudio: https://forms.gle/snyGBbvdN69sS6x77

## <b>Desarrollo</b>
Las dos muestras obtenidas conforman un dataset con el que entrenamos un modelo `k-means` que determine grupos de comportamiento distintitos entre sí. El desarrollo del modelo (con las muestras debidamente anonimizadas) se encuentra en el notebook `desarrollo.ipynb`

## <b>Resultados</b>

El modelo resultante distingue **4 grupos de personalidad**. A cada uno de estos grupos les he generado una breve descripción copiando y pegando fragmentos de los grupos zodiacales clásicos (mezclando a lo Frankenstein) de la siguiente web: https://www.lavanguardia.com/horoscopo/signos-zodiaco. También les he añadido propiedades características típicas como color, elemento, estación... Esto se puede encontrar en `nuevos_signos.pdf`.

Los resultados son verdaderamente sorprendentes. Primero porque, al yo conocer a todos los individuos de las muestras, **sí** reconozco muchos parecidos en la forma de ser entre las personas que forman parte de un mismo grupo. Y segundo porque para mi sorpresa hay notables concentraciones de los signos zodiacales clásicos (me sé la mayoría de los cumpleaños) en ciertos grupos, por poner un ejemplo hay un grupo en el que de 7 individuos hay 3 géminis y 2 cáncer (signos consecutivos)... En los otros grupos también se aprecia algo parecido.

Quizá este experimento sea un pequeño indicio de que la astrología tradicional no es algo tan aleatorio! 😋

## <b>Implantación y próximos pasos</b>

Si te interesa conocer tu nuevo signo zodiacal puedes rellenar el cuestionario de Google Forms y pedirme que le aplique el modelo al fichero .csv que genera. Además tu participación ayudaría a reenetrenar al modelo y que este calibre mejor su segmentación! Y bueno, a ver si realmente te encaja el resultado!

En un futuro quisiera desplegar una pequeña web con una interfaz de usuario sencilla en donde uno pueda introducir el resultado de su cuestionario (el .csv) y que esta le devuelva el output del modelo en una nueva ventana personalizada con su signo... `#in_progress` 😎.

