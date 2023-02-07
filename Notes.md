# Notes to learn python 

## Data types

<img src="Datatype.PNG">

# Sintaxis de una clase

<img src="Clase.PNG">

# GIT

## Comandos

- **git Init**: Se ejecuta una vez y es cuando comienza el proyecto
        -Crea dos áreas donde almacena los archivos: 
        Stagind área (Area de ensayo): Es un área temporal donde el desarrollador puede observar qué archivos tiene seguimiento y el estado de cada una
        Repositoria local: Es donde se guarda la copia de los archivos o la foto que toma el git y de donde se recatan los archivos
- **git add**: se ajecuta para indicar a qué archivos se desea hacer seguimiento y  se añade al area de ensayo
- **git commit**: traslada el archivos a del área de ensayo al repositorio local. La forma de agregar es **git commit -m "Nombre del commit"**

<img src="GitIni.PNG">

- **Documentación** [ Link MArkdown Doc ]( https://git-scm.com/docs)

- **git status -s**: para visualizar las elementos que están en la carpetay validar cuales están añadidos al repositorio el simbolo **??** quiere decir que no está haciendo seguimiento

- **git log --oneline**: nos indica el nombre de los commits que se han realizado

- **git reset --hard** **código de la instantánea**

## Cómo subir un repositorio a GitHUB y otros comandos

- Se hace para subir una copia de seguridad
- **git add .** : para agregar todos los elementos de una carpeta
- **git commit -am "Nombre del comit"** : Para hacer add y commit en el mismo comando
- **git commit --amend** : Para abrir el editor bin y modificar las descripciones de los commits

### Editor Bin
<img src="EditorBin.PNG">

- :i -> para empezar a editar en el editor bin
- tecla suprimir para borrar
- Esc para vovler al editos
- :i -> para volver a escribir
- Añadir la nueva descripción y pulsar enter
- pulsar Esc
- :wq -> para salir del editor bin

### Subir proyecto a GitHUB
- **git remote add origin https://github.com/EdwarRL/CursoGit.git** : Comando usado para subir por primera vez el proyecto
- **git push -u origen main** :

## Editar desde GitHub, crear teags, clonación en reporsitorio local

- Para editar en githut, se modifica con la opción del lápiz, se de da commit changes y despues en el local se da **git pull** para halar la información desde el repositorio remoto.
- Para crear una tag se utiliza el comando **git tag 06-02-2023 -m "Version 1 del proyecto"** y el git lo almacena, para subirlo al repositoria se utiliza el comando **git push --tags**
- Para clonar un proyecto se utiliza el comando **git clone "se pega la url que se saca del github boton <>Code-->Clone**"

## Ramas o branches

- Para crear una rama se utiliza el comando **git branch Rama1**
- Para ver las ramas del proyecto y en que rama me encuentro, utilizo el comando **git branch**
- Para moverse a otra rama se utiliza el comando **git checkout Rama1**




