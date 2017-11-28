#coding=utf-8

UPLOADAPKHTML = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Android性能测试-上传apk文件 type="file"</title>
<link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
<script src="http://libs.baidu.com/jquery/1.10.2/jquery.min.js"></script>
<style type="text/css">
body{
font-size:14px;
align-text:center;
}
input{ 
vertical-align:middle;
margin:0;
padding:0
}
.file-box{
position:relative;
width:340px;
margin:0px auto;
}
.txt{
height:30px;
border:1px solid #cdcdcd;
width:180px;
}
.btn{
background-color:#FFF;
border:1px solid #CDCDCD;
height:30px;
width:73px;
}
.file{
position:absolute;
top:0;
right:80px;
height:24px;
filter:alpha(opacity:0);
opacity: 0;
width:260px
}
</style>

</head>
<body>
<nav class="navbar navbar-default">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="">Android性能测试</a>
        </div>

        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li><a href="/meminfo">内存监控</a></li>
                <li><a href="/cupinfo">CUP监控</a></li>
                <li><a href="/wifinfo">流量监控</a></li>
                <li><a href="/wifinfo">GFX监控</a></li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>
<div class="file-box">
<form action="/upload" method="post" enctype="multipart/form-data">
<input type='text' name='textfield' id='textfield' class='txt' />  
<input type='button' class='btn' value='浏览...' />
<input type="file" name="fileField" class="file" id="fileField" size="28" onchange="document.getElementById('textfield').value=this.value" /> 
<input type="submit" name="submit" class="btn btn-default" value="上传文件" onclick=""/>
</form>
<P>
<div class="panel panel-default">
  <div class="panel-heading">使用说明：</div>
  <div class="panel-body">
    1，Panel content Panel content Panel content 
    2，Panel content Panel content Panel content
    3，Panel content Panel content Panel content
    4，Panel content Panel content Panel content
    5，Panel content Panel content Panel content
  </div>
</div>
</div>
</body>
</html>
"""

UPLOADAPKHTML2 = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Android性能测试中心</title>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/1.10.2/jquery.min.js"></script>
    <script src="static/js/dark.js"></script>
    <script src="static/js/charts.js"></script>
    <script src="static/js/echarts.common.min.js"></script>
</head>
<body>
<nav class="navbar navbar-default">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <a class="navbar-brand" href="http://127.0.0.1/index.html">Android性能测试中心</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li><a href="/monkey">应用遍历</a></li>
                <li><a href="/apklist">应用列表</a></li>
                <li><a href="/memhtml">内存监控</a></li>
                <li><a href="/cpuhtml">CPU监控</a></li>
                <li><a href="/wifinfo">流量监控</a></li>
                <li><a href="/wifinfo">GFX监控</a></li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>

<div class="panel panel-info">
        <div class="panel-heading">
            <h2 class="panel-title">setup 1:</h2>
        </div>
        <div class="panel-body">

            <p>
        上传测试apk：
        <form action="/upload" method="post" enctype="multipart/form-data">
<input type="file" name="fileField" class="file" id="fileField" size="38" onchange="document.getElementById('textfield').value=this.value" />
<input type="submit" name="submit" class="btn btn-default" value="上传文件" onclick=""/>
</form></p>
            <p>如果想知道设备所有应用包名，请点击右侧按钮
                <button type="button" class="btn btn-default" id="get_third_packagename">获取设备应用信息</button>
            </p>
            <p>如果想知道当前安装应用包名，请点击右侧按钮
            <button type="button" class="btn btn-default" id="get_cur_packagename">获取当前应用包名</button>
            <div id="pkinfo"><span id="package_name"></span> <span id="activity_name"></span></div>
            </p>
        </div>
</div>
<!--第三方包列表的容器-->
    <div id="third_list_container">
        <div class="panel-heading" id="pk_list_header"></div>
        <div class="panel-body">
            <ul class="list-group" id="pk_list">
            </ul>
        </div>
    </div>
<!-- ECharts容器 -->
<div class="container">
    <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-8">
            <div id="main" style="width: 100%;height: 500px;">
            </div>
        </div>
        <div class="col-md-3"></div>
    </div>
</div>
</body>
</html>
"""