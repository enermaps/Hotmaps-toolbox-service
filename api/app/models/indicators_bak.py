# -*- coding: utf-8 -*-
from app.constants import hectare_name, lau2, nuts0, nuts1, nuts2, nuts3

# LAYERS
""" POPULATION_TOT = constants.POPULATION_TOT
HEAT_DENSITY_TOT = constants.HEAT_DENSITY_TOT
wwtp = constants.WWTP
WWTP_CAPACITY = constants.WWTP_CAPACITY
WWTP_POWER = constants.WWTP_POWER
grass = constants.GRASS_FLOOR_AREA_TOT
GRASS_FLOOR_AREA_RES = constants.GRASS_FLOOR_AREA_RES
GRASS_FLOOR_AREA_NON_RES = constants.GRASS_FLOOR_AREA_NON_RES
BUILDING_VOLUMES_TOT = constants.BUILDING_VOLUMES_TOT
BUILDING_VOLUMES_RES = constants.BUILDING_VOLUMES_RES
BUILDING_VOLUMES_NON_RES = constants.BUILDING_VOLUMES_NON_RES
LAND_SURFACE = 'land_surface_temperature'
HEAT_DENSITY_RES = constants.HEAT_DENSITY_RES
HEAT_DENSITY_NON_RES = constants.HEAT_DENSITY_NON_RES
indSites = constants.INDUSTRIAL_SITES
INDUSTRIAL_SITES_EMISSIONS = constants.INDUSTRIAL_SITES_EMISSIONS
INDUSTRIAL_SITES_EXCESS_HEAT = constants.INDUSTRIAL_SITES_EXCESS_HEAT
BIOMASS_POTENTIAL = constants.BIOMASS_POTENTIAL
MUNICIPAL_SOLID_WASTE = constants.MUNICIPAL_SOLID_WASTE
WIND_POTENTIAL = constants.WIND_POTENTIAL
SOLAR_POTENTIAL = constants.SOLAR_POTENTIAL
GEOTHERMAL_POTENTIAL_HEAT_COND = constants.GEOTHERMAL_POTENTIAL_HEAT_COND2
ELECRICITY_CO2_EMISSION_FACTOR = constants.ELECRICITY_CO2_EMISSION_FACTOR
hdd = constants.HDD_CUR
cdd = constants.CDD_CUR """

POPULATION_TOT = "pop_tot_curr_density"
HEAT_DENSITY_TOT = "heat_tot_curr_density"
HEAT_DENSITY_NON_RES = "heat_nonres_curr_density"
HEAT_DENSITY_RES = "heat_res_curr_density"
GRASS_FLOOR_AREA_TOT = "gfa_tot_curr_density"
GRASS_FLOOR_AREA_RES = "gfa_res_curr_density"
GRASS_FLOOR_AREA_NON_RES = "gfa_nonres_curr_density"
BUILDING_VOLUMES_RES = "vol_res_curr_density"
BUILDING_VOLUMES_TOT = "vol_tot_curr_density"
BUILDING_VOLUMES_NON_RES = "vol_nonres_curr_density"
INDUSTRIAL_SITES = "industrial_database"
INDUSTRIAL_SITES_EMISSIONS = "industrial_database_emissions"
INDUSTRIAL_SITES_EXCESS_HEAT = "industrial_database_excess_heat"
WWTP = "wwtp"
WWTP_CAPACITY = "wwtp_capacity"
WWTP_POWER = "wwtp_power"
POTENTIAL_FOREST = "potential_forest"
LIVESTOCK_EFFLUENTS = "livestock_effluents_view"
MUNICIPAL_SOLID_WASTE = "potential_municipal_solid_waste"
WIND_SPEED = "output_wind_speed"
WIND_POTENTIAL = "wind_50m"
SOLAR_POTENTIAL = "solar_optimal_total"
# GEOTHERMAL_POTENTIAL_HEAT_COND = 'potential_shallowgeothermal_heat_cond'
GEOTHERMAL_POTENTIAL_HEAT_COND = "potential_shallowgeothermal"
ELECTRICITY_CO2_EMISSION_FACTOR = "yearly_co2_emission"
HDD_CUR = "hdd_curr"
CDD_CUR = "cdd_curr"
ELECRICITY_MIX = "stat.yearly_electricity_generation_mix"
LAND_SURFACE_TEMP = "land_surface_temperature"
AGRICULTURAL_RESIDUES = "agricultural_residues_view"
SOLAR_RADIATION = "solar_radiation"


