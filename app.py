from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Data pengguna awal
users = {
    "20230001": {"nama": "Dimas Juniandani", "jabatan": "Ketua", "password": "123321"},
    "20230002": {"nama": "Imam Syahid Al Hikam", "jabatan": "Sekretaris", "password": "123321"},
    "20230003": {"nama": "Andiny As", "jabatan": "Bendahara", "password": "123321"},
    "20230004": {"nama": "M Darga Prawira", "jabatan": "Wakil Sekretaris", "password": "123321"},
    "20230005": {"nama": "Aditya Fauzan Adzima", "jabatan": "Kepala Bidang Keorganisasian dan Pengembangan Sumber Daya Manusia", "password": "123321"},
    "20230006": {"nama": "Alya Kusumua", "jabatan": "Kepala Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230007": {"nama": "Ahmad Dwi Prasetyo", "jabatan": "Kepala Bidang Humas dan Kemitraan", "password": "123321"},
    "20230008": {"nama": "Neneng Gustriani", "jabatan": "Kepala Bidang Usaha Ekonomi Produktif", "password": "123321"},
    "20230009": {"nama": "Marza Fathan", "jabatan": "Kepala Bidang Pemuda dan Olahraga", "password": "123321"},
    "20230010": {"nama": "Alisha", "jabatan": "Plt. Kepala Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230011": {"nama": "M Rofi", "jabatan": "Anggota Bidang Keorganisasian dan Pengembangan Sumber Daya Manusia", "password": "123321"},
    "20230012": {"nama": "Tatang Slamet", "jabatan": "Anggota Bidang Keorganisasian dan Pengembangan Sumber Daya Manusia", "password": "123321"},
    "20230013": {"nama": "Novianti Pratiwi", "jabatan": "Anggota Bidang Keorganisasian dan Pengembangan Sumber Daya Manusia", "password": "123321"},
    "20230014": {"nama": "Hans", "jabatan": "Anggota Bidang Keorganisasian dan Pengembangan Sumber Daya Manusia", "password": "123321"},
    "20230015": {"nama": "Akbar", "jabatan": "Anggota Bidang Keorganisasian dan Pengembangan Sumber Daya Manusia", "password": "123321"},
    "20230016": {"nama": "Melsya", "jabatan": "Anggota Bidang Keorganisasian dan Pengembangan Sumber Daya Manusia", "password": "123321"},
    "20230017": {"nama": "Ramdani", "jabatan": "Anggota Bidang Keorganisasian dan Pengembangan Sumber Daya Manusia", "password": "123321"},
    "20230018": {"nama": "Dava Haviz", "jabatan": "Anggota Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230019": {"nama": "Alisha", "jabatan": "Anggota Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230020": {"nama": "Viona", "jabatan": "Anggota Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230022": {"nama": "Avicenna", "jabatan": "Anggota Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230023": {"nama": "Naila", "jabatan": "Anggota Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230024": {"nama": "Torik Budi", "jabatan": "Anggota Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230025": {"nama": "Samsul", "jabatan": "Anggota Bidang Sosial Kemasyarakatan", "password": "123321"},
    "20230026": {"nama": "Sandrina Malakiano", "jabatan": "Anggota Bidang Humas dan Kemitraan", "password": "123321"},
    "20230027": {"nama": "Mutia", "jabatan": "Anggota Bidang Humas dan Kemitraan", "password": "123321"},
    "20230028": {"nama": "M Bagas H", "jabatan": "Anggota Bidang Humas dan Kemitraan", "password": "123321"},
    "20230029": {"nama": "Tata", "jabatan": "Anggota Bidang Humas dan Kemitraan", "password": "123321"},
    "20230030": {"nama": "Indri", "jabatan": "Anggota Bidang Humas dan Kemitraan", "password": "123321"},
    "20230031": {"nama": "Hugo", "jabatan": "Anggota Bidang Usaha Ekonomi Produktif", "password": "123321"},
    "20230032": {"nama": "Ridho", "jabatan": "Anggota Bidang Usaha Ekonomi Produktif", "password": "123321"},
    "20230033": {"nama": "Dika", "jabatan": "Anggota Bidang Usaha Ekonomi Produktif", "password": "123321"},
    "20230034": {"nama": "Alif", "jabatan": "Anggota Bidang Usaha Ekonomi Produktif", "password": "123321"},
    "20230035": {"nama": "Faisal Abdi Negara A.Md", "jabatan": "Anggota Bidang Pemuda dan Olahraga", "password": "123321"},
    "20230036": {"nama": "Nabil", "jabatan": "Anggota Bidang Pemuda dan Olahraga", "password": "123321"},
    "20230037": {"nama": "Dimas", "jabatan": "Anggota Bidang Pemuda dan Olahraga", "password": "123321"},
    "20230038": {"nama": "Fiqri", "jabatan": "Anggota Bidang Pemuda dan Olahraga", "password": "123321"},
}

@app.route('/')
def home():
    if 'nrp' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nrp = request.form['nrp']
        password = request.form['password']
        if nrp in users and users[nrp]['password'] == password:
            session['nrp'] = nrp
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='NRP atau password salah')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'nrp' in session:
        user = users[session['nrp']]
        return render_template('dashboard.html', user=user)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('nrp', None)
    return redirect(url_for('login'))

daftar_aktivitas = []

@app.route('/aktivitas')
def aktivitas():
    if 'nrp' in session:
        user = users[session['nrp']]
        return render_template('aktivitas.html', user=user, daftar_aktivitas=daftar_aktivitas)
    return redirect(url_for('login'))

@app.route('/tambah_aktivitas', methods=['POST'])
def tambah_aktivitas():
    if 'nrp' in session:
        nama_kegiatan = request.form['nama_kegiatan']
        tanggal = request.form['tanggal']
        deskripsi = request.form['deskripsi']
        aktivitas_baru = {
            "nama_kegiatan": nama_kegiatan,
            "tanggal": tanggal,
            "deskripsi": deskripsi,
            "status": "Menunggu Validasi"
        }
        daftar_aktivitas.append(aktivitas_baru)
        return redirect(url_for('aktivitas'))
    return redirect(url_for('login'))

@app.route('/validasi_aktivitas/<int:aktivitas_id>')
def validasi_aktivitas(aktivitas_id):
    if 'nrp' in session and users[session['nrp']]['jabatan'] == 'Ketua':
        if 0 <= aktivitas_id < len(daftar_aktivitas):
            daftar_aktivitas[aktivitas_id]['status'] = 'Tervalidasi'
        return redirect(url_for('aktivitas'))
    return redirect(url_for('login'))

@app.route('/cetak_aktivitas')
def cetak_aktivitas():
    if 'nrp' in session:
        # Logika untuk membuat file PDF atau halaman cetak
        return "Halaman Cetak Aktivitas Bulanan"
    return redirect(url_for('login'))

daftar_laporan = []

@app.route('/laporan')
def laporan():
    if 'nrp' in session:
        user = users[session['nrp']]
        return render_template('laporan.html', user=user, daftar_laporan=daftar_laporan, range=range)
    return redirect(url_for('login'))

@app.route('/tambah_laporan', methods=['POST'])
def tambah_laporan():
    if 'nrp' in session:
        nama_laporan = request.form['nama_laporan']
        periode = request.form['periode']
        tahun = request.form['tahun']
        deskripsi = request.form['deskripsi']
        laporan_baru = {
            "nama_laporan": nama_laporan,
            "periode": periode,
            "tahun": tahun,
            "deskripsi": deskripsi,
            "status": "Menunggu Validasi"
        }
        daftar_laporan.append(laporan_baru)
        return redirect(url_for('laporan'))
    return redirect(url_for('login'))

@app.route('/validasi_laporan/<int:laporan_id>')
def validasi_laporan(laporan_id):
    if 'nrp' in session and users[session['nrp']]['jabatan'] == 'Ketua':
        if 0 <= laporan_id < len(daftar_laporan):
            daftar_laporan[laporan_id]['status'] = 'Tervalidasi'
        return redirect(url_for('laporan'))
    return redirect(url_for('login'))

@app.route('/cetak_laporan')
def cetak_laporan():
    if 'nrp' in session:
        # Logika untuk membuat file PDF atau halaman cetak
        return "Halaman Cetak Laporan Kinerja"
    return redirect(url_for('login'))

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/profil')
def profil():
    if 'nrp' in session:
        user = users[session['nrp']]
        return render_template('profil.html', user=user)
    return redirect(url_for('login'))

@app.route('/update_profil', methods=['POST'])
def update_profil():
    if 'nrp' in session:
        nrp = session['nrp']
        users[nrp]['nama'] = request.form['nama']
        if request.form['password']:
            users[nrp]['password'] = request.form['password']

        if 'foto' in request.files:
            file = request.files['foto']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                users[nrp]['foto'] = filename

        return redirect(url_for('profil'))
    return redirect(url_for('login'))

@app.route('/tambah_pengguna', methods=['POST'])
def tambah_pengguna():
    if 'nrp' in session and users[session['nrp']]['jabatan'] == 'Ketua':
        nrp = request.form['nrp']
        nama = request.form['nama']
        jabatan = request.form['jabatan']
        password = request.form['password']
        users[nrp] = {"nama": nama, "jabatan": jabatan, "password": password}
        return redirect(url_for('profil'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
