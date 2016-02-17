<?php

# Set headers for event stream
header( 'Content-Type: text/event-stream' );
header( 'Cache-Control: no-cache' );

# Open JSON file
$json = file_get_contents( '../logs/data.json' );

# Decode JSON and re-parse for JSON Server-Sent Events
$json_array = json_decode( $json, true );
foreach ( $json_array as $key => $value ) {
    echo "$key: $value\n\n";
}

flush();