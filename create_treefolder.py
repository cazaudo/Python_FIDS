import os

# Définir l'arborescence à créer
directory_structure = {
    'cours_mathematiques': ['TD1', 'TD2', 'TD3'],
    'cours_automatique': ['TD1', 'TD2']
}

# Créer les répertoires
for main_dir, sub_dirs in directory_structure.items():
    os.makedirs(main_dir, exist_ok=True) # Crée le répertoire principal si inexistant
    print(f"Répertoire principal créé : {main_dir}/")
    for sub_dir in sub_dirs:
        path = os.path.join(main_dir, sub_dir)
        os.makedirs(path, exist_ok=True) # Crée le sous-répertoire si inexistant
        print(f"  Sous-répertoire créé : {path}/")

print("\nArborescence de dossiers créée avec succès.")
