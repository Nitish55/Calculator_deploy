from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method == 'POST'):
        try:
            operation = request.form['operation']
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
        except Exception as e:
            return render_template('index1.html', result=e)
        else:
            if (operation == 'add'):
                r = num1 + num2
                result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'subtract'):
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'multiply'):
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'divide'):
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            if (operation == 'Sqre'):
                r = num1 ** num2
                result = 'the Square when ' + str(num1) + ' times of  ' + str(num2) + ' is ' + str(r)
            if (operation == 'Prime'):
                lt = list()
                for i in range(num1, num2):
                    if i > 1:
                        for j in range(2, i - 1):
                            if i % j == 0:
                                break
                        else:
                            lt.append(i)

                result = 'Prime no between ' + str(num1) + ' and  ' + str(num2) + ' is ' + str(lt)

            if (operation == 'Fibonacci'):
                n1, n2 = num1, 1
                n3 = num1
                cnt = num1
                lt1 = list()
                while (num1 < num2):
                    lt1.append(n1)
                    n1 = n2 + n1
                    n2 = n3
                    n3 = n1
                    num1 += 1
                result = 'Finonacci series between ' + str(cnt) + ' and  ' + str(num2) + ' is ' + str(lt1)

            return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run()
