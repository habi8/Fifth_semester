<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$servername = "localhost";
$username = "root"; // Change if necessary
$password = ""; // Change if necessary
$dbname = "contact_form"; // Change if necessary

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    echo "<pre>";
    print_r($_POST);
    echo "</pre>";

    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $subject = trim($_POST['subject']);
    $message = trim($_POST['message']);

    // Validate inputs
    if (!empty($name) && !empty($email) && !empty($subject) && !empty($message)) {
        // Sanitize inputs
        $name = mysqli_real_escape_string($conn, $name);
        $email = mysqli_real_escape_string($conn, $email);
        $subject = mysqli_real_escape_string($conn, $subject);
        $message = mysqli_real_escape_string($conn, $message);

        // Insert into database
        $sql = "INSERT INTO submissions (name, email, subject, message) VALUES ('$name', '$email', '$subject', '$message')";

        if (mysqli_query($conn, $sql)) {
            echo "Thank you for contacting us! We will get back to you soon.";
            
        } else {
            echo "Error: " . mysqli_error($conn);
        }
    } else {
        echo "All fields are required!";
    }
}

// Close connection
mysqli_close($conn);
?>
