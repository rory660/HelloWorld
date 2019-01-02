import os

def getText(language):
	os.listdir("../helloWorld")
	return "\n".join(open("../helloWorld/" + language + "/" + file, "r").read() for file in os.listdir("../helloWorld/" + language))

def getData(language):
	text = getText(language)
	return {"files" : len(os.listdir("../helloWorld/" + language)), "lines" : len(text.split("\n")), "characters" : len(text)}

def getFormattedData(language):
	data = getData(language)
	return "## " + language + "\n" + "\n\n".join([str(value) + " " + str(key) for key, value in data.items()]) + "\n---\n"

def main():
	languages = os.listdir("../helloWorld")
	
	with open("../templates/README.md", "r") as readme:
		template = readme.read()

	with open("../README.md", "w") as readme:
		readme.write(template + "\n".join([getFormattedData(language) for language in languages]))

if __name__ == "__main__":
	main()