# Amlobot
bot de las mañaneras de amlo hecho con webscrapping y cadenas de markov

## requisitos

instalar desde `requirements.txt`

> pip install -r requirements.txt

## Modelo de trabajo

se utilizó la url https://lopezobrador.org.mx/transcripciones/ que estaba compuesta por páginas, donde cada página agrupa  al menos 6 transcripciones.


para obtener todos los links a las transcripciones por página (página con formato https://lopezobrador.org.mx/transcripciones/page/1) se usó el selector `div.entry-post > h2 > a`.


Para obtener el texto de una página de transcripción se usó el selector `div.entry-content p`, se filtró únicamente el texto donde amlo hablaba, es decir, todo el que tuviera la etiqueta textual "PRESIDENTE ANDRÉS MANUEL LÓPEZ OBRADOR:".

El texto se normalizó usando el algoritmo unicodedata NFC.


## Entrenamiento

se agrega al repositorio un archivo json `trained_data.json` entrenado con fecha del 20 de agosto del 2022, que puede ser usado para generar nuevo texto.
En cualquier caso, para entrenar desde cero:


> python scripts/trainer.py --start 1 --number 10 > trained_data.json # para entrenar desde la página 1 las primeras 10 páginas 


## Generación de texto


> python scripts/generate.py presidente 20 scripts/trained_data.json --random_ratio 0.5 # genera 20 palabras desde la palabra presidente con un coeficiente de randomización del 50%


### Ejemplos 

> python generate.py petróleo 100 trained_data.json --random_ratio 0.5 


```
petróleo crudo y se amparan en reconocerlo y se revisan todo, sin embargo, aunque no pensaron que se engañó durante el usar la disposición. Lo atiende a recordarle al acero, el 49 por la pista, bueno, eso ¿cuánto era el secuestrador de 1996, la gente constantemente. Sí, precisamente por la carne?’ ‘A ver, vamos encaminados, tenemos que entenderlos. También se va porque inclusive hasta lugares inhóspitos, en el que alcanzar. Adelante. Sí, podríamos hacer un campo, desde luego trabajé de concesiones? Cero, presos que se va una consulta- trascedentes, como lo contratado, una tasa, bueno, mucho talento, tiene básicamente. ¿Por cuestiones
```

> python generate.py corrupción 100 trained_data.json --random_ratio 0.5 


```
corrupción y atienda tu reflexión respetuosa- por criminal a Pinochet; pero no existían, que determinan si agilizamos todos busquemos transformar a argumentar a apoyar, llega estar visitado hace Hugo, Hugo. Muy pocos. No, ustedes, resistir déficits altos, tienen ideología, cuál de salvar a la población?, ya llevo y abandonada desde antes. ‘Tengo preocupación y convirtieron al Tsuru, bueno, las médicas, ahora regresamos. Estamos ocupados sobre todo en campo, igual tú, ¿de abajo todavía tiene deuda, y niños, que… Has hecho inmensamente ricos al gobierno atravesó por delincuentes, pues no llevábamos entregados por ofrecer, las empresas producen, pues empezamos precisamente organizando otras
```


## Posibles mejoras 

Al ser entrenado usando markov con una palabra consecuente, se guarda la relación:


```json
{
  "palabra1":{
    "palabra2": 1,
    "palabra3": 2
  },
  "palabra2":{
    "palabra3": 2
  },
  "palabra3":{
    "palabra1": 1,
  },
}
```

El entrenamiento podría mejorar si se conservasen más número consecuentes de palabras, por ejemplo 2 o 3, aún se necesitan pruebas.
