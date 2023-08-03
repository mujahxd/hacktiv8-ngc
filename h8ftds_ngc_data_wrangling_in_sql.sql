SELECT
  EXTRACT(YEAR FROM PARSE_DATE('%Y%m%d', Filing_Date)) AS year,
  EXTRACT(MONTH FROM PARSE_DATE('%Y%m%d', Filing_Date)) AS month,
  COUNT(*) AS total_patent
FROM `patents-public-data.uspto_oce_cancer.publications`

WHERE
  EXTRACT(YEAR FROM PARSE_DATE('%Y%m%d', Filing_Date)) BETWEEN 2012 AND 2023
  AND LOWER(Patent_Title) LIKE '%data mining%'
GROUP BY
  year, month
ORDER BY
  year DESC, month;



