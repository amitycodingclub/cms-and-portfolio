<?php
include "includes/navbar.php";
?>

<div class="main">
<div class="card-panel">
<h5 class="center">Settings</h5>
<?php
if(isset($_SESSION['message']))
{
echo $_SESSION['message'];
unset($_SESSION['message']);
}
?>
<form action="setting.php" method="POST">
<input type="password" name="password" placeholder="Change Password">
<input type="password" name="con_password" placeholder="Confirm Password">
<div class="center">
<input type="submit" name="update" value="Change Password" class="btn">
</div>
</form>
</div>
</div>