<?php
    include("database.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Me</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="validation.js"></script>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="homepage.html">Home</a></li>
                <li><a href="educational_info.html">Educational Info</a></li>
                <li><a href="work_info.html">Work Info</a></li>
                <li><a href="contact.html">Contact Me</a></li>
                <li><a href="admin.php">Admin</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Contact Me</h1>
        <form action="submit_contact.php" method="POST" onsubmit="return validateForm()">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject" required>
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            
            <button type="submit">Submit</button>
        </form>
    </main>
    <footer>
        <p>&copy; 2025 My Website</p>
    </footer>
</body>
</html>

<?php
     if($_SERVER["REQUEST_METHOD"]=="POST"){
        $name = filter_input(INPUT_POST,"name",FILTER_SANITIZE_SPECIAL_CHARS);
        $email = filter_input(INPUT_POST,"email",FILTER_SANITIZE_SPECIAL_CHARS);
        $subject = filter_input(INPUT_POST,"subject",FILTER_SANITIZE_SPECIAL_CHARS);
        $message = filter_input(INPUT_POST,"message",FILTER_SANITIZE_SPECIAL_CHARS);
        if(empty($name)){
           echo "Please enter your name";
       }
       elseif(empty($email)){
           echo "Please enter your email";
       }
         
       elseif(empty($subject)){
             echo "Please enter a subject";
        }

        elseif(empty($message)){
             echo "Please write a message";
        }

      else {
          // $hash = password_hash($password,PASSWORD_DEFAULT);
           $sql = "INSERT INTO submissions (name,email,subject,message)
               VALUES('$name','$email','$subject','$message')";
       
       mysqli_query($conn,$sql);
       echo "You're message has been sent";
       }
       
      }
      
    mysqli_close($conn);
?>
