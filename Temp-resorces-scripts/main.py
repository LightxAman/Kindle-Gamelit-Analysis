import os

# Define project structure
project_name = "gamelit_litrpg_analysis"
structure = {
    "": ["README.md", "requirements.txt", "config.yaml", "setup.py"],
    "data": ["raw/", "processed/", "logs/"],
    "src": ["__init__.py", "scraper.py", "tracker.py", "sentiment.py", "earnings.py", "storage.py", "utils.py"],
    "dashboard": ["app.py", "assets/"],
    "notebooks": ["exploration.ipynb", "report.ipynb"]
}

# Create directories and files
os.makedirs(project_name, exist_ok=True)
for folder, items in structure.items():
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)
    for item in items:
        # Determine full path
        file_path = os.path.join(folder_path, item)
        # If item indicates a directory (ends with '/'), make directory
        if item.endswith('/'):
            os.makedirs(file_path, exist_ok=True)
        else:
            # Create empty file or with placeholder content
            with open(file_path, 'w') as f:
                # Placeholder for Python files
                if file_path.endswith('.py'):
                    f.write("# TODO: Implement {}\n".format(os.path.basename(file_path)))
                # Placeholder for README.md
                elif file_path.endswith('README.md'):
                    f.write("# GameLit & LitRPG Kindle Analysis\n\nProject overview and setup instructions.\n")
                # Placeholder for requirements.txt
                elif file_path.endswith('requirements.txt'):
                    f.write(
                        "requests\nbeautifulsoup4\npandas\nsqlalchemy\npyyaml\nschedule\nnltk\nvaderSentiment\nstreamlit\nplotly\n")
                # Placeholder for config.yaml
                elif file_path.endswith('config.yaml'):
                    f.write("user_agent: \"Your User Agent\"\nsleep_seconds: 5\n")
                else:
                    # Generic placeholder
                    f.write("")

print(f"Project scaffold '{project_name}' created successfully.")
