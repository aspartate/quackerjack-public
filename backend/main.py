from flask import Flask, request, jsonify
import openai
import tempfile
import os

with open('secrets.txt', 'r') as f:
    openai.api_key = f.read()


def return_response(name, snippet, mode):
    # Mode determines the prompt to use
    if mode == 'mean':
        prompt = f'Insult {name} (make the insult as savage as possible, but also related to the conversation).\n\nJack: '
    elif mode == 'nice':
        prompt = f'Make {name} feel better about themselves.\n\nJack: '
    elif mode == 'tesla':
        prompt = f'Segue from whatever the conversation is about to convince {name} to buy Tesla stock.\n\nJack: '

    # Read history from file
    if not os.path.exists('/tmp/history.txt'):
        write_history('')

    with open('/tmp/history.txt', 'r') as f:
        history = f.read()
    print(history)

    # Generate payload
    payload = history + f'\n\{name}: ' + snippet + '\n\n' + prompt

    # Generate response
    response = openai.Completion.create(model="text-davinci-003", prompt=payload, temperature=1, max_tokens=200)
    result = response['choices'][0]['text'].split(f'\n{name}:')[0].strip() # Remove everything after an instance of "{name}:", in case the model over-generates

    # Append result to history and save
    write_history(history + f'\n\n{name}: ' + snippet + '\n\nJack: ' + result)

    return result

def write_history(content):
    # Append result to history and save
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(content)

    # Replace history file with the new file
    os.replace(f.name, '/tmp/history.txt')

app = Flask(__name__)

# Method to get response from chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    request_data = request.get_json()
    print('Incoming request: ' + str(request_data))
    name = request_data['name']
    snippet = request_data['snippet']
    mode = request_data['mode']
    response = return_response(name, snippet, mode)
    return jsonify({'response': response})

# Method to reset history
@app.route('/reset', methods=['POST'])
def reset():
    write_history('')
    return jsonify({'response': 'History reset'})

# Method to return history
@app.route('/history', methods=['GET'])
def history():
    with open('/tmp/history.txt', 'r') as f:
        history = f.read()
    return jsonify({'response': history})

if __name__ == '__main__':
    app.run(debug = True)