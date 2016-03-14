<?php

# Set headers for event stream.
header( 'Content-Type: text/event-stream' );
header( 'Cache-Control: no-cache' );

# Open original JSON file.
$json = file_get_contents( '../logs/data.json' );

# Prepare content for event stream.
echo 'data: ' . $json . "\n\n";

# Flush system output buffer.
flush();