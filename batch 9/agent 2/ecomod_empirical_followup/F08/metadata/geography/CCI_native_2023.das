Attributes {
    lon {
        String long_name "WGS84 longitude coordinate";
        String standard_name "longitude";
        String units "degrees_east";
        String bounds "lon_bnds";
        Float64 valid_min -180.0;
        Float64 valid_max 180.0;
        Int32 _ChunkSizes 405000;
    }
    lat {
        String long_name "WGS84 latitude coordinate";
        Float64 valid_max 80.0;
        String standard_name "latitude";
        String bounds "lat_bnds";
        String units "degrees_north";
        Float64 valid_min -60.0;
        Int32 _ChunkSizes 157500;
    }
    time {
        String long_name "single-year period";
        String standard_name "time";
        String bounds "time_bnds";
        String units "days since 1990-01-01";
        Int32 _ChunkSizes 1;
    }
    agb {
        String long_name "Above-ground biomass";
        Float64 valid_max 10000.0;
        Int16 _FillValue -32768;
        String ancillary_variables "agb_se";
        String units "Mg/ha";
        String grid_mapping "crs";
        Float64 valid_min 0.0;
        Int32 _ChunkSizes 1, 11250, 11250;
    }
    agb_sd {
        String long_name "Above-ground biomass standard_deviation";
        String grid_mapping "crs";
        String units "Mg/ha";
        Float64 valid_min 0.0;
        Float64 valid_max 10000.0;
        Int16 _FillValue -32768;
        Int32 _ChunkSizes 1, 11250, 11250;
    }
    crs {
        String long_name "CRS definition";
        Float64 inverse_flattening 298.257223563;
        Float64 false_easting 0.0;
        Float64 false_northing 0.0;
        Float64 semi_major_axis 6378137.0;
        String GeoTransform "-180   0.00088888888888                  0                 80                  0  -0.00088888888888";
        Float64 longitude_of_prime_meridian 0.0;
        String spatial_ref "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0],UNIT[\"degree\",0.0174532925199433],AUTHORITY[\"EPSG\",\"4326\"]]";
        String grid_mapping_name "latitude_longitude";
        DODS {
            Int32 strlen 0;
        }
    }
    lon_bnds {
    }
    lat_bnds {
    }
    time_bnds {
    }
    NC_GLOBAL {
        String title "ESA CCI above-ground biomass product level 4, year 2023";
        String institution "GAMMA Remote Sensing";
        String source "ALOS-1/2 PALSAR-2 FB and WB mosaics, Sentinel-1 GRD, ENVISAT ASAR";
        String history "AGB estimation with BIOMASAR-L,v202509, AGB estimation with BIOMASAR-C,v202509, Merging of AGB estimates,v202509";
        String references "http://cci.esa.int/biomass";
        String tracking_id "1AA9B124-65A9-46A2-88E3-BF7C60E381E7";
        String Conventions "CF-1.7";
        String product_version "7.0";
        String format_version "CCI Data Standards v2.1";
        String summary "This dataset contains a global map of above-ground biomass of the epoch 2023 obtained from L-and C-band spaceborne SAR backscatter, placed onto a regular grid.";
        String keywords "satellite, observation, forest, biomass";
        String id "ESACCI-BIOMASS-L4-AGB-MERGED-100m-2023-fv7.0.nc";
        String naming_authority "ch.gamma-rs";
        String keywords_vocabulary "NASA Global Change Master Directory (GCMD) Science Keywords";
        String cdm_data_type "INT";
        String comment "These data were produced at ESA CCI as part of the ESA Biomass CCI project.";
        String creator_name "GAMMA Remote Sensing";
        String creator_url "www.gamma-rs.ch";
        String creator_email "santoro@gamma-rs.ch";
        String project "Climate Change Initiative - European Space Agency";
        String geospatial_lat_min "-60";
        String geospatial_lat_max "80";
        String geospatial_lon_min "-180";
        String geospatial_lon_max "180";
        String geospatial_vertical_min "0.0";
        String geospatial_vertical_max "0.0";
        String license "ESA CCI Data Policy: free and open access";
        String time_coverage_start "20230101T000000Z";
        String time_coverage_end "20231231T235959Z";
        String time_coverage_duration "P1Y";
        String time_coverage_resolution "P1Y";
        String standard_name_vocabulary "NetCDF Climate and Forecast (CF) Metadata Convention version 67";
        String platform "ALOS-2, Sentinel-1A, Sentinel-1B";
        String sensor "PALSAR-2, SAR-C";
        String spatial_resolution "100 m";
        String key_variables "agb";
        String geospatial_lon_units "degrees_east";
        String geospatial_lat_units "degrees_north";
        String geospatial_lon_resolution "0.00088889";
        String geospatial_lat_resolution "0.00088889";
        String date_created "09-Dec-2025 20:20:33";
        String EPSG "4326";
        String proj4 "+proj=longlat +datum=WGS84 +no_defs";
    }
}
