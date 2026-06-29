# 📐 Linear Algebra Tutor - Web App

Web app interaktif untuk belajar Linear Algebra dengan tampilan CLI/terminal.

## Fitur

- 🎨 **Tampilan CLI** - Desain terminal yang aesthetic
- 📚 **4 Topik Utama**:
  - Vector (definisi, operasi, dot product, magnitude)
  - Matrix (operasi, transpose, determinan, inverse)
  - Sistem Persamaan Linear (substitusi, eliminasi, Gauss, Cramer)
  - Eigenvalues & Eigenvectors
- 🧮 **Kalkulator Interaktif** - Hitung langsung di browser
- 📐 **Rumus Matematika** - Ditampilkan dengan MathJax

## Cara Menjalankan

### 1. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Jalankan Server

```bash
python3 app.py
```

### 3. Buka Browser

Buka http://localhost:8080

## Struktur Projek

```
linear-algebra-tutor/
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
├── README.md             # Dokumentasi
├── templates/
│   ├── index.html        # Halaman utama
│   └── lesson.html       # Halaman pelajaran
└── static/
    ├── css/
    │   └── terminal.css  # Styling terminal
    └── js/
        └── app.js        # JavaScript interaktif
```

## Topik yang Tersedia

### 📐 Vector
- Apa itu Vector?
- Operasi Vector (penjumlahan, pengurangan, perkalian skalar)
- Dot Product
- Magnitude & Normalisasi

### 📊 Matrix
- Apa itu Matrix?
- Operasi Matrix
- Transpose Matrix
- Determinant
- Inverse Matrix

### 📝 Sistem Persamaan Linear
- Apa itu Sistem Persamaan?
- Metode Substitusi
- Metode Eliminasi
- Eliminasi Gauss
- Aturan Cramer

### 🔢 Eigenvalues & Eigenvectors
- Apa itu Eigenvalues?
- Mencari Eigenvalues
- Mencari Eigenvectors
- Verifikasi Eigenvalues

## Keyboard Shortcuts

- `ESC` - Kembali ke halaman utama

## Technologies

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Math**: NumPy, MathJax
- **Design**: Terminal/CLI aesthetic with JetBrains Mono font

## License

MIT
