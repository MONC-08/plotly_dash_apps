import dash 
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Welcome to the dash Polling app!"),
    html.Div([
        "Input: ", dcc.Input(id="input1", type="text", placeholder="initial value")
    ]),
    html.Br(),
    html.Div(id="output-div")
])

@app.callback(Output(), input())

if __name__ == "__main__":
    app.run(debug = True)



