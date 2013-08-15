<h2 style="text-align:center">{{title}}</h2>
<div class="hero-unit">
	{% for comment in comments %}	
		{% if comment %}
		<div class="well" style="background-color:rgb(254,238,205)">
	       	<dl>
				<dt>活动：{{comment.activity.name}}</dt>
	        	<br>
	       	 	<dt>时间：{{comment.date}}</dt>
	        	<dt>内容：</dt>
	        	<dd>{{comment.text}}</dd>
        	</dl>
		</div>
		{% endif %}
	{% endfor %}
</div>
