with source_data as (
    select *
    from {{ref('cast_obj')}}
),
final as (
    select count(*) as total_count
    from source_data
)
SELECT *
FROM final