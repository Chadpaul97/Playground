from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template('play.html')

@app.route("/play/<num_of_boxes>")
def mutiple_boxes(num_of_boxes):
    boxes = int(num_of_boxes)
    return render_template('play2.html', boxes=boxes)

@app.route("/play/<num_of_boxes>/<color>")
def coloring_boxes(num_of_boxes,color):
    boxes = (int(num_of_boxes))
    colors = color
    return render_template('play3.html',boxes=boxes,colors=colors)



if __name__ == "__main__":
    app.run(debug=True)