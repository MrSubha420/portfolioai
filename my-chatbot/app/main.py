from flask import Flask, request, jsonify
from flask_cors import CORS
from app.rag_pipeline import RAGPipeline

app = Flask(__name__)
CORS(app)

rag = RAGPipeline("data/personal_info.pdf")

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    answer = rag.generate_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)