from flask import Flask, render_template, request
from phe import paillier

app = Flask(__name__)

# Generate Paillier public and private key pairs
public_key, private_key = paillier.generate_paillier_keypair()


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    # Get plaintext from HTML form
    plaintext = int(request.form['plaintext'])

    # Encrypt plaintext using Paillier public key
    ciphertext = public_key.encrypt(plaintext)

    return render_template('result.html', ciphertext=ciphertext)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
