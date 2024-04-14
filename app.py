from flask import render_template
import config
from data import make_tree

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
  tree = make_tree()
  return render_template("home.html", data=tree)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8765, debug=True)
