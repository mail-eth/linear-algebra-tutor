"""Linear Algebra Tutor - Web App with CLI Aesthetic"""

from flask import Flask, render_template, jsonify, request
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')

# Math utilities
def create_vector(*components):
    return np.array(components, dtype=float)

def create_matrix(rows):
    return np.array(rows, dtype=float)

def vector_add(v1, v2):
    return v1 + v2

def vector_subtract(v1, v2):
    return v1 - v2

def scalar_multiply(scalar, vector):
    return scalar * vector

def dot_product(v1, v2):
    return np.dot(v1, v2)

def vector_magnitude(vector):
    return np.linalg.norm(vector)

def vector_normalize(vector):
    mag = vector_magnitude(vector)
    if mag == 0:
        raise ValueError("Cannot normalize zero vector")
    return vector / mag

def matrix_add(m1, m2):
    return m1 + m2

def matrix_multiply(m1, m2):
    return np.matmul(m1, m2)

def matrix_transpose(matrix):
    return matrix.T

def matrix_determinant(matrix):
    return np.linalg.det(matrix)

def matrix_inverse(matrix):
    return np.linalg.inv(matrix)

def eigenvalues_eigenvectors(matrix):
    return np.linalg.eig(matrix)

def solve_linear_system(A, b):
    return np.linalg.solve(A, b)


def format_number(n):
    """Format number to remove unnecessary decimals."""
    if isinstance(n, (int, np.integer)):
        return str(int(n))
    if isinstance(n, (float, np.floating)):
        if n == int(n):
            return str(int(n))
        return f"{n:.4f}"
    if isinstance(n, complex):
        if n.imag == 0:
            return format_number(n.real)
        return f"{n.real:.2f}+{n.imag:.2f}i"
    return str(n)


def format_vector(v):
    """Format vector as string."""
    return "[" + ", ".join(format_number(x) for x in v) + "]"


def format_matrix(m):
    """Format matrix as list of lists."""
    return [[format_number(m[i][j]) for j in range(len(m[i]))] for i in range(len(m))]


# Lesson data
LESSONS = {
    'vectors': {
        'title': '📐 Vector',
        'topics': [
            {'id': 'what-is-vector', 'title': 'Apa itu Vector?'},
            {'id': 'vector-operations', 'title': 'Operasi Vector'},
            {'id': 'dot-product', 'title': 'Dot Product'},
            {'id': 'magnitude', 'title': 'Magnitude & Normalisasi'},
        ]
    },
    'matrices': {
        'title': '📊 Matrix',
        'topics': [
            {'id': 'what-is-matrix', 'title': 'Apa itu Matrix?'},
            {'id': 'matrix-operations', 'title': 'Operasi Matrix'},
            {'id': 'transpose', 'title': 'Transpose Matrix'},
            {'id': 'determinant', 'title': 'Determinant'},
            {'id': 'inverse', 'title': 'Inverse Matrix'},
        ]
    },
    'systems': {
        'title': '📝 Sistem Persamaan Linear',
        'topics': [
            {'id': 'what-is-system', 'title': 'Apa itu Sistem Persamaan?'},
            {'id': 'substitution', 'title': 'Metode Substitusi'},
            {'id': 'elimination', 'title': 'Metode Eliminasi'},
            {'id': 'gaussian', 'title': 'Eliminasi Gauss'},
            {'id': 'cramers-rule', 'title': 'Aturan Cramer'},
        ]
    },
    'eigenvalues': {
        'title': '🔢 Eigenvalues & Eigenvectors',
        'topics': [
            {'id': 'what-is-eigen', 'title': 'Apa itu Eigenvalues?'},
            {'id': 'finding-eigenvalues', 'title': 'Mencari Eigenvalues'},
            {'id': 'finding-eigenvectors', 'title': 'Mencari Eigenvectors'},
            {'id': 'verification', 'title': 'Verifikasi Eigenvalues'},
        ]
    }
}


@app.route('/')
def index():
    return render_template('index.html', lessons=LESSONS)

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


@app.route('/lesson/<category>/<topic>')
def lesson(category, topic):
    if category not in LESSONS:
        return "Lesson not found", 404

    lesson_data = LESSONS[category]
    topic_data = None
    for t in lesson_data['topics']:
        if t['id'] == topic:
            topic_data = t
            break

    if not topic_data:
        return "Topic not found", 404

    return render_template('lesson.html',
                         category=category,
                         lesson=lesson_data,
                         topic=topic_data,
                         all_lessons=LESSONS)


@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    params = data.get('params', {})

    try:
        if operation == 'vector_add':
            v1 = create_vector(*params['v1'])
            v2 = create_vector(*params['v2'])
            result = vector_add(v1, v2)
            return jsonify({'success': True, 'result': format_vector(result)})

        elif operation == 'vector_subtract':
            v1 = create_vector(*params['v1'])
            v2 = create_vector(*params['v2'])
            result = vector_subtract(v1, v2)
            return jsonify({'success': True, 'result': format_vector(result)})

        elif operation == 'scalar_multiply':
            scalar = params['scalar']
            v = create_vector(*params['v'])
            result = scalar_multiply(scalar, v)
            return jsonify({'success': True, 'result': format_vector(result)})

        elif operation == 'dot_product':
            v1 = create_vector(*params['v1'])
            v2 = create_vector(*params['v2'])
            result = dot_product(v1, v2)
            return jsonify({'success': True, 'result': format_number(result)})

        elif operation == 'vector_magnitude':
            v = create_vector(*params['v'])
            result = vector_magnitude(v)
            return jsonify({'success': True, 'result': format_number(result)})

        elif operation == 'vector_normalize':
            v = create_vector(*params['v'])
            result = vector_normalize(v)
            return jsonify({'success': True, 'result': format_vector(result)})

        elif operation == 'matrix_add':
            m1 = create_matrix(params['m1'])
            m2 = create_matrix(params['m2'])
            result = matrix_add(m1, m2)
            return jsonify({'success': True, 'result': format_matrix(result)})

        elif operation == 'matrix_multiply':
            m1 = create_matrix(params['m1'])
            m2 = create_matrix(params['m2'])
            result = matrix_multiply(m1, m2)
            return jsonify({'success': True, 'result': format_matrix(result)})

        elif operation == 'matrix_transpose':
            m = create_matrix(params['m'])
            result = matrix_transpose(m)
            return jsonify({'success': True, 'result': format_matrix(result)})

        elif operation == 'matrix_determinant':
            m = create_matrix(params['m'])
            result = matrix_determinant(m)
            return jsonify({'success': True, 'result': format_number(result)})

        elif operation == 'matrix_inverse':
            m = create_matrix(params['m'])
            result = matrix_inverse(m)
            return jsonify({'success': True, 'result': format_matrix(result)})

        elif operation == 'eigenvalues':
            m = create_matrix(params['m'])
            eigenvalues, eigenvectors = eigenvalues_eigenvectors(m)
            return jsonify({
                'success': True,
                'eigenvalues': [format_number(v) for v in eigenvalues],
                'eigenvectors': [format_vector(eigenvectors[:, i]) for i in range(len(eigenvalues))]
            })

        elif operation == 'solve_system':
            A = create_matrix(params['A'])
            b = create_vector(*params['b'])
            result = solve_linear_system(A, b)
            return jsonify({'success': True, 'result': format_vector(result)})

        else:
            return jsonify({'success': False, 'error': 'Unknown operation'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=8080)

# For Vercel
application = app
