#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
from keras.models import load_model
model = load_model("dia_model.h5")

f = cgi.FieldStorage()

pregnant = float(f.getvalue("pregnant"))
glucose = float(f.getvalue("glucose"))
bloodpressure = float(f.getvalue("bloodpressure"))
skin = float(f.getvalue("skin"))
insulin = float(f.getvalue("insulin"))
mass = float(f.getvalue("mass"))
diabetes = float(f.getvalue("diabetes"))
age = float(f.getvalue("age"))

output = model.predict([[pregnant,glucose,bloodpressure,skin,insulin,mass,diabetes,age]])

if output[0][0] < 1:
    print("yes")
else:
    print("No")

print(output)
