import os
from datetime import datetime
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='.')

# قاعدة بيانات مؤقتة في الذاكرة
users_db = {}
messages_db = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/auth', methods=['POST'])
def auth():
    data = request.json
    username = data.get('username')
    display_name = data.get('display_name')
    phone = data.get('phone')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'يرجى إدخال اسم المستخدم وكلمة المرور'}), 400

    if username in users_db:
        if users_db[username]['password'] == password:
            return jsonify({
                'success': True,
                'username': username,
                'display_name': users_db[username]['display_name'],
                'phone': users_db[username]['phone']
            })
        else:
            return jsonify({'success': False, 'message': 'كلمة المرور غير صحيحة'}), 400
    else:
        users_db[username] = {
            'display_name': display_name or username,
            'phone': phone or '+000000000',
            'password': password
        }
        return jsonify({
            'success': True,
            'username': username,
            'display_name': users_db[username]['display_name'],
            'phone': users_db[username]['phone']
        })

@app.route('/api/chats', methods=['GET'])
def get_chats():
    current_user = request.args.get('user')
    chat_list = []
    
    for u, data in users_db.items():
        if u != current_user:
            last_msg = "اضغط للبدء بالمحادثة"
            time_str = "الآن"
            
            for m in reversed(messages_db):
                if (m['sender'] == current_user and m['receiver'] == u) or (m['sender'] == u and m['receiver'] == current_user):
                    last_msg = m['message']
                    time_str = m['time']
                    break
                    
            chat_list.append({
                'username': u,
                'display_name': data['display_name'],
                'last_message': last_msg,
                'time': time_str
            })
            
    return jsonify(chat_list)

@app.route('/api/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'POST':
        data = request.json
        now = datetime.now().strftime("%I:%M %p")
        msg_obj = {
            'sender': data.get('sender'),
            'receiver': data.get('receiver'),
            'message': data.get('message'),
            'time': now
        }
        messages_db.append(msg_obj)
        return jsonify({'success': True, 'message': msg_obj})
    
    sender = request.args.get('sender')
    receiver = request.args.get('receiver')
    
    filtered = [
        m for m in messages_db 
        if (m['sender'] == sender and m['receiver'] == receiver) or 
           (m['sender'] == receiver and m['receiver'] == sender)
    ]
    return jsonify(filtered)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
