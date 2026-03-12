import dash 
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    # html.H1("Welcome to the dash Polling app!"),

    dcc.Location(id="url", refresh=False),
    
    # dcc.Link("Home", href="/"),
    # html.Br(),
    # dcc.Link("polls", href="/polls"),
    # html.Br(),
    # dcc.Link("Poll Result", href="/polls_result"),

    html.Div(id="output-div") # output div
])

home_layout = html.Div(children=[
    html.H1("Welcome to the dash Polling app!"),
    dcc.Link("Home", href="/"),
    html.Br(),
    dcc.Link("polls", href="/polls"),
    html.Br(),
    dcc.Link("Poll Results", href="/polls_results")
])

polls_layout = html.Div(children=[
    html.H1("This is the Poll page..."),
    dcc.Link("Home", href="/")
])

polls_results_layout = html.Div(children=[
    html.H1("Here is the Poll results..."),
    dcc.Link("Home", href="/")
])

@app.callback(
    Output(component_id="output-div", component_property="children"), 
    Input(component_id="url", component_property="pathname")
)
def update_output(pathname):

    # output_val = f'Output: {input_value}'
    if pathname == "/polls":
        return polls_layout
    elif pathname == "/polls_results":
        return polls_results_layout
    else:
        return home_layout
    


if __name__ == "__main__":
    app.run(debug = True)