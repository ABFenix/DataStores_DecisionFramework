# VARIABLES GENERALES

from ipywidgets import widgets, Button, Layout, IntSlider, HBox, VBox, IntText, FloatSlider, interact, Label, Box, FloatRangeSlider, IntRangeSlider
import ipywidgets
style = {'button_width': 'initial',
        'description_width': 'initial'}
form_record_layout = Layout(
    display='flex',
    flex_flow='row',
    justify_content='space-between',
    align_items='inherit'#, 'center', flex-start', 'flex-end', 'center', 'baseline', 'stretch', 'inherit', 'initial', 'unset',
)
form2_record_layout = Layout(
    display='flex',
    flex_flow='row',
    justify_content='space-between',
    align_items='inherit',#, 'center', flex-start', 'flex-end', 'center', 'baseline', 'stretch', 'inherit', 'initial', 'unset',
    width = '55%'
)
variable_record_layout = Layout(
    #flex='0 1 auto', 
    width='40%',
    #display='flex',
    flex_flow='row',
    justify_content='flex-start',
    align_content='stretch',
    align_items='initial',#, 'center', flex-start', 'flex-end', 'center', 'baseline', 'stretch', 'inherit', 'initial', 'unset',
)
form_column_layout = Layout(
    display='flex',
    flex_flow='column',
    border='solid 2px',
    #align_items='stretch',
    #width='100%'
)
form_column2_layout = Layout(
    display='flex',
    flex_flow='column',
    #border='solid 2px',
    justify_content='space-between',
    align_items='stretch'
    #width='100%'
)
