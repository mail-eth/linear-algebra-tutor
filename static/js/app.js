/* Linear Algebra Tutor - JavaScript */

// Show quiz section
function showQuiz() {
    const quizSection = document.getElementById('quiz-section');
    if (quizSection) {
        quizSection.classList.toggle('hidden');
        if (!quizSection.classList.contains('hidden')) {
            loadQuizContent();
        }
    }
}

// Load quiz content
function loadQuizContent() {
    const quizContent = document.querySelector('.quiz-content');
    if (!quizContent) return;

    quizContent.innerHTML = `
        <div class="section">
            <h3 class="section-title">🎯 Quick Quiz - Linear Algebra</h3>
            <div class="section-content">
                <h4>Soal 1 - Vector:</h4>
                <p>Berapa dot product dari A = [1, 2] dan B = [3, 4]?</p>

                <h4>Soal 2 - Matrix:</h4>
                <p>Berapa determinan dari A = [[1,2],[3,4]]?</p>

                <h4>Soal 3 - Sistem Persamaan:</h4>
                <p>Selesaikan: x + y = 5, x - y = 1</p>

                <h4>Soal 4 - Eigenvalues:</h4>
                <p>Berapa eigenvalue dari A = [[2,0],[0,3]]?</p>
            </div>
        </div>

        <div class="section">
            <h3 class="section-title">📝 Jawaban</h3>
            <div class="section-content">
                <h4>Soal 1:</h4>
                <p>A · B = (1×3) + (2×4) = 3 + 8 = <strong>11</strong></p>

                <h4>Soal 2:</h4>
                <p>det(A) = (1×4) - (2×3) = 4 - 6 = <strong>-2</strong></p>

                <h4>Soal 3:</h4>
                <p>x = 3, y = 2</p>

                <h4>Soal 4:</h4>
                <p>Untuk matrix diagonal, eigenvalue = elemen diagonal: <strong>2 dan 3</strong></p>
            </div>
        </div>
    `;
}

// Add typing effect to elements
function typeWriter(element, text, speed = 50) {
    let i = 0;
    element.textContent = '';

    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }

    type();
}

// Add terminal-like effects
document.addEventListener('DOMContentLoaded', function() {
    // Add click sound effect (optional)
    const buttons = document.querySelectorAll('button, .menu-item, .lesson-link');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Could add a subtle animation
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 100);
        });
    });

    // Add keyboard navigation
    document.addEventListener('keydown', function(e) {
        // ESC to go back
        if (e.key === 'Escape') {
            if (window.location.pathname !== '/') {
                window.location.href = '/';
            }
        }
    });
});

// Matrix display helper
function formatMatrixDisplay(matrix) {
    if (!Array.isArray(matrix)) return matrix;

    const rows = matrix.length;
    const cols = matrix[0].length;

    let html = '<table class="matrix-display">';

    // Add bracket styling
    html += '<tr>';
    html += '<td class="bracket-left" rowspan="' + rows + '">[</td>';

    for (let i = 0; i < rows; i++) {
        if (i > 0) html += '</tr><tr>';
        for (let j = 0; j < cols; j++) {
            html += '<td>' + matrix[i][j] + '</td>';
        }
    }

    html += '<td class="bracket-right" rowspan="' + rows + '">]</td>';
    html += '</tr>';
    html += '</table>';

    return html;
}

// Vector display helper
function formatVectorDisplay(vector) {
    if (!Array.isArray(vector)) return vector;
    return '[' + vector.join(', ') + ']';
}

// Console-like log (for debugging)
function consoleLog(message) {
    console.log('%c[Linear Algebra Tutor]', 'color: #00ff41; font-weight: bold;', message);
}
