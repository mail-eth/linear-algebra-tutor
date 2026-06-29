"""Matrix lessons for Linear Algebra Tutor."""

import numpy as np
from utils.display import (
    console, show_lesson_title, show_concept, show_step,
    show_matrix, show_calculation, show_success, show_info,
    show_warning, wait_for_next, show_menu
)
from utils.math_utils import (
    create_matrix, matrix_add, matrix_subtract, matrix_multiply,
    scalar_matrix_multiply, matrix_transpose, matrix_determinant,
    matrix_inverse, matrix_trace, is_invertible
)


def lesson_what_is_matrix():
    """Lesson: What is a Matrix?"""
    show_lesson_title("Apa itu Matrix?", "Memahami konsep dasar matrix")

    show_concept("Definisi Matrix", """
**Matrix** adalah susunan angka dalam bentuk **baris dan kolom** yang disusun dalam kurung siku.

### Notasi:
$A = \\begin{bmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\end{bmatrix}$

### Jenis Matrix:
- **Matrix 2×2**: 2 baris, 2 kolom
- **Matrix 3×3**: 3 baris, 3 kolom
- **Matrix persegi**: jumlah baris = kolom
- **Matrix identitas (I)**: diagonal = 1, lainnya = 0

### Contoh Matrix Identitas 3×3:
$I = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}$

Matrix identitas seperti "angka 1" dalam perkalian matrix.
""")

    show_info("Mari kita lihat contoh matrix!")
    wait_for_next()

    # Example matrices
    A = create_matrix([[1, 2], [3, 4]])
    show_matrix("A (2×2)", A)

    B = create_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    show_matrix("I (Identitas 3×3)", B)

    show_success("Kamu sekarang tahu apa itu matrix!")
    wait_for_next()


def lesson_matrix_operations():
    """Lesson: Matrix Operations."""
    show_lesson_title("Operasi Matrix", "Penjumlahan, pengurangan, dan perkalian")

    show_concept("Operasi Dasar Matrix", """
### 1. Penjumlahan Matrix
Hanya bisa dilakukan pada matrix dengan **ukuran sama**.
$C = A + B$ → $c_{ij} = a_{ij} + b_{ij}$

### 2. Pengurangan Matrix
Sama seperti penjumlahan, komponen per komponen.
$C = A - B$ → $c_{ij} = a_{ij} - b_{ij}$

### 3. Perkalian Matrix
**PENTING**: Perkalian matrix **tidak komutatif**!
$A \\times B \\neq B \\times A$ (biasanya)

Syarat: kolom A = baris B
Jika A (m×n) dan B (n×p), maka AB = (m×p)

### Cara menghitung AB:
$c_{ij} = \\sum_{k=1}^{n} a_{ik} \\times b_{kj}$
""")

    wait_for_next()

    A = create_matrix([[1, 2], [3, 4]])
    B = create_matrix([[5, 6], [7, 8]])

    show_matrix("A", A)
    show_matrix("B", B)

    # Addition
    console.print("[bold cyan]Penjumlahan A + B:[/bold cyan]")
    C = matrix_add(A, B)
    show_step(1, "Komponen per komponen:")
    show_step(2, f"[1+5, 2+6] = [{C[0,0]:.0f}, {C[0,1]:.0f}]")
    show_step(3, f"[3+7, 4+8] = [{C[1,0]:.0f}, {C[1,1]:.0f}]")
    show_matrix("A + B", C)

    # Multiplication
    console.print("\n[bold cyan]Perkalian A × B:[/bold cyan]")
    show_step(1, "Baris 1 × Kolom 1: (1×5) + (2×7) = 19")
    show_step(2, "Baris 1 × Kolom 2: (1×6) + (2×8) = 22")
    show_step(3, "Baris 2 × Kolom 1: (3×5) + (4×7) = 43")
    show_step(4, "Baris 2 × Kolom 2: (3×6) + (4×8) = 50")

    C = matrix_multiply(A, B)
    show_matrix("A × B", C)

    # Show non-commutative
    console.print("\n[bold yellow]Apakah B × A = A × B?[/bold yellow]")
    D = matrix_multiply(B, A)
    show_matrix("B × A", D)

    if not np.allclose(C, D):
        show_warning("TIDAK! Perkalian matrix tidak komutatif!")

    wait_for_next()


