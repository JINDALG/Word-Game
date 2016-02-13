$(document).ready(function(){

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
$('#submit').hide()
$('#question').hide()
$('#answer').hide()
var q_text
var img_url
var count
var interval,time
function load_questions() {
	$.ajax({
		url : 'load_q/',
		type : 'POST',
		success : function(q_data) {
			$('#question').show()
			$('#answer').hide()
			$('#start').remove()
			console.log(q_data);
			q_text = q_data.question
			img_url = q_data.img
			count = q_data.count
			$("#question img").attr("src",q_data.img);
			$("#q_text").text(q_data.question);
			$('#question #score').text(q_data.score)
			$('#option1').val(q_data.option1)
			$('label[for="option1"]').text(q_data.option1)
			$('#option2').val(q_data.option2)
			$('label[for="option2"]').text(q_data.option2)
			$('#option3').val(q_data.option3)
			$('label[for="option3"]').text(q_data.option3)
			$('#option4').val(q_data.option4)
			$('label[for="option4"]').text(q_data.option4)
			console.log('success')
			$("#answer img").attr("src",'');
			$("#answer #score").text('');
			$("#complement").text('');
			$("#full_answer").text('');
			$("#main_word").text('');
			$("#sentence").text('');
			$('input[type="radio"]').prop('checked', false);
			remain_time = 30
			$('#time').text(remain_time)
			time = setTimeout(function(){ 
				if ($('#check').is(":visible")) {
					$('#check').click()
				}
					 }, 30000);

			interval =  setInterval(function(){
				remain_time -= 1
				$('#time').text(remain_time)
			},1000);
			
		},

		error : function(xhr,errmsg,err) {
			$('#error_q').val('question not load')
			console.log(xhr.status + ' : ' + xhr.responseText);
		}
	})
}
$('#check').on('click',function(event) {
	event.preventDefault();
	u_answer = null
	if($("input:radio[name='answers']").is(":checked")) {
		u_answer = $('input:radio[name=answers]:checked').val()
	}
	else {
		u_answer = 'None'
	}
	check_answer(u_answer);
})

function check_answer(u_answer) {
	clearTimeout(time)
	clearInterval(interval)
	console.log('data is loading');
	$.ajax({
		url : 'check_ans/',
		type : 'POST',
		data : {q_text : q_text, img : img_url, u_answer : u_answer },

		success : function(check_response) {
			console.log('hello');
			$('#question').hide()
			$('#answer').show()
			console.log(check_response.u_answer);
			$("#answer img").attr("src",check_response.img);
			$("#answer #score").text(check_response.score);
			$("#complement").text(check_response.complement);
			$("#full_answer").text(check_response.answer);
			$("#main_word").text(check_response.main_word);
			$("#sentence").text(check_response.sentence);
			console.log('success')
		},

		error : function(xhr,errmsg,err) {
			$('#error_q').val('question not load')
			console.log(xhr.status + ' : ' + xhr.responseText);
		}
	})
}



$('#next').on('click',function(event) {
	if (count < 3 ) {
		event.preventDefault();
		load_questions();
	}
	else {
		$('#answer').remove()
		$('#submit').show()
	}
})
});