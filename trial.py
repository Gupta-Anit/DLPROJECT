''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput,TextAreaInput
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import CustomJS, Button
from bokeh.layouts import row, column
from bokeh.plotting import figure

def get_the_headline(sent):
    return sent+' '+sent


def textsummary(summary):
    get_the_headline(text_input.value)
    summary_output.value=get_the_headline(text_input.value)
text_input="Enter Headline"

text_input = TextAreaInput(cols=200, title="Enter Headline")
summary_output = TextInput(title="Summary Generated")
savebutton = Button(label="Generate Summary", button_type="success")


savebutton.on_click(textsummary)


inputs = column(text_input,summary_output,savebutton)

curdoc().add_root(row(inputs, width=800))
curdoc().title = "Sliders"
show(inputs)
