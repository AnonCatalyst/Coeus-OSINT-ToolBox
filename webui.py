from flask import Flask, render_template
import os
import markdown

app = Flask(__name__, template_folder='tem')

@app.route('/')
def index():
    # Specify the folder containing Markdown files
    folder_path = os.path.dirname(os.path.realpath(__file__))

    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter Markdown files
    markdown_files = [file for file in files if file.endswith('.md')]

    # Group files by category
    categories = {}
    for file in markdown_files:
        category = file.split('_')[0]  # Assuming files are named like 'category_filename.md'
        if category not in categories:
            categories[category] = []
        categories[category].append(file)

    return render_template('index.html', categories=categories)

@app.route('/file/<filename>')
def file_detail(filename):
    # Read the Markdown file
    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    return html_content

if __name__ == '__main__':
    app.run(debug=True)
