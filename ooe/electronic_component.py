from owlready2 import AllDisjoint


def electronic_component(onto, emmo):
    system = emmo.get_by_label('system')
    component = emmo.get_by_label('component')
    physical_quantity = emmo.get_by_label('physical_quantity')
    definition = emmo.get_by_label('definition')


    class ElectronicSystem(system):
        namespace = onto

    class ElectronicComponent(component):
        namespace = onto

    definition[ElectronicComponent] = '''
    ElectronicComponent = Def. A component which is used in an ElectronicSystem.
    '''


    class Resistor(ElectronicComponent):
        namespace = onto

    definition[Resistor] = '''
    Resistor = Def. An ElectronicComponent which implements Resistance in an
    ElectronicSystem.
    '''

    class Capacitor(ElectronicComponent):
        namespace = onto

    definition[Capacitor] = '''
    Capacitor = Def. An ElectronicComponent which implements Capacitance in an
    ElectronicSystem.
    '''

    class Inductor(ElectronicComponent):
        namespace = onto

    definition[Inductor] = '''
    Inductor = Def. An ElectronicComponent which implements Inductance in an
    ElectronicSystem.
    '''

    class Fuse(ElectronicComponent):
        namespace = onto

    # TODO
    definition[Fuse] = '''
    '''

    AllDisjoint([Resistor, Capacitor, Inductor, Fuse])


    class FixedResistor(Resistor):
        namespace = onto

    definition[FixedResistor] = '''
    FixedResistor = Def. A Resistor which has a defined Resistance.
    '''

    class DependentResistor(Resistor):
        namespace = onto

    definition[DependentResistor] = '''
    DependentResistor = Def. A Resistor which has a Resistance that depends on a
    physical_quantity.
    '''

    class VariableResistor(Resistor):
        namespace = onto

    definition[VariableResistor] = '''
    VariableResistor = Def. A Resistor which has an adjustable Resistance value.
    '''

    AllDisjoint([FixedResistor, VariableResistor, DependentResistor])


    class Conductor(FixedResistor):
        namespace = onto

    definition[Conductor] = '''
    Conductor = Def. A FixedResistor whose function is the transmission of
    ElectricalPower.
    '''

    class HeatingResistor(FixedResistor):
        namespace = onto

    definition[HeatingResistor] = '''
    HeatingResistor = Def. A FixedResistor whose function is the generation of
    Heat.
    '''

    AllDisjoint([Conductor, HeatingResistor])


    class Wire(Conductor):
        namespace = onto

    definition[Wire] = '''
    Wire = Def. A Conductor used to connect ElectronicSystems.
    '''

    class Track(Conductor):
        namespace = onto

    definition[Track] = '''
    Track = Def. A Conductor used to connect ElectronicComponents in an
    ElectronicSystem.
    '''

    class Via(Conductor):
        namespace = onto

    definition[Via] = '''
    Via = Def. A Conductor used to connect Tracks accross Layers of an
    ElectronicSystem.
    '''

    AllDisjoint([Wire, Track, Via])


    class Varistor(DependentResistor):
        namespace = onto

    definition[Varistor] = '''
    Varistor = Def. A DependentResistor which depends on Voltage.
    '''

    class Thermistor(DependentResistor):
        namespace = onto

    definition[Thermistor] = '''
    Thermistor = Def. A DependentResistor which depends on Temperature.
    '''

    class LightDependentResistor(DependentResistor):
        namespace = onto

    definition[LightDependentResistor] = '''
    LightDependentResistor = Def. A DependentResistor which depends on
    Illumination.
    '''

    AllDisjoint([Varistor, Thermistor, LightDependentResistor])


    class NTC(Thermistor):
        namespace = onto

    definition[NTC] = '''
    NTC = Def. A Thermistor which has a negative thermal coefficient.
    '''

    class PTC(Thermistor):
        namespace = onto

    definition[PTC] = '''
    PTC = Def. A Thermistor which has a positive thermal coefficient.
    '''

    AllDisjoint([NTC, PTC])


    class Potentiometer(VariableResistor):
        namespace = onto

    definition[Potentiometer] = '''
    Potentiometer = Def. Two VariableResistors where the ratio of
    ElectricalResistance is user adjustable during ElectronicSystem operation.
    '''

    class TrimPotentiometer(VariableResistor):
        namespace = onto

    definition[TrimPotentiometer] = '''
    TrimPotentiometer = Def. Two VariableResistors where the ratio of
    ElectricalResistance is oem adjustable during ElectronicSystem manufacturing.
    '''

    class Rheostat(VariableResistor):
        namespace = onto

    definition[VariableResistor] = '''
    Rheostat = Def. A VariableResistor which is user adjustable during
    ElectronicSystem operation.
    '''

    class PresetResistor(VariableResistor):
        namespace = onto

    definition[PresetResistor] = '''
    PresetResistor = Def. A VariableResistor which is oem adjustable during
    ElectronicSystem manufacturing.
    '''

    AllDisjoint([Potentiometer, TrimPotentiometer, Rheostat, PresetResistor])



    # TODO capacitor, inductor, fuse classification
    class VariableCapacitor(Capacitor):
        namespace = onto
