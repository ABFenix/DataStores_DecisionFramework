exec(open("./Widgets/Widgets-VariablesGenerales.py").read())

## VOLATILIDAD

w_VolatilidadEnt = IntRangeSlider(
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

w_VolatilidadReg = IntRangeSlider(
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

def f_displayVolatilidadEnt(x):
    w_ValorInfEstaticaEnt = Label(value= str(x[0]))
    w_ValorInfHistoricaEnt = Label(value= str(x[1] - x[0]))
    value_w_Result = str(100 - x[1])
    w_ValorInfVolatilEnt = Label(value= value_w_Result)
    form5_items = Box([w_TitleInfEstaticaEnt, w_ValorInfEstaticaEnt,
                      w_TitleInfHistoricaEnt, w_ValorInfHistoricaEnt,
                      w_TitleInfVolatilEnt, w_ValorInfVolatilEnt], 
                     layout=form_record_layout)
    display(form5_items)
def f_displayVolatilidadReg(x):
    w_ValorInfEstaticaReg = Label(value= str(x[0]))
    w_ValorInfHistoricaReg = Label(value= str(x[1] - x[0]))
    value_w_Result = str(100 - x[1])
    w_ValorInfVolatilReg = Label(value= value_w_Result)
    form6_items = Box([w_TitleInfEstaticaReg, w_ValorInfEstaticaReg,
                      w_TitleInfHistoricaReg, w_ValorInfHistoricaReg,
                      w_TitleInfVolatilReg, w_ValorInfVolatilReg], 
                     layout=form_record_layout)
    display(form6_items)


w_TitleInmutabilidadEnt = Label(value='Grado de inmutabilidad de las entidades de datos (%):')
w_TitleInfEstaticaEnt = Label(value='Entidades con información estática:')
w_TitleInfHistoricaEnt = Label(value='Entidades con información histórica:')
w_TitleInfVolatilEnt = Label(value='Entidades con información volatil:')
w_TitleInmutabilidadReg = Label(value='Grado de inmutabilidad de los registros (%):')
w_TitleInfEstaticaReg = Label(value='Registros con información estática:')
w_TitleInfHistoricaReg = Label(value='Registros con información histórica:')
w_TitleInfVolatilReg = Label(value='Registros con información volatil:')


## MAIN ##
##########

out13_1 = widgets.interactive_output(f_displayVolatilidadEnt, {'x': w_VolatilidadEnt})
out14_1 = widgets.interactive_output(f_displayVolatilidadReg, {'x': w_VolatilidadReg})

#display ("VOLATILIDAD")
display (w_TitleInmutabilidadEnt, w_VolatilidadEnt, out13_1, w_TitleInmutabilidadReg, w_VolatilidadReg, out14_1)
