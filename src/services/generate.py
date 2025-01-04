import logging
import subprocess
import os

def generate_latex_with_ai(app):
    def generate_latex(name, title, content, document_type="article", theme="default", image_path=None, image_size="1.0\\textwidth", image_align="center"):
        try:
            if document_type == "beamer":
                document_class = r"\documentclass{beamer}"
                theme_setup = f"\\usetheme{{{theme}}}" if theme != "default" else ""
                inputenc_package = ""
            else:
                document_class = r"\documentclass{article}"
                theme_setup = ""
                inputenc_package = r"\usepackage[utf8]{inputenc}"

            image_code = (
                rf"""
                \begin{{figure}}[{image_align}]
                \includegraphics[width={image_size}]{{{os.path.basename(image_path)}}}
                \end{{figure}}
                """
                if image_path
                else ""
            )

            latex_content = rf"""
            {document_class}
            {inputenc_package}
            {theme_setup}
            \usepackage{{graphicx}}
            \usepackage{{xcolor}}
            \title{{{title}}}
            \author{{{name}}}
            \date{{\today}}

            \begin{{document}}
            \maketitle
            {content}
            {image_code}
            \end{{document}}
            """

            tex_path = os.path.join(app.config['UPLOAD_FOLDER'], "document.tex")
            with open(tex_path, 'w', encoding='utf-8') as f:
                f.write(latex_content)
            logging.debug(f"Arquivo LaTeX criado em: {tex_path}")

            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', tex_path],
                cwd=app.config['UPLOAD_FOLDER'],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                logging.error(f"Erro na compilação do LaTeX: {result.stderr}")
                raise Exception(f"Erro na compilação do documento LaTeX: {result.stderr}")

            logging.debug("Documento LaTeX compilado com sucesso.")
            return tex_path.replace('.tex', '.pdf')

        except Exception as e:
            logging.error(f"Erro ao gerar o documento: {e}")
            raise

    return generate_latex
