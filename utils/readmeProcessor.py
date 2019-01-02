import os

def getText(language):
	os.listdir("../helloWorld")
	return "\n".join(open("../helloWorld/" + language + "/" + file, "r").read() for file in os.listdir("../helloWorld/" + language))

def getData(language):
	text = getText(language)
	return {"file" : len(os.listdir("../helloWorld/" + language)), "line" : len(text.split("\n")), "character" : len(text)}

def getFormattedData(language):
	data = getData(language)
	return language + " | " + " | ".join([str(value) + " " + str(key) + ("s" if value > 1 else "") for key, value in data.items()])

def main():
	languages = os.listdir("../helloWorld")
	
	with open("../templates/README.md", "r") as readme:
		template = readme.read()

	with open("../README.md", "w") as readme:
		schema = getData(languages[0]).keys()
		readme.write(template + "Language | " + "s | ".join(schema) + "s\n" + " | ".join(["---" for item in schema]) + "\n" + "\n".join([getFormattedData(language) for language in languages]))

if __name__ == "__main__":
	main()