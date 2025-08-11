from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Aquí luego podemos pasar datos reales
    league = {"name": "Mi Liga"}
    standings = []
    teams = []
    return render_template("league.html", league=league, standings=standings, teams=teams)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
