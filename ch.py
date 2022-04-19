from  dash import dash, dcc, html
import dash_bootstrap_components as dbc

page_chauffeur_bis = html.Div([
    # html.Video(src="/assets/CSPro The Tutorial Questionnaire.mp4", autoPlay=True, style={'width': '30%'},
    #            controls=True),
    dbc.Row(dbc.Col(
                dbc.Card([
                    # dbc.CardHeader("Entête"),
                    dbc.CardBody(html.H4("Tableau De Bord De Suivi Consommation Carburant Coordination Carto RGPH-5")),
                    # dbc.CardFooter("Pied de page")
                ], style={'text-align': 'center', 'margin': "15px"}, color="#33C6FF")

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

if '__name__'=="__main__":
    print("tsthnpez")