<?php
    $servername = "localhost";
    $username = "root"; // Change this as needed
    $password = "";
    $dbname = "contact_form"; // Your database name
    $conn = "";

    try{
        $conn = mysqli_connect($db_server,$db_username,$db_password,$db_name);

    }

    catch(mysqli_sql_exception){
        echo "Could not connect! <br>";
    }
?>