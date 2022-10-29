# The SPARQL Query here is not correct. With these condistions it will not find anything. Please do the following:
# 1. Find the lable for "ind" which are in a class and save them in a dictionary. Then print the items from this dictionary.
# 2. Find the lable for "ind" which are in a Sub Function property and save them in a dictionary. Then print the items from this dictionary.

from rdflib import Graph


g = Graph()
g.parse(file=open("KBSPARQL.n3", "r"), format="text/n3")

class_label = "class_label"
subfunction_label = "subfunction_label"


query_result = g.query(
   f"""SELECT DISTINCT ?function ?subFunction ?{class_label} ?{subfunction_label}
      WHERE {{
         ?function rdf:type ?classes.
         ?subFunction prop:SubFunction ?function.
         ?function rdfs:label ?{class_label}.
         ?subFunction rdfs:label ?{subfunction_label}.
      }}""")


for desired_label in (class_label, subfunction_label):
   query_name = desired_label.split("_")[0]
   print(f'=======labels from {query_name}======')

   labels = set()
   for row in query_result:
      label = str(row.asdict()[desired_label].toPython())
      if label not in list(labels):
         labels.add(label)
         print(label)
