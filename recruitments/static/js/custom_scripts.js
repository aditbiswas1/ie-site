//functions used to apply random font sizes over a given element
function typografy() {
            var minSize = 70;
            var maxSize = 250;
            $(".randomsize").each(function () {
                var retHTML = "";
                //get the text
                var allText = $(this).text().trim().split('`');

                //now add each word one by one
                for (i = 0; i < allText.length - 1; i++) {
                    var size = getRandomInt(minSize, maxSize);
                    size = Math.ceil(size / 10) * 10;
                    retHTML += "<span style='font-size:"+size+"%;'>" + allText[i] + "</span>";
                }
                $(this).text('');
                $(this).html(retHTML);
                
            });
			
			minSize = 120;
			maxSize=300;
			
			$(".randomsize-large").each(function () {
                var retHTML = "";
                //get the text
                var allText = $(this).text().trim().split('`');

                //now add each word one by one
                for (i = 0; i < allText.length - 1; i++) {
                    var size = getRandomInt(minSize, maxSize);
                    size = Math.ceil(size / 10) * 10;
                    retHTML += "<span style='font-size:"+size+"%;'>" + allText[i] + "</span>";
                }
                $(this).text('');
                $(this).html(retHTML);
                
            });
}

function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
}

$(document).ready(function(){

	//enabling redirects through the href attribute
	$('button').click(function(){
		window.location=$(this).attr('href');
	});
	
	//obvious
	$('input[type="checkbox"]').addClass('checkbox-inline');
	
	//popovers for SIG icons
	$('#code').popover({
		placement : 'right',
		animation : 'true',
		html : 'true',
		title : 'Code (Core)',
		content : '<i>Bringing you the best hackathons and all nighters.</i><p>Bringing everything related to coding, applications and other software-driven products under one roof.</p>'
	});
	
	$('#code').mouseenter(function(){
		$(this).popover('show');
	});
	
	$('#code').mouseleave(function(){
		$(this).popover('hide');
	});
	
	$('#gadget').popover({
		placement : 'top',
		animation : 'true',
		html : 'true',
		title : 'Gadget (Core)',
		content : "<i>Forever meddling with man's best friends.</i><p>Combining everything that an electronics or gadget freak could dream of, be it robotics, sensors or displays.</p>"
	});
	
	$('#gadget').mouseenter(function(){
		$(this).popover('show');
	});
	
	$('#gadget').mouseleave(function(){
		$(this).popover('hide');
	});
	
	$('#garage').popover({
		placement : 'left',
		animation : 'true',
		html : 'true',
		title : 'Garage (Core)',
		content : "<i>There's always a new mad machine to tame.</i><p>The pitstop, not only for automobile enthusiasts, but also those interested in all things related to mechanics, structures or materials.</p>"
	});
	
	$('#garage').mouseenter(function(){
		$(this).popover('show');
	});
	
	$('#garage').mouseleave(function(){
		$(this).popover('hide');
	});
	
	$('#finance').popover({
		placement : 'right',
		animation : 'true',
		html : 'true',
		title : 'Finance (Auxiliary)',
		content : '<i>Delving deep into the backbone of the modern world.</i><p>Discussions related to finance, economics, stock markets etc.</p>'
	});
	
	$('#finance').mouseenter(function(){
		$(this).popover('show');
	});
	
	$('#finance').mouseleave(function(){
		$(this).popover('hide');
	});
	
	$('#vriddhi').popover({
		placement : 'top',
		animation : 'true',
		html : 'true',
		title : 'Vriddhi (Auxiliary)',
		content : '<i>Service with a smile.</i><p>Our social initiative, which aims at small to large scale rural development programmes in collaboration with various NGOs.</p>'
	});
	
	$('#vriddhi').mouseenter(function(){
		$(this).popover('show');
	});
	
	$('#vriddhi').mouseleave(function(){
		$(this).popover('hide');
	});
	
	$('#studio').popover({
		placement : 'left',
		animation : 'true',
		html : 'true',
		title : 'Studio (Auxiliary)',
		content : "<i>For those with a need to cut out life's boring parts.</i><p>Holds regular sessions on film appreciation, discussing intricate, and often technical, details behind specific films. Movie screenings for the purpose of technical analysis are also a part of its agenda, although its primary aim is to keep making short films.</p>"
	});
	
	$('#studio').mouseenter(function(){
		$(this).popover('show');
	});
	
	$('#studio').mouseleave(function(){
		$(this).popover('hide');
	});
	
	//assigning event names random font sizes for decorative purposes
	typografy();
});