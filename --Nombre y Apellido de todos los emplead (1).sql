--Nombre y Apellido de todos los empleados, en orden alfabético.--

SELECT FirstName, LastName FROM employees  
ORDER by  LastName ASC

--Nombre y duración de todas las canciones del álbum "Big Ones" ordenados del más largo al más corto--

SELECT name, Milliseconds FROM tracks t 
JOIN albums a ON t.AlbumId= a.AlbumId 
WHERE Title = "Big Ones" 
ORDER by Milliseconds DESC 

--Nombre y precio total de los 10 discos más baratos


SELECT a.Title , t.UnitPrice FROM tracks t 
JOIN albums a on t.AlbumId= a.AlbumId
LIMIT 10 

--Nombre del tema, nombre del género y nombre del disco del los temas que valen $0.99

SELECT t.Name, t.UnitPrice FROM tracks t 
JOIN genres g on t.GenreId= g.GenreId
JOIN albums a on t.AlbumId = a.AlbumId
WHERE t.UnitPrice = 0.99

--Nombre del tema, duración, nombre del disco y nombre del artista de los 20 temas más cortos

SELECT t.Name, t.Milliseconds FROM tracks t 
JOIN albums a on t.AlbumId = a.AlbumId
JOIN artists ar on a.ArtistId = ar.ArtistId
ORDER by t.Milliseconds ASC
LIMIT 20

--Apellido, puesto, apellido del jefe y cantidad de clientes que atiende de todos los empleados, 
--ordenado desde los que atienden más clientes a los que atienden menos.

SELECT emp.LastName AS ape_emple, emp.Title, jefe.LastName AS jefe_ape, COUNT(c.CustomerId) AS cant_cli FROM employees emp
JOIN employees jefe on jefe.EmployeeId= emp.ReportsTo
JOIN customers c  on c.SupportRepId= emp.EmployeeId
GROUP by emp.EmployeeId
ORDER by cant_cli DESC 

--Nombre y apellido del empleado/a y nombre y apellido del cliente/a que atiende cada empleado/a 
