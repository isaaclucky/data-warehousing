with source_data as (
    select *
    from {{ref('cast_obj')}}
),
final as (
    select " type",
        AVG(" avg_speed")
    from source_data
    group by " type"
)
SELECT *
FROM final