<?php
include "includes/navbar.php";
?>
<div class="row main">
<div class="col s12 m12 l12">
<div class="card-panel">
<ul class="collection with-header">
<li class="collection-header teal">
<h5 class="white-text">Recent Posts</h5>
<span id="message"></span>
</li>
<?php
$sql="select * from posts order by id desc";
$res=mysqli_query($conn,$sql);
if(mysqli_num_rows($res)>0)
{
while($row=mysqli_fetch_assoc($res))
{
?>
<li class="collection-item">
<a href=""><?php echo $row['title']?></a>
<br>
<span><a href="edit.php?id=<?php echo $row['id']; ?>"><i class="material-icons tiny">edit</i> Edit</a>| <a href="" id="<?php echo $row['id']; ?>" class="delete"><i class="material-icons tiny red-text">clear</i> Delete</a> | <a href=""><i class="material-icons tiny green-text">share</i> Share</a></span>
</li>

<?php
}
}
else
{
  echo "<div class='chip red white-text'>No Post in Database , write a New One by clicking circular button Below</div>";
}
?>
</ul>
</div>
</div>
</div>
<div class="fixed-action-btn">
<a href="write.php" class="btn-floating btn btn-large white-text pulse"><i class="material-icons">edit</i></a>
</div>
<div class="fixed-action-btn">
<a href="write.php" class="btn-floating btn btn-large white-text pulse"><i class="material-icons">edit</i></a>
</div>
<script>
<script>
const del=document.querySelectorAll(".delete");
del.forEach(function(item,index)
{
item.addEventListener("click",deleteNow)
})

function deleteNow(e)
{
  e.preventDefault();
  if(confirm("Do you really Want to Delete"))
  {
const xhr=new XMLHttpRequest();
xhr.open("GET","delete.php?id="+Number(e.target.id),true)
xhr.onload=function()
{
  const messg=xhr.responseText;
  const message=document.getElementById("message")
  message.innerHTML=messg;
}
xhr.send()
  }

}
</script>
<?php
include "includes/footer.php";

?>