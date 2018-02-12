import os
import sys

root_dir = os.path.join(os.path.dirname(__file__), '..')
# Needed for mercurial version of owlready2 because it doesn't
# follow the standard python package conventions
sys.path.append(os.path.join(os.environ['VIRTUAL_ENV'], 'src'))
# Add EMMO to path
sys.path.append(os.path.join(root_dir, 'EMMO'))

import emmo
import owlready2

emmoOntology = emmo.get_ontology('emmo-0.3_2017-10-26.owl')
emmoOntology.load()

# not sure why it isn't easier to get the 'component' entity
component = emmoOntology.search(iri='*EMMO_000168')[0]

onto = owlready2.get_ontology('https://ontology-of-electonics.github.io')

import electronic_component
electronic_component.electronic_component(onto, component)

onto.save(file=os.path.join(root_dir, 'owl/electronics.owl'), format='rdfxml')
