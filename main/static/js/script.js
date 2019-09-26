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

	$('button[type="submit"]').click(function() {
		let query = $('input[name="query"]').val()
		let frame1 = '<div class="col-sm-6 mt-3 px-2" style="height: 400px;"><iframe class="mt-3" src="https://www.youtube.com/embed/'
		let frame2 = ' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
		let title1 = '<div id="title-container" class="mt-2 d-flex justify-content-center"><h4>'
		let title2 = '</h4></div></div>'
		$.get('json?query=' + query, function(data) {
			obj = JSON.parse(data)
			$('#vids-container').empty()
			$(obj).each(function() {
				let vid_id = this.id.videoId
				let vid_title = this.snippet.title
				$('#vids-container').append(frame1 + vid_id + '"'+ frame2 + title1 + vid_title + title2)
			})
		} )
	})
})