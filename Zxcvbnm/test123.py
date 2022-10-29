ln=["arun","nayab"]
la=[12,15]

test={}
name={}
for sub, marks in zip(ln, la):
    test.update(name.update({sub:marks}))

print(test)






#{'temp':{'arun':12},{'nayab':13}}