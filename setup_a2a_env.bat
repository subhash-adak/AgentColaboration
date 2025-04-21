@echo off
set PY310=C:\Python310\python.exe

echo 🧪 Creating virtual environment...
%PY310% -m venv .venv

echo ✅ Activating environment...
call .venv\Scripts\activate

echo 📦 Installing dependencies (Torch 2.0.1 CPU-safe)...
pip install --upgrade pip
pip install torch==2.0.1+cpu torchvision==0.15.2+cpu torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cpu
pip install sentence-transformers==2.2.2 streamlit pinecone python-docx pymupdf

echo 💾 Saving dependencies...
pip freeze > requirements.txt

echo.
echo ✅ Setup complete!
echo Run the app with:
echo call .venv\Scripts\activate && streamlit run app.py
pause
