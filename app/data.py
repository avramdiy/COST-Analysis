from flask import Flask, render_template_string, Response
import pandas as pd

app = Flask(__name__)

# Load and preprocess the data once
file_path = r"C:\Users\avram\OneDrive\Desktop\TRG Week 33\cost.us.txt"
df_master = pd.read_csv(file_path, sep=",", parse_dates=['Date'], engine="python")

# Drop 'OpenInt' if it exists
if 'OpenInt' in df_master.columns:
    df_master = df_master.drop(columns=['OpenInt'])

# Define date-filtered DataFrames
df_90 = df_master[(df_master['Date'] >= '1990-01-01') & (df_master['Date'] <= '1995-12-31')]
df_95 = df_master[(df_master['Date'] >= '1995-01-01') & (df_master['Date'] <= '2000-12-31')]
df_00 = df_master[(df_master['Date'] >= '2000-01-01') & (df_master['Date'] <= '2005-12-31')]
df_05 = df_master[(df_master['Date'] >= '2005-01-01') & (df_master['Date'] <= '2010-12-31')]
df_10 = df_master[(df_master['Date'] >= '2010-01-01') & (df_master['Date'] <= '2015-12-31')]

# Helper function to render HTML
def render_table(df, title):
    table_html = df.to_html(classes='table table-bordered table-striped', index=False)
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1 class="mt-4 mb-4">{title}</h1>
            {table_html}
        </div>
    </body>
    </html>
    """)

@app.route('/90')
def show_90():
    return render_table(df_90, "COST Data: 1990–1995")

@app.route('/95')
def show_95():
    return render_table(df_95, "COST Data: 1995–2000")

@app.route('/00')
def show_00():
    return render_table(df_00, "COST Data: 2000–2005")

@app.route('/05')
def show_05():
    return render_table(df_05, "COST Data: 2005–2010")

@app.route('/10')
def show_10():
    return render_table(df_10, "COST Data: 2010–2015")

@app.route('/highs_by_year_block')
def highs_by_year_block():
    import matplotlib.pyplot as plt
    import io
    import base64

    # Ensure 'Date' is datetime in all DataFrames
    for df in [df_90, df_95, df_00, df_05, df_10]:
        df['Date'] = pd.to_datetime(df['Date'])

    def get_yearly_avg_high(df, start_year):
        df_filtered = df[(df['Date'].dt.year >= start_year) & (df['Date'].dt.year < start_year + 5)]
        return df_filtered.groupby(df_filtered['Date'].dt.year)['High'].mean()

    # Get the 5 data series
    avg_90 = get_yearly_avg_high(df_90, 1990)
    avg_95 = get_yearly_avg_high(df_95, 1995)
    avg_00 = get_yearly_avg_high(df_00, 2000)
    avg_05 = get_yearly_avg_high(df_05, 2005)
    avg_10 = get_yearly_avg_high(df_10, 2010)

    # Build the aligned structure
    x_labels = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
    years = range(5)

    # Convert to lists and align
    highs_data = {
        '1990-1994': avg_90.tolist(),
        '1995-1999': avg_95.tolist(),
        '2000-2004': avg_00.tolist(),
        '2005-2009': avg_05.tolist(),
        '2010-2014': avg_10.tolist(),
    }

    # Plotting
    plt.figure(figsize=(10, 6))
    for label, values in highs_data.items():
        if len(values) == 5:
            plt.plot(x_labels, values, marker='o', label=label)

    plt.title('Average "High" Price Comparison Across 5-Year Blocks')
    plt.xlabel('Year Within Block')
    plt.ylabel('Average High Price')
    plt.legend()
    plt.grid(True)

    # Convert plot to image
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return f'''
        <html>
        <head><title>High Price 5-Year Comparison</title></head>
        <body>
            <div style="text-align: center;">
                <h1>Average "High" Price Over 5-Year Windows</h1>
                <img src="data:image/png;base64,{plot_url}" />
            </div>
        </body>
        </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)
