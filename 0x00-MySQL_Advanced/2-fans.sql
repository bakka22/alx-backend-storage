-- ranks county origins of bands orderd by the number of fans
SELECT origin, COUNT(fans) AS nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
