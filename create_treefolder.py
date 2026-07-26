import os

# Définir l'arborescence à créer
directory_structure = {
    'cours_mathematiques': ['TD1', 'TD2', 'TD3'],
    'cours_automatique': ['TD1', 'TD2']
}

# Créer les répertoires et y ajouter des fichiers
for main_dir, sub_dirs in directory_structure.items():
    os.makedirs(main_dir, exist_ok=True) # Crée le répertoire principal si inexistant
    print(f"Répertoire principal créé : {main_dir}/")
    for sub_dir in sub_dirs:
        path = os.path.join(main_dir, sub_dir)
        os.makedirs(path, exist_ok=True) # Crée le sous-répertoire si inexistant
        print(f"  Sous-répertoire créé : {path}/")

        # Ajout de fichiers aléatoires
        if sub_dir == 'TD1':
            with open(os.path.join(path, 'notes.txt'), 'w') as f: f.write('Contenu des notes.\nDeuxieme ligne de notes.')
            with open(os.path.join(path, 'exercice.py'), 'w') as f: f.write('print("Hello World")')
        elif sub_dir == 'TD2':
            with open(os.path.join(path, 'solution.pdf'), 'w') as f: f.write('%PDF-1.4\n') # Juste un en-tête pour simuler un PDF
            with open(os.path.join(path, 'README.md'), 'w') as f: f.write('# TD2 - Readme\nCeci est le README pour le TD2.')
        elif sub_dir == 'TD3':
            with open(os.path.join(path, 'cours.txt'), 'w') as f: f.write('Résumé du cours.\nLigne 2 du cours.\nLigne 3 du cours.')

print("\nArborescence de dossiers et fichiers créée avec succès.")
