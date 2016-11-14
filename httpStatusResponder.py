from flask import Flask
app = Flask(__name__)

@app.route("/status/<int:code>//<path:path>")
@app.route("/status/<int:code>/<path:path>")
@app.route("/status/<int:code>", defaults = {'path':''} )
def error(code, path):
    content = "<html><head>"
    content += "<link href=\"https://fonts.googleapis.com/css?family=Delius+Unicase\" rel=\"stylesheet\">" 
    content += "<style>body{font-family: \"Delius Unicase\", cursive; margin:75px; color: white; background:#4e4e4e;} h1{font-size:1.2em}</style></head><body>"
    content += "<h1>status " + str(code) + "</h1>"
    content += "<p>here is the status you requested</p>"
    content += "</body></html>"

    return content, code
    

if __name__ == "__main__":
    app.run()
    
