def generic_model_mutation_process(model, data, id=None, commit=True):
    """
    Permite crear o actualizar una instancia de un modelo en específico,
    si el parámetro commit es verdadero el cambio se vera reflejado en la
    base de datos, de lo contrario solamente quedara en el objeto generado.

    :param model: clase del modelo del cual se va a generar la instancia
    :param data: información de los campos a modificar en la instancia
    :param id: id del registro a actualizar (solo para actualización)
    :param commit: boleano que especifica si se guardara en la base de datos
    :return: una instancia del modelo con la información actualizada
    """
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item
