import pandas as pd

from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource, figure
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.layouts import column, row

output_file('vt-income.html')

file = 'vt_income.csv'
counties = pd.read_csv(file)

county_income = ColumnDataSource(counties)

color_mapper = CategoricalColorMapper(factors=['Addison VT', 'Bennington VT', 'Caledonia VT', 
												'Chittenden VT', 'Essex VT', 'Franklin VT', 
												'Grand Isle VT', 'Lamoille VT', 'Orange VT' 
												'Orleans VT', 'Rutland VT', 'Washington VT', 
												'Windham VT', 'Windsor VT'], 
												palette=['red', 'blue', 'yellow',
														 'green', 'purple','orange',
														 'black', 'brown', 'FireBrick',
														 'DeepPink','cyan', 'lightblue',
														 'lightyellow','darkgreen'])

plot=figure(x_axis_label='Population', y_axis_label='Avg-Income', tools='pan, wheel_zoom, box_zoom, reset, hover, save', title='Population vs Income')

plot.circle(x='Population', y='Avg-Income',source=county_income, size=10, color=dict(field='County', transform=color_mapper), legend='County')

hover = plot.select_one(HoverTool)
hover.tooltips = [('County', '@County'),('Avg-Income', '@Avg-Income'), ('Population', '@Population')]

plot.legend.location = 'bottom_right'
plot.legend.background_fill_color = 'lightgrey'

plot.xaxis[0].formatter.use_scientific = False
show(plot)