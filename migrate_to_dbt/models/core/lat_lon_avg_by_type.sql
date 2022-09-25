
with source_data as (
    select *
    from {{ref('cast_obj')}}
),
final as (
    select " type",
       SUM(" avg_speed"),AVG(" traveled_d")
    from source_data
    group by " type"
)
SELECT *
FROM final