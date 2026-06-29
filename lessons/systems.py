"""Systems of Linear Equations lessons."""

import numpy as np
from utils.display import (
    console, show_lesson_title, show_concept, show_step,
    show_matrix, show_vector, show_calculation, show_success,
    show_info, show_warning, wait_for_next, show_menu
)
from utils.math_utils import (
    create_matrix, create_vector, solve_linear_system,
    gaussian_elimination, matrix_determinant
)


def lesson_what_is_system():
    """Lesson: What is a System of Linear Equations?"""
    show_lesson_title("Sistem Persamaan Linear", "Memahami konsep dasar")

    show_concept("Definisi Sistem Persamaan Linear", """
**Sistem Persamaan Linear** adalah kumpulan persamaan linear yang memiliki variabel yang sama.

### Contoh Sistem 2 Variabel:
```
2x + 3y = 8
4x -  y = 2
```

### Representasi Matrix (Ax = b):
$\\begin{bmatrix} 2 & 3 \\\\ 4 & -1 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} = \\begin{bmatrix} 8 \\\\ 2 \\end{bmatrix}$

### Jenis Solusi:
1. **Solusi unik**: Satu titik potong
2. **Tidak ada solusi**: Garis sejajar
3. **Tak hingga solusi**: Garis berimpit
""")

    show_info("Mari kita visualisasikan!")
    console.print("""
    y
    ^
    |   /
    |  / ← 2x + 3y = 8
    | • → Titik potong (solusi)
    |/   \\
    +--------→ x
        \\ ← 4x - y = 2
    """)

    wait_for_next()


def lesson_substitution():
    """Lesson: Substitution Method."""
    show_lesson_title("Metode Substitusi", "Menyelesaikan sistem dengan substitusi")

    show_concept("Metode Substitusi", """
### Langkah-langkah:
1. **Isolasi** satu variabel dari salah satu persamaan
2. **Substitusi** ke persamaan lain
3. **Selesaikan** untuk variabel tersisa
4. **Substitusi balik** untuk mendapatkan variabel pertama

### Contoh:
```
x + 2y = 5    ... (1)
3x - y = 1    ... (2)
```

Dari (1): x = 5 - 2y

Substitusi ke (2): 3(5 - 2y) - y = 1
""")

    wait_for_next()

    console.print("[bold cyan]Contoh Penyelesaian:[/bold cyan]")
    console.print("Persamaan:")
    console.print("  x + 2y = 5  ... (1)")
    console.print("  3x - y = 1  ... (2)")

    show_step(1, "Dari persamaan (1), isolasi x:")
    console.print("     x = 5 - 2y")

    show_step(2, "Substitusi ke persamaan (2):")
    console.print("     3(5 - 2y) - y = 1")

    show_step(3, "Selesaikan:")
    console.print("     15 - 6y - y = 1")
    console.print("     15 - 7y = 1")
    console.print("     -7y = -14")
    console.print("     y = 2")

    show_step(4, "Substitusi balik ke (1):")
    console.print("     x + 2(2) = 5")
    console.print("     x + 4 = 5")
    console.print("     x = 1")

    show_success("Solusi: x = 1, y = 2")

    # Verify
    console.print("\n[bold yellow]Verifikasi:[/bold yellow]")
    console.print(f"  (1): 1 + 2(2) = 1 + 4 = 5 ✓")
    console.print(f"  (2): 3(1) - 2 = 3 - 2 = 1 ✓")

    wait_for_next()


def lesson_elimination():
    """Lesson: Elimination Method."""
    show_lesson_title("Metode Eliminasi", "Menyelesaikan sistem dengan eliminasi")

    show_concept("Metode Eliminasi", """
### Langkah-langkah:
1. **Samakan koefisien** salah satu variabel
2. **Jumlah/kurangkan** persamaan untuk eliminasi variabel
3. **Selesaikan** untuk variabel tersisa
4. **Substitusi** untuk variabel lain

### Contoh:
```
2x + 3y = 8    ... (1)
4x -  y = 2    ... (2)
```
""")

    wait_for_next()

    console.print("[bold cyan]Contoh Penyelesaian:[/bold cyan]")
    console.print("Persamaan:")
    console.print("  2x + 3y = 8  ... (1)")
    console.print("  4x -  y = 2  ... (2)")

    show_step(1, "Kalikan (2) dengan 3 untuk samakan koefisien y:")
    console.print("     12x - 3y = 6  ... (2')")

    show_step(2, "Jumlahkan (1) dan (2'):")
    console.print("     2x + 3y = 8")
    console.print("   + 12x - 3y = 6")
    console.print("   ─────────────")
    console.print("     14x     = 14")

    show_step(3, "Selesaikan:")
    console.print("     x = 14 / 14 = 1")

    show_step(4, "Substitusi x=1 ke (1):")
    console.print("     2(1) + 3y = 8")
    console.print("     3y = 6")
    console.print("     y = 2")

    show_success("Solusi: x = 1, y = 2")
    wait_for_next()


