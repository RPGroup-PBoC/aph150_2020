
# Mapping the world's free-flowing rivers

## Description
In order to estimate the extent of river fragmentation, we rely on data compiled and generated by [Grill _et al._](https://www.nature.com/articles/s41586-019-1111-9) a csv file of which can be found on Zenodo as linked below.

Grill _et al._ provide an extensive, high-resolution (500 m) dataset of global rivers whose upstream catchment areas are greater than 10 km<sup>2</sup> or whose discharge is greater than 100 liters per second. This results in a global river network of 35.9 million kilometers. Rivers were then broken up into "reaches", defined as a segment between two river confluences.

## Key Numbers
Importantly to this analysis, the attributes of each reach contain information pertaining to continent 'CONTINENT' / 'CON_ID', backbone river 'BB_NAME' / 'BB__ID', volume (thousand m<sup>3</sup>) 'VOLUME_TCM', average long-term (1971-2000) discharge (m<sup>3</sup> / s) 'DIS_AV_CMS', ocean connectivity of backbone river 'BB_OCEAN', dominant pressure factor 'CSI_D', and whether it belongs to a free-flowing river 'CSI_FF1'.

## Source Information
* **Source Website**: Zenodo: Sarai, Nicholas S. (2020). Mapping the world's free-flowing rivers: CSV Dataset (Version 0.1.0) [Data set]. Zenodo.
* **URL**: CSV dataset used in this analysis: http://doi.org/10.5281/zenodo.3875115, original dataset: https://figshare.com/articles/Mapping_the_world_s_free-flowing_rivers_data_set_and_technical_documentation/7688801
* **Bias**: `NOT ANNOTATED`

## Notes
8.5 million of these reaches with an average reach length of 4.2 km result. Hydrographic, geometric, and free-flowing status attributes were associated with the river reaches as described in the documentation of the [original dataset](https://figshare.com/articles/Mapping_the_world_s_free-flowing_rivers_data_set_and_technical_documentation/7688801). A comprehensive definition of connectivity, and thus free-flowing status is provided that encompasses longitudinal, lateral, vertical, and temporal connectivity. Using a set of weights guided by the literature, a connectivity status index (CSI) was calculated for each river reach. Free-flowing rivers are defined as those that have a CSI ≥ 95 throughout their length.

Grill _et al._ present a well-curated and described set of rivers. The data are mostly compiled from international datasets of rivers that appear reliable. I do not have the expertise in rivers to evaluate the 95 CSI threshold used to divide free-flowing and non-free-flowing rivers. This number could be subject to biases by the authors.
