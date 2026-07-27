# Sistema_bancario
# Sistema Bancario

## Descripción del proyecto

Sistema de información básico para un banco desarrollado como proyecto académico, aplicando programación en Python, control de versiones con Git y la metodología Git Flow.

El sistema permite gestionar la información de clientes, crear cuentas bancarias y realizar operaciones financieras básicas como consulta de saldo, consignaciones, retiros y transferencias.

El proyecto fue desarrollado por dos integrantes, donde cada uno trabajó en funcionalidades específicas utilizando ramas independientes de tipo **feature**, realizando commits frecuentes y sincronizando los cambios mediante GitHub.

---

# Objetivo del proyecto

Desarrollar un sistema bancario básico que permita administrar clientes y cuentas, aplicando buenas prácticas de programación, organización del código y trabajo colaborativo mediante el uso de Git Flow.

---

# Tecnologías utilizadas

- Python 3
- Git
- GitHub
- Git Flow
- Visual Studio Code

---

# Estructura del proyecto

```
Sistema_bancario/

│
├── controllers/
│   ├── cliente_controller.py
│   ├── cuenta_controller.py
│   └── operaciones_controller.py
│
├── models/
│   ├── cliente.py
│   └── cuenta.py
│
├── data/
│   └── Archivos para almacenamiento de información
│
├── utils/
│   └── Funciones auxiliares
│
├── src/
│   └── main.py
│
└── README.md
```

---

# Metodología Git Flow

Para el desarrollo del proyecto se aplicó la metodología Git Flow, permitiendo organizar el trabajo de manera colaborativa y mantener versiones estables del sistema.

## Rama main

La rama **main** contiene únicamente versiones estables y funcionales del proyecto listas para entrega.

## Rama develop

La rama **develop** fue utilizada para integrar los cambios realizados por los integrantes antes de llevarlos a la rama principal.

## Ramas feature

Cada funcionalidad fue desarrollada en una rama independiente.

Ramas utilizadas:

```
feature/registro-clientes

feature/crear-cuentas
```

Estas ramas permitieron desarrollar funcionalidades sin afectar el código principal.

---

# Integrantes y funcionalidades realizadas

## Integrante 1

Nombre: _Daniela Casatañeda_____________________

Rama utilizada:

```
feature/registro-clientes
```

## Funcionalidades desarrolladas:

### Registro de clientes

Se desarrolló el módulo encargado de registrar nuevos clientes dentro del sistema bancario.

Información solicitada:

- Nombre del cliente
- Documento de identidad
- Teléfono
- Correo electrónico
- Dirección

Validaciones realizadas:

- Verificación de campos obligatorios.
- Control de información ingresada.
- Almacenamiento de datos del cliente.

### Consulta de saldo

Se implementó la funcionalidad que permite consultar el saldo disponible de una cuenta bancaria.

Esta opción permite al usuario conocer la cantidad de dinero disponible asociada a una cuenta.

---

# Integrante 2

Nombre: Isabell Valencia__________________________

Rama utilizada:

```
feature/crear-cuentas
```

## Funcionalidades desarrolladas:

### Creación de cuentas bancarias

Se creó el módulo encargado de registrar nuevas cuentas asociadas a los clientes.

Información manejada:

- Número de cuenta.
- Tipo de cuenta.
- Cliente asociado.
- Saldo inicial.

### Operaciones bancarias

Se implementaron operaciones básicas del sistema:

### Consignaciones

Permite aumentar el saldo de una cuenta mediante un depósito de dinero.

### Retiros

Permite disminuir el saldo de una cuenta validando que exista disponibilidad suficiente.

### Transferencias

Permite realizar movimientos de dinero entre diferentes cuentas registradas.

---

# Control de versiones con Git

Durante el desarrollo se utilizaron diferentes comandos de Git para administrar los cambios del proyecto.

## Inicialización del repositorio

```
git init
```

## Crear ramas

```
git checkout -b nombre-rama
```

## Agregar cambios

```
git add .
```

## Crear commits

Ejemplos:

```
git commit -m "Implementación registro de clientes"

git commit -m "Creación módulo cuentas bancarias"

git commit -m "Implementación operaciones bancarias"
```

## Subir cambios a GitHub

```
git push
```

## Actualizar cambios del repositorio

```
git pull
```

---

# Resolución de conflictos

Durante el desarrollo colaborativo se presentaron conflictos debido a modificaciones realizadas sobre archivos compartidos.

Para solucionarlos se realizaron los siguientes pasos:

1. Se identificaron los archivos con conflicto utilizando:

```
git status
```

2. Se revisaron los cambios realizados por cada integrante.

3. Se seleccionó y organizó la información correcta.

4. Se agregaron nuevamente los archivos solucionados:

```
git add .
```

5. Se realizó un nuevo commit:

```
git commit -m "Resolución de conflictos"
```

De esta manera se logró integrar correctamente el trabajo de ambos integrantes.

---

# Instalación y ejecución del proyecto

## Requisitos

Antes de ejecutar el sistema se debe tener instalado:

- Python 3
- Git
- Visual Studio Code

---

## Clonar el repositorio

Ejecutar:

```
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto:

```
cd Sistema_bancario
```

---

## Ejecutar el sistema

Ejecutar el siguiente comando:

```
python -m src.main
```

El sistema mostrará un menú donde el usuario podrá seleccionar las diferentes opciones disponibles.

---

# Funcionalidades del sistema

Actualmente el sistema cuenta con:

✅ Registro de clientes  
✅ Creación de cuentas bancarias  
✅ Consulta de saldo  
✅ Consignaciones  
✅ Retiros  
✅ Transferencias  

---

# Evidencias del proyecto

El repositorio contiene:

- Código fuente del sistema.
- Historial de commits realizados por los integrantes.
- Ramas creadas mediante Git Flow.
- Integración de funcionalidades en la rama develop.
- Versión estable del sistema en la rama main.

---

# Participación mediante Git Flow

Cada integrante realizó aportes mediante ramas independientes:

- Daniela Casatñeda  desarrolló la gestión de clientes y consulta de saldo.
- Isabell Valencia  desarrolló la creación de cuentas y operaciones bancarias.

Posteriormente, las funcionalidades fueron integradas en la rama develop para realizar las pruebas correspondientes antes de pasar a main.

---

# Conclusión

El desarrollo del Sistema Bancario permitió aplicar conocimientos de programación, manejo de archivos, estructuras de código y control de versiones.

La implementación de Git Flow facilitó el trabajo colaborativo, permitiendo dividir las tareas, controlar los cambios realizados y mantener una organización adecuada del proyecto.

El uso de ramas, commits y resolución de conflictos permitió simular un ambiente real de desarrollo de software trabajando en equipo.