def lesson_transpose():
    """Lesson: Matrix Transpose."""
    show_lesson_title("Transpose Matrix", "Membalik baris dan kolom")

    show_concept("Transpose Matrix", """
**Transpose** adalah operasi yang **menukar baris dan kolom**.

### Notasi:
$A^T$ (A transpose)

### Aturan:
Jika $A = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}$

Maka $A^T = \\begin{bmatrix} a & c \\\\ b & d \\end{bmatrix}$

### Sifat:
- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(AB)^T = B^T A^T$ ← urutan berubah!
""")

    wait_for_next()

    A = create_matrix([[1, 2, 3], [4, 5, 6]])
    show_matrix("A (2×3)", A)

    console.print("[bold cyan]Transpose A:[/bold cyan]")
    show_step(1, "Baris 1 → Kolom 1: [1, 4]")
    show_step(2, "Baris 2 → Kolom 2: [2, 5]")
    show_step(3, "Baris 3 → Kolom 3: [3, 6]")

    AT = matrix_transpose(A)
    show_matrix("Aᵀ (3×2)", AT)

    show_success("Transpose membalik baris menjadi kolom!")
    wait_for_next()


def lesson_determinant():
    """Lesson: Matrix Determinant."""
    show_lesson_title("Determinant", "Angka penting dari matrix persegi")

    show_concept("Apa itu Determinant?", """
**Determinant** adalah angka yang dihitung dari matrix persegi.

### Notasi:
$det(A)$ atau $|A|$

### Untuk Matrix 2×2:
$det\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} = ad - bc$

### Untuk Matrix 3×3 (Sarrus):
$det\\begin{bmatrix} a & b & c \\\\ d & e & f \\\\ g & h & i \\end{bmatrix} = aei + bfg + cdh - ceg - bdi - afh$

### Interpretasi:
- **det(A) ≠ 0**: Matrix bisa di-inverse, sistem punya solusi unik
- **det(A) = 0**: Matrix singular, tidak bisa di-inverse
- **|det(A)|**: Faktor skala transformasi
""")

    wait_for_next()

    A = create_matrix([[1, 2], [3, 4]])
    show_matrix("A", A)

    console.print("[bold cyan]Menghitung det(A):[/bold cyan]")
    show_step(1, "Rumus 2×2: ad - bc")
    show_step(2, "a=1, b=2, c=3, d=4")
    show_step(3, "det(A) = (1×4) - (2×3)")
    show_step(4, "det(A) = 4 - 6 = -2")

    det = matrix_determinant(A)
    show_calculation("det(A)", f"{det:.0f}")

    if det != 0:
        show_success(f"det(A) ≠ 0 → Matrix A bisa di-inverse!")
    else:
        show_warning("det(A) = 0 → Matrix A singular!")

    wait_for_next()


