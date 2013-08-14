<h2 style="text-align:center">{{title}}</h2>
<div class="hero-unit">
	{% for activityRelation in activitys %}	
		{% if activityRelation %}
		<div class="well" style="background-color:rgb(254,238,205)">
	        	<dl>
	       	 	<dt><a href="/show/ac{{activityRelation.activity.id}}">{{activityRelation.activity.name}}</a></dt>
	        	<br>
	        	<dt>活动举办方：</dt>
	            	<dd>
	            	{% for organizerR in activityRelation.activity.organizerR_activity.all %}
	            	<a href="/u{{organizerR.user.id}}">{{organizerR.user.alias}}</a>&nbsp;
	            	{% endfor %}
	            	</dd>
	        	<dt>活动简介：</dt>
	            	<dd>{{activityRelation.activity.introduction}}</dd>
	        	</dl>
				<div class="btn-group">
					<a href="/show/ac{{activityRelation.activity.id}}/remove/"><button class="btn btn-danger">退出</button></a>
				</div>
		</div>
		{% endif %}
	{% endfor %}
</div>
