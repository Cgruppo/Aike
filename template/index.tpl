{% extends 'base.tpl' %}
{% block content %}
<h2 align="center">艺术细胞拙计</h2>
<div class="row">
<div align="center" id="myCarousel" class="carousel span8 offset2">
    <!-- Carousel items -->
    <div class="carousel-inner">

    <div class="active item">
    	<img src="/static/images/blbq.jpg">
    	<div class="carousel-caption">
    		<h4>不离不弃</h4>
    		<p>额，要说些什么呢</p>
    	</div>
    </div>
    <div class="item">
    	<img src="/static/images/lol.jpg">
    	<div class="carousel-caption">
    		<h4>LOL</h4>
    		<p>额，要说些什么呢-------------</p>
    	</div>
    </div>
    <div class="item">
    	<img src="/static/images/renren.jpg">
    	<div class="carousel-caption">
    		<h4>人人</h4>
    		<p>额，~~~~~TTTTTTTTT</p>
    	</div>
    </div>

    </div>

    <!-- Carousel nav -->
    <a class="carousel-control left" href="#myCarousel" data-slide="prev">&lsaquo;</a>
    <a class="carousel-control right" href="#myCarousel" data-slide="next">&rsaquo;</a>
</div>
</div>

<div class="span3 well">
	<div class="hero-unit">
	</div>
</div>
<div class="span8">
	<div class="hero-unit">
	<p>已有 <strong>{{usercount}}</strong> 个用户</p>
	<p>一共开展了 <strong>{{activitycount}}</strong> 个活动</p>
	</div>
</div>
{% endblock%}

{% block js %}
<script type="text/javascript">
	$('.carousel').carousel({
    interval: 5000
    })
</script>
{% endblock %}
