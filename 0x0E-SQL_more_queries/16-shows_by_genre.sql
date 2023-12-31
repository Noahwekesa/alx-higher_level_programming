-- Script to List Shows and Genres from hbtn_0d_tvshows Database

SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.show_id
ORDER BY tv_shows.title ASC, genre ASC;