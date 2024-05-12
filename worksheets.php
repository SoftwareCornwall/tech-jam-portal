<?php 

include_once "content/header.html";
include "classes/worksheets_class.php";
?>
<body>

<?php include_once "components/navbar.php";
?>
<div class="py-5"><?php
$language = $_GET['language'];
$worksheets = new worksheets();
$worksheets->display_language_worksheets($language);
?>
</div>

<?php 
include "components/footer.php";
