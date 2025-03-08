-- Get top 5 most downloaded apps
SELECT App, Installs FROM playstore_apps ORDER BY Installs DESC LIMIT 5;

-- Average rating by category
SELECT Category, AVG(Rating) FROM playstore_apps GROUP BY Category ORDER BY AVG(Rating) DESC;
