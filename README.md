# Sistema de Venta de Pasajes para Vuelos-Duoc

Este programa en Python permite gestionar la venta de pasajes para la compañía Vuelos-Duoc. El sistema maneja una matriz de 42 asientos, con precios diferenciados para asientos normales y VIP, e incluye funcionalidades como la compra de asientos, anulación de pasajes, y modificación de datos de pasajeros.

## Requisitos

- Python 3.x
- Biblioteca `numpy`

## Instalación

1. Clona este repositorio o descarga los archivos.

2. Instala la biblioteca `numpy` si no la tienes:
    ```bash
    pip install numpy
    ```

3. Ejecuta el script principal:
    ```bash
    python nombre_del_script.py
    ```

## Uso

El sistema presenta un menú con las siguientes opciones:

1. **Ver asientos disponibles**: Muestra una matriz de los asientos disponibles, indicando los asientos ocupados con una "X".

2. **Comprar asiento**: Permite al usuario ingresar sus datos, seleccionar un asiento y confirmar la compra. Si el usuario ingresa el código de descuento "bancoduoc", recibe un descuento del 15%.

3. **Anular vuelo**: Permite anular una compra, haciendo el asiento nuevamente disponible y eliminando los datos del pasajero.

4. **Modificar datos de pasajero**: Permite modificar el nombre o teléfono de un pasajero, solicitando el RUT para verificación.

5. **Salir**: Finaliza la ejecución del programa.

## Ejemplo de Ejecución

A continuación, se muestra un ejemplo de cómo funciona el programa:



## Funciones Principales

- **ver_asientos()**: Muestra una matriz de asientos disponibles.
- **comprar_asiento()**: Permite al usuario comprar un asiento ingresando sus datos.
- **anular_vuelo()**: Anula la compra de un asiento, haciéndolo disponible nuevamente.
- **modificar_datos()**: Permite modificar el nombre o teléfono del pasajero mediante la verificación del RUT.
---
Este README proporciona una visión general del programa, desde la instalación hasta el uso de las funcionalidades principales. Si tienes alguna pregunta o necesitas más información, no dudes en contactarme.
