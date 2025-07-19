from flask import Flask, render_template_string, Response
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_dataframe():
    file_path = r"C:\Users\avram\OneDrive\Desktop\TRG Week 33\cost.us.txt"

    try:
        # Load data
        df = pd.read_csv(file_path, sep=",", engine="python", parse_dates=['Date'])

        # Drop 'OpenInt' column if it exists
        if 'OpenInt' in df.columns:
            df = df.drop(columns=['OpenInt'])

        # Convert to HTML
        html_table = df.to_html(classes='table table-bordered table-striped', index=False)

        # Render in Bootstrap HTML template
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>COST Stock Data - Week 33</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h1 class="mt-4 mb-4">COST Stock Data (Raw Table)</h1>
                {html_table}
            </div>
        </body>
        </html>
        """

        return render_template_string(html_template)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
