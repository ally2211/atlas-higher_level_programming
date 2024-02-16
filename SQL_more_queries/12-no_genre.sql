--  lists all shows contained in the database hbtn_0d_tvshows.
SELECT title,
CASE WHEN genre_id IS NULL THEN NULL ELSE genre_id END AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;