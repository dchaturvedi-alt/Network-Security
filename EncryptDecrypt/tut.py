from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
	return render_template("index.html")

@app.route("/crypt", methods=["POST"])
def crypt():
	s = request.form["fname"]
	t = ""
	for c in s:
		if ord(c) >= ord('a') and ord(c) <= ord('z'):
			t += chr(ord('z')-ord(c)+ord('a'))
		elif  ord(c) >= ord('A') and ord(c) <= ord('Z'):
			t += chr(ord('Z')-ord(c)+ord('A'))
		else:
			t += c

	if "encrypt" in request.form:
		print("YES")
		return render_template("crypt.html", content=t, ty="encrypt", org=s)
	else:
		return render_template("crypt.html", content=t, ty="decrypt", org=s)


if __name__ == "__main__":
	app.run()
