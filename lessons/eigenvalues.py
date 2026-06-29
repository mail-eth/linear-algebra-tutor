"""Eigenvalue and Eigenvector lessons."""

import numpy as np
from utils.display import (
    console, show_lesson_title, show_concept, show_step,
    show_matrix, show_vector, show_calculation, show_success,
    show_info, show_warning, wait_for_next, show_menu
)
from utils.math_utils import (
    create_matrix, eigenvalues_eigenvectors, matrix_multiply,
    matrix_determinant
)


def lesson_what_is_eigen():
    """Lesson: What are Eigenvalues and Eigenvectors?"""
    show_lesson_title("Eigenvalues & Eigenvectors", "Konsep penting dalam linear algebra")

    show_concept("Definisi Eigenvalues & Eigenvectors", """
### Eigenvalue (Nilai Eigen) - λ
**Eigenvalue** adalah skalar yang menunjukkan seberapa besar vector di-stretch atau di-compress oleh transformasi.

### Eigenvector (Vector Eigen) - v
**Eigenvector** adalah vector yang arahnya **tidak berubah** setelah transformasi matrix (hanya berubah besarnya).

### Persamaan Fundamental:
$Av = \\lambda v$

Di mana:
- A = matrix transformasi
- v = eigenvector
- λ = eigenvalue

### Interpretasi Geometris:
Jika A mewakili transformasi, maka:
- Eigenvector menunjukkan **arah yang tetap**
- Eigenvalue menunjukkan **faktor scaling** pada arah tersebut
""")

    console.print("""
    [bold yellow]Visualisasi:[/bold yellow]

    Sebelum transformasi:     Sesudah transformasi (A):

         ↑ v                        ↑ Av = λv
         |                          |
         |                          | (λ > 1: stretch)
         |                          | (λ = 1: tetap)
         +----→                     +----→
                                    (arah tetap!)
    """)

    wait_for_next()


def lesson_finding_eigenvalues():
    """Lesson: Finding Eigenvalues."""
    show_lesson_title("Mencari Eigenvalues", "Menyelesaikan karakteristik equation")

    show_concept("Cara Mencari Eigenvalues", """
### Langkah-langkah:
1. **Tulis persamaan karakteristik**: $det(A - \\lambda I) = 0$
2. **Selesaikan** persamaan polinomial untuk λ

### Contoh Matrix 2×2:
$A = \\begin{bmatrix} 3 & 1 \\\\ 0 & 2 \\end{bmatrix}$

$A - \\lambda I = \\begin{bmatrix} 3-\\lambda & 1 \\\\ 0 & 2-\\lambda \\end{bmatrix}$

$det(A - \\lambda I) = (3-\\lambda)(2-\\lambda) = 0$

Eigenvalues: $\\lambda_1 = 3, \\lambda_2 = 2$
""")

    wait_for_next()

    A = create_matrix([[3, 1], [0, 2]])
    show_matrix("A", A)

    console.print("[bold cyan]Mencari Eigenvalues:[/bold cyan]")

    show_step(1, "Tulis A - λI:")
    console.print("     [3-λ,  1  ]")
    console.print("     [0,   2-λ ]")

    show_step(2, "Hitung determinan:")
    console.print("     det = (3-λ)(2-λ) - (1)(0)")
    console.print("     det = (3-λ)(2-λ)")

    show_step(3, "Set = 0 dan selesaikan:")
    console.print("     (3-λ)(2-λ) = 0")
    console.print("     λ₁ = 3, λ₂ = 2")

    eigenvalues, eigenvectors = eigenvalues_eigenvectors(A)
    show_success(f"Eigenvalues: λ₁ = {eigenvalues[0]:.0f}, λ₂ = {eigenvalues[1]:.0f}")

    wait_for_next()


def lesson_finding_eigenvectors():
    """Lesson: Finding Eigenvectors."""
    show_lesson_title("Mencari Eigenvectors", "Vector yang arahnya tetap")

    show_concept("Cara Mencari Eigenvectors", """
### Langkah-langkah:
Setelah menemukan eigenvalue λ:
1. **Substitusi** λ ke $(A - \\lambda I)v = 0$
2. **Selesaikan** sistem homogen untuk v

### Contoh (lanjutan):
$A = \\begin{bmatrix} 3 & 1 \\\\ 0 & 2 \\end{bmatrix}$, $\\lambda_1 = 3$

$(A - 3I)v = 0$
$\\begin{bmatrix} 0 & 1 \\\\ 0 & -1 \\end{bmatrix} \\begin{bmatrix} v_1 \\\\ v_2 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$

Dari baris 1: $v_2 = 0$
$v_1$ bebas → pilih $v_1 = 1$

Eigenvector: $v_1 = \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}$
""")

    wait_for_next()

    A = create_matrix([[3, 1], [0, 2]])
    show_matrix("A", A)

    eigenvalues, eigenvectors = eigenvalues_eigenvectors(A)

    console.print("[bold cyan]Mencari Eigenvector untuk λ₁ = 3:[/bold cyan]")

    show_step(1, "A - 3I:")
    A_shifted = A - 3 * np.eye(2)
    show_matrix("A - 3I", A_shifted)

    show_step(2, "(A - 3I)v = 0:")
    console.print("     0·v₁ + 1·v₂ = 0")
    console.print("     → v₂ = 0")

    show_step(3, "Pilih v₁ = 1:")
    console.print("     v₁ = [1, 0]")

    show_vector("v₁", eigenvectors[:, 0].real)

    console.print("\n[bold cyan]Eigenvector untuk λ₂ = 2:[/bold cyan]")
    show_vector("v₂", eigenvectors[:, 1].real)

    show_success("Eigenvector ditemukan!")
    wait_for_next()


