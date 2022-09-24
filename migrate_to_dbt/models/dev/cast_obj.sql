with source_data_cast as (
    select *
    from {{ source('traffic_data_view', 'traffic_data') }}
),
final as (
    select id,
        track_id,
        " type",
        cast(" traveled_d" as float) as " traveled_d",
        " avg_speed",
        " lat",
        " lon",
        " speed",
        " lon_acc",
        " lat_acc"
    from source_data_cast
)
SELECT *
FROM final