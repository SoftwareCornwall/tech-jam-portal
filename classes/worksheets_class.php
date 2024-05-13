<?php

include_once "library/db.php";
include_once "components/header.php";



class Worksheets {
    function display_all_worksheets() {
        $conn = connect();
        $sql = "SELECT * FROM worksheets";
        $result = $conn->query($sql);
?>

<div class="container text-center">
    <h1>Popular Worksheets!</h1>
    <div class="row d-flex align-items-stretch">
        <?php while ($row = $result->fetch_array(MYSQLI_ASSOC)) { ?>
            <div class="col-4 mb-4">
                <a href="worksheets/Microbit/Microbit_Gravity/microbit_zero_g.pdf">
                    <div class="image_desc h-100 p-3">
                        <img src="images/tech-jam-website-logo-1280x1280.png" class="images_worksheet">
                        <h2><?php echo $row["title"]; ?></h2>
                        <p>Difficulty - <?php echo $row["difficulty"]; ?></p>
                        <p><b>Language - <?php echo $row["language"]; ?></b></p>
                        <p><?php echo $row["description"]; ?></p>
                    </div>
                </a>
            </div>
        <?php } ?>
    </div>
</div>

<?php
        $result->free_result();
        $conn->close();
    }

    function display_3_random_worksheets() {
        $conn = connect();
        $sql = "SELECT DISTINCT * FROM worksheets ORDER BY RAND() LIMIT 3;";
        $result = $conn->query($sql);
?>

<div class="container text-center">
    <h1>Popular Worksheets!</h1>
    <div class="row d-flex align-items-stretch">
        <?php while ($row = $result->fetch_array(MYSQLI_ASSOC)) { ?>
            <div class="col-4 mb-4">
                <?php $id = $row["id"] ?>
                <a href="worksheets/Microbit/Microbit_Gravity/microbit_zero_g.pdf">
                    <div class="image_desc h-100 p-3">
                        <img src="images/tech-jam-website-logo-1280x1280.png" class="images_worksheet">
                        <h2><?php echo $row["title"]; ?></h2>
                        <p>Difficulty - <?php echo $row["difficulty"]; ?></p>
                        <p><?php echo $row["description"]; ?></p>
                    </div>
                </a>
            </div>
        <?php } ?>
    </div>
</div>

<?php
        $result->free_result();
        $conn->close();
    }

    function display_language_worksheets($language) {
        $conn = connect();
        $sql = "SELECT * FROM worksheets WHERE language = '" . $language . "'";
        $result = $conn->query($sql);
?>

<div class="container text-center">
    <div class="row d-flex align-items-stretch">
        <?php while ($row = $result->fetch_array(MYSQLI_ASSOC)) { ?>
            <div class="col-4 mb-4">
                <?php $file_path = $row["file_path"] ?>
                '<a href="' . $file_path . '">
                    <div class="image_desc h-100 p-3">
                        <img src="images/tech-jam-website-logo-1280x1280.png" class="images_worksheet">
                        <h2><?php echo $row["title"]; ?></h2>
                        <p>Difficulty - <?php echo $row["difficulty"]; ?></p>
                        <p><b>Language - <?php echo $row["language"]; ?></b></p>
                        <p><?php echo $row["description"]; ?></p>
                    </div>
                </a>
            </div>
        <?php } ?>
        <div class="py-5">
        <?php
            if ($result->num_rows === 0) {
                echo "No one here but Garry :)";
                ?>
                <img src="images/garry_image.jpg">
                <?php
            }
            ?>
            </div>
    </div>
</div>

<?php
        $result->free_result();
        $conn->close();
    }
    
}

