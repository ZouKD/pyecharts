from example.commons import Faker
from pyecharts.charts import Map


def test_map_base():
    c = Map().add(
        "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
