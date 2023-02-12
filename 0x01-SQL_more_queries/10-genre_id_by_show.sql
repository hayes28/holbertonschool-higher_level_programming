-- import database from 'hbtn_0d_tvshows'
-- Lists all shows in 'hbtn_0d_tvshows' with at least
-- one genre linked
SELECT tv_shows.title, tv_shows.id=tv_shows_genres.tv_show_id
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id=tv_shows_genres.tv_show_id
GROUP BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;
