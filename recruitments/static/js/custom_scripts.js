$(document).ready(function(){

	//enabling redirects through the href attribute
	$('button').click(function(){
		window.location=$(this).attr('href');
	});

	
	$('input[type="checkbox"]').addClass('checkbox-inline');
});