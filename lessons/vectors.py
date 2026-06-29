"""Vector lessons for Linear Algebra Tutor."""

import numpy as np
from utils.display import (
    console, show_lesson_title, show_concept, show_step,
    show_vector, show_calculation, show_success, show_info,
    wait_for_next, show_menu
)
from utils.math_utils import (
    create_vector, vector_add, vector_subtract, scalar_multiply,
    dot_product, vector_magnitude, vector_normalize
)


def lesson_what_is_vector():
    """Lesson: What is a Vector?"""
    show_lesson_title("Apa itu Vector?", "Memahami konsep dasar vector")

    show_concept("Definisi Vector", """
**Vector** adalah objek matematika yang memiliki **besar (magnitude)** dan **arah (direction)**.

Dalam linear algebra, vector direpresentasikan sebagai **daftar angka** yang disusun secara vertikal atau horizontal.

### Contoh:
- Vector 2D: `[3, 4]` → titik di koordinat (3, 4)
- Vector 3D: `[1, 2, 3]` → titik di ruang 3 dimensi

### Notasi:
- Notasi kolom: $\vec{v} = \\begin{bmatrix} 3 \\\\ 4 \\end{bmatrix}$
- Notasi baris: $\vec{v} = [3, 4]$
""")

    show_info("Mari kita coba dengan contoh interaktif!")
    wait_for_next()

    # Interactive example
    show_step(1, "Buat Vector A = [3, 4]")
    v_a = create_vector(3, 4)
    show_vector("A", v_a)

    show_step(2, "Buat Vector B = [1, 2]")
    v_b = create_vector(1, 2)
    show_vector("B", v_b)

    show_step(3, "Lihat kedua vector pada bidang kartesius")
    console.print("""
    y
    ^
    |   A (3,4)
    4 +   •
    |
    3 |
    |
    2 +   • B (1,2)
    |
    1 |
    +---+---+---+---+--> x
        1   2   3   4
    """)

    show_success("Kamu sekarang tahu apa itu vector!")
    wait_for_next()


def lesson_vector_operations():
    """Lesson: Vector Operations."""
    show_lesson_title("Operasi Vector", "Penjumlahan, pengurangan, dan perkalian skalar")

    show_concept("Operasi Dasar Vector", """
### 1. Penjumlahan Vector
$\vec{A} + \vec{B}$ dilakukan secara komponen per komponen.

Jika $\vec{A} = [a_1, a_2]$ dan $\vec{B} = [b_1, b_2]$, maka:
$\vec{A} + \vec{B} = [a_1 + b_1, a_2 + b_2]$

### 2. Pengurangan Vector
$\vec{A} - \vec{B} = [a_1 - b_1, a_2 - b_2]$

### 3. Perkalian Skalar
$c \\times \vec{A} = [c \\times a_1, c \\times a_2]$

Skalar mengubah **besar** vector tanpa mengubah arah (jika positif).
""")

    wait_for_next()

    # Interactive examples
    v_a = create_vector(3, 4)
    v_b = create_vector(1, 2)

    show_vector("A", v_a)
    show_vector("B", v_b)

    console.print("\n[bold cyan]Penjumlahan A + B:[/bold cyan]")
    show_step(1, "Komponen x: 3 + 1 = 4")
    show_step(2, "Komponen y: 4 + 2 = 6")
    result = vector_add(v_a, v_b)
    show_vector("A + B", result)

    console.print("\n[bold cyan]Pengurangan A - B:[/bold cyan]")
    show_step(1, "Komponen x: 3 - 1 = 2")
    show_step(2, "Komponen y: 4 - 2 = 2")
    result = vector_subtract(v_a, v_b)
    show_vector("A - B", result)

    console.print("\n[bold cyan]Perkalian Skalar 2 × A:[/bold cyan]")
    show_step(1, "Komponen x: 2 × 3 = 6")
    show_step(2, "Komponen y: 2 × 4 = 8")
    result = scalar_multiply(2, v_a)
    show_vector("2A", result)

    show_success("Kamu sekarang bisa operasi vector!")
    wait_for_next()


def lesson_dot_product():
    """Lesson: Dot Product."""
    show_lesson_title("Dot Product", "Perkalian titik antara dua vector")

    show_concept("Apa itu Dot Product?", """
**Dot Product** (perkalian titik) adalah operasi yang menghasilkan **skalar** (angka tunggal) dari dua vector.

### Rumus:
$\vec{A} \\cdot \vec{B} = a_1 b_1 + a_2 b_2$

### Interpretasi Geometris:
$\vec{A} \\cdot \vec{B} = |\\vec{A}| \\times |\\vec{B}| \\times \\cos(\\theta)$

Di mana $\\theta$ adalah sudut antara kedua vector.

### Artinya:
- Jika $\vec{A} \\cdot \vec{B} > 0$ → sudut < 90° (searah)
- Jika $\vec{A} \\cdot \vec{B} = 0$ → sudut = 90° (tegak lurus)
- Jika $\vec{A} \\cdot \vec{B} < 0$ → sudut > 90° (berlawanan arah)
""")

    wait_for_next()

    v_a = create_vector(3, 4)
    v_b = create_vector(1, 2)

    show_vector("A", v_a)
    show_vector("B", v_b)

    console.print("\n[bold cyan]Menghitung A · B:[/bold cyan]")
    show_step(1, "Kalikan komponen x: 3 × 1 = 3")
    show_step(2, "Kalikan komponen y: 4 × 2 = 8")
    show_step(3, "Jumlahkan: 3 + 8 = 11")

    result = dot_product(v_a, v_b)
    show_calculation("A · B", f"{result:.0f}")

    # Show angle interpretation
    mag_a = vector_magnitude(v_a)
    mag_b = vector_magnitude(v_b)
    cos_theta = result / (mag_a * mag_b)
    theta = np.degrees(np.arccos(np.clip(cos_theta, -1, 1)))

    console.print(f"\n[bold yellow]Interpretasi Geometris:[/bold yellow]")
    show_info(f"|A| = {mag_a:.2f}")
    show_info(f"|B| = {mag_b:.2f}")
    show_info(f"cos(θ) = {cos_theta:.4f}")
    show_info(f"θ = {theta:.1f}°")
    show_success("Kedua vector membentuk sudut {:.1f}°".format(theta))

    wait_for_next()