def lesson_eigen_verification():
    """Lesson: Verifying Eigenvalues."""
    show_lesson_title("Verifikasi Eigenvalues", "Memastikan jawaban benar")

    show_concept("Verifikasi Av = λv", """
### Cara Verifikasi:
Untuk setiap pasangan eigenvalue-eigenvector, pastikan:
$Av = \\lambda v$

### Sifat Penting:
1. Eigenvector bukan nol vector
2. Eigenvector bisa di-scale (2v juga eigenvector)
3. Eigenvalue bisa nol (tapi eigenvector tidak)

### Matrix Symmetric:
- Eigenvalues selalu **real**
- Eigenvectors saling **orthogonal**
""")

    wait_for_next()

    A = create_matrix([[3, 1], [0, 2]])
    show_matrix("A", A)

    eigenvalues, eigenvectors = eigenvalues_eigenvectors(A)

    for i in range(len(eigenvalues)):
        λ = eigenvalues[i].real
        v = eigenvectors[:, i].real

        console.print(f"\n[bold cyan]Verifikasi λ{i+1} = {λ:.0f}:[/bold cyan]")
        show_vector(f"v{i+1}", v)

        # Calculate Av
        Av = matrix_multiply(A, v.reshape(-1, 1)).flatten()
        show_step(1, f"Av = ", "")
        show_vector("Av", Av)

        # Calculate λv
        λv = λ * v
        show_step(2, f"λv = {λ:.0f} × v = ", "")
        show_vector("λv", λv)

        if np.allclose(Av, λv):
            show_success("Av = λv ✓")
        else:
            show_warning("Verifikasi gagal!")

    wait_for_next()


def lesson_eigen_practice():
    """Practice problems for eigenvalues."""
    show_lesson_title("Latihan Eigenvalues", "Coba sendiri!")

    show_concept("Soal Latihan", """
Temukan eigenvalues dan eigenvectors untuk matrix berikut:

**Soal 1:**
$A = \\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \\end{bmatrix}$

**Soal 2:**
$B = \\begin{bmatrix} 1 & 2 \\\\ 2 & 4 \\end{bmatrix}$

**Soal 3:**
$C = \\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix}$ (Rotasi 90°)
""")

    wait_for_next()

    # Problem 1
    console.print("[bold cyan]Soal 1:[/bold cyan]")
    A = create_matrix([[2, 1], [1, 2]])
    show_matrix("A", A)
    eigenvalues, eigenvectors = eigenvalues_eigenvectors(A)
    show_info(f"Eigenvalues: {eigenvalues[0]:.0f}, {eigenvalues[1]:.0f}")
    show_vector("v₁", eigenvectors[:, 0].real)
    show_vector("v₂", eigenvectors[:, 1].real)

    # Problem 2
    console.print("\n[bold cyan]Soal 2:[/bold cyan]")
    B = create_matrix([[1, 2], [2, 4]])
    show_matrix("B", B)
    eigenvalues, eigenvectors = eigenvalues_eigenvectors(B)
    show_info(f"Eigenvalues: {eigenvalues[0]:.0f}, {eigenvalues[1]:.0f}")
    show_vector("v₁", eigenvectors[:, 0].real)
    show_vector("v₂", eigenvectors[:, 1].real)

    # Problem 3
    console.print("\n[bold cyan]Soal 3 (Rotasi):[/bold cyan]")
    C = create_matrix([[0, -1], [1, 0]])
    show_matrix("C", C)
    eigenvalues, eigenvectors = eigenvalues_eigenvectors(C)
    show_info(f"Eigenvalues: {eigenvalues[0]:.2f}, {eigenvalues[1]:.2f}")
    show_info("Eigenvalues kompleks → tidak ada arah yang tetap dalam ruang real!")

    show_success("Selesai! Eigenvalues adalah konsep yang powerful!")
    wait_for_next()


def eigenvalues_menu():
    """Main eigenvalue lessons menu."""
    while True:
        choice = show_menu("📚 Eigenvalues & Eigenvectors", [
            "Apa itu Eigenvalues?",
            "Mencari Eigenvalues",
            "Mencari Eigenvectors",
            "Verifikasi Eigenvalues",
            "Latihan Eigenvalues",
            "← Kembali ke Menu Utama"
        ])

        if choice == 1:
            lesson_what_is_eigen()
        elif choice == 2:
            lesson_finding_eigenvalues()
        elif choice == 3:
            lesson_finding_eigenvectors()
        elif choice == 4:
            lesson_eigen_verification()
        elif choice == 5:
            lesson_eigen_practice()
        elif choice == 6:
            break
