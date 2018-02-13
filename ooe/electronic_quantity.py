from owlready2 import AllDisjoint


def electronic_quantity(onto, emmo):
    intensive_property = emmo.get_by_label('intensive_property')
    extensive_property = emmo.get_by_label('extensive_property')

    class ElectricalResistivity(intensive_property):
        namespace = onto

    class RelativePermittivity(intensive_property):
        namespace = onto

    class RelativePermeability(intensive_property):
        namespace = onto

    class Resistance(extensive_property):
        namespace = onto

    class Capacitance(extensive_property):
        namespace = onto

    class Inductance(extensive_property):
        namespace = onto
