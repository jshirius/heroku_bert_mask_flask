from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index_html():
    #テンプレート作成
    return render_template('index.html')

## 起動
if __name__ == "__main__":
	#bertの初期化
	
    app.run(debug=True)