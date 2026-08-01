#recupera información sobre peliculas
prompt=input("Ingrese el nombre de la película, banda musical, o serie: ").lower()
match prompt:
    case "el padrino":
        info="El Padrino es una película de 1972 dirigida por Francis Ford Coppola, basada en la novela homónima de Mario Puzo. Es considerada una de las mejores películas de la historia del cine y ha ganado varios premios, incluyendo el Oscar a la Mejor Película."
        tipo="película"
    case "titanic":
        info="Titanic es una película de 1997 dirigida por James Cameron, que narra la historia de dos jóvenes que se enamoran a bordo del RMS Titanic."
        tipo="película"
    case "inception":
        info="Inception es una película de 2010 dirigida por Christopher Nolan, que explora el concepto de los sueños y la manipulación de la mente humana."
        tipo="película"
    case "the beatles":
        info="The Beatles fue una banda británica de rock formada en Liverpool en 1960. Son considerados una de las bandas más influyentes en la historia de la música."
        tipo="banda"
    case "queen":
        info="Queen es una banda británica de rock formada en Londres en 1970. Son conocidos por su estilo musical diverso y sus icónicas actuaciones en vivo."
        tipo="banda"
    case "stray kids":
        info="Stray Kids es una banda surcoreana de rock formada en 2018. Son conocidos por su estilo musical innovador y sus actuaciones en vivo."
        tipo="banda"
    case "xlov":
        info="XLOV es una banda surcoreana de ballroom formada en 2025. Son conocidos por su estilo musical innovador y sus actuaciones en vivo."
        tipo="banda"
    case "the wheel of time":
        info="The Wheel of Time es una serie de televisión basada en la saga de novelas de Robert Jordan."
        tipo="serie"
    case ("dr. stone" | "dr stone"):
        info="Dr. Stone es una serie de televisión japonesa que sigue la historia de un científico que es transformado en piedra y debe encontrar una manera de regresar a la humanidad."
        tipo="serie"
    case "beastars":
        info="Beastars es una serie de televisión japonesa que sigue la historia de un lobo y una coneja antropomorfos donde carnívoros y herbívoros deben convivir en paz."
        tipo="serie"
    case _:
        info=None
        tipo=None


print("No se encontró información" if info is None else f"Resultado sobre {tipo} '{prompt}': \n{info}")