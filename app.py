from  dash import dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_extensions as de
import ch

df = pd.read_excel('db.xlsx', index_col="Code Chauffeur")

app = dash.Dash()
server = app.server
#------------------------------------Lotties------------------------------------------------------------------
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
#------------------------------------------------------------------------------------------------------
max_kilomettrage = df.groupby("VEHICULE").max("KILOMETRAGE")["KILOMETRAGE"].sum()
max_consommation = df["CONSOMMATION"].sum()
max_montant = df.groupby("VEHICULE").max("MONTANT TOTAL EN FCFA")["MONTANT TOTAL EN FCFA"].sum()
#--------------------------------------GRAPHIQUE----------------------------------------------------------
graph_kilo = px.bar(df, x='VEHICULE', y=['KILOMETRAGE', 'MONTANT TOTAL EN FCFA'])
graph_conso = px.pie(df,names='VEHICULE',values='CONSOMMATION', hole=.3, color_discrete_sequence=px.colors.sequential.RdBu)
#-----------------------------------------------IMAGES------------------------------------------------
img_speed = "assets/81852-speedometer.json"
img_conso = "assets/76838-fuel-pump.json"
img_money = "assets/69192-money.json"
#------------------------------------------------PAGES------------------------------------------------
nav_bar = dbc.Nav(children=[
    html.Img(src='/assets/RGPH-5.jpg',style={'border':'solid', 'border-radius':'10px','width':'80%',
                                             'margin-left':'15px'}),
    html.Hr(),
    dbc.NavLink("Accueil", href="/",active="exact"),
    dbc.NavLink("Situation par chauffeur", href="/page-1-ch",active="exact"),
    dbc.NavLink("Situation par carte", href="/page-2-carte",active="exact"),
],
    vertical=True,
    pills=True,
    style={
        'position':'fixed',
        'top':0,
        'bottom':0,
        'left':0,
        'width':'200px',
        'background':'#33C6FF'
    }
)



card_color='#33C6FF'
marge = '15px'
page_accueil = html.Div(children=[
    dbc.Row(dbc.Col(
                dbc.Card([
                    # dbc.CardHeader("Entête"),
                    dbc.CardBody(html.H4("Tableau De Bord De Suivi Consommation Carburant Coordination Carto RGPH-5")),
                    # dbc.CardFooter("Pied de page")
                ], style={'text-align': 'center', 'margin': marge}, color=card_color)

    )),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(de.Lottie(options=options, url=img_speed, width="20%", height="20%")),
                dbc.CardBody(daq.LEDDisplay(value=max_kilomettrage,  color="black"))
            ], color=card_color)
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(de.Lottie(options=options, url=img_conso, width="16.5%", height="15%")),
                dbc.CardBody(daq.LEDDisplay(value=max_consommation, color='black'))
            ], color=card_color)
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(de.Lottie(options=options, url=img_money, width="20%", height="20%")),
                dbc.CardBody(daq.LEDDisplay(value=max_montant, color='black'))
            ], color=card_color)
        ]),
    ], style={'margin': marge}),

    dbc.Row([
        dbc.Col(dbc.Card(
                    dbc.CardHeader(dcc.Graph(figure=graph_kilo)),
                    color=card_color
                ),
            width=7
        ),
        dbc.Col(dbc.Card(
            dbc.CardHeader(dcc.Graph(figure=graph_conso)),
            color=card_color
        ),
            width=5
        ),
    ], style={'margin': marge})


])

page_chauffeur = html.Div([
    dbc.Row(dbc.Col(
                dbc.Card([
                    # dbc.CardHeader("Entête"),
                    dbc.CardBody(html.H4("Tableau De Bord De Suivi Consommation Carburant Coordination Carto RGPH-5")),
                    # dbc.CardFooter("Pied de page")
                ], style={'text-align': 'center', 'margin': marge}, color=card_color)

    )),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H3("")),
            dbc.CardBody(dcc.Dropdown(options=[
                {'label':i, 'value':i} for i in ['val1','val2','val3']
            ]))
        ])),
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H3("")),
            dbc.CardBody(dcc.Dropdown(options=[
                {'label':i, 'value':i} for i in ['val1','val2','val3']
            ]))
        ]))
    ])
])
container = html.Div(
    id='container',
    style={
        'margin-left': '12.5rem'
    }
)
#---------------------------------------------Nav bar-----------------------------------------------------------
app.layout = html.Div([
    dcc.Location(id="url"), # pathname
    nav_bar,
    container
])

@app.callback(
    Output(component_id='container', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def load_page(path):
    if path=='/':
        return page_accueil
    elif path=='/page-1-ch':
        return ch.page_chauffeur_bis
    return "Error 404 : Cette page n'existe pas !"
app.title = 'Suivi Conso RGPH5'
app.run_server(debug=True)
