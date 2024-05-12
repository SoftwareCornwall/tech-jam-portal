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
                '<a href="worksheets.php?id=' . $id . '">
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

    
}

