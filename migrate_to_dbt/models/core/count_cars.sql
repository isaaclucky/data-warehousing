with source_data as (
    select *
    from {{ref('cast_obj')}}
),
final as (
    select count(" type") as cars_type_count
    from source_data
    group by " type"
)
SELECT *
FROM final