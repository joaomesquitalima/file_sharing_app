from flask import Flask, render_template, request, send_from_directory, redirect, jsonify
import os
import signal


def shutdown_server():
    os.kill(os.getpid(), signal.SIGINT)


class MeuAppFlask:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['UPLOAD_FOLDER'] = 'upload_arquivos/arquivos/'
        # self.app.config['UPLOAD_'] = 'C:/Users/esquita/Desktop/midias'
        
        

        self.app.route('/delete/<filename>', methods=['DELETE'])(self.delete_file)
        self.app.route('/upload', methods=['POST'])(self.upload_file)
        self.app.route('/uploads/<filename>',methods=['GET'])(self.uploaded_file)
        self.app.route('/shutdown')(self.shutdown)
        self.app.route('/')(self.index)
        # self.app.route('/login',methods=['POST'])(self.login)
        self.app.route('/arquivos', methods=['POST','GET'])(self.index)

    # def home(self):
    #     return render_template('home.html')
    
    # def login(self):
    #     nome = request.form['nome']
    #     senha = request.form['senha']

    #     if nome == 'mesquita' and senha == '040586ac':
    #         return redirect('/arquivos')


    #     # if nome == 'mesquita' and senha == '040586ac':
    #     #     return redirect('/arquivos')

    def index(self):
        files = os.listdir(self.app.config['UPLOAD_FOLDER'])
        return render_template('index.html', os=os, files=files)

    def delete_file(self, filename):
        try:
            file_path = os.path.join("upload_arquivos/arquivos", filename)
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
            # print("Escolha algo")
            return redirect(request.url)

        if file:
            filename = os.path.join(self.app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return redirect('/')

    def uploaded_file(self, filename):
        
        return send_from_directory('arquivos/',filename)
    

    def shutdown(self):
        shutdown_server()
        return "Servidor está desligando..."
    


    def run(self):
        self.app.run(debug=False, host='0.0.0.0', port=5000)




if __name__ == '__main__':
    meu_app = MeuAppFlask()
    meu_app.run()