# Stack Overbuxef
## Contenidos
- [Prerrequisitos](#prerrequisitos)
- [Instalación](#instalación)
- [Descripción del proyecto](#descripción-del-proyecto)

## Prerrequisitos
Se debe disponer al menos de [git](https://git-scm.com), [python](https://www.python.org) y [pip](https://pip.pypa.io/en/stable/) para poder levantar el proyecto.

## Instalación
Primero se debe clonar el repositorio y moverse a la respectiva carpeta creada:
```sh
git clone "https://github.com/DCC-CC4401/2024-1-CC4401-1-grupo-4.git"
cd "2024-1-CC4401-1-grupo-4"
```

Ahora debemos crear un ambiente virtual en el cual instalar los paquetes del proyecto usando los siguientes comandos:
```sh
python -m venv <nombre-del-ambiente>
<nombre-del-ambiente>/Scripts/activate
pip install -r requirements.txt
```

Teniendo los paquetes instalados finalmente es posible visualizar la página ejecutando el archivo `manage.py` de la siguiente forma:
```sh
python .\manage.py makemigrations stack_overbuxef
python .\manage.py migrate
python .\manage.py loaddata initial_tags.json
python .\manage.py runserver
```

## Descripción del proyecto
Stack Overbuxef es una plataforma destinada a la realización de consultas acádemicas para el contexto de la Facultad de Ciencias Físicas y Matemáticas, en el cual se entrega la posibilidad de plantear dudas sobre cualquier ramo y responderlas, implementando varias carácteristicas que posee [Stack Overflow](https://stackoverflow.com), con la principal diferencia de que se pueden publicar preguntas de forma anónima con el propósito de que todos los usuarios puedan utilizarla sin la ansiedad que les pueda provocar.
