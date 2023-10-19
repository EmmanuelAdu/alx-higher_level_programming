-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
SELECT tg.name
FROM tv_genres AS tg
WHERE tg.id NOT IN
(SELECT tg.id
FROM tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
INNER JOIN tv_shows AS ts
ON tsg.show_id = ts.id
WHERE ts.title = "Dexter")
ORDER BY tg.name;
