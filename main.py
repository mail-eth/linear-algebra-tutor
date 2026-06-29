#!/usr/bin/env python3
"""
Linear Algebra Tutor - Interactive CLI Application
Learn linear algebra step-by-step with Rich terminal UI
"""

from utils.display import (
    console, show_welcome, show_menu, show_info,
    clear_screen, wait_for_next
)
from lessons.vectors import vector_menu
from lessons.matrices import matrices_menu
from lessons.systems import systems_menu
from lessons.eigenvalues import eigenvalues_menu


def show_about():
    """Show about information."""
    console.print("""
[bold cyan]Tentang Linear Algebra Tutor[/bold cyan]

Aplikasi CLI interaktif untuk belajar linear algebra secara step-by-step.

[bold yellow]Topik yang tersedia:[/bold yellow]
  📐 Vector - Konsep dasar, operasi, dot product
  📊 Matrix - Operasi, determinan, inverse
  📝 Sistem Persamaan - Substitusi, eliminasi, Cramer
  🔢 Eigenvalues - Eigenvalues dan eigenvectors

[bold green]Fitur:[/bold green]
  • Penjelasan konsep dengan notasi matematika
  • Contoh interaktif dengan perhitungan step-by-step
  • Visualisasi dan verifikasi
  • Latihan soal

[bold magenta]Dibuat dengan:[/bold magenta]
  • Python 3
  • Rich (terminal UI)
  • NumPy (perhitungan matematika)
""")

    wait_for_next()


def show_quick_quiz():
    """Show a quick quiz across all topics."""
    from utils.math_utils import (
        create_vector, create_matrix, dot_product, vector_magnitude,
        matrix_determinant, solve_linear_system, eigenvalues_eigenvectors
    )

    console.print("\n[bold magenta]🎯 Quick Quiz - Linear Algebra[/bold magenta]")
    console.print("=" * 50)

    # Question 1: Vector
    console.print("\n[bold cyan]Soal 1 - Vector:[/bold cyan]")
    console.print("Berapa dot product dari A = [1, 2] dan B = [3, 4]?")
    v_a = create_vector(1, 2)
    v_b = create_vector(3, 4)
    result = dot_product(v_a, v_b)
    console.print(f"[bold green]Jawaban: {result:.0f}[/bold green]")
    console.print("  (1×3) + (2×4) = 3 + 8 = 11")

    # Question 2: Matrix
    console.print("\n[bold cyan]Soal 2 - Matrix:[/bold cyan]")
    console.print("Berapa determinan dari A = [[1,2],[3,4]]?")
    A = create_matrix([[1, 2], [3, 4]])
    det = matrix_determinant(A)
    console.print(f"[bold green]Jawaban: {det:.0f}[/bold green]")
    console.print("  det = (1×4) - (2×3) = 4 - 6 = -2")

    # Question 3: System
    console.print("\n[bold cyan]Soal 3 - Sistem Persamaan:[/bold cyan]")
    console.print("Selesaikan: x + y = 5, x - y = 1")
    A_sys = create_matrix([[1, 1], [1, -1]])
    b = create_vector(5, 1)
    x = solve_linear_system(A_sys, b)
    console.print(f"[bold green]Jawaban: x = {x[0]:.0f}, y = {x[1]:.0f}[/bold green]")

    # Question 4: Eigenvalue
    console.print("\n[bold cyan]Soal 4 - Eigenvalues:[/bold cyan]")
    console.print("Berapa eigenvalue dari A = [[2,0],[0,3]]?")
    A_eig = create_matrix([[2, 0], [0, 3]])
    eigenvalues, _ = eigenvalues_eigenvectors(A_eig)
    console.print(f"[bold green]Jawaban: {eigenvalues[0]:.0f}, {eigenvalues[1]:.0f}[/bold green]")
    console.print("  (Untuk matrix diagonal, eigenvalue = elemen diagonal)")

    console.print("\n" + "=" * 50)
    console.print("[bold yellow]Bagaimana skormu?[/bold yellow]")
    wait_for_next()


def main():
    """Main application loop."""
    clear_screen()
    show_welcome()

    while True:
        choice = show_menu("🏠 Menu Utama", [
            "📐 Pelajaran Vector",
            "📊 Pelajaran Matrix",
            "📝 Sistem Persamaan Linear",
            "🔢 Eigenvalues & Eigenvectors",
            "🎯 Quick Quiz",
            "ℹ️  Tentang Aplikasi",
            "🚪 Keluar"
        ])

        if choice == 1:
            vector_menu()
        elif choice == 2:
            matrices_menu()
        elif choice == 3:
            systems_menu()
        elif choice == 4:
            eigenvalues_menu()
        elif choice == 5:
            show_quick_quiz()
        elif choice == 6:
            show_about()
        elif choice == 7:
            console.print("\n[bold magenta]Terima kasih telah belajar! 👋[/bold magenta]")
            console.print("[dim]Semoga sukses dengan linear algebra![/dim]\n")
            break


if __name__ == "__main__":
    main()
