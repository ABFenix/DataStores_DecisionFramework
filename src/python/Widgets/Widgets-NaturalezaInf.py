exec(open("./Widgets/Widgets-VariablesGenerales.py").read())

## NATURALEZA DE LA INFORMACIÓN

w_Relacion = widgets.Dropdown(
    options={'Inexistentes': 1, 'Pocas': 2, 'Muchas': 3},
    value=3,
    description='Relaciones:',
)
w_Estructuracion = widgets.Dropdown(
    options={'Rigidas': 1, 'Variables': 2, 'Dinamicas': 3},
    value=1,
    description='Estructuras:',
)
w_Volumen = widgets.Dropdown(
    options={'Inferior a 1Tb': 1, 'Inferior a 1Pb': 2, 'Superior a 1Pb': 3},
    value=2,
    description='Volumen:',
)

w_RelacionesDinamicas = widgets.Checkbox(
    value=False,
    description='Rel. Dinamicas',
    disabled=False
)
w_ImportanciaRelDinamicas = widgets.BoundedIntText(
    value=5,
    description='',
    min=0, max=10,
    disabled=False
)

w_DatosBlob = widgets.Checkbox(
    value=False,
    description='Datos BLOB',
    disabled=False
)
w_ImportanciaDatosBlob = widgets.BoundedIntText(
    value=5,
    description='',
    min=0, max=10,
    disabled=False
)

def f_displayImportanciaRelDinamicas(x):
    items = []
    if x: 
        items = items + [w_TitleImportancia, w_ImportanciaRelDinamicas ]
    else:
        w_ImportanciaRelDinamicas.value = 5
    form3_items = Box(children=items)
    display(form3_items)
def f_displayImportanciaDatosBlob(x):
    items = []
    if x: 
        items = items + [w_TitleImportancia, w_ImportanciaDatosBlob ]
    else:
        w_ImportanciaDatosBlob.value = 5
    form4_items = Box(children=items)
    display(form4_items)


## MAIN ##
##########
form_items = Box([w_Relacion, w_Estructuracion, w_Volumen], 
                     layout=form_record_layout
                )

out11_1 = widgets.interactive_output(f_displayImportanciaRelDinamicas, {'x': w_RelacionesDinamicas})
out12_1 = widgets.interactive_output(f_displayImportanciaDatosBlob, {'x': w_DatosBlob})

form2_items = VBox([HBox([w_RelacionesDinamicas, out11_1]), HBox([w_DatosBlob, out12_1])],
                   layout = form_column2_layout)


##display ("CARACTERÍSTICAS DE LOS DATOS")
display (form_items, form2_items)
