exec(open("./Widgets/Widgets-VariablesGenerales.py").read())

## NATURALEZA DE LAS CONSULTAS

w_ImportanciaBasica = widgets.Dropdown(
    options={'Críticas': 1, 'Alta': 2, 'Media': 3, 'No se requieren': 4},
    value=2,
    description='Básicas:',
)
w_ImportanciaSimple = widgets.Dropdown(
    options={'Críticas': 1, 'Alta': 2, 'Media': 3, 'No se requieren': 4},
    value=2,
    description='Simples:',
)
w_ImportanciaCompleja = widgets.Dropdown(
    options={'Críticas': 1, 'Alta': 2, 'Media': 3, 'No se requieren': 4},
    value=2,
    description='Complejas:',
)

w_Complejidad = IntRangeSlider(
    value=[40, 60],
    min=0,
    max=100,
    step=1,
    #description='Porcentaje:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d',
)

w_Dinamicas = widgets.Checkbox(
    value=False,
    description='Consultas Dinamicas',
    disabled=False
)

w_Predef = widgets.Checkbox(
    value=False,
    description='Consultas Predefinidas',
    disabled=False
)

w_FTS = widgets.Checkbox(
    value=False,
    description='Consultas FTS',
    disabled=False
)
w_ImportanciaFTS = widgets.BoundedIntText(
    value=5,
    description='',
    min=0, max=10,
    disabled=False
)

w_Filtros = widgets.Checkbox(
    value=True,
    description='Filtrados',
    disabled=False
)
w_ImportanciaFiltros = widgets.BoundedIntText(
    value=5,
    description='',
    min=0, max=10,
    disabled=False
)

w_Agreg = widgets.Checkbox(
    value=True,
    description='Agregaciones',
    disabled=False
)
w_ImportanciaAgreg = widgets.BoundedIntText(
    value=5,
    description='',
    min=0, max=10,
    disabled=False
)

w_vacia = Box([])

w_TitleComplejidad = Label(value='Grado de Importancia de las Consultas por Tipo:')
w_TitleConsultaBasica = Label(value='Consultas Basicas:')
w_TitleConsultaSimple = Label(value='Consultas Simples:')
w_TitleConsultaCompleja = Label(value='Consultas Complejas:')
w_TitlePorcentajexTipo = Label(value='Porcentaje de consultas por tipología:')
w_TitleCapacidades = Label(value='Capacidades:')
w_TitleImportancia = Label(value='Importancia:')

'''
def f_Porcentajes(x, y, z):
    if not ((x != y) 
        and (y != z)
        and (x != z)):
        out1_2 = widgets.interactive_output(f_displayComplejidad, {'h': w_Complejidad})
        display(w_Complejidad, out1_2)
    else:
        w_Complejidad.value = (40,60)
        display(w_vacia)
'''

def f_displayComplejidad(h):
    w_ValorConsultaBasica = Label(value= str(h[0]))
    w_ValorConsultaSimple = Label(value= str(h[1] - h[0]))
    value_w_Result = str(100 - h[1])
    w_ValorConsultaCompleja = Label(value= value_w_Result)
    form2_items = Box([w_TitleConsultaBasica, w_ValorConsultaBasica,
                      w_TitleConsultaSimple, w_ValorConsultaSimple,
                      w_TitleConsultaCompleja, w_ValorConsultaCompleja], 
                     layout=form2_record_layout)
    display(form2_items)

def f_Complejas(z):
    if z != 4:
        out2_2 = widgets.interactive_output(f_Dinamicas, {'x': w_Dinamicas})
        variable_record_layout.width = '40%'
        first_Vbox = HBox([w_Dinamicas, w_TitleCapacidades],
                          layout=variable_record_layout)
        form3_items = HBox([first_Vbox, out2_2])
    else:
        w_Dinamicas.value = False
        form3_items = w_vacia
    display(form3_items)
        
def f_Dinamicas(x):
    if x:
        #display(w_FTS, w_Filtros, w_Agreg)
        out2_3 = widgets.interactive_output(f_displayImportanciaFTS, {'x': w_FTS})
        out2_4 = widgets.interactive_output(f_displayImportanciaFiltros, {'x': w_Filtros})
        out2_5 = widgets.interactive_output(f_displayImportanciaAgreg, {'x': w_Agreg})
        form4_items = VBox([HBox([w_FTS, out2_3]), HBox([w_Filtros, out2_4]), HBox([w_Agreg, out2_5])],
                          layout = form_column_layout)
    else:
        w_FTS.value = False
        w_Filtros.value = True
        w_Agreg.value = True
        form4_items = w_vacia
    display(form4_items)
         
def f_displayImportanciaFTS(x):
    items = []
    if x: 
        items = items + [w_TitleImportancia, w_ImportanciaFTS ]
    else:
        w_ImportanciaFTS.value = 5
    form6_items = Box(children=items)
    display(form6_items)
def f_displayImportanciaFiltros(x):
    items = []
    if x: 
        items = items + [w_TitleImportancia, w_ImportanciaFiltros ]
    else:
        w_ImportanciaFiltros.value = 5
    form7_items = Box(children=items)
    display(form7_items)
def f_displayImportanciaAgreg(x):
    items = []
    if x: 
        items = items + [w_TitleImportancia, w_ImportanciaAgreg ]
    else:
        w_ImportanciaAgreg.value = 5
    form8_items = Box(children=items)
    display(form8_items)

def f_ComplejasPredef(z):
    if z != 4:
        form5_items = w_Predef
    else:
        w_Predef.value = False
        form5_items = w_vacia
    display(form5_items)
    
    
## MAIN ##
##########
form_items = Box([w_ImportanciaBasica, w_ImportanciaSimple, w_ImportanciaCompleja], 
                     layout=form_record_layout
                )

#out1_1 = widgets.interactive_output(f_Porcentajes, {'x': w_ImportanciaBasica, 'y': w_ImportanciaSimple, 'z': w_ImportanciaCompleja })    
out1_2 = widgets.interactive_output(f_displayComplejidad, {'h': w_Complejidad}) 
out2_1 = widgets.interactive_output(f_Complejas, {'z': w_ImportanciaCompleja })
out3_1 = widgets.interactive_output(f_ComplejasPredef, {'z': w_ImportanciaCompleja })

##display ("NATURALEZA DE LAS CONSULTAS")
display(w_TitleComplejidad, form_items, w_TitlePorcentajexTipo, w_Complejidad, out1_2, out2_1, out3_1)
