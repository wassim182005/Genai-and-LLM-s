# Install dependencies for this project (PowerShell)
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Download spaCy English model
python -m spacy download en_core_web_sm

Write-Output "Dependencies installed. You can now run: python Text_rank.py"