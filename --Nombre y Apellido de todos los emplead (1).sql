--1 Nombre y Apellido de todos los empleados, en orden alfabético.--

SELECT FirstName, LastName FROM employees  
ORDER by  LastName ASC

--2 Nombre y duración de todas las canciones del álbum "Big Ones" ordenados del más largo al más corto--

SELECT name, Milliseconds FROM tracks t 
JOIN albums a ON t.AlbumId= a.AlbumId 
WHERE Title = "Big Ones" 
ORDER by Milliseconds DESC 

--3 Nombre y precio total de los 10 discos más baratos


SELECT a.Title , t.UnitPrice FROM tracks t 
JOIN albums a on t.AlbumId= a.AlbumId
LIMIT 10 

--4 Nombre del tema, nombre del género y nombre del disco del los temas que valen $0.99

SELECT t.Name, t.UnitPrice FROM tracks t 
JOIN genres g on t.GenreId= g.GenreId
JOIN albums a on t.AlbumId = a.AlbumId
WHERE t.UnitPrice = 0.99

--5 Nombre del tema, duración, nombre del disco y nombre del artista de los 20 temas más cortos

SELECT t.Name, t.Milliseconds FROM tracks t 
JOIN albums a on t.AlbumId = a.AlbumId
JOIN artists ar on a.ArtistId = ar.ArtistId
ORDER by t.Milliseconds ASC
LIMIT 20

--6 Apellido, puesto, apellido del jefe y cantidad de clientes que atiende de todos los empleados, 
--ordenado desde los que atienden más clientes a los que atienden menos.

SELECT emp.LastName AS ape_emple, emp.Title, jefe.LastName AS jefe_ape, COUNT(c.CustomerId) AS cant_cli FROM employees emp
JOIN employees jefe on jefe.EmployeeId= emp.ReportsTo
JOIN customers c  on c.SupportRepId= emp.EmployeeId
GROUP by emp.EmployeeId
ORDER by cant_cli DESC 

--7 Nombre y apellido del empleado/a y nombre y apellido del cliente/a que atiende cada empleado/a
SELECT e.FirstName, e.LastName, c.FirstName, c.LastName
FROM employees e
JOIN customers c ON e.EmployeeId = c.SupportRepId; 

--8 Nombre, apellido y direccion del cliente/a y la factura correspondiente a ese cliente.
SELECT c.FirstName, c.LastName, c.Address, i.InvoiceId
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId; 

--9 Mostrar el nombre del género y el número total de canciones asociadas a cada uno, ordenados de mayor a menor cantidad. 
SELECT g.Name, COUNT(t.TrackId) AS Cantidad
FROM genres g
JOIN tracks t ON g.GenreId = t.GenreId
GROUP BY g.GenreId, g.Name
ORDER BY Cantidad DESC; 

--10 Mostrar el nombre del cliente y el nombre del artista de las canciones que ha comprado, ordenado alfabéticamente por cliente para ver qué variedad de artistas consume cada uno.
SELECT c.FirstName, c.LastName, ar.Name AS Artista
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items il ON i.InvoiceId = il.InvoiceId
JOIN tracks t ON il.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists ar ON a.ArtistId = ar.ArtistId
ORDER BY c.LastName;

--11 Mostrar el nombre del cliente, la ciudad donde vive, el nombre de la canción que compró y el nombre del género de esa canción.
SELECT c.FirstName, c.City, T.name, g.name FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items il ON i.InvoiceId = il.InvoiceId
JOIN tracks t ON il.TrackId = t.TrackId
JOIN genres g ON t.GenreId = g.GenreId

--12 Se puede realizar una sentencia que una todas las tablas? En caso de que sea un sí, realizar la sentencia, en caso de que sea no, justificar la respuesta.
SELECT *
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON ii.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists ar ON a.ArtistId = ar.ArtistId
JOIN genres g ON t.GenreId = g.GenreId
JOIN employees e ON c.SupportRepId = e.EmployeeId
JOIN media_types mt ON t.MediaTypeId = mt.MediaTypeId
JOIN playlist_track pt ON t.TrackId = pt.TrackId
JOIN playlists p ON pt.PlaylistId = p.PlaylistId;
 
