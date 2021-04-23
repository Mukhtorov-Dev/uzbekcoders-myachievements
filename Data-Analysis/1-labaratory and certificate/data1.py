# test1
SELECT invoice.*
FROM invoice
where invoice.invoicedate between '2013-01-01' and '2014-01-01'

# test2
SELECT firstName,lastName,country
FROM customer
WHERE country IN("Brazil","Canada","India","Sweden")

# test3
SELECT Track.name, Track.Composer, Album.Title
FROM Track
JOIN Album
ON Track.AlbumId = Album.AlbumId
WHERE Track.name LIKE 'A%' AND Track.Composer NOT LIKE '' 

# test4
SELECT C.Firstname,C.Lastname,I.Total
FROM Customer AS C
JOIN Invoice AS I
ON C.CustomerId = I.CustomerId
ORDER BY I.total DESC
LIMIT 10