from string import Template


def main():
    # Traditional formatting with method format()
    phrase = "Reviewing {0} concepts in {1}.".format("advanced", "Python")
    print(phrase)

    # Format using Template()
    templ = Template("Reviewing ${level} concepts in ${lang}.")
    phrase_2 = templ.substitute(
        level="advanced",
        lang="Python"
    )
    print(phrase_2)

    # Using a dictionary to define the data
    data = {
        "level": "advanced",
        "lang": "Python"
    }
    phrase_3 = templ.substitute(data)
    print(phrase_3)
    

if __name__ == "__main__":
    main()
