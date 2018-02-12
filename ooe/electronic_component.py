
def electronic_component(onto, component):

    class ElectronicComponent(component):
        namespace = onto

    class PassiveComponent(ElectronicComponent):
        namespace = onto

    class Resistor(PassiveComponent):
        namespace = onto

    class Capacitor(PassiveComponent):
        namespace = onto
