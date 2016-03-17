<!doctype html>
<html>
<head>
  <meta charset="utf-8">
</head>
</body>
<?php
  if($_GET["key"] == "少女祈祷中"){
    $sqlObj = new mysqli("localhost","root","1a2B3c4E?///","touhou");
    $stmt = $sqlObj->prepare("SELECT * FROM online_application_log ORDER BY id DESC");
    $stmt->execute();
    $stmt->store_result();
    $stmt->bind_result($id,$name,$referrer,$skills,$resume,$contact,$tojoin);
?>
<style>
  table {
    width:100%;
  }
  table tr td {
    padding:10px;
  }
</style>
    <table border="1">
      <tr>
        <td>ID</td>
        <td>名字</td>
        <td>推荐人</td>
        <td>擅长的区域</td>
        <td>简介</td>
        <td>联系方式</td>
        <td>加入的群</td>
      </tr>
<?php while($stmt->fetch()){ ?>
      <tr>
        <td><?php echo $id; ?></td>
        <td><?php echo $name; ?></td>
        <td><?php echo $referrer; ?></td>
        <td><?php echo $skills; ?></td>
        <td><?php echo $resume; ?></td>
        <td><?php echo $contact; ?></td>
        <td><?php echo $tojoin; ?></td>
      </tr>
<?php } ?>
    </table>
<?php
  $stmt->close();
  }
?>
</body>
</html>
