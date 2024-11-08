import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Load the Excel data
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Initialize Dash app
app = Dash(__name__)

# Load Excel file data using your specified file path
file_path = r'D:\\2024\\Polio-2024\\NID-II Feb (26 Feb to 3 Mar) 2024\\Reports NID-II Feb 2024\\Day-1 NID-II  (26 Feb to 3 March), 2024 District Rawalpindi.xlsx'
df = load_data(file_path)

# Assuming relevant columns exist: 'Total Target', 'Coverage', 'House to House Target', 'NA', 'Refusal', 'Vaccine', 'HRMP'
# You might need to adjust column names depending on your data structure.

# Dashboard layout
app.layout = html.Div(children=[
    html.H1(children='Polio Campaign Performance Dashboard'),

    # Performance Table
    html.Div([
        html.H3('Performance Table'),
        html.Table(
            # Header
            [html.Tr([html.Th(col) for col in ['Metric', 'Value']])] +
            # Data rows
            [
                html.Tr([html.Td('Total Target'), html.Td(df['Coverage'].sum())]),
                html.Tr([html.Td('Coverage Against Target'), html.Td(df['Coverage'].sum())]),
                html.Tr([html.Td('House to House Target'), html.Td(df['Coverage'].sum())])
            ]
        )
    ]),

    # Dropdown to select metric for graph charts
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Coverage Against Overall Target', 'value': 'Coverage'},
            {'label': 'House to House Target', 'value': 'House to House Target'},
            {'label': 'NA (Not Available)', 'value': 'NA'},
            {'label': 'Refusal', 'value': 'Refusal'},
            {'label': 'Vaccine', 'value': 'Vaccine'},
            {'label': 'HRMP', 'value': 'HRMP'}
        ],
        value='Coverage',  # Default selection
        clearable=False
    ),

    # Graphs for Coverage and Metrics
    html.Div([
        dcc.Graph(id='bar-chart'),
        dcc.Graph(id='pie-chart')
    ])
])

# Callback to update the bar and pie charts based on selected metric
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('metric-dropdown', 'value')]
)
def update_graphs(selected_metric):
    # Bar Chart
    bar_fig = px.bar(df, x=df.index, y=selected_metric, title=f'{selected_metric} Bar Chart')
    
    # Pie Chart
    pie_fig = px.pie(df, names=df.index, values=selected_metric, title=f'{selected_metric} Pie Chart')

    return bar_fig, pie_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
