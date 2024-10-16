python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf docs
reflex init
reflex export --frontend-only
unzip frontend.zip -d docs
rm -f frontend.zip
deactivate

