import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify
from flask_cors import CORS 
flask groq import GROQ 
from core.promp_mestre import Prompt_Mestre 

app = Flask(__name__)
CORS(app)

client = GROQ(api_key=os.environ.get("GROQ_API_KEY"))
prompt = PromptMestre()

@app.route("/api/chat", methods = ("POST"))
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem", "")

    resposta = client.chat.completions.create(
        model= "llhama3-8b-8192",
        messages=[
            {"role": "system","content": prompt.get_prompt()},
            {"role": "user", "content": mensagem}
        ]
    )
    return jsonify({"resposta": resposta.choices{0}. message.content})