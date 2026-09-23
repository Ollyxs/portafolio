python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
touch public/.nojekyll

# Copiar el CNAME si existe en la raíz, o generarlo si sabemos el dominio
if [ -f CNAME ]; then
    cp CNAME public/CNAME
else
    echo "ollyxs.com.ar" > public/CNAME
fi

rm -f frontend.zip
deactivate