stat = "stat_"
vector_type = "vector"
raster_type = "raster"

stat_schema = "stat"
public_schema = "public"
geo_schema = "geo"

geometry_column = "geometry"
geom_column = "geom"


# ALL DATA FOR THE STATS
layersData = {
    HEAT_DENSITY_TOT: {
        "tablename": HEAT_DENSITY_TOT,
        "from_indicator_name": stat + HEAT_DENSITY_TOT,
        "where": "",
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "crs": "3035",
        "geo_column": geometry_column,
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": True,
        "indicators": [
            {
                "table_column": "sum",
                "unit": "MWh",
                "indicator_id": "consumption",
                "factor": 0.00001,
            },
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "min", "unit": "MWh", "indicator_id": "consumption_min"},
            {"table_column": "max", "unit": "MWh", "indicator_id": "consumption_max"},
            {"table_column": "mean", "unit": "MWh/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "consumption",
                "reference_tablename_indicator_id_1": HEAT_DENSITY_TOT,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "MWh/person",
                "indicator_id": HEAT_DENSITY_TOT + "_per_" + POPULATION_TOT,
            },
        ],
    },
    HEAT_DENSITY_RES: {
        "tablename": HEAT_DENSITY_RES,
        "from_indicator_name": stat + HEAT_DENSITY_RES,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "MWh", "indicator_id": "consumption"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "mean", "unit": "MWh/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "consumption",
                "reference_tablename_indicator_id_1": HEAT_DENSITY_RES,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "MWh/person",
                "indicator_id": HEAT_DENSITY_RES + "_per_" + POPULATION_TOT,
            },
        ],
    },
    HEAT_DENSITY_NON_RES: {
        "tablename": HEAT_DENSITY_NON_RES,
        "from_indicator_name": stat + HEAT_DENSITY_NON_RES,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "MWh", "indicator_id": "consumption"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "mean", "unit": "MWh/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "consumption",
                "reference_tablename_indicator_id_1": HEAT_DENSITY_NON_RES,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "MWh/person",
                "indicator_id": HEAT_DENSITY_NON_RES + "_per_" + POPULATION_TOT,
            },
        ],
    },
    GRASS_FLOOR_AREA_TOT: {
        "tablename": GRASS_FLOOR_AREA_TOT,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + GRASS_FLOOR_AREA_TOT,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "m2", "indicator_id": "total"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "mean", "unit": "m2/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "total",
                "reference_tablename_indicator_id_1": GRASS_FLOOR_AREA_TOT,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "m2/person",
                "indicator_id": GRASS_FLOOR_AREA_TOT + "_per_" + POPULATION_TOT,
            },
        ],
    },
    GRASS_FLOOR_AREA_RES: {
        "tablename": GRASS_FLOOR_AREA_RES,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + GRASS_FLOOR_AREA_RES,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "m2", "indicator_id": "total"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "mean", "unit": "m2/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "total",
                "reference_tablename_indicator_id_1": GRASS_FLOOR_AREA_RES,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "m2/person",
                "indicator_id": GRASS_FLOOR_AREA_RES + "_per_" + POPULATION_TOT,
            },
        ],
    },
    GRASS_FLOOR_AREA_NON_RES: {
        "tablename": GRASS_FLOOR_AREA_NON_RES,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + GRASS_FLOOR_AREA_NON_RES,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "m2", "indicator_id": "total"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "mean", "unit": "m2/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "total",
                "reference_tablename_indicator_id_1": GRASS_FLOOR_AREA_NON_RES,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "m2/person",
                "indicator_id": GRASS_FLOOR_AREA_NON_RES + "_per_" + POPULATION_TOT,
            },
        ],
    },
    BUILDING_VOLUMES_TOT: {
        "tablename": BUILDING_VOLUMES_TOT,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + BUILDING_VOLUMES_TOT,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "m3", "indicator_id": "total"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "mean", "unit": "m3/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "total",
                "reference_tablename_indicator_id_1": BUILDING_VOLUMES_TOT,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "m3/person",
                "indicator_id": BUILDING_VOLUMES_TOT + "_per_" + POPULATION_TOT,
            },
        ],
    },
    BUILDING_VOLUMES_RES: {
        "tablename": BUILDING_VOLUMES_RES,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + BUILDING_VOLUMES_RES,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "m3", "indicator_id": "total"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "mean", "unit": "m3/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "total",
                "reference_tablename_indicator_id_1": BUILDING_VOLUMES_RES,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "m3/person",
                "indicator_id": BUILDING_VOLUMES_RES + "_per_" + POPULATION_TOT,
            },
        ],
    },
    BUILDING_VOLUMES_NON_RES: {
        "tablename": BUILDING_VOLUMES_NON_RES,
        "from_indicator_name": stat + BUILDING_VOLUMES_NON_RES,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "m3", "indicator_id": "total"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {"table_column": "mean", "unit": "m3/ha", "indicator_id": "density"},
            {
                "reference_indicator_id_1": "total",
                "reference_tablename_indicator_id_1": BUILDING_VOLUMES_NON_RES,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "m3/person",
                "indicator_id": BUILDING_VOLUMES_NON_RES + "_per_" + POPULATION_TOT,
            },
        ],
    },
    INDUSTRIAL_SITES_EMISSIONS: {
        "tablename": INDUSTRIAL_SITES_EMISSIONS,
        "from_indicator_name": stat + INDUSTRIAL_SITES_EMISSIONS,
        "schema_scalelvl": public_schema,
        "schema_hectare": public_schema,
        "geo_column": geom_column,
        "crs": "4326",
        "table_type": vector_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": False,
        "indicators": [
            {
                "table_column": "emissions_ets_2014",
                "unit": "Tonnes/year",
                "indicator_id": "value",
            },
        ],
    },
    INDUSTRIAL_SITES_EXCESS_HEAT: {
        "tablename": INDUSTRIAL_SITES_EXCESS_HEAT,
        "from_indicator_name": stat + INDUSTRIAL_SITES_EXCESS_HEAT,
        "schema_scalelvl": public_schema,
        "schema_hectare": public_schema,
        "geo_column": geom_column,
        "crs": "4326",
        "table_type": vector_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": False,
        "indicators": [
            {
                "table_column": "excess_heat_100_200c",
                "unit": "GWh/year",
                "indicator_id": "value1",
            },
            {
                "table_column": "excess_heat_200_500c",
                "unit": "GWh/year",
                "indicator_id": "value2",
            },
            {
                "table_column": "excess_heat_500c",
                "unit": "GWh/year",
                "indicator_id": "value3",
            },
            {
                "table_column": "excess_heat_total",
                "unit": "GWh/year",
                "indicator_id": "total",
            },
        ],
    },
    POPULATION_TOT: {
        "tablename": POPULATION_TOT,
        "from_indicator_name": stat + POPULATION_TOT,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "geo_column": geometry_column,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "sum", "unit": "person", "indicator_id": "population"},
            {"table_column": "count", "unit": "cells", "indicator_id": "count_cell"},
            {
                "reference_indicator_id_1": "population",
                "reference_tablename_indicator_id_1": POPULATION_TOT,
                "operator": "/",
                "reference_indicator_id_2": "count_cell",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "person/ha",
                "indicator_id": "density",
            },
        ],
    },
    WWTP: {
        "tablename": WWTP,
        "from_indicator_name": stat + WWTP,
        "schema_scalelvl": geo_schema,
        "schema_hectare": geo_schema,
        "geo_column": geom_column,
        "crs": "3035",
        "table_type": vector_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": False,
        "indicators": [
            {"table_column": "capacity", "unit": "kW", "indicator_id": "power"},
            {
                "table_column": "power",
                "unit": "Person equivalent",
                "indicator_id": "capacity",
            },
        ],
    },
    WWTP_CAPACITY: {
        "tablename": WWTP_CAPACITY,
        "schema_scalelvl": public_schema,
        "schema_hectare": public_schema,
        "crs": "3035",
        "table_type": vector_type,
        "from_indicator_name": stat + WWTP_CAPACITY,
        "geo_column": geometry_column,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": False,
        "indicators": [
            {
                "table_column": "capacity",
                "unit": "Person equivalent",
                "indicator_id": "capacity",
            },
        ],
    },
    WWTP_POWER: {
        "tablename": WWTP_POWER,
        "schema_scalelvl": public_schema,
        "schema_hectare": public_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": vector_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + WWTP_POWER,
        "data_aggregated": False,
        "indicators": [
            {"table_column": "power", "unit": "kW", "indicator_id": "power"},
        ],
    },
    LIVESTOCK_EFFLUENTS: {
        "tablename": LIVESTOCK_EFFLUENTS,
        "from_indicator_name": stat + LIVESTOCK_EFFLUENTS,
        "where": "livestock_effluents",
        "schema_scalelvl": geo_schema,
        "schema_hectare": geo_schema,
        "crs": "3035",
        "geo_column": geometry_column,
        "table_type": vector_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "scalelvl_column": "code",
        "data_aggregated": True,
        "indicators": [
            {"table_column": "value", "unit": "PJ", "indicator_id": "NUTS_potential"},
            {
                "reference_indicator_id_1": "NUTS_potential",
                "reference_tablename_indicator_id_1": LIVESTOCK_EFFLUENTS,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "PJ/person",
                "indicator_id": "Livestock_effl_pp",
            },
        ],
    },
    AGRICULTURAL_RESIDUES: {
        "tablename": AGRICULTURAL_RESIDUES,
        "from_indicator_name": stat + AGRICULTURAL_RESIDUES,
        "where": "livestock_effluents",
        "schema_scalelvl": geo_schema,
        "schema_hectare": geo_schema,
        "crs": "3035",
        "geo_column": geometry_column,
        "table_type": vector_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "scalelvl_column": "code",
        "data_aggregated": True,
        "indicators": [
            {"table_column": "value", "unit": "PJ", "indicator_id": "NUTS_potential"},
            {
                "reference_indicator_id_1": "NUTS_potential",
                "reference_tablename_indicator_id_1": AGRICULTURAL_RESIDUES,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "PJ/person",
                "indicator_id": "agriculture_pp",
            },
        ],
    },
    POTENTIAL_FOREST: {
        "tablename": POTENTIAL_FOREST,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + POTENTIAL_FOREST,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "mean", "unit": "PJ/ha", "indicator_id": "average"},
            {"table_column": "sum", "unit": "PJ/ha x cells", "indicator_id": "value"},
            {"table_column": "count", "unit": "cells", "indicator_id": "cells"},
        ],
    },
    MUNICIPAL_SOLID_WASTE: {
        "tablename": MUNICIPAL_SOLID_WASTE,
        "from_indicator_name": stat + MUNICIPAL_SOLID_WASTE,
        "where": "",
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "crs": "3035",
        "geo_column": geometry_column,
        "table_type": vector_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "scalelvl_column": "code",
        "data_aggregated": True,
        "indicators": [
            {"table_column": "value", "unit": "PJ", "indicator_id": "val"},
            {
                "reference_indicator_id_1": "val",
                "reference_tablename_indicator_id_1": MUNICIPAL_SOLID_WASTE,
                "operator": "/",
                "reference_indicator_id_2": "population",
                "reference_tablename_indicator_id_2": POPULATION_TOT,
                "unit": "PJ/person",
                "indicator_id": "agriculture_pp",
            },
        ],
    },
    GEOTHERMAL_POTENTIAL_HEAT_COND: {
        "tablename": GEOTHERMAL_POTENTIAL_HEAT_COND,
        "from_indicator_name": stat + GEOTHERMAL_POTENTIAL_HEAT_COND,
        "schema_scalelvl": geo_schema,
        "schema_hectare": geo_schema,
        "geo_column": geom_column,
        "crs": "4326",
        "table_type": vector_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": False,
        "indicators": [
            {"table_column": "sum", "unit": "W/mK", "indicator_id": "value"}
        ],
    },
    SOLAR_POTENTIAL: {
        "tablename": SOLAR_POTENTIAL,
        "from_indicator_name": stat + SOLAR_POTENTIAL,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": True,
        "indicators": [
            {"table_column": "mean", "unit": "kWh/m^2", "indicator_id": "average"},
            {"table_column": "min", "unit": "kWh/m^2", "indicator_id": "min"},
            {"table_column": "max", "unit": "kWh/m^2", "indicator_id": "max"},
            {"table_column": "count", "unit": "cells", "indicator_id": "cells"},
        ],
    },
    WIND_POTENTIAL: {
        "tablename": WIND_POTENTIAL,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + WIND_POTENTIAL,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "mean", "unit": "m/s", "indicator_id": "average"},
            {"table_column": "max", "unit": "m/s", "indicator_id": "max"},
            {"table_column": "min", "unit": "m/s", "indicator_id": "min"},
            {"table_column": "count", "unit": "cells", "indicator_id": "cells"},
        ],
    },
    HDD_CUR: {
        "tablename": HDD_CUR,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + HDD_CUR,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "mean", "unit": "Kd", "indicator_id": "average"},
            {"table_column": "max", "unit": "Kd", "indicator_id": "max"},
            {"table_column": "min", "unit": "Kd", "indicator_id": "min"},
            {"table_column": "count", "unit": "cells", "indicator_id": "cells"},
        ],
    },
    CDD_CUR: {
        "tablename": CDD_CUR,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + CDD_CUR,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "mean", "unit": "Kd", "indicator_id": "average"},
            {"table_column": "max", "unit": "Kd", "indicator_id": "max"},
            {"table_column": "min", "unit": "Kd", "indicator_id": "min"},
            {"table_column": "count", "unit": "cells", "indicator_id": "cells"},
        ],
    },
    LAND_SURFACE_TEMP: {
        "tablename": LAND_SURFACE_TEMP,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + LAND_SURFACE_TEMP,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "count", "unit": "cells", "indicator_id": "cells"},
            {"table_column": "min", "unit": "degree C", "indicator_id": "minimum"},
            {"table_column": "max", "unit": "degree C", "indicator_id": "maximum"},
            {"table_column": "mean", "unit": "degree C", "indicator_id": "average"},
        ],
    },
    SOLAR_RADIATION: {
        "tablename": SOLAR_RADIATION,
        "from_indicator_name": stat + SOLAR_RADIATION,
        "where": "",
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "crs": "3035",
        "geo_column": geometry_column,
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": True,
        "indicators": [
            {"table_column": "mean", "unit": "kWh/m^2", "indicator_id": "average"},
            {"table_column": "min", "unit": "kWh/m^2", "indicator_id": "min"},
            {"table_column": "max", "unit": "kWh/m^2", "indicator_id": "max"},
            {"table_column": "count", "unit": "cells", "indicator_id": "cells"},
        ],
    },
    WIND_SPEED: {
        "tablename": WIND_SPEED,
        "schema_scalelvl": stat_schema,
        "schema_hectare": geo_schema,
        "geo_column": geometry_column,
        "crs": "3035",
        "table_type": raster_type,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "from_indicator_name": stat + WIND_SPEED,
        "data_aggregated": True,
        "indicators": [
            {"table_column": "mean", "unit": "m/s", "indicator_id": "average"},
            {"table_column": "max", "unit": "m/s", "indicator_id": "max"},
            {"table_column": "min", "unit": "m/s", "indicator_id": "min"},
            {"table_column": "count", "unit": "cells", "indicator_id": "cells"},
        ],
    },
    ELECTRICITY_CO2_EMISSION_FACTOR: {
        "tablename": ELECTRICITY_CO2_EMISSION_FACTOR,
        "schema_scalelvl": public_schema,
        "schema_hectare": public_schema,
        "geo_column": geom_column,
        "crs": "4258",
        "table_type": vector_type,
        "level_of_data": "NUTS 0",
        "from_indicator_name": stat + ELECTRICITY_CO2_EMISSION_FACTOR,
        "data_lvl": [nuts0, nuts1, nuts2, nuts3, lau2, hectare_name],
        "data_aggregated": True,
        "indicators": [
            {"table_column": "value", "unit": "kg/MWh", "indicator_id": "density"}
        ],
    },
}
