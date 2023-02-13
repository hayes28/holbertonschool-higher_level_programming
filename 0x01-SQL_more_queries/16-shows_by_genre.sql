-- Write a script that lists all shows, and all genres linked
-- to that show, from the database hbtn_0d_tvshows
SELECT shows.title, genre.name
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS tvshowgenre
ON shows.id = tvshowgenre.show_id
LEFT JOIN tv_genres AS genre 
ON tvshowgenre.genre_id = genre.id
ORDER BY shows.title ASC, genre.name ASC;
