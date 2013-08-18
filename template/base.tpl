<!DOCTYPE html>
<html lang="en">
<head>
{% include 'head.tpl' %}
{% block css %}
{% endblock %}
</head>
<body>
<!-- Navbar -->
<div id="wrap">
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
					<li class="dropdown">
						<a class="dropdown-toggle" data-toggle="dropdown" href="#notice"><i class="icon-comment icon-white"></i>
						<b class="caret"></b>
						</a>
						<ul class="dropdown-menu">
						{% include 'notice.tpl' %}
						</ul>
					</li>
					<li><a href="/myspace/myinfo">{{request.user.alias}}&nbsp;<i class="icon-user icon-white"></i></a></li>
					<li><a href="/logout">注销</a></li>
					{% else %}
					<li><a href="/register">注册</a></li>
					<li><a data-toggle="modal" href="#login">登陆</a></li>
					{% endif %}
					<li class="divider-vertical"></li>
					<li><a href="/help">帮助</a></li>
				</ul>
			</div>
		</div> <!--container -->
	</div>
</div>

<div class="modal hide fade" id="login">
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
				{% csrf_token %}
				<dl>
				<dt>帐号</dt>
				<dd><input type="text" name="account"></dd>
				<dt>密码</dt>
				<dd><input type="password" name="password"></dd>
				<div align="center">
				<br><input type="submit" value="登陆" class="btn btn-info">
				</div>
				</dl>
			</form>
			{% endif %}
		</div>
    </div>

</div><!-- login -->

<div class="container" >
{% block content %}
{% endblock%}
</div>

</div> <!-- wrap -->
{% include 'foo.tpl' %}
{% block js %}
{% endblock %}
<script type="text/javascript">
	$(".dropdown-toggle").dropdown();
</script>
</body>
</html>
