from flask import request, send_from_directory, after_this_request, render_template
from controllers.controllers import generate_content, generate_latex_ai
import logging
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_content_route(app):
    @app.route('/generate', methods=['POST'])
    def generate():
        generate_latex = generate_latex_ai(app)
        title = request.form.get('title', 'Título do Documento')  
        name = request.form.get('name')
        user_prompt = request.form.get('content', '') 
        document_type = request.form.get('document_type', 'article')
        theme = request.form.get('theme', 'default')  
        image = request.files.get('image')  
        image_size = request.form.get('image_size', '1.0\\textwidth') 
        image_align = request.form.get('image_align', 'center')  
        file_format = request.form.get('file_format', 'pdf')  

        image_path = None
        if image and image.filename != '':
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)

        try:
            pdf_path = generate_latex(name, title, generate_content(user_prompt), document_type, theme, image_path, image_size, image_align)

            @after_this_request
            def cleanup(response):
                try:
                    if file_format == 'pdf':
                        os.remove(pdf_path)
                    os.remove(pdf_path.replace('.pdf', '.tex'))  # Excluir o arquivo .tex
                    if image_path:
                        os.remove(image_path)
                    aux_files = ['.aux', '.log']
                    for ext in aux_files:
                        aux_path = pdf_path.replace('.pdf', ext)
                        if os.path.exists(aux_path):
                            os.remove(aux_path)
                    logging.debug("Arquivos temporários removidos com sucesso.")
                except Exception as e:
                    logging.error(f"Erro ao limpar arquivos: {e}")
                return response

            if file_format == 'pdf':
                return send_from_directory(app.config['UPLOAD_FOLDER'], 'document.pdf', as_attachment=True)
            elif file_format == 'tex':
                return send_from_directory(app.config['UPLOAD_FOLDER'], 'document.tex', as_attachment=True)
            else:
                return "Formato inválido solicitado. Escolha entre 'pdf' ou 'tex'.", 400

        except Exception as e:
            logging.error(f"Erro ao gerar o documento: {e}")
            return f"Erro ao gerar o documento: {e}", 500


def index_route(app):
    @app.route('/')
    def index():
        return render_template('index.html')
