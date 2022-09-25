with source_data_cast as (
    select *
    from {{ source('traffic_data_view', 'traffic_data') }}
),
final as (
    select id,
        track_id,
        " type",
        cast(" traveled_d" as float) as " traveled_d",
        cast(" avg_speed" as float) as " avg_speed",
        cast(" lat" as float) as " lat",
        cast(" lon" as float) as " lon",
        cast(" speed" as float) as " speed",
        cast(" lon_acc" as float) as " lon_acc",
        cast(" lat_acc" as float) as " lat_acc"
    from source_data_cast
)
SELECT *
FROM final