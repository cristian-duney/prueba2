import os
import pandas as pd
from dash import Dash, html, dash_table, dcc
import plotly.express as px

# 1) Definir rutas absolutas
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "ejemplo.csv")

# 2) Leer CSV
df = pd.read_csv(CSV_PATH)

# 3) Crear instancia de Dash
app = Dash(__name__)
server = app.server  # Exponer el servidor para Gunicorn/Render

# 4) Crear gráfico de barras
bar_fig = px.bar(df, x='Nombre', y='Edad', title='Edad por persona')

# 5) Definir layout
app.layout = html.Div([
    html.H1("Dash en Render – Ejemplo con data/ fuera de src"),
    
    html.H2("Tabla de datos"),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in df.columns],
        style_table={'margin-bottom': '50px'}
    ),

    html.H2("Gráfico de barras"),
    dcc.Graph(figure=bar_fig)
])

# 6) Arranque local
if __name__ == '__main__':
    app.run(debug=True)
