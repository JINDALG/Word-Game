$(window).load(function(){

	sessionStorage.clickcount = 555;

	var pathname = location.pathname;
	console.log(pathname)
	$('#question').hide()
	$('#answer').hide()
	$('#submit').hide()
	$('#start_game').on('click',function(event) {
		$('#submit').show()
		event.preventDefault();
		load_questions();

	})
	var count
	var interval,time
	function load_questions() {
		$.ajax({
			url : '/game/load_q',
			type : 'POST',
			success : function(q_data) {
				$('#question').show()
				$('#answer').hide()
				$('#start').remove()
				console.log(q_data);
				$("#question img").attr("src",q_data.img);
				$("#question #word").text(q_data.word);
				$('#option1').val(q_data.option1)
				$('label[for="option1"]').text(q_data.option1)
				$('#option2').val(q_data.option2)
				$('label[for="option2"]').text(q_data.option2)
				$('#option3').val(q_data.option3)
				$('label[for="option3"]').text(q_data.option3)
				$('#option4').val(q_data.option4)
				$('label[for="option4"]').text(q_data.option4)
				$("#meaning").text('');
				$("#sentence").text('');
				$("#phrase").text('');
				$('input[type="radio"]').prop('checked', false);
				remain_time = 30
				$('#time').text(remain_time)
				time = setTimeout(function(){ 
					if ($('#check').is(":visible")) {
						check_answer('None')
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
		u_answer = null
		if($("input:radio[name='answers']").is(":checked")) {
			event.preventDefault();
			u_answer = $('input:radio[name=answers]:checked').val()
			check_answer(u_answer);
		}
	})
var slot
	function check_answer(u_answer) {
		clearTimeout(time)
		clearInterval(interval)
		$.ajax({
			url : '/game/check_ans',
			type : 'POST',
			data : {u_answer : u_answer },
			success : function(check_response) {

				console.log(check_response);

				count = check_response.count
				$('#question').hide()
				$('#answer').show()
				$("#answer img").attr("src",check_response.img);
				$("#complement").text(check_response.complement);
				$("#answer #phrase").text(check_response.phrase);
				$("#meaning").text(check_response.meaning);
				$("#answer #word").text(check_response.word);
				$("#sentence").text(check_response.sentence);
				slot = check_response.slot_size
				count = check_response.count
				console.log(slot)
				console.log('success')

			},

			error : function(xhr,errmsg,err) {
				$('#error_q').val('question not load')
				console.log(xhr.status + ' : ' + xhr.responseText);
			}
		})
	}
	$('#next').on('click',function(event) {
		if (count < slot ) {
			event.preventDefault();
			load_questions();
		}
	})
});