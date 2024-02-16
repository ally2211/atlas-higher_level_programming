--   lists all Comedy shows.
SELECT tv_shows.title,
CASE WHEN tv_genres.name IS NULL THEN NULL ELSE tv_genres.name END AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, CASE WHEN tv_genres.name IS NULL THEN NULL ELSE tv_genres.name END;