from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def function():
    return render_template('home.html')

@app.route('/mylabs', methods=['GET','POST'])
def function2():
    if(request.method == 'POST'):
        w1 = request.form.get('word_1')
        w2 = request.form.get('word_2')
        w3 = request.form.get('word_3')
        w4 = request.form.get('word_4')
        w5 = request.form.get('word_5')
        w6 = request.form.get('word_6')
        w7 = request.form.get('word_7')
        w8 = request.form.get('word_8')
        w9 = request.form.get('word_9')
        w10 = request.form.get('word_10')
        w11 = request.form.get('word_11')
        w12 = request.form.get('word_12')
        w13 = request.form.get('word_13')
        w14 = request.form.get('word_14')
        w15 = request.form.get('word_15')
        w16 = request.form.get('word_16')

        return render_template('mylabs.html', w1=w1, w2=w2, w3=w3, w4=w4, w5=w5, w6=w6, w7=w7, w8=w8, w9=w9, w10=w10, w11=w11, w12=w12, w13=w13, w14=w14, w15=w15,w16=w16)

if __name__ == '__main__':
    app.run()
