from dataclasses import dataclass

# Clase Cliente utilizando dataclass

@dataclass
class Cliente:
    id_cliente: int
    nombre: str
    correo: str