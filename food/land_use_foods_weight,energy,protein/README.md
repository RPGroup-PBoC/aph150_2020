# Land Use for food products per kg, 1000 kcal, 100 g protein (global average)

## Description 
This data describes the global average land use of various foods in their production.
The 4 columns show the food type and land use measured in meters squared (m<sup>2</sup>) per kilogram, 
per 1000 kilocalories, and  per 100 grams of protein respectively.

## Key Numbers
Agriculture number = Beef (beef herd) [land use/energy] /Maize (corn) [land use/energy] = 170.

## Source Information

* **Source Website**: Our World in Data: https://ourworldindata.org/environmental-impacts-of-food
* **URL**: These were 3 related datasets. For land use per weight:
https://ourworldindata.org/grapher/land-use-per-kg-poore , for land use per energy:
https://ourworldindata.org/grapher/land-use-kcal-poore , for land use per protein:
https://ourworldindata.org/grapher/land-use-protein-poore
* **Bias**: LEFT-CENTER BIAS, HIGH factual Reporting 
(often publish factual information that utilizes loaded words)

## Notes 
The data represent the global average land use of food products.
It is important to keep in mind that variation around the average is significant
(For this reason the dataset `land_use_foods_distribution` was added to the `food/` directory).

The data is the result of an extensive meta-analysis of food system impact studies published in Science magazine
([Poore & Nemecek, 2018](https://science.sciencemag.org/content/360/6392/987)).
Science magazine is a PRO-SCIENCE source and it’s factual reporting is labeled
VERY HIGH which increases the credibility of the data.

The authors note the following about the scope of the studies included in this meta-analysis:
"We derived data from a comprehensive meta-analysis, identifying 1530 studies for potential
inclusion, which were supplemented with additional data received from 139 authors.
Studies were assessed against 11 criteria designed to standardize methodology,
resulting in 570 suitable studies with a median reference year of 2010.
The data set covers ~38,700 commercially viable farms in 119 countries and 40 products
representing ~90% of global protein and calorie consumption'.

Poore & Nemecek do not provide data per 100g protein for food
products which are not protein-rich, or kilocalorie measures for non-stale crops.
To provide footprints for all products Our World in Data have filled these gaps by calculating 
footprints per nutritional unit using food composition factors from the FAO INFOODS International 
Database and Food Balance Sheets

![](media/land-use-per-kg-poore.png)
![](media/land-use-kcal-poore.png)
![](media/land-use-protein-poore.png) 
