from sys import argv
from app.main_app import main

if __name__ == '__main__':
	_, base_path, file_extension, project_name = argv
	main(base_path, file_extension, project_name)
