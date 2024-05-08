
# Import config
from config import *
from src.utils.io import *
from src.utils.print import *
import json

# Prepare lang dictionnary and lang_format function
lang = {}
def lang_format(text: str):
	""" Get alphanumeric characters from a string and return it.
	Args:
		text (str): The text to format
	Returns:
		str: The formatted text
	"""
	text = text.replace("\\n", "_").replace(".","_")
	alpha_num = "".join(char for char in text if char.isalnum() or char in " _-").lower()
	for char in [' ', '-', "__"]:
		alpha_num = alpha_num.replace(char, "_")
	alpha_num = alpha_num[:64].strip("_").strip()
	if alpha_num.startswith(NAMESPACE):
		return alpha_num
	else:
		return (NAMESPACE + "." + alpha_num)


# For each file in FILES_TO_WRITE
possibles_texts = ['"text":', '\\"text\\":']
for file, content in FILES_TO_WRITE.items():

	# For each line while "text" is in line
	new_content = []
	for line in content.split("\n"):
		while any(possible_text in line for possible_text in possibles_texts):
			for possible_text in possibles_texts:
				if possible_text not in line:
					continue

				# Get the text
				splitted = line.split(possible_text)
				text = '"'.join(splitted[1].split('"')[1:])	# Get the starting text
				text_end = 0	# Get the end of the text
				for i, char in enumerate(text):
					try:
						if char == '"':
							if (possible_text == possibles_texts[0] and text[i-1] != "\\"):		# "text":"..."
								text_end = i
								break
							elif (possible_text == possibles_texts[1] and text[i-1] == "\\" and text[i-2] != "\\\\"):	# \"text\":\"...\"
								text_end = i - 1
								break
					except IndexError:
						pass
				text = text[:text_end]	# Get the text without the ending " (and the rest of the line)

				# Get the lang format and add the key value to the dictionnary
				key_for_lang = lang_format(text)
				if key_for_lang not in lang.keys():
					lang[key_for_lang] = text
				elif lang[key_for_lang] != text:
					warning(f"The text '{text}' is already used by '{lang[key_for_lang]}' for key '{key_for_lang}' with a different value.")

				# Replace the text in the line by the lang format
				line = line.replace(text, key_for_lang, 1)

				# Replace "text" by "translate"
				line = line.replace(possible_text, possible_text.replace("text", "translate"), 1)
		new_content.append(line)
	
	# Write the new content to the file
	FILES_TO_WRITE[file] = "\n".join(new_content)


# Write the lang file
FILES_TO_WRITE[f"{BUILD_RESOURCE_PACK}/assets/minecraft/lang/en_us.json"] = super_json_dump(lang)

