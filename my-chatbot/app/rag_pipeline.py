from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from app.utils.vector_db import VectorDB
from app.utils.pdf_processor import extract_text_from_pdf

class RAGPipeline:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.vector_db = VectorDB()
        self._initialize()

    def _initialize(self):
        # Extract text from PDF
        text = extract_text_from_pdf(self.pdf_path)
        chunks = text.split("\n\n")  # Simple chunking
        self.vector_db.add_texts(chunks)

    def generate_answer(self, question):
        # Retrieve relevant chunks
        indices = self.vector_db.search(question)
        context = " ".join([chunks[i] for i in indices])
        # Generate answer using LLM
        llm = OpenAI(api_key="your-openai-api-key")
        qa = RetrievalQA.from_chain_type(llm, chain_type="stuff")
        answer = qa.run(context + "\n\nQuestion: " + question)
        return answer