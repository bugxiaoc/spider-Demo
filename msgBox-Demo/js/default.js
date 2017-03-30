$.box = function(opts){ 
		$box = $(
		"<div class='message'>                                	                       "+
		"	<div class='title'>                                                        "+
		"		<h3>"+opts['title']+"</h3>                                             "+
		"		<a class='close' href='javascript:void(0)'>X</a>                       "+
		"	</div>                                                                     "+
		"	<div class='context' align='center'>                                       "+
		"		<div class='inText'>                                                   "+
		"			<p>用户名:<input class='username' type='text'/></p><br/>           "+
		"			<p>密码:&nbsp;<input class='password' type='password' /></p>             "+
		"		</div>                                                                 "+
		"		<input type='button' value='登陆' class='login' />                     "+
		"		<input type='button' value='关闭' class='close'/>                      "+
		"	</div>                                                                     "+
		"</div>");
		if(opts.three)
		{
			$("body").append($box).append($("<div class='three'></div>"));
		}
		$("body").append($box);
		centerBox($box);
		initEvent($box,opts);
		$(window).resize(function(){
			centerBox($box);
		});
	}
function initEvent($box,opts)
{
	$box.find(".title").mousedown(function(){
		var ev =  ev || window.event;
		$box= $(this.parentNode);
		var _l = ev.clientX - $box.offset().left;
		var _t = ev.clientY - $box.offset().top;
		var move = true;
		$box.find(".title").mousemove(function(ev){
			if(move)
			{
				var l = ev.clientX -_l;
				var t = ev.clientY -_t;
				
				$(this.parentNode).css({
					top:t,
					left:l
				});
			}
		});
		$("body").mouseup(function(){
			move = false;
		});
	});
	$(".close").click(function(){
		$box.fadeOut(500,function(){
			$box.remove();
			$(".three").remove();
		});
		if(opts.callback)
		{
			opts.callback(false);
		}
	});
	$(".login").click(function(){
		$box.fadeOut(500,function(){
			$box.remove();
			$(".three").remove();
		});
		if(opts.callback)
		{
			opts.callback(true);
		}
	});
}

function centerBox($box){
	var w = $box.width();
	var h = $box.height();
	var autow = $(window).width() -w;
	var autoh = $(window).height() -h;
	$box.css({top:autoh/2,left:autow/2});
}
