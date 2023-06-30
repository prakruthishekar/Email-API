from flask import Flask, jsonify, request
from flask_mail import Mail, Message

from config import MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)

# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "bostonhealthservice@gmail.com"
app.config['MAIL_PASSWORD'] = "flemhtqfurzhrvmo"

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    sender_name = data.get('sender_name')
    sender_email = data.get('sender_email')
    body = data.get('body')

    if not sender_email or not body or not sender_name:
        return jsonify({'error': 'Missing required parameters'}), 400

    msg = Message(subject="Message From Portfolio", sender=(sender_name, sender_email), recipients=['prakruthisomashekar29@gmail.com'])
    msg.body = body

    try:
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()