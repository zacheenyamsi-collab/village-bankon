# start_ngrok.py
from pyngrok import ngrok
import os
import re

# Démarre un tunnel sur le port 8000
public_url = ngrok.connect(8000, bind_tls=True)
print("✅ URL publique :", public_url)

# Chemin vers settings.py
settings_path = os.path.join(os.path.dirname(__file__), 'village', 'settings.py')

# Lire le fichier settings.py
with open(settings_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Met à jour ou ajoute CSRF_TRUSTED_ORIGINS
pattern = r"CSRF_TRUSTED_ORIGINS\s*=\s*\[.*?\]"
replacement = f"CSRF_TRUSTED_ORIGINS = ['{public_url}']"

if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
else:
    content += f"\n\n{replacement}\n"

# Écriture du nouveau contenu
with open(settings_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ settings.py mis à jour avec CSRF_TRUSTED_ORIGINS.")

# Met à jour ou ajoute ALLOWED_HOSTS
host = public_url.replace('https://', '').replace('http://', '').split('/')[0]
allowed_pattern = r"ALLOWED_HOSTS\s*=\s*\[.*?\]"
allowed_replacement = f"ALLOWED_HOSTS = ['localhost', '127.0.0.1', '{host}']"

if re.search(allowed_pattern, content, re.DOTALL):
    content = re.sub(allowed_pattern, allowed_replacement, content, flags=re.DOTALL)
else:
    content += f"\n\n{allowed_replacement}\n"
