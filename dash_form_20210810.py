import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
#import smtplib,ssl
from tinydb import TinyDB, Query


#dashboard component
email_input = dbc.FormGroup(
                [dbc.Label("Email", html_for="email-row", width=2)
                , dbc.Col(dbc.Input(type="email"
                , id="email-row"
                , placeholder="Email ") #end input
                , width=10) #end col
                ], row=True)#end formgroup

user_input = dbc.FormGroup(
                [dbc.Label("Name", html_for="name-row", width=2)
                ,dbc.Col(dbc.Input(type="text"
                , id="name-row"
                , placeholder="Name "
                , maxLength = 80)#end input
                , width=10) #end column
                ],row=True)#end form group

term = dbc.FormGroup([dbc.Label("Term(s) ", html_for="term-row", width=2)
                ,dbc.Col(dbc.Textarea(id = "term-row"
                , className="mb-3"
                , placeholder="Term(s) separated by comma (,) "
                , required = True) #end textarea
                , width=10) #end column
                ], row=True) #end form group

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

color = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#Layout section: Bootstrap (https://hackerthemes.com/bootstrap-cheatsheet/)
app.layout = html.Div([
            dbc.Container([
                dbc.Card(
                    dbc.CardBody([
                        dbc.Form([email_input, user_input, term])
                        ,
                        html.Div(id = 'div-button', children = [
                            dbc.Button('Submit',
                                        color = 'primary',
                                        id='button-submit',
                                        n_clicks=0)
                            ] #end children
                        ) #end div
                    ])#end cardbody
                )#end card
                , html.Br()
                , html.Br()
            ]) #end container
            ,
            html.Table([html.Tr([
                html.Td(id='out-email'),
                html.Td(id='out-name'),
                html.Td(id='out-term')
            ])])#end htmlTable
            ]) #end div

@app.callback(
        [
            Output(component_id='out-email', component_property='children'),
            Output(component_id='out-name', component_property='children'),
            Output(component_id='out-term', component_property='children')
        ],
        [Input(component_id='button-submit', component_property='n_clicks')
        ,
        ]
        ,
        [
        State('email-row','value'),
        State('name-row','value'),
        State('term-row','value')
        ],
        prevent_initial_call=True
        )

def update_output(n_clicks,emailval,nameval,termval):
    if n_clicks is None:
        raise PreventUpdate
    else:

        #Storing in DB called db.json
        db = TinyDB('db.json')
        db.insert({'email':emailval, 'name':nameval, 'term': termval, 'ds': 'testing'})
        return emailval, nameval, termval
        

if __name__ == '__main__':
    app.run_server(debug=True)
