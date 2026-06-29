"""Display utilities using Rich for beautiful terminal output."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.markdown import Markdown
from rich.text import Text
from rich.rule import Rule
from rich import box
import numpy as np

console = Console()


def show_welcome():
    """Display welcome banner."""
    title = Text("📐 Linear Algebra Tutor", style="bold magenta")
    subtitle = Text("Belajar Linear Algebra Step-by-Step", style="italic cyan")

    panel = Panel(
        f"{title}\n{subtitle}",
        box=box.DOUBLE,
        border_style="bright_blue",
        padding=(1, 2),
    )
    console.print(panel)
    console.print()


def show_menu(title: str, options: list[str]) -> int:
    """Display a menu and return user choice."""
    table = Table(
        title=title,
        box=box.ROUNDED,
        border_style="cyan",
        title_style="bold yellow",
    )
    table.add_column("No", style="bold green", justify="center")
    table.add_column("Menu", style="white")

    for i, option in enumerate(options, 1):
        table.add_row(str(i), option)

    console.print(table)
    console.print()

    choice = IntPrompt.ask(
        "[bold yellow]Pilih menu[/bold yellow]",
        choices=[str(i) for i in range(1, len(options) + 1)],
    )
    return choice


def show_lesson_title(title: str, subtitle: str = ""):
    """Display lesson title."""
    console.print()
    console.print(Rule(title, style="bold magenta"))
    if subtitle:
        console.print(Text(subtitle, style="italic cyan"), justify="center")
    console.print()


def show_concept(title: str, explanation: str):
    """Display a concept with explanation."""
    panel = Panel(
        Markdown(explanation),
        title=f"[bold cyan]{title}[/bold cyan]",
        box=box.ROUNDED,
        border_style="blue",
        padding=(1, 2),
    )
    console.print(panel)
    console.print()


def show_step(step_num: int, description: str, detail: str = ""):
    """Display a step in a process."""
    console.print(f"\n[bold green]Step {step_num}:[/bold green] {description}")
    if detail:
        console.print(f"  [dim]{detail}[/dim]")


def show_matrix(name: str, matrix: np.ndarray):
    """Display a matrix in a formatted way."""
    rows, cols = matrix.shape
    table = Table(
        title=f"Matrix {name}",
        box=box.SIMPLE,
        border_style="cyan",
        title_style="bold",
        show_header=False,
        pad_edge=False,
    )

    for _ in range(cols):
        table.add_column(justify="right", min_width=8)

    for i in range(rows):
        row = [f"{matrix[i, j]:.2f}" for j in range(cols)]
        table.add_row(*row)

    console.print(table)
    console.print()


def show_vector(name: str, vector: np.ndarray):
    """Display a vector."""
    formatted = [f"{v:.2f}" for v in vector]
    console.print(f"[bold cyan]Vector {name}:[/bold cyan] [{', '.join(formatted)}]")


def show_calculation(expression: str, result: str):
    """Show a calculation and its result."""
    console.print(f"  [dim]{expression}[/dim] = [bold yellow]{result}[/bold yellow]")


def show_success(message: str):
    """Display success message."""
    console.print(f"\n[bold green]✓ {message}[/bold green]")


def show_info(message: str):
    """Display info message."""
    console.print(f"[bold blue]ℹ {message}[/bold blue]")


def show_warning(message: str):
    """Display warning message."""
    console.print(f"[bold yellow]⚠ {message}[/bold yellow]")


def wait_for_next():
    """Wait for user to continue."""
    console.print()
    Prompt.ask("[dim]Tekan Enter untuk melanjutkan...[/dim]", default="")


def clear_screen():
    """Clear the terminal screen."""
    console.clear()
