#coding=utf-8

CUPINFO="""
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Android性能测试-CUP监控 type="file"</title>
<link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
<script src="http://libs.baidu.com/jquery/1.10.2/jquery.min.js"></script>
<script src="static/js/dark.js"></script>
<script src="static/js/charts.js"></script>
<script src="static/js/echarts.common.min.js"></script>
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
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <a class="navbar-brand" href="">Android性能测试</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li><a href="/monkey">浅度遍历</a></li>
                <li><a href="/allinfo">全信息监控</a></li>
                <li><a href="/meminfo">内存监控</a></li>
                <li><a href="/cupinfo">CUP监控</a></li>
                <li><a href="/wifinfo">流量监控</a></li>
                <li><a href="/wifinfo">GFX监控</a></li>
                <li><a href="/wifinfo">GFX监控</a></li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>

<div class="panel panel-info">
        <div class="panel-heading">
            <h2 class="panel-title">CUP信息:</h2>
        </div>
        <div class="panel-body">
            
        </div>
</div>


<!--第三方包列表的容器-->
    <div id="get_cupinfo">
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