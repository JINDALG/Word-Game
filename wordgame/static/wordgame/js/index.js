$('.toggle').on('click', function() {
  $('.container').stop().addClass('active');
});

$('.close').on('click', function() {
  $('.container').stop().removeClass('active');
});

error = $('.error').text();
if (error) {
	$('.container').stop().addClass('active');
}

$('#start_game').on('click',function(event) {
	event.preventDefault();
	load_questions();
})

function load_questions() {
	console.log('data is loading');
	$.ajax({
		url : 'load_q/',
		type : 'DELETE',

		success : function(json) {
			console.log('hello')
			$('#start_game').remove()
			console.log(json);
			console.log('success')
		},

		error : function(xhr,errmsg,err) {
			$('#error_q').val('question not load')
			console.log(xhr.status + ' : ' + xhr.responseText);
		}
	})
}
