<!DOCTYPE html>
<html lang="en">
{% include 'head.tpl' %}

<body>
<!-- Navbar -->
<div class="navbar navbar-fixed-top">
	<div class="navbar navbar-inner">
		<div class="container">
			<a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
			    <span class="icon-bar"></span>
			    <span class="icon-bar"></span>
			    <span class="icon-bar"></span>
			</a>
			<a class="brand" href="/">爱克</a>
			<div class="nav-collapse">
				<ul class="nav">
					<li class="{{nav1}}"><a href="/myspace">个人空间</a></li>
					<li class="{{nav2}}"><a href="/show">活动展示</a></li>	
					<li class="{{nav3}}"><a href="/friend">好友</a></li>
					<li class="{{nav4}}"><a href="/create">开展活动</a></li>
				</ul>
			</div>
			<div class="nav pull-right">
				<ul class="nav">
					{% if request.user.is_authenticated %}
					<li><a href="/myspace/myinfo"><i class="icon-user icon-white"></i>&nbsp;{{request.user.alias}}</a></li>
					<li><a href="/logout">注销</a></li>
					{% else %}
					<li><a href="/register">注册</a></li>
					<li><a href="/login">登陆</a></li>
					{% endif %}
					<li class="divider-vertical"></li>
					<li><a href="/help">帮助</a></li>
				</ul>
			</div>
		</div> <!--container -->
	</div>
</div>

<div class="container" >
<img src="/show/testqrcode">
<a class="btn" data-toggle="modal" href="#login" >点击触发对话框</a>

<div class="modal fade" id="login">
    <div class="modal-header">
    <a class="close" data-dismiss="modal">×</a>
    <h3>请登录</h3>
    </div>
    <div class="modal-body">
	    <div class="span4 well">
			{% if request.user.is_authenticated %}
			<h4>你已经登陆！无需重复登陆</h4>
			{% else %}
			<h4>请输入帐号和密码</h4>
			<form action="/login/" method="post">
				<dl>
				<dt>帐号</dt>
				<dd><input type="text" name="account"></dd>
				<dt>密码</dt>
				<dd><input type="password" name="password"><dd>
				<div align="center">
				<br><input type="submit" value="登陆" class="btn btn-info">
				</div>
				<dl>
			</form>
			{% endif %}
		</div>
    </div>
    
    </div>

</div><!-- login -->
<script type="text/javascript" src="/static/js/jquery.js"></script>
<script type="text/javascript" src="/static/js/bootstrap.js"></script>
</body>
</html>
