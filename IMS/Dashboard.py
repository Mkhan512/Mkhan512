import pandas as pd
import matplotlib.pyplot as plt
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

# Dashboard layout
app.layout = html.Div(children=[
    html.H1(children='Excel Data Dashboard'),
    
    # Dropdown to select column for pie chart
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0],
        clearable=False
    ),
    
    # Table
html.Div([
    html.H3('Data Table'),
    html.Table(
        # First row - headers
        [html.Tr([html.Th(col) for col in df.columns])] +  # Headers

        # Data rows
        [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(min(len(df), 10))]  # Data rows
    )
]),

    # Graphs
    html.Div([
        dcc.Graph(id='bar-chart'),
        dcc.Graph(id='pie-chart')
    ])
])

# Callback to update the bar and pie chart
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('column-dropdown', 'value')]
)
def update_graphs(selected_column):
    # Bar chart
    bar_fig = px.bar(df, x=selected_column, y=df.index, title=f'{selected_column} Bar Chart')
    
    # Pie chart
    pie_fig = px.pie(df, names=df.index, values=selected_column, title=f'{selected_column} Pie Chart')
    
    return bar_fig, pie_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