def lesson_gaussian():
    """Lesson: Gaussian Elimination."""
    show_lesson_title("Eliminasi Gauss", "Metode umum untuk sistem besar")

    show_concept("Eliminasi Gauss (Row Echelon Form)", """
### Konsep:
Eliminasi Gauss mengubah sistem persamaan menjadi **bentuk segitiga atas** menggunakan operasi baris elementer.

### Operasi Baris Elementer:
1. Tukar dua baris
2. Kalikan baris dengan konstanta
3. Jumlahkan dua baris

### Contoh 3×3:
```
x + 2y + 3z = 9
2x + 5y + 7z = 21
3x + 7y + 9z = 27
```

### Matrix Augmented:
$[A|b] = \\begin{bmatrix} 1 & 2 & 3 & | & 9 \\\\ 2 & 5 & 7 & | & 21 \\\\ 3 & 7 & 9 & | & 27 \\end{bmatrix}$
""")

    wait_for_next()

    A = create_matrix([[1, 2, 3], [2, 5, 7], [3, 7, 9]])
    b = create_vector(9, 21, 27)

    show_matrix("A", A)
    show_vector("b", b)

    console.print("[bold cyan]Proses Eliminasi Gauss:[/bold cyan]")

    # Show steps
    x, steps = gaussian_elimination(A, b)

    for i, step in enumerate(steps, 1):
        show_step(i, step)

    console.print("\n[bold cyan]Hasil Back Substitution:[/bold cyan]")
    show_vector("x", x)

    show_success("Solusi ditemukan!")
    wait_for_next()


def lesson_cramers_rule():
    """Lesson: Cramer's Rule."""
    show_lesson_title("Aturan Cramer", "Solusi menggunakan determinan")

    show_concept("Aturan Cramer", """
### Rumus:
Untuk sistem $Ax = b$:

$x_i = \\frac{det(A_i)}{det(A)}$

Di mana $A_i$ adalah matrix A dengan kolom ke-i diganti oleh vector b.

### Syarat:
- Matrix A harus persegi
- $det(A) \\neq 0$

### Contoh 2×2:
```
ax + by = e
cx + dy = f
```

$x = \\frac{det\\begin{bmatrix} e & b \\\\ f & d \\end{bmatrix}}{det(A)} = \\frac{ed - bf}{ad - bc}$

$y = \\frac{det\\begin{bmatrix} a & e \\\\ c & f \\end{bmatrix}}{det(A)} = \\frac{af - ce}{ad - bc}$
""")

    wait_for_next()

    A = create_matrix([[2, 3], [4, -1]])
    b = create_vector(8, 2)

    show_matrix("A", A)
    show_vector("b", b)

    det_A = matrix_determinant(A)
    show_info(f"det(A) = {det_A:.0f}")

    console.print("[bold cyan]Menghitung dengan Aturan Cramer:[/bold cyan]")

    # For x
    A_x = create_matrix([[8, 3], [2, -1]])
    det_A_x = matrix_determinant(A_x)
    show_step(1, f"A_x = [[8,3],[2,-1]], det(A_x) = {det_A_x:.0f}")
    x = det_A_x / det_A
    show_calculation("x", f"{det_A_x:.0f} / {det_A:.0f} = {x:.0f}")

    # For y
    A_y = create_matrix([[2, 8], [4, 2]])
    det_A_y = matrix_determinant(A_y)
    show_step(2, f"A_y = [[2,8],[4,2]], det(A_y) = {det_A_y:.0f}")
    y = det_A_y / det_A
    show_calculation("y", f"{det_A_y:.0f} / {det_A:.0f} = {y:.0f}")

    show_success(f"Solusi: x = {x:.0f}, y = {y:.0f}")
    wait_for_next()


def lesson_systems_practice():
    """Practice problems for systems."""
    show_lesson_title("Latihan Sistem Persamaan", "Coba sendiri!")

    show_concept("Soal Latihan", """
Selesaikan sistem persamaan berikut:

**Soal 1:**
```
x + y = 5
x - y = 1
```

**Soal 2:**
```
2x + 3y = 12
4x -  y = 5
```

**Soal 3 (3 variabel):**
```
x + y + z = 6
2x - y + z = 3
x + 2y - z = 5
```

Gunakan metode apapun yang kamu pahami!
""")

    wait_for_next()

    # Problem 1
    console.print("[bold cyan]Soal 1:[/bold cyan]")
    console.print("  x + y = 5")
    console.print("  x - y = 1")

    A = create_matrix([[1, 1], [1, -1]])
    b = create_vector(5, 1)
    x = solve_linear_system(A, b)
    show_success(f"Solusi: x = {x[0]:.0f}, y = {x[1]:.0f}")

    # Problem 2
    console.print("\n[bold cyan]Soal 2:[/bold cyan]")
    console.print("  2x + 3y = 12")
    console.print("  4x -  y = 5")

    A = create_matrix([[2, 3], [4, -1]])
    b = create_vector(12, 5)
    x = solve_linear_system(A, b)
    show_success(f"Solusi: x = {x[0]:.0f}, y = {x[1]:.0f}")

    # Problem 3
    console.print("\n[bold cyan]Soal 3:[/bold cyan]")
    console.print("  x + y + z = 6")
    console.print("  2x - y + z = 3")
    console.print("  x + 2y - z = 5")

    A = create_matrix([[1, 1, 1], [2, -1, 1], [1, 2, -1]])
    b = create_vector(6, 3, 5)
    x = solve_linear_system(A, b)
    show_success(f"Solusi: x = {x[0]:.0f}, y = {x[1]:.0f}, z = {x[2]:.0f}")

    show_success("Selesai! Semoga pemahamanmu semakin baik!")
    wait_for_next()


def systems_menu():
    """Main systems lessons menu."""
    while True:
        choice = show_menu("📚 Sistem Persamaan Linear", [
            "Apa itu Sistem Persamaan?",
            "Metode Substitusi",
            "Metode Eliminasi",
            "Eliminasi Gauss",
            "Aturan Cramer",
            "Latihan Sistem Persamaan",
            "← Kembali ke Menu Utama"
        ])

        if choice == 1:
            lesson_what_is_system()
        elif choice == 2:
            lesson_substitution()
        elif choice == 3:
            lesson_elimination()
        elif choice == 4:
            lesson_gaussian()
        elif choice == 5:
            lesson_cramers_rule()
        elif choice == 6:
            lesson_systems_practice()
        elif choice == 7:
            break
