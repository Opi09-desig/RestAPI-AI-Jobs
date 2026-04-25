import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import requests
import pandas as pd

# Usamos FLATLY que es muy limpio para reportes corporativos
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# --- FUNCIONES PARA OBTENER DATOS (Tus rutas funcionales) ---
def get_top_companies():
    try:
        r = requests.get("http://localhost:8000/kpi/top-hiring-companies")
        data = r.json()
        # Forzamos los nombres sin importar qué mande el API
        df = pd.DataFrame(data)
        df.columns = ["Company Name", "Total Jobs"] 
        return df
    except Exception as e:
        print(f"Error en Top Companies: {e}")
        return pd.DataFrame(columns=["Company Name", "Total Jobs"])

def get_location_demand():
    try:
        r = requests.get("http://localhost:8000/kpi/demand-by-location")
        data = r.json()
        df = pd.DataFrame(data)
        df.columns = ["Location", "Total"]
        return df
    except Exception as e:
        print(f"Error en Location Demand: {e}")
        return pd.DataFrame(columns=["Location", "Total"])

# --- COMPONENTE DE TARJETA (KPI) ESTILO IMAGEN 1 ---
def create_kpi_card(title, value, color="primary"):
    return dbc.Card(
        dbc.CardBody([
            html.H6(title, className="card-title text-uppercase text-muted small"),
            html.H2(value, className=f"card-text fw-bold text-{color}")
        ]),
        # Añadimos una sombra y un borde lateral para que se vea más moderno
        className=f"shadow-sm border-0 border-start border-{color} border-5"
    )

# --- PREPARAR GRÁFICAS MEJORADAS ---
df_comp = get_top_companies()
fig_comp = px.bar(
    df_comp, x="Company Name", y="Total Jobs", 
    title="Top Hiring Companies",
    template="plotly_white",
    color="Total Jobs", 
    color_continuous_scale="Blues"
)
fig_comp.update_layout(margin=dict(l=20, r=20, t=50, b=20), showlegend=False)

df_loc = get_location_demand()
fig_loc = px.pie(
    df_loc, names="Location", values="Total", 
    title="Market Share by Location", 
    hole=0.5, # Efecto dona para que sea más moderno
    color_discrete_sequence=px.colors.sequential.GnBu_r
)
fig_loc.update_layout(margin=dict(l=20, r=20, t=50, b=20))

# --- DISEÑO (LAYOUT) SIGUIENDO TU ESTRUCTURA ---
app.layout = dbc.Container([
    # Título Principal
    dbc.Row(dbc.Col(html.H1("AI Jobs Market Intelligence", className="text-center my-5 fw-bold text-dark"))),
    
    # Fila de FILTROS (Esquina derecha como en tu dibujo)
    dbc.Row([
        dbc.Col([
            html.Label("Filter by Location:", className="text-muted small mb-1"),
            dbc.Select(options=[{"label": "All USA", "value": "1"}], value="1")
        ], width=3)
    ], className="mb-4 justify-content-end"),

    # Fila de 4 KPIs (Imagen 1)
    dbc.Row([
        dbc.Col(create_kpi_card("Total Jobs", "500+", "primary"), width=3),
        dbc.Col(create_kpi_card("Top Employer", "Amazon", "success"), width=3),
        dbc.Col(create_kpi_card("Avg Salary", "$120k", "info"), width=3),
        dbc.Col(create_kpi_card("Active Skills", "15", "warning"), width=3),
    ], className="mb-5"),

    # Fila de Gráficas (Chart 1 y Chart 2 con fondo blanco y sombra)
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(figure=fig_comp), className="shadow-sm border-0 p-2"), width=6),
        dbc.Col(dbc.Card(dcc.Graph(figure=fig_loc), className="shadow-sm border-0 p-2"), width=6),
    ], className="mb-5")

], fluid=True, style={"backgroundColor": "#fcfcfc", "minHeight": "100vh"})

if __name__ == '__main__':
    app.run(debug=True, port=8050)