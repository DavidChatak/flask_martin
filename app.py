from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return "hello world"
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/hello<name>")
def hello(name):
    return f'sonuc vs - {name}\n'
    # return  f"hello {name}"
@app.route("/<num>")
def math(num):
    num = int(num)
    result = f"{num**2, num**3}"
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug="on")