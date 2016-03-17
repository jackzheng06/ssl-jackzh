<!doctype html>
<html>
  <head>
    <title>感谢您的申请！</title>
    <link href="less/main.less?v=001" type="text/less" rel="stylesheet" />
    <script src="https://use.typekit.net/hkm2lpt.js"></script>
    <script>try{Typekit.load({ async: true });}catch(e){}</script>
    <meta charset="utf-8">
    <script src="https://ssl.jackzh.com/file/js/less-js/less.min.js"></script>
    <script src="https://ssl.jackzh.com/file/js/jquery/jquery-1.11.3.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>

  <body>
    <?php if($_POST["name"] == "" || $_POST["contact"] == "" || $_POST["skills"] == "" || $_POST["resume"] == ""){ ?>
      <h1>Oops, 您填写的信息不完整</h1>
      <p>
        请返回检查之后再填写
      </p>
    <?php } else { ?>
      <?php
        $name = strip_tags($_POST["name"]);
        $contact = strip_tags($_POST["contact"]);
        $skills = strip_tags($_POST["skills"]);
        $resume = strip_tags($_POST["resume"]);
        $resume = str_replace("\n","<br>",$resume);
        $referrer = strip_tags($_POST["referrer"]);
        $tojoin = strip_tags($_POST["tojoin"]);
        $to = "junzheng@exchange.niyume.com, 578903564@qq.com";
        $subject = "$name - 东方脑洞乡申请";
        $message = "
        <html>
        <head>
        <title>$name - 东方脑洞乡申请</title>
        </head>
        <body>
        <h1>$name - 东方脑洞乡申请</h1>
        <p>名字 － $name</p>
        <p>推荐人 － $referrer</p>
        <p>擅长的领域 － $skills</p>
        <p>个人介绍 － $resume</p>
        <p>联系方式 － $contact</p>
        <p>希望加入 － $tojoin</p>
        </body>
        </html>
        ";

        // Always set content-type when sending HTML email
        $headers = "MIME-Version: 1.0" . "\r\n";
        $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

        // More headers
        $headers .= 'From: <admin@jackzh.com>' . "\r\n";

        mail($to,$subject,$message,$headers);

        $sqlObj = new mysqli("localhost","root","1a2B3c4E?///","touhou");
        $stmt = $sqlObj->prepare("INSERT INTO online_application_log (name,referrer,skills,resume,contact,tojoin) VALUES (?,?,?,?,?,?)");
        $stmt->bind_param("ssssss",$name,$referrer,$skills,$resume,$contact,$tojoin);
        $stmt->execute();
        $stmt->close();
      ?>
      <h1>感谢您对我们的支持</h1>
      <p>
        通常来说，您提交的表单将在48小时内收到回复，如未收到邮件，请检查垃圾箱
      </p>
    <?php } ?>
  </body>
</html>
<script type="text/javascript">
  function ckFm(){
    if($("#username-textbox").val() == "") {
      alert("请填写您的名字！");
    } else if ($("#skills-textbox").val() == "") {
      alert("请填写您的擅长领域！");
    } else if ($("#resume-textbox").val() == "") {
      alert("请写一个简短的个人介绍");
    } else if ($("#contact-textbox").val() == "") {
      alert("请填写一个联系方式");
    }
  }

  console.log("没事干看什么源码！不要想着做坏事，快快回去填表");
</script>
