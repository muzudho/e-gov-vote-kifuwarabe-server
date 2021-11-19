from flask import Flask, request, render_template
from e_gov_put_bestmove_item import put_bestmove
from pprint import pprint

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('enter.html',
                           yourName='',
                           secret='',
                           errorMessage='')

@app.route('/vote', methods=['POST'])
def vote():
    yourName = request.form['yourName']
    # 長文送られても困るし適当にスライスしよ（＾～＾）
    yourName = yourName[0:20]
    # secret を難読にする時間がなかったので平文で埋め込み
    secret=request.form['secret']
    secret = secret[0:20]

    if len(yourName) < 1 or len(secret) < 1:
        return render_template('enter.html',
                               yourName=yourName,
                               secret=secret,
                               errorMessage='1文字以上入力してください')
    else:
        return render_template('vote.html',
                               yourName=yourName,
                               secret=secret)

@app.route('/thanks', methods=['POST'])
def thanks():
    yourName = request.form['yourName']
    yourName = yourName[0:20]
    secret=request.form['secret']
    secret = secret[0:20]
    m = request.form['bestmove']
    m = m[0:10]

    if len(m) < 1:
        return render_template('vote.html',
                        yourName=yourName,
                        secret=secret,
                        bestmove=m,
                        errorMessage='1文字以上入力してください')
    else:
        # 投票します
        response = put_bestmove(yourName, secret, m)
        print("Put bestmove succeeded:")
        pprint(response, sort_dicts=False)

        return render_template('thanks.html',
                            yourName=yourName,
                            secret=secret,
                            bestmove=m)

@app.route('/back', methods=['POST'])
def back():
    yourName = request.form['yourName']
    yourName = yourName[0:20]
    secret=request.form['secret']
    if 0 < len(secret):
        secret = secret[0:20]
    return render_template('vote.html',
                           yourName=yourName,
                           secret=secret)

# メイン・プログラムとして走らせるとき。
if __name__ == "__main__":
    app.run(debug=True)
