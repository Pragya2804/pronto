# coding: utf-8
from __future__ import unicode_literals

#class OboSection(enum.Enum):
class OboSection(object):
    meta    = 1
    typedef = 2
    term    = 3

#class OwlSection(enum.Enum):
class OwlSection(object):
    ontology = 1
    classes  = 2


owl_ns = {
    'dc':       "http://purl.org/dc/elements/1.1/",
    'doap':     "http://usefulinc.com/ns/doap#",
    'foaf':     "http://xmlns.com/foaf/0.1/",
    'meta':     "http://www.co-ode.org/ontologies/meta.owl#",
    'obo':      "http://purl.obolibrary.org/obo/",
    'oboInOwl': "http://www.geneontology.org/formats/oboInOwl#",
    'owl':      "http://www.w3.org/2002/07/owl#",
    'protege':  "http://protege.stanford.edu/plugins/owl/protege#",
    'rdf':      "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'rdfs':     "http://www.w3.org/2000/01/rdf-schema#",
    'skos':     "http://www.w3.org/2004/02/skos/core#",
    'ubprop':   "http://purl.obolibrary.org/obo/ubprop#",
    'uberon':   "http://purl.obolibrary.org/obo/uberon#",
    'xsd':      "http://www.w3.org/2001/XMLSchema#",
}

owl_to_obo = {
    'hasDbXref': 'xref',
    'equivalentClass': 'equivalent_to',
    'inSubset': 'subset',
    'hasOBONamespace': 'namespace',
    'hasOBOFormatVersion': 'format-version',
    'hasExactSynonym': 'exact_synonym',
    'hasBroadSynonym': 'broad_synonym',
    'hasNarrowSynonym': 'narrow_synonym',

    #FEAT# Translate Information Ontology
    #FEAT# 'IAO_0000115': 'definition',

    #FEAT# Extract Owl defined Relationship
    #FEAT# 'is_metadata_tag': 'is_metadata_tag',
}


