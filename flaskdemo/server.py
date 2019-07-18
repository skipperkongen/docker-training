from flask import Flask, send_from_directory, render_template
import redis
import socket


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
hostname = socket.gethostname()


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.errorhandler(500)
def error(e):
    return render_template('error.html', hostname=hostname, error=e), 500


@app.route("/")
def index():
    try:
        numhits = get_hit_count()
    except:
        numhits = '? (counter unavailable)'
    return render_template("index.html", hostname=hostname, numhits=numhits)

@app.route("/slides")
def slides():
    return render_template("slides.html")


@app.route("/assets/<path:path>")
def assets(path):
    return send_from_directory("assets", path)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
