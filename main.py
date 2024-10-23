import generation


if __name__ == "__main__":
    title = input("Enter title: ")
    author = input("Enter author (optional): ")
    themes = {1: "default", 2: "gaia"}
    theme_choice = int(input("Choose theme:\n1) default\n2) gaia\n> "))
    chosen_theme = themes[theme_choice]

    # Generate a presentation
    generator = generation.Generator()
    generator.generate_presentation(title, author, chosen_theme)

    print("Done")
