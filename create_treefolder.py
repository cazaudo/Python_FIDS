import os
import argparse
import shutil # Ajouté pour l'option --clean

# Définition de la structure de cours par défaut, sans le répertoire racine
DEFAULT_COURSE_STRUCTURE = {
    'cours_mathematiques': ['TD1', 'TD2', 'TD3'],
    'cours_automatique': ['TD1', 'TD2']
}

# --- Analyse des arguments --- #
parser = argparse.ArgumentParser(description="Crée une arborescence de dossiers et de fichiers pour des cours.")
parser.add_argument('--courses', type=str,
                    help='Liste des cours principaux à créer, séparés par des virgules (ex: cours_mathematiques,cours_automatique). Si non spécifié, tous les cours par défaut seront créés.')
parser.add_argument('--root_dir', type=str, default='.',
                    help='Répertoire racine où créer l\'arborescence (par défaut: .).')
parser.add_argument('--clean', action='store_true',
                    help='Supprime les répertoires principaux existants (dans le root_dir) avant de les créer.')

# sys.argv contient des arguments spécifiques à l'interpréteur.
# Passer une liste vide à parse_args() simule l'absence d'arguments en ligne de commande.
# Pour tester avec des arguments dans le notebook, vous pouvez modifier cette ligne, par exemple :
# args = parser.parse_args(['--courses', 'cours_mathematiques', '--root_dir', 'my_courses'])
args = parser.parse_args()

# Déterminer les cours à créer en fonction des arguments
courses_to_create = {}
if args.courses:
    custom_course_names = [c.strip() for c in args.courses.split(',')]
    for course_name in custom_course_names:
        if course_name in DEFAULT_COURSE_STRUCTURE:
            courses_to_create[course_name] = DEFAULT_COURSE_STRUCTURE[course_name]
        else:
            print(f"Attention : Le cours '{course_name}' n'est pas reconnu dans la structure par défaut. Création de sous-répertoires génériques (TD1, TD2) pour celui-ci.")
            courses_to_create[course_name] = ['TD1', 'TD2']
else:
    courses_to_create = DEFAULT_COURSE_STRUCTURE

# Construire la structure finale des répertoires avec le root_dir
final_directory_structure_paths = {} # Cela stockera les chemins réels comme 'my_courses/cours_mathematiques'
for main_dir_name, sub_dirs_list in courses_to_create.items():
    actual_main_dir_path = os.path.join(args.root_dir, main_dir_name)
    final_directory_structure_paths[actual_main_dir_path] = sub_dirs_list

# Si l'option --clean est activée, supprimer les répertoires principaux existants
if args.clean:
    print(f"Suppression des répertoires principaux existants dans '{args.root_dir}'...")
    for main_dir_path in final_directory_structure_paths.keys():
        if os.path.exists(main_dir_path):
            shutil.rmtree(main_dir_path)
            print(f"  Répertoire supprimé : {main_dir_path}/")
    print("Suppression terminée.")


# Créer les répertoires et y ajouter des fichiers
for main_dir_path, sub_dirs in final_directory_structure_paths.items():
    os.makedirs(main_dir_path, exist_ok=True)
    print(f"Répertoire principal créé : {main_dir_path}/")
    for sub_dir in sub_dirs:
        path = os.path.join(main_dir_path, sub_dir)
        os.makedirs(path, exist_ok=True)
        print(f"  Sous-répertoire créé : {path}/")

        # Ajout de fichiers aléatoires (la logique dépend du nom du sous-répertoire)
        if sub_dir == 'TD1':
            with open(os.path.join(path, 'notes.txt'), 'w') as f: f.write('Contenu des notes.\nDeuxieme ligne de notes.')
            with open(os.path.join(path, 'exercice.py'), 'w') as f: f.write('print("Hello World")')
        elif sub_dir == 'TD2':
            with open(os.path.join(path, 'solution.pdf'), 'w') as f: f.write('%PDF-1.4\n') # Juste un en-tête pour simuler un PDF
            with open(os.path.join(path, 'README.md'), 'w') as f: f.write('# TD2 - Readme\nCeci est le README pour le TD2.')
        elif sub_dir == 'TD3':
            with open(os.path.join(path, 'cours.txt'), 'w') as f: f.write('Résumé du cours.\nLigne 2 du cours.\nLigne 3 du cours.')

print("\nArborescence de dossiers et fichiers créée avec succès.")
