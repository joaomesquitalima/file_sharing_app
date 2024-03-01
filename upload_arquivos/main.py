from flask import Flask, render_template, request, send_from_directory, redirect, jsonify
import os

class MeuAppFlask:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['UPLOAD_FOLDER'] = 'arquivos'
        
        self.app.route('/')(self.index)
        self.app.route('/delete/<filename>', methods=['DELETE'])(self.delete_file)
        self.app.route('/upload', methods=['POST'])(self.upload_file)
        self.app.route('/uploads/<filename>')(self.uploaded_file)

    def index(self):
        return render_template('index.html', os=os)

    def delete_file(self, filename):
        try:
            file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
            os.remove(file_path)
            return jsonify({'success': True})
        except Exception as e:
            print(f'Erro ao excluir o arquivo: {e}')
            return jsonify({'success': False})

    def upload_file(self):
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = os.path.join(self.app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return redirect('/')

    def uploaded_file(self, filename):
        return send_from_directory(self.app.config['UPLOAD_FOLDER'], filename)

    def run(self):
        self.app.run(debug=False, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    meu_app = MeuAppFlask()
    meu_app.run()
