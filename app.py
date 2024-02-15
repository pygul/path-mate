from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')


@app.route("/object_detection")
def obj():
  return render_template('obj.html')


@app.route("/face_recognition")
def face():
  return render_template('face.html')


@app.route("/distance_analysis")
def dis():
  return render_template('dis.html')


@app.route("/process_object", methods=["POST"])
def process_object():
  if 'image' in request.files:
    image_file = request.files['image']
    # You can save it to a specific location, process it, etc.
    return "Image received and processing started!"
  else:
    return "No image selected."


@app.route("/process_face", methods=["POST"])
def process_face():
  if 'image' in request.files:
    image_file = request.files['image']
    # Process the image for face recognition
    return "Image received for face recognition!"
  else:
    return "No image selected for face recognition."


@app.route("/process_distance", methods=["POST"])
def process_distance():
  if 'image' in request.files:
    image_file = request.files['image']
    # Process the image for distance analysis
    return "Image received for distance analysis!"
  else:
    return "No image selected for distance analysis."


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
