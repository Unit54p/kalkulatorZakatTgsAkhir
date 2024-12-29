from flask import Flask, render_template, request
# import mysql.connector

app = Flask(__name__)

# variabel global
nisab = 82312725
# Konfigurasi database
# db = mysql.connector.connect(
#      host="localhost",
#      user="root",
#      password="",
#      database="kalkulator_zakat_db"
# )
# try:
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="kalkulator_zakat_db"
#     )
#     print("Koneksi ke database berhasil!")
# except mysql.connector.Error as err:
#     print(f"Error: {err}")


@app.route('/')
def index():
     return render_template('index.html')

@app.route('/calculate_zakat', methods=['POST'])
def calculate():
     # Input dari form
     income = float(request.form['income'])
     

     # Hitung zakat
     if income >= nisab:
          zakat = income * 0.025  # 2.5% dari penghasilan
     else:
          zakat = 0.0
          
     formatted_number = "{:,}".format(zakat).replace(",",".")
     formatted_nissab = "{:,}".format(nisab).replace(",",".")
     formatted_pengahasilan = "{:,}".format(income).replace(",",".")

     return render_template('index.html', zakat=formatted_number, income=formatted_pengahasilan, nisab=formatted_nissab)


@app.route('/calculate_zakat_perdagangan', methods=['POST'])
def calculate_perdagangan():
     # Input dari form
     asset = float(request.form['asset'])
     laba = float(request.form['laba'])
     income = asset + laba

     # Hitung zakat
     if income >= nisab:
          zakat = income * 0.025  # 2.5% dari penghasilan
     else:
          zakat = 0.0
          
     formatted_number = "{:,}".format(zakat).replace(",",".")
     formatted_nissab = "{:,}".format(nisab).replace(",",".")
     formatted_pengahasilan = "{:,}".format(income).replace(",",".")

     return render_template('index.html', zakat=formatted_number, income=formatted_pengahasilan, nisab=formatted_nissab)

# @app.route('/history')
# def history():
#      cursor = db.cursor(dictionary=True)
#      cursor.execute("SELECT * FROM riwayat_zakat ORDER BY id ASC")
#      history = cursor.fetchall()
#      return render_template('index.html ', history=history)

if __name__ == '__main__':
     app.run(debug=True)
     
