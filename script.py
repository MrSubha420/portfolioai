import os

def create_folder_structure():
    structure = {
        "my-chatbot": [
            "app/__init__.py",
            "app/main.py",
            "app/rag_pipeline.py",
            "app/utils/pdf_processor.py",
            "app/utils/vector_db.py",
            "static/styles.css",
            "templates/index.html",
            "data/personal_info.pdf",
            "requirements.txt",
            "README.md",
            "app.py"
        ]
    }
    
    for base, files in structure.items():
        for file in files:
            file_path = os.path.join(base, file)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    pass  # Create an empty file
    
    print("Folder structure created successfully!")

if __name__ == "__main__":
    create_folder_structure()