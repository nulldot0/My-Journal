$(document).ready(function(){
	$('#main-text').slideDown('slow');
	$('#login-form').slideDown('slow');
	$('#write-form').slideDown('slow');
	$('#read').slideDown('slow');
	$('#content').slideDown(1300);


	$('#fullscreen-btn').click(function(){
		$('#date-list').toggle()
		$('#reading').css('display', 'none');
		$('#reading').toggleClass('col-lg-12');
		$('#reading').fadeIn('slow')
	})
})