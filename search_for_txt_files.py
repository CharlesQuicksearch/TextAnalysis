import os

#Kolla igenom mappar och filer efter filer som slutar på .txt
#Kör analys på texten
#Skicka till script som lägger till analysen i en dataframe csv fil

class FileHandler:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def check_for_txt_files(self):
        for root, dirs, files in os.walk(self.folder_path):
            if 'directory' in dirs:
                dirs.remove('directory')
            if 'archive' in dirs:
                dirs.remove('archive')
            for filename in files:
                if any(filename.endswith(".txt") and not filename.startswith("analyzed")):
                    current_dir = os.getcwd()
                    file_path = os.path.join(root, filename)

