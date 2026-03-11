import dash 
from dash import html
from dash import dcc
from dash import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Welcome to the dash Polling app!"),
    html.Div([
        "Input: ", dcc.Input(id="input1", type="text", placeholder="initial value", value="") # input 
    ]),
    html.Br(),
    html.Div(id="output-div") # output div
])

@app.callback(
    Output(component_id="output-div", component_property="children"), 
    Input(component_id="input1", component_property="value")
)
def update_output(input_value):

    output_val = f'Output: {input_value}'

    return output_val


if __name__ == "__main__":
    app.run(debug = True)