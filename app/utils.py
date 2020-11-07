import glob


def recursive_read(root_dir, extension, project_name):
	resume = []

	for filename in glob.iglob(normalize_base_path(root_dir) + '/**/*.' + extension, recursive=True):
		index = filename.index(project_name)
		file_name = filename[index:]

		with open(filename, 'r') as file:
			file_content = file.read()

		resume.append([file_name, file_content])

	return resume


def normalize_base_path(root_dir):
	normalized_dir = root_dir

	if not str(root_dir).startswith("/"):
		normalized_dir = "/" + root_dir
	elif not str(root_dir).endswith("/"):
		normalized_dir = normalized_dir + "/"

	return normalized_dir


def write_as_txt(content, save_path):
	text_file = open(save_path, "wt")
	n = text_file.write(content)
	text_file.close()
