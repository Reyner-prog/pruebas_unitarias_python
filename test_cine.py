# test_cine.py
import pytest
from cine import Pelicula

def test_compra_exitosa():
    pelicula = Pelicula("Test Movie", 10, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Test Movie. Total: $50"
    assert pelicula.asientos_disponibles == 5
    
def test_compra_asientos_insuficientes():
    pelicula = Pelicula("Test Movie", 3, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."
    assert pelicula.asientos_disponibles == 3

def test_compra_cero_entradas():
    pelicula = Pelicula("Test Movie", 10, 10)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Test Movie. Total: $0"
    assert pelicula.asientos_disponibles == 10

if __name__ == "__main__":
    pytest.main()
