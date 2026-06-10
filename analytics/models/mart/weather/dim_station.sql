{{ config(materialized='table') }}

SELECT DISTINCT
    station_id,
    "name",
    latitude,
    longitude,
    elevation
FROM {{ ref('stg_weather') }}