const server_indicator_color = "6px solid #0000ff"; //blue
const server_indicator_location = "border-left";

$(document).ready(function() {
  player_serve = 1; //player who is serving, first player serves in beginning by default
  tiebreak_point = 0; //increases after each tie break point, resets to 0 after tiebreak is over
  $("#player1_name_id").css(server_indicator_location,server_indicator_color);
  player1 = parseInt($("#player1_sets_id").html());
  player2 = parseInt($("#player2_sets_id").html());
  tb_points = parseInt($("#tiebreaker_pts").html());
  num_sets = parseInt($("#num_sets").html());
  player1_name_id = String($("#player1_name_id").html());
  player2_name_id = String($("#player2_name_id").html());


  $("#player1_win_id").click(function() {
    point_won(1);//increase the score counter of the tennis match for player 1
  });
  $("#player2_win_id").click(function() {
    point_won(2);//increase the score counter of the tennis match for player2
  });
  /*
    The two methods below allow the user to choose which player serves using two buttons.
    These buttons allow the user to keep track of who is serving
    with the help of blue colored server indicator. */
  $("#player1_serve_id").click(function(){
    set_serve(1);
  });
  $("#player2_serve_id").click(function() {
    set_serve(2);
  });


});


function point_won(winner)
{
  if(player1 > num_sets/2)
  {
    alert(player1_name + " has already won. Please stop pressing the button");
  }
  else if(player2 > num_sets/2)
  {
    alert(player2_name + " has already won. Please stop pressing the button");
  }
  else
  {
    //send point increase to server via ajax call
    $.post("/receiveinfo", {"point_winner": winner, "player_serve": player_serve});
    var num_columns = $("#player1_row_id > td").length;
    var player1_game_id = "#player1" + "_game" + (num_columns - 4) + "_id";
    var player2_game_id = "#player2" +"_game" + (num_columns - 4) + "_id";
    var player1_game_score = parseInt($(player1_game_id).html());
    var player2_game_score = parseInt($(player2_game_id).html());
    if(player1_game_score === 6 && player2_game_score === 6)
    {
      update_tiebreak_score(winner=winner);
    }
    else {
      update_score(winner=winner)
    }
  }
}
function change_server()
{
  player_serve_id = "#player" + player_serve + "_name_id";
  $(player_serve_id).css('border-left', 'transparent');
  player_serve = 3 - player_serve;
  player_serve_id = "#player" + player_serve + "_name_id";
  $(player_serve_id).css(server_indicator_location, server_indicator_color);
}

function set_serve(next_set_serve)
{
  player_serve = next_set_serve;
  player_serve_id = "#player" + player_serve + "_name_id";
  $(player_serve_id).css(server_indicator_location,server_indicator_color);
  $("#player" + (3-player_serve) + "_name_id").css('border-left','transparent');//remove server color indicator for receiver
}

//increase tiebreak score
function update_tiebreak_score(winner)
{
  if(tiebreak_point == 0)
  {
    next_set_serve = 3 - player_serve;
  }
  tiebreak_point += 1;
  if(tiebreak_point % 2 == 1)
  {
    change_server();
  }
  var player1_points = "#player" + winner + "_points";
  var player2_points = "#player" + (3 - winner) + "_points";
  var player1_game_score = parseInt($(player1_points).text());
  var player2_game_score = parseInt($(player2_points).text());

  player1_game_score += 1;
  $(player1_points).text(player1_game_score);
  /*
    check if user selected 9 point tiebreaker.

    In other words, check if the user has chosen a sudden death tiebreaker.
    if the tie breakpoint is 5, then that means the user has chosen sudden death
  */
  if(tb_points === 5)
  {
    if(player1_game_score === tb_points)//first player that gets to 5 points wins
    {
      tiebreak_point = 0;
      $(player1_points).text(0);
      $(player2_points).text(0);
      set_serve(next_set_serve);
      update_set_score(winner, player2_game_score);
    }
  }
  else if((player1_game_score >= tb_points) && (player1_game_score - player2_game_score >= 2))
  {
    tiebreak_point = 0;
    $(player1_points).text(0);
    $(player2_points).text(0);
    set_serve(next_set_serve);//set player who will serve first game of new set
    update_set_score(winner, player2_game_score);
  }
}

function update_score(winner)
{
  var player1_points = "#player" + winner + "_points";
  var player2_points = "#player" + (3 - winner) + "_points";

  var player1_game_score = $(player1_points).text();

  switch(player1_game_score)
  {
    case "0":
      $(player1_points).text(15); //player scores 1 point or 15
      break;
    case "15":
      $(player1_points).text(30); //player scores 2 points or 30
      break;
    case "30":
      $(player1_points).text(40); //player scores  3 points or 40
      break;
    case "40":
      var player2_game_score = $(player2_points).text();
      if(player2_game_score < 40)
      {
        $(player1_points).text(0);
        $(player2_points).text(0);
        change_server();
        update_set_score(winner);
      }
      else if(player2_game_score == 40)//this means both players are 40 - 40 or deuce
      {
        $(player1_points).text("AD"); //player has advantage point
      }
      else
      {
        $(player2_points).text(40);
      }
      break;
    case "AD"://indicates an advantage point for a player
      $(player1_points).text(0);
      $(player2_points).text(0);
      change_server();
      update_set_score(winner);
      break;

    default:
      alert("No match found");
  }
}
//updates game score
//there are 6 games at a minimum in a set in tennis
//updates number of sets player won
function update_set_score(winner,loss_tiebreak_score)
{
  var num_columns = $("#player1_row_id > td").length;
  var player1_game_id = "#player1"+ "_game" + (num_columns - 4) + "_id";
  var player2_game_id = "#player2" + "_game" + (num_columns - 4) + "_id";
  var player1_game_score = parseInt($(player1_game_id).html());
  var player2_game_score = parseInt($(player2_game_id).html());

  if(winner == 1)
  {
    player1_game_score += 1;
    $(player1_game_id).text(player1_game_score);
    if(loss_tiebreak_score >= 0)
    {
      $(player2_game_id).text(player2_game_score + " (" + loss_tiebreak_score + ")" );
    }
  }
    else
    {
      player2_game_score += 1;
      $(player2_game_id).text(player2_game_score);
      if(loss_tiebreak_score >= 0)
      {
        $(player1_game_id).text(player1_game_score + " (" + loss_tiebreak_score + ")" );
      }
    }

    if((player1_game_score == 6 && player2_game_score < 5) ||
        (player1_game_score == 7) || (player2_game_score == 6 && player1_game_score < 5) ||
         (player2_game_score == 7))
      {
        if(winner == 1)
        {
          player1 += 1;
          $("#player1_sets_id").html(player1);
        }
        else {
          player2 += 1;
          $("#player2_sets_id").html(player2);
        }

    //check if tennis match is over
    if(player1 > num_sets/2 || player2 > num_sets/2)
    {
      const message = (player1 > player2) ? player1_name_id + " won the tennis match.": player2_name_id + " won the tennis match.";
      alert("Tennis match is over! " + message);
      $("#player1_name_id").css('border-left', 'transparent');
      $("#player2_name_id").css('border-left', 'transparent');
      if(player1 > player2)//compare player1 and player2 total set scores
      {
        /*highlight player 1 row with blue coloring to denote the
         the winner of the tennis match
         */
        $("#player1_row_id").css('background','#3391ff');
      }
      else
      {
        $("#player2_row_id").css('background', '#3391ff');
      }
    }
    else
    {
      var prev_set_id = "#prev_sets" + (num_columns - 4) + "_id";
      num_columns = num_columns + 1;
      $(prev_set_id).after("<th id='prev_sets" + (num_columns - 4) + "_id'>Set " + ((num_columns-4))+" (Games)</th>");
      $(player1_game_id).after("<td id='player1_game" + (num_columns - 4) + "_id'>0</td>");
      $(player2_game_id).after("<td id='player2_game" + (num_columns - 4) + "_id'>0</td>");

    }

  }

}
