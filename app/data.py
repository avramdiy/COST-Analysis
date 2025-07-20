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

if __name__ == '__main__':
    app.run(debug=True)
