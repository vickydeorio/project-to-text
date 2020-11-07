from traceback import print_exc
from app.utils import *


def main(base_path, file_extension, project_name):
	try:
		content_list = recursive_read(base_path, file_extension, project_name)

		content_to_write = project_name + "\n\n\n"
		for obj in content_list:
			content_to_write += obj[0] + "\n" + obj[1] + "\n\n\n"

		write_as_txt(content_to_write, f"resources/{project_name}-{file_extension}-to-text.txt")

	except Exception as ex:
		print_exc()
