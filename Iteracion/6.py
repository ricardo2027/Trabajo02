import datetime
d={'Cumpleaños':20,'Ricardo':2002,'Fecha':datetime.date.today()}
for k,v in zip(d.keys(),d.values()):
    print(k,v)