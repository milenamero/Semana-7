# Sistema Restaurante

## Nombre del estudiante

Milena Mayerli Mero Loor
Mendoza Velez Grace Rosalinda

## Descripción

Este proyecto corresponde al desarrollo de un sistema de restaurante realizado en Python utilizando Programación Orientada a Objetos.

El sistema permite registrar, listar y buscar productos y clientes mediante un menú interactivo desde consola.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

## Constructor

La clase Producto utiliza el constructor `__init__()` para crear objetos con nombre, categoría, precio y disponibilidad.

## Uso de @property y @setter

Se utilizan para controlar el acceso a los atributos del producto y validar que:

- El nombre no esté vacío.
- La categoría no esté vacía.
- El precio sea mayor que cero.

## Uso de @dataclass

La clase Cliente utiliza `@dataclass`, lo que simplifica la creación de objetos sin escribir un constructor manual.

## Menú interactivo

El sistema permite:

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Salir del programa.

## Reflexión

Crear objetos a partir de datos ingresados por el usuario permite desarrollar aplicaciones más dinámicas y organizadas. Además, facilita la reutilización del código mediante la Programación Orientada a Objetos y una estructura modular.