exec(open("./Widgets/Widgets-VariablesGenerales.py").read())

## NATURALEZA DE LAS ESCRITURAS
w_Operaciones = widgets.SelectMultiple(
    options=['INSERT', 'UPDATE', 'DELETE'],
    value=['INSERT'],
    #rows=10,
    description='Operaciones',
    disabled=False
)

w_Recepcion = IntSlider(
    min=0, max=100, 
    value=50, 
    description='Real-time:',
    disabled=False
)

w_Concurrencia = widgets.Checkbox(
    value=False,
    description='Concurrencia en la recepcion',
    disabled=False
)

w_TitleMetodo = Label(value='Metodo de recepción:')
w_TitleRealTime = Label(value='Datos recibidos en real-time:')
w_TitleBatch = Label(value='Datos recibidos en batch:')

def f_displayRecepcion(x):
    w_ValorRealTime = Label(value= str(x))
    value_w_Result = str(100 - x)
    w_ValorBatch = Label(value= value_w_Result)
    form_items = Box([w_TitleRealTime, w_ValorRealTime,
                      w_TitleBatch, w_ValorBatch], 
                     layout=form2_record_layout)
    display(form_items)

## MAIN ##
##########

out = widgets.interactive_output(f_displayRecepcion, {'x': w_Recepcion})

form_items = Box([w_Recepcion, w_Concurrencia], 
                     layout=form_record_layout
                )

display(w_Operaciones)
display(w_TitleMetodo, form_items, out)