from flask import Flask, render_template

app = Flask(__name__)

# Tableau Public URLs
TABLEAU_URLS = {
    'story': 'https://public.tableau.com/views/GlobalOlympicSportsPerformance/Story1',
    'dashboard1': 'https://public.tableau.com/views/GlobalOlympicSportsPerformance/Dashboard1',
    'dashboard2': 'https://public.tableau.com/views/GlobalOlympicSportsPerformance/Dashboard2'
}

@app.route('/')
def home():
    return render_template('index.html', urls=TABLEAU_URLS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)