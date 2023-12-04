from flask import Flask, render_template, request
import sympy as sp
import numpy as np

app = Flask(__name__)

###### --------------- Metode Eliminasi Gauss --------------- ######
@app.route('/', methods=['GET', 'POST'])
def home():
    x, y, z = sp.symbols('x y z')
    variabel = [x, y, z]

    solusi = None
    pesan_error = None
    solusi_x = None
    solusi_y = None
    solusi_z = None

    if request.method == 'POST':
        persamaan1 = request.form['persamaan1']
        persamaan2 = request.form['persamaan2']
        persamaan3 = request.form['persamaan3']

        try:
            persamaan = [
                persamaan1,
                persamaan2,
                persamaan3
            ]
            
            augmentasi_matriks = sp.Matrix(persamaan)
            ref_matrix = augmentasi_matriks.rref()
            solusi = sp.solve(persamaan, variabel)

            solusi_x = solusi[x]
            solusi_y = solusi[y]
            solusi_z = solusi[z]

            print("Solusi:", solusi)
            print("Solusi x:", solusi_x)
            print("Solusi y:", solusi_y)
            print("Solusi z:", solusi_z)

        except Exception as e:
            pesan_error = "Maaf, cek lagi persamaan yang Anda masukkan. \n (ex: 2*x - 3*y - z - 3)"

    return render_template('gauss.html', solusi=solusi, solusi_x=solusi_x, solusi_y=solusi_y, solusi_z=solusi_z, pesan_error=pesan_error)


###### --------------- Metode Eliminasi --------------- ######
@app.route('/eliminasi', methods=['GET', 'POST'])
def eliminasi():
    nilai = None
    nilai_x = None
    nilai_y = None
    nilai_z = None
    pesan_error = None

    if request.method == 'POST':
        A1 = request.form['A1']
        A2 = request.form['A2']
        A3 = request.form['A3']
        konstanta = request.form['konstanta']

        try:
            A1 = [float(x) for x in A1.split(',')]
            A2 = [float(x) for x in A2.split(',')]
            A3 = [float(x) for x in A3.split(',')]
            konstanta = [float(x) for x in konstanta.split(',')]

            koefisien = np.array([A1, A2, A3], dtype=float)
            konstan = np.array(konstanta, dtype=float)

            nilai = np.linalg.solve(koefisien, konstan)

            nilai_x = nilai[0]
            nilai_y = nilai[1]
            nilai_z = nilai[2]

            print("nilai x :", nilai_x)
            print("nilai y :", nilai_y)
            print("nilai z :", nilai_z)

        except Exception as e:
            pesan_error = "Maaf, cek lagi persamaan yang Anda masukkan harus berbentuk matriks dipisahkan dengan (,) \n (ex: 2, 3, 5)"

    return render_template('eliminasi.html', nilai=nilai, nilai_x=nilai_x, nilai_y=nilai_y, nilai_z=nilai_z, pesan_error=pesan_error)

if __name__ == '__main__':
    app.run(debug=True)