def lesson_inverse():
    """Lesson: Matrix Inverse."""
    show_lesson_title("Inverse Matrix", "Kebalikan dari matrix")

    show_concept("Apa itu Inverse?", """
**Inverse Matrix** adalah matrix yang jika dikalikan dengan matrix asli, menghasilkan matrix identitas.

### Notasi:
$A^{-1}$ (A inverse)

### Syarat:
- Matrix harus **persegi** (n×n)
- **det(A) ≠ 0** (tidak singular)

### Sifat:
$A \\times A^{-1} = A^{-1} \\times A = I$

### Rumus 2×2:
$A^{-1} = \\frac{1}{det(A)} \\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix}$

### Kegunaan:
Menyelesaikan sistem persamaan: $Ax = b$ → $x = A^{-1}b$
""")

    wait_for_next()

    A = create_matrix([[1, 2], [3, 4]])
    show_matrix("A", A)

    det = matrix_determinant(A)
    show_info(f"det(A) = {det:.0f}")

    if det != 0:
        console.print("[bold cyan]Menghitung A⁻¹:[/bold cyan]")
        show_step(1, f"1/det(A) = 1/{det:.0f} = {1/det:.4f}")
        show_step(2, "Tukar diagonal: [4, 1]")
        show_step(3, "Negasi non-diagonal: [-2, -3]")
        show_step(4, f"Kalikan dengan 1/det(A)")

        A_inv = matrix_inverse(A)
        show_matrix("A⁻¹", A_inv)

        # Verify
        console.print("[bold cyan]Verifikasi A × A⁻¹ = I:[/bold cyan]")
        I = matrix_multiply(A, A_inv)
        show_matrix("A × A⁻¹", np.round(I, 10))

        show_success("A × A⁻¹ = I ✓")
    else:
        show_warning("Matrix singular, tidak bisa di-inverse!")

    wait_for_next()


def lesson_matrices_practice():
    """Practice problems for matrices."""
    show_lesson_title("Latihan Matrix", "Coba sendiri!")

    show_concept("Soal Latihan", """
Berikut soal untuk menguji pemahamanmu tentang matrix:

1. **Penjumlahan**: Jika A = [[1,2],[3,4]] dan B = [[5,6],[7,8]], berapa A + B?

2. **Determinant**: Berapa det dari A = [[1,2],[3,4]]?

3. **Transpose**: Berapa transpose dari B = [[1,2,3],[4,5,6]]?

4. **Inverse**: Apakah matrix C = [[2,1],[4,2]] bisa di-inverse?
""")

    wait_for_next()

    # Problem 1
    console.print("[bold cyan]Soal 1: A + B[/bold cyan]")
    A = create_matrix([[1, 2], [3, 4]])
    B = create_matrix([[5, 6], [7, 8]])
    show_matrix("A", A)
    show_matrix("B", B)
    C = matrix_add(A, B)
    show_matrix("A + B", C)

    # Problem 2
    console.print("\n[bold cyan]Soal 2: det(A)[/bold cyan]")
    show_matrix("A", A)
    det = matrix_determinant(A)
    show_step(1, "det = (1×4) - (2×3) = 4 - 6")
    show_calculation("det(A)", f"{det:.0f}")

    # Problem 3
    console.print("\n[bold cyan]Soal 3: Bᵀ[/bold cyan]")
    show_matrix("B", B)
    BT = matrix_transpose(B)
    show_matrix("Bᵀ", BT)

    # Problem 4
    console.print("\n[bold cyan]Soal 4: Apakah C bisa di-inverse?[/bold cyan]")
    C = create_matrix([[2, 1], [4, 2]])
    show_matrix("C", C)
    det = matrix_determinant(C)
    show_step(1, f"det(C) = (2×2) - (1×4) = 4 - 4 = {det:.0f}")

    if det == 0:
        show_warning("det(C) = 0 → Matrix C SINGULAR, tidak bisa di-inverse!")
    else:
        show_success("det(C) ≠ 0 → Matrix C bisa di-inverse!")

    show_success("Selesai! Semoga pemahamanmu tentang matrix semakin baik!")
    wait_for_next()


def matrices_menu():
    """Main matrix lessons menu."""
    while True:
        choice = show_menu("📚 Pelajaran Matrix", [
            "Apa itu Matrix?",
            "Operasi Matrix",
            "Transpose Matrix",
            "Determinant",
            "Inverse Matrix",
            "Latihan Matrix",
            "← Kembali ke Menu Utama"
        ])

        if choice == 1:
            lesson_what_is_matrix()
        elif choice == 2:
            lesson_matrix_operations()
        elif choice == 3:
            lesson_transpose()
        elif choice == 4:
            lesson_determinant()
        elif choice == 5:
            lesson_inverse()
        elif choice == 6:
            lesson_matrices_practice()
        elif choice == 7:
            break
