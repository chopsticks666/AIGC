from flask import Flask, render_template, redirect, url_for, send_file
from flask import Flask, render_template, request, jsonify
from backend.model import Adder, MusicGenerator

app = Flask(__name__)
adder = Adder()
music_generator = MusicGenerator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test_page', methods=['GET', 'POST'])
def test_page():
    return render_template('test_page.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = adder.add_numbers(num1, num2)
        return render_template('result.html', result=result)
    else:
        return redirect(url_for('test_page.html'))  # 如果是 GET 请求，重定向到主页


@app.route('/about_us')
def another_page():
    return render_template('about_us.html')


@app.route('/github')
def github_page():
    return render_template('github.html')


@app.route('/generate')
def music_path():
    return render_template('generate_music.html')

@app.route('/generate_music', methods=['POST'])
def generate_music():
    if 'audio' not in request.files and  'prompt' not in request.form:
        return jsonify({'error': 'Audio file or prompt are required.'}), 400

    if 'audio' not in request.files:
        audio_file = None
    else:
        audio_file = request.files['audio']
    prompt = request.form['prompt']

    output_filename = music_generator.generate_music(prompt, audio_file)

    return send_file(output_filename, mimetype='audio/wav')

@app.route('/load_model')
def load_model():
    model_id = request.args.get('model')
    if not model_id:
        return jsonify({'error': 'Model ID is required as a parameter.', 'status': 'error'}), 400
    
    try:
        print(f"Loading model with ID: {model_id}")
        music_generator.change_to_model(model_id=int(model_id))
        return jsonify({'message': f'Model {model_id} loaded successfully.', 'status': 'loaded'}), 200
    except Exception as e:
        print(f"Failed to load model {model_id}: {str(e)}")
        return jsonify({'error': f'Failed to load model {model_id}.', 'status': 'error'}), 500
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
