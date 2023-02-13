-- script that lists all Comedy shows
-- in the database hbtn_0d_tvshows
SELECT shows.title FROM tv_shows AS shows
JOIN tv_show_genres AS tvshowgenre
ON shows.id = tvshowgenre.show_id
JOIN tv_genres AS genres
ON tvshowgenre.genre_id = genres.id
WHERE genres.name = 'Comedy'
ORDER BY shows.title ASC;
