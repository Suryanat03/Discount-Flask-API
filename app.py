from flask import Flask , request , jsonify


app = Flask(__name__)

@app.route("/ass" , methods = ['POST'])
def discount():
    if (request.method == 'POST'):
        item1 = request.json['item1']
        item2 = request.json['item2']
        item3 = request.json['item3']
        item4 = request.json['item4']
        item5 = request.json['item5']
        subtotal = item1 + item2 + item3 + item4 + item5
        total=0
        

        if subtotal <=1000:
            total += subtotal*0.9
        elif ((subtotal>1000) and (subtotal<=3000)):
            total += subtotal*0.8
        elif subtotal > 3000:
            total += subtotal*0.7
        return jsonify(f"The dicounted price is {total}")




if __name__ == '__main__':
    app.run(host= '0.0.0.0' , port= 5001)




