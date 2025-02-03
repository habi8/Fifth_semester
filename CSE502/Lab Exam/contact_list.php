<?php
session_start();
if (!isset($_SESSION['admin_logged_in']) || $_SESSION['admin_logged_in'] !== true) {
    header("Location: admin.php");
    exit;
}

$servername = "localhost";
$username = "root"; // Change this as needed
$password = "";
$dbname = "LabFinal"; // Your database name

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT id, name, email, subject, message, submitted_at FROM submissions";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Messages</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h2>Contact Messages</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Subject</th>
            <th>Message</th>
            <th>Date</th>
        </tr>

        <?php while ($row = $result->fetch_assoc()): ?>
        <tr>
            <td><?php echo $row["id"]; ?></td>
            <td><?php echo $row["name"]; ?></td>
            <td><?php echo $row["email"]; ?></td>
            <td><?php echo $row["subject"]; ?></td>
            <td><?php echo $row["message"]; ?></td>
            <td><?php echo $row["submitted_at"]; ?></td>
        </tr>
        <?php endwhile; ?>
    </table>

    <br>
    <a href="homepage.html">Logout</a>
</body>
</html>

<?php
$conn->close();
?>
