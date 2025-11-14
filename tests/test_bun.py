
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from praktikum.bun import Bun
def test_bun_fields_and_methods():
    bun = Bun("white bun", 150)
    assert bun.get_name() == "white bun"
    assert bun.get_price() == 150
