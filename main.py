movies = []

menu_prompt = "\n Enter your choice: 'a' for adding a movie, 's' for showing a movie, 'f' to find a movie, " \
              "'q' for quitting : "


def add_movie():
    name_movie = input('please enter the name of the movie')
    year_movie = input('please enter the year of the movie')
    movies.append(
        dict(name=name_movie, year=year_movie)
    )


def show_movie():
    for movie in movies:
        print(f" title : {movie['name']}")
        print(f" year : {movie['year']}")


def find_movie():
    movie_title = input('enter the name of the movie you want to search')
    for movie in movies:
        if movie['name'] == movie_title:
            print(f" title : {movie['name']}")
            print(f" year : {movie['year']}")
        else:
            print(" the movie name doesn't exist in our database")
            break


def menu_selection():
    menu = input(menu_prompt)
    while menu != 'q':
        if menu == 'a':
            add_movie()
        elif menu == 's':
            show_movie()
        elif menu == 'f':
            find_movie()
        else:
            print('you have not entered a correct choice')
        menu = input(menu_prompt)


menu_selection()
