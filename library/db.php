<?php
function connect() {
    $servername = "localhost";
    $username = "bobfrwas";
    $password = "";

    $conn = new mysqli($servername, $username, $password, "worksheets");

    if ( $conn ->connect_error ) {
        die("Connection failed: " . $conn->connect_error);
    }

    return $conn;
}


?> 