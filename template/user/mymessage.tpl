<h2 style="text-align:center">{{title}}</h2>
<div class="hero-unit">
	<div class="well" style="background-color:rgb(254,238,205)">
    	<dl>
		<h4>给别人留下的足迹</h4>
		{% for mymessage in mymessages %}	
			{% if mymessage %}
				<dt>对 {{mymessage.to.alias}}</dt>
	        	<br>
	       	 	<dt>时间：{{mymessage.date}}</dt>
	        	<dd>内容：{{mymessage.text}}</dd>
			{% endif %}
		{% endfor %}
       	</dl>
		<br>
		<dl>
		<h4>我的留言版</h4>
		{% for tomessage in tomessages %}
			<dt>{{tomessage.owner.alias}} 回复我：</dt>
			<br>
			<dt>时间：{{tomessage.date}}</dt>
			<dd>内容: {{tomessage.date}}</dd>
		{% endfor %}
		</dl>
		</div>
</div>
