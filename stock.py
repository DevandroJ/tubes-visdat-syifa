from bokeh.models.widgets.tables import TableWidget
import numpy as np
from random import randint

from bokeh.io import curdoc, show, output_notebook
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn, CustomJS, Dropdown
from bokeh.models import ColumnDataSource, Select, Div, Title, WidgetBox, Panel, Tabs, Paragraph
from bokeh.models.widgets import Button

from bokeh.plotting import figure
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
# from test import datetime
from datetime import date
import pandas as pd
from bokeh.palettes import Spectral4
import bokeh.sampledata

import os

bokeh.sampledata.download()

# Helper untuk formatting data date & time
def datetime(x):
    return np.array(x, dtype=np.datetime64)

# GET ALL STOCK DATA
p_all = figure(width=1800, height=500, x_axis_type="datetime")
p_all.title.text = 'Click on legend entries to hide the corresponding lines'

for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    p_all.line(df['date'], df['close'], line_width=2, color=color, alpha=0.8, legend_label=name)

p_all.legend.location = "top_left"
p_all.legend.click_policy="hide"

# Inisiasi Tabel Dataset Apple
data = dict(
        # dates=[date(2014, 3, i+1) for i in range(10)],
        dates=[(AAPL['date'], i+1) for i in range(10)],
        adj_close=[(AAPL['adj_close'], i+1) for i in range(10)],
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="dates", title="Date"),
        TableColumn(field="adj_close", title="Adj Close"),
    ]
data_table = DataTable(source=source, columns=columns, width=700, height=280)

# Inisiasi Tabel Dataset Google
data_google = dict(
        # dates=[date(2014, 3, i+1) for i in range(10)],
        dates=[(GOOG['date'], i+1) for i in range(10)],
        adj_close=[(GOOG['adj_close'], i+1) for i in range(10)],
    )
source_google = ColumnDataSource(data_google)

columns_google = [
        TableColumn(field="dates", title="Date"),
        TableColumn(field="adj_close", title="Adj Close"),
    ]
data_table_google = DataTable(source=source_google, columns=columns_google, width=700, height=280)

# Inisiasi Tabel Dataset IBM
data_ibm = dict(
        # dates=[date(2014, 3, i+1) for i in range(10)],
        dates=[(IBM['date'], i+1) for i in range(10)],
        adj_close=[(IBM['adj_close'], i+1) for i in range(10)],
    )
source_ibm = ColumnDataSource(data_ibm)

columns_ibm = [
        TableColumn(field="dates", title="Date"),
        TableColumn(field="adj_close", title="Adj Close"),
    ]
data_table_ibm = DataTable(source=source_ibm, columns=columns_ibm, width=700, height=280)

# Inisiasi Tabel Dataset MICROSOFT
data_msft = dict(
        # dates=[date(2014, 3, i+1) for i in range(10)],
        dates=[(MSFT['date'], i+1) for i in range(10)],
        adj_close=[(MSFT['adj_close'], i+1) for i in range(10)],
    )
source_msft = ColumnDataSource(data_msft)

columns_msft = [
        TableColumn(field="dates", title="Date"),
        TableColumn(field="adj_close", title="Adj Close"),
    ]
data_table_msft = DataTable(source=source_msft, columns=columns_msft, width=700, height=280)

# Paragraf untuk Judul Pada Tabel
p = Paragraph(text="""Dataset Closing Stock Market Apple""",
width=400, height=10)

# Paragraf untuk Judul Pada Tabel
pg = Paragraph(text="""Dataset Closing Stock Market Google""",
width=400, height=10)

# Paragraf untuk Judul Pada Tabel
pibm = Paragraph(text="""Dataset Closing Stock Market IBM""",
width=400, height=10)

pm = Paragraph(text="""Dataset Closing Stock Market Microsoft""",
width=400, height=10)


# Tombol Download untuk mengunduh dataset Stock
source = ColumnDataSource({'Date':AAPL['date'],'Adj_Close':AAPL['adj_close']})
button = Button(label="Download Dataset APPLE Stock", button_type="success")
button.js_on_click(CustomJS(args=dict(source=source),code=open(os.path.join(os.path.dirname(__file__),"download.js")).read()))

source2 = ColumnDataSource({'Date':GOOG['date'],'Adj_Close':GOOG['adj_close']})
button2 = Button(label="Download Dataset GOOGLE Stock", button_type="success")
button2.js_on_click(CustomJS(args=dict(source=source2),code=open(os.path.join(os.path.dirname(__file__),"download.js")).read()))

source3 = ColumnDataSource({'Date':IBM['date'],'Adj_Close':IBM['adj_close']})
button3 = Button(label="Download Dataset IBM Stock", button_type="success")
button3.js_on_click(CustomJS(args=dict(source=source3),code=open(os.path.join(os.path.dirname(__file__),"download.js")).read()))

source4 = ColumnDataSource({'Date':MSFT['date'],'Adj_Close':MSFT['adj_close']})
button4 = Button(label="Download Dataset MICROSOFT Stock", button_type="success")
button4.js_on_click(CustomJS(args=dict(source=source4),code=open(os.path.join(os.path.dirname(__file__),"download.js")).read()))

p_kel = Paragraph(text="""Nama Kelompok: """,
width=400, height=10)

p_kel1 = Paragraph(text="""Arif Jundi Firdausi(1301174081)""",
width=400, height=10)

p_kel2 = Paragraph(text="""Syifa Khairunnisa Salsabila(1301184109)""",
width=400, height=10)

p_kel3 = Paragraph(text="""Artamira R. (1301184394)""",
width=400, height=10)

kel_tab = column(p_kel, p_kel1, p_kel2, p_kel3)

# Gabungkan semua konten grafik pada 1 tab menggunakan Tabs
# Gabungkan dan urutkan sesuai Paragraf, Tabel, Tombol Download, & juga Dropdown
dataset_layout1 = column(p, data_table, button, pg, data_table_google, button2)
dataset_layout2 = column(pibm, data_table_ibm, button3, pm, data_table_msft, button4)
dataset_layout = row(dataset_layout1, dataset_layout2)


tab1 = Panel(child=p_all, title="Grafik Saham")
tab2 = Panel(child=dataset_layout, title="Dataset")
tab3 = Panel(child=kel_tab, title="Nama Kelompok")

layout = Tabs(tabs=[tab3, tab1, tab2])

# show(layout) # akan otomatis membuka Browser (dir)

curdoc().add_root(layout)
curdoc().title = "Stock Interactive Visualization using Bokeh"
