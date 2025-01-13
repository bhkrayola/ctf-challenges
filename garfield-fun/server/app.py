from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

@app.route('/')
def function():
    return render_template('home.html')

@app.route('/mylabs', methods=['GET'])
def index():
    words = [
        request.args.get(f'word_{i}', "")
        for i in range(1, 17)
    ]
        
    template_string = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../static/style2.css">
    <script src="../static/script2.js"></script>
</head>
<body>
    <h1>Your Garfield Lasagna Monday Madlib</h1>
    <p>
        Once upon a time, in a {} land, Garfield and his trusty {}
        set out to {} on a(n) {} adventure. 
        Garfield was feeling {} about the prospect of finding a treasure trove of {}!
        
        They {} to the secret location, and to their amazement, they found a {}
        chest filled with {}. Garfield couldn't resist {} into the delicious treat!
        
        Filled with {}, Garfield decided to {} all the way back home with the treasure chest. 
        He proudly displayed it in his {} and invited all his {} friends to join the celebration. 
        They {} and danced around the chest, having a fantastic {}.       
    </p>
</body>
</html>
'''.format(*words)
    return render_template_string(template_string)

if __name__ == '__main__':
    app.run(debug=True)
