from flask import Flask, render_template, request, send_from_directory, redirect, jsonify
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'arquivos'

@app.route('/')
def index():
    return render_template('index.html', os=os)


@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.remove(file_path)
        return jsonify({'success': True})
    except Exception as e:
        print(f'Erro ao excluir o arquivo: {e}')
        return jsonify({'success': False})



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return redirect('/')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
