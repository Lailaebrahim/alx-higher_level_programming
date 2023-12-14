
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.show_id
GROUB BY GENRE
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
