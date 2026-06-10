{{ config(materialized='table') }}

{% set min_date_query %}
    SELECT MIN("date") FROM {{ ref('stg_weather') }}
{% endset %}

{% set max_date_query %}
    SELECT MAX("date") + INTERVAL 1 DAY FROM {{ ref('stg_weather') }}
{% endset %}

WITH dates AS (
    {{ dbt_utils.date_spine(
        datepart="day",
        start_date="(" ~ min_date_query ~ ")",
        end_date="(" ~ max_date_query ~ ")"
    ) }}
)

SELECT * FROM dates