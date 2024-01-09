from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Path to the hosts file on Windows
hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/block', methods=['POST'])
def block_websites():
    if request.method == 'POST':
        websites_to_block = request.form.get('websites').split(',')
        try:
            block_websites_in_hosts(websites_to_block)
            return render_template('index.html', message='Websites blocked successfully')
        except Exception as e:
            return render_template('index.html', message=f'Error: {str(e)}')

def block_websites_in_hosts(websites_to_block):
    with open(hosts_file_path, 'a') as hosts_file:
        for website in websites_to_block:
            hosts_file.write('127.0.0.1 ' + website.strip() + '\n')

if __name__ == '__main__':
    app.run(debug=True)
