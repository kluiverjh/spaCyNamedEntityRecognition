
import en_core_web_sm
# import xx_ent_wiki_sm
import json
from pprint import pprint

nlp = en_core_web_sm.load()
# nlp = xx_ent_wiki_sm.load()

f=open("plaintext.txt", "r")
contents =f.read()
f.close

nytimes= nlp(contents)

# entities=[(i, i.label_, i.label) for i in nytimes.ents]

# span type 

x = {
  "PERSON": "|".join([i.text for i in nytimes.ents if i.label_ == "PERSON"]),
  "NORP": "|".join([i.text for i in nytimes.ents if i.label_ == "NORP"]),
  "FAC": "|".join([i.text for i in nytimes.ents if i.label_ == "FAC"]),
  "ORG": "|".join([i.text for i in nytimes.ents if i.label_ == "ORG"]),
  "GPE": "|".join([i.text for i in nytimes.ents if i.label_ == "GPE"]),
  "LOC": "|".join([i.text for i in nytimes.ents if i.label_ == "LOC"]),
  "PRODUCT": "|".join([i.text for i in nytimes.ents if i.label_ == "PRODUCT"]),
   "EVENT": "|".join([i.text for i in nytimes.ents if i.label_ == "EVENT"])
}
y = json.dumps(x, indent=4)

# the result is a JSON string:
print(y)

