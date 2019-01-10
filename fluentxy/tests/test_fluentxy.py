from .. import parse_data


def test_parse_data():
    with open('axial-velocity-mesh-1.xy') as m:
        mesh_1 = m.readlines()
    parse_data(mesh_1)
