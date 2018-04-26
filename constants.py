import course
import song

COURSES = [
    course.Course(period=1,
                  name='Intro to Computer Science',
                  teacher_name='Ms. Lee',
                  resource_name='repl.it',
                  resource_url='https://repl.it/'),
    course.Course(period=2,
                  name='U.S. History',
                  teacher_name='Mr. Killeen',
                  resource_name='ArtHistory.net',
                  resource_url='http://www.arthistory.net/'),
    course.Course(period=3,
                  name='AP Lang',
                  teacher_name='Mrs. Pacia-McCann',
                  resource_name='Spark Notes',
                  resource_url='http://www.sparknotes.com/'),
    course.Course(period=4,
                  name='Algebra 2',
                  teacher_name='Ms. Song',
                  resource_name='Khan Academy',
                  resource_url='https://www.khanacademy.org/math/geometry/'),
    course.Course(period=5,
                  name='Biotechnology',
                  teacher_name='Mr. Ng',
                  resource_name='Active Simuations',
                  resource_url='https://phet.colorado.edu/en/simulations/category/physics'),
    course.Course(period=6,
                  name='Art 1',
                  teacher_name='Ms. Hoover',
                  resource_name='Wikipedia',
                  resource_url='https://en.wikipedia.org/wiki/Biology'),
]

TOP_TEN_SONGS = [
    song.Song(title="XO TOUR LIFE",
        artist_name="Lil Uzi Vert,"
        youtube_url="