import os

def getText(language):
	os.listdir("../helloWorld")
	return "\n".join(open("../helloWorld/" + language + "/" + file, "r").read() for file in os.listdir("../helloWorld/" + language))

def getData(language):
	text = getText(language)
	return {"Files" : len(os.listdir("../helloWorld/" + language)), "Lines" : len(text.split("\n")), "Characters" : len(text)}

def getFormattedData(language):
	data = getData(language)
	return language + " | " + " | ".join([str(val) for val in data.values()])

def main():
	languages = os.listdir("../helloWorld")
	
	with open("../templates/README.md", "r") as readme:
		template = readme.read()

	with open("../README.md", "w") as readme:
		schema = getData(languages[0]).keys()
		readme.write(template + "Language | " + " | ".join(schema) + "\n" + " | ".join(["---" for item in range(len(schema) + 1)]) + "\n" + "\n".join([getFormattedData(language) for language in languages]))

if __name__ == "__main__":
	main()