# The SPARQL Query here is not correct. With these condistions it will not find anything. Please do the following:
# 1. Find the lable for "ind" which are in a class and save them in a dictionary. Then print the items from this dictionary.
# 2. Find the lable for "ind" which are in a Sub Function property and save them in a dictionary. Then print the items from this dictionary.

from rdflib import Graph


g = Graph()
g.parse(file=open("KBSPARQL.n3", "r"), format="text/n3")

queries = {}

labels_in_classes = g.query(
   """SELECT DISTINCT ?label
      WHERE {
         ?ind rdf:type ?classes.
         ?ind rdfs:label ?label.
      }""")
queries["classes"] = labels_in_classes 

labels_in_properties = g.query(
   """SELECT DISTINCT ?label
      WHERE {
         ?ind prop:SubFunction ?function.
         ?ind rdfs:label ?label.
      }""")
queries["properties"] = labels_in_properties

for selection, query in queries.items():
   print(f'=======ind labels from {selection}======')
   for row in query:
      label = str(row.asdict()['label'].toPython())
      print(label)