def lesson_magnitude_normalize():
    """Lesson: Vector Magnitude and Normalization."""
    show_lesson_title("Magnitude & Normalisasi", "Panjang vector dan vector satuan")

    show_concept("Magnitude (Panjang Vector)", """
**Magnitude** atau panjang vector dihitung menggunakan teorema Pythagoras.

### Rumus (2D):
$|\\vec{A}| = \\sqrt{a_1^2 + a_2^2}$

### Rumus (3D):
$|\\vec{A}| = \\sqrt{a_1^2 + a_2^2 + a_3^2}$

### Normalisasi:
**Vector satuan** (unit vector) adalah vector dengan panjang = 1.

$\\hat{A} = \\frac{\\vec{A}}{|\\vec{A}|}$

Normalisasi mempertahankan arah, hanya mengubah panjang menjadi 1.
""")

    wait_for_next()

    v_a = create_vector(3, 4)
    show_vector("A", v_a)

    console.print("\n[bold cyan]Menghitung Magnitude:[/bold cyan]")
    show_step(1, "Komponen: [3, 4]")
    show_step(2, "Rumus: √(3² + 4²)")
    show_step(3, "Hitung: √(9 + 16) = √25 = 5")

    mag = vector_magnitude(v_a)
    show_calculation("|A|", f"{mag:.2f}")

    console.print("\n[bold cyan]Normalisasi Vector A:[/bold cyan]")
    show_step(1, "Bagi setiap komponen dengan magnitude")
    show_step(2, f"x: 3 / 5 = {3/5:.2f}")
    show_step(3, f"y: 4 / 5 = {4/5:.2f}")

    normalized = vector_normalize(v_a)
    show_vector("Â", normalized)

    verify_mag = vector_magnitude(normalized)
    show_info(f"Verifikasi: |Â| = {verify_mag:.2f} ✓")

    show_success("Vector satuan memiliki panjang 1!")
    wait_for_next()


def lesson_vector_practice():
    """Practice problems for vectors."""
    show_lesson_title("Latihan Vector", "Coba sendiri!")

    show_concept("Soal Latihan", """
Berikut beberapa soal untuk menguji pemahamanmu tentang vector:

1. **Penjumlahan**: Jika A = [2, 3] dan B = [1, -1], berapa A + B?

2. **Dot Product**: Jika A = [1, 0] dan B = [0, 1], berapa A · B?
   (Petunjuk: ini adalah vector tegak lurus!)

3. **Magnitude**: Berapa panjang vector C = [5, 12]?

4. **Normalisasi**: Berapa vector satuan dari D = [3, 4]?

Coba hitung sendiri dulu, lalu lihat jawabannya!
""")

    wait_for_next()

    # Problem 1
    console.print("[bold cyan]Soal 1: A + B[/bold cyan]")
    v_a = create_vector(2, 3)
    v_b = create_vector(1, -1)
    show_vector("A", v_a)
    show_vector("B", v_b)
    result = vector_add(v_a, v_b)
    show_vector("A + B", result)

    # Problem 2
    console.print("\n[bold cyan]Soal 2: A · B[/bold cyan]")
    v_a = create_vector(1, 0)
    v_b = create_vector(0, 1)
    show_vector("A", v_a)
    show_vector("B", v_b)
    result = dot_product(v_a, v_b)
    show_calculation("A · B", f"{result:.0f}")
    show_info("Vector tegak lurus → dot product = 0!")

    # Problem 3
    console.print("\n[bold cyan]Soal 3: |C|[/bold cyan]")
    v_c = create_vector(5, 12)
    show_vector("C", v_c)
    mag = vector_magnitude(v_c)
    show_step(1, "√(5² + 12²) = √(25 + 144) = √169")
    show_calculation("|C|", f"{mag:.0f}")

    # Problem 4
    console.print("\n[bold cyan]Soal 4: Normalisasi D[/bold cyan]")
    v_d = create_vector(3, 4)
    show_vector("D", v_d)
    normalized = vector_normalize(v_d)
    show_vector("D̂", normalized)

    show_success("Selesai! Semoga pemahamanmu tentang vector semakin baik!")
    wait_for_next()


def vector_menu():
    """Main vector lessons menu."""
    while True:
        choice = show_menu("📚 Pelajaran Vector", [
            "Apa itu Vector?",
            "Operasi Vector",
            "Dot Product",
            "Magnitude & Normalisasi",
            "Latihan Vector",
            "← Kembali ke Menu Utama"
        ])

        if choice == 1:
            lesson_what_is_vector()
        elif choice == 2:
            lesson_vector_operations()
        elif choice == 3:
            lesson_dot_product()
        elif choice == 4:
            lesson_magnitude_normalize()
        elif choice == 5:
            lesson_vector_practice()
        elif choice == 6:
            break
