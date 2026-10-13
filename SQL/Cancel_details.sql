SELECT * FROM dbo.Cancels_details;

--Cancel orders by country
SELECT 
	Country,
	count(*) AS Totalrecords
	FROM
dbo.Cancels_details
Group by Country
order by Totalrecords DESC;

--highest cancel country
SELECT TOP 1
    Country,
    COUNT(*) AS TotalCancellations
FROM dbo.Cancels_details
GROUP BY Country
ORDER BY TotalCancellations DESC;

--lowest cancel
SELECT
    Country,
    COUNT(*) AS TotalCancellations
FROM dbo.Cancels_details
GROUP BY Country
HAVING COUNT(*) = 1;