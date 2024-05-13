<?php 

include "library/db.php";
include_once "classes/worksheets_class.php";

?>

<!DOCTYPE html>
<html lang="en">

    <?php 
    include_once 'components/header.php';
    ?>

    <?php 
    //include "partials/menu.php"; I don't know what this is?
    ?> 

    <body>

    <?php 
    include_once 'components/navbar.php';
    include_once 'components/carousel.php';
    ?>

<?php 

$worksheets = new worksheets();
$worksheets->display_3_random_worksheets();

?>
<button onclick="openPopup()">Open Popup</button>

<div id="popup" class="popup">
    <h2>Popup Content</h2>
    <p>This is a popup!</p>
    <button onclick="closePopup()">Close</button>
</div>

<script>
    function openPopup() {
        document.getElementById("popup").style.display = "block";
    }

    function closePopup() {
        document.getElementById("popup").style.display = "none";
    }
</script>

<?php
include "components/footer.php";
?>

    </body>
</html>