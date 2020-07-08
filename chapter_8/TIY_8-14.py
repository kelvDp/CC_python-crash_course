def make_car(manufacturer,model_name,**kwargs):

    kwargs["manufacturer"]= manufacturer
    kwargs["model name"]= model_name
    return kwargs

car = make_car("Subaru","outback",color="red",automatic=False)

print(car)
    