```<!DOCTYPE HTML5>
{% load static %}

<html>
    <head>
        <title>Game</title>
        <link href="{% static "mainapp/tailwind-output.css"%}" rel="stylesheet" type="text/css">
        <link rel="shortcut icon" href="{% static 'images/favicon.ico' %}" >
    </head>

    <body class="h-24 bg-gradient-to-b from-teal-300 to-blue-700">

        <form id="post-req" class="absolute opacity-0" action="/result" method="POST">
            {% csrf_token %}
            {{ form }}
            <input type="submit" value="Submit">
        </form>

        <div id="name-getter-layout" class="absolute bg-black bg-opacity-75 w-screen h-screen">
            <div class="grid grid-rows-2 gap-1 rounded-md bg-gray-300 text-black w-3/12 m-auto mt-40 animate-fall">
                <h4 class="relative text-sm md:text-lg lg:text-2xl xl:text-3xl subfont-cumono font-bold ml-2">Enter your Name:</h4>

                <input id="name-getter" type="text" maxlength="10" placeholder="Enter Name" class="border-blue-800 border-2 float-left focus:outline-none text-black text-md lg:text-lg xl:text-xl text-center subfont-cumono rounded-md w-40 md:w-48 mr-3 lg:ml-8 xl:ml-16">

                <button id="name-getter-button" onclick="clickhandle()" class="rounded-lg shadow-md text-md md:text-lg mx-8 md:mx-12 lg:mx-16 xl:mx-20 border-blue-600 hover:border-white hover:bg-blue-600 hover:text-white active:bg-blue-800 border-2 focus:outline-none subfont-cumono">Enter</button>
            </div>
        </div>

        <div id="Grid" class="grid float-left grid grid-rows-3 grid-cols-3 gap-2 w-1/2 ml-20 mt-2 border-transparent blue-700 border-8 shadow-2xl">
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
            <div class="grid grid-rows-3 grid-cols-3 gap-1 h-16 sm:h-24 md:h-32 lg:h-44 xl:h-48">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
                <input class="sm:text-md md:text-lg lg:text-2xl xl:text-3xl text-center subfont-cumono focus:bg-blue-200 focus:outline-none" maxlength="1" type="text">
            </div>
        </div>
        <div class="float-right bg-gray-300 rounded-xl shadow-2xl border-4 w-48 md:w-56 lg:w-64 xl:w-rem20 lg:h-64 h-48 md:h-56 lg:h-rem20 xl:h-rem21 mr-10 lg:mr-16 xl:mr-32 mt-10 lg:mt-16 xl:mt-32">
            <div class="rounded-lg shadow-md m-4 bg-gray-100 border-2 h-24 sm:h-32 md:h-36 lg:h-48 xl:h-56">
                <h5 id="Name-headline" class="rounded-lg shadow-md text-sm md:text-md lg:text-xl xl:text-2xl text-center subfont-cumono font-bold">NAME</h5>
                <h5 id="Timer" class="text-sm md:text-md lg:text-xl xl:text-2xl text-center mt-5 subfont-cumono">Time Elapsed: <br> 0min 00s</h5>
                <button id="Sudoku-button" onclick="SubmitHandle()" class="rounded-lg shadow-md
                px-1 mx-10 md:mx-16 xl:mx-24 mt-2 lg:mt-4 text-sm lg:text-xl xl:text-2xl border-red-500 hover:border-white hover:bg-red-500 hover:text-white active:bg-red-700 border-2 focus:outline-none subfont-cumono">Submit</button>
            </div>

            <div class="grid grid-cols-2 gap-2">
                <!--/leaderboard/home is a redirect link that goes back to the home page-->
                <a href="/leaderboard/home" class="shadow-md rounded-lg md:mt-1 lg:mb-2 md:py-1 text-center text-xs lg:text-lg border-blue-600 hover:border-white hover:bg-blue-600 hover:text-white active:bg-blue-800 border-2 subfont-ubmono">Home</a>
                <a href="/leaderboard/lb" class="shadow-md rounded-lg md:mt-1 lg:mb-2 md:py-1 text-center text-xs lg:text-lg border-blue-600 hover:border-white hover:bg-blue-600 hover:text-white active:bg-blue-800 border-2 subfont-ubmono">LeaderBoard</a>

            </div>
            <div class="text-center">board id: {{board_id}}</div>
        </div>
        
    
    </body>
</html>

<script>

    var form = document.getElementById('post-req')
    console.log(form.children)

    //Timer Code
    var name_text_holder = document.getElementById('name-getter')
    var name_text_button = document.getElementById('name-getter-button')
    var name_getter_layout = document.getElementById('name-getter-layout')

    var sudoku_submit_button = document.getElementById("Sudoku-button")
    var name
    var seconds = 0

    function update_timer(){
        seconds += 1
        if (window.second1 == 5 && window.second2 == 9){
            window.mins++
            window.second1 = 0
            window.second2 = 0
        } else if (window.second2 == 9) {
            window.second1++
            window.second2 = 0
        } else {
            window.second2++
        } 
        window.timer.innerText = "Time Elapsed:\n" + String(window.mins) + "min " + String(window.second1) + String(window.second2) + "s"
    }
  
    function timer_start(){
        window.timer = document.getElementById("Timer")
        window.mins = parseInt(timer.innerText[14])
        window.second1 = parseInt(timer.innerText[19])
        window.second2 = parseInt(timer.innerText[20])
        window.timer_interval = setInterval(update_timer, 1000)
    }

    function replace_name(name){
        document.getElementById("Name-headline").innerText = name
    }

    // Main Function 1 -> makes the board and starts timer.
    function clickhandle(){
        fillboard(board_values, board_template)
        name = name_text_holder.value
        name_getter_layout.remove()
        replace_name(name)
        timer_start()
    }

    // Main Function 2 -> Handles user submission.
    function SubmitHandle(){
        if (check_board_result(board_template)){
            clearInterval(window.timer_interval)
            post_req(name, seconds)
        }
        
    }

    //Code to fill the Sudoku Board
    var board_values = {{game_board}}
    var board_template = document.getElementById("Grid").children

    function fillgrid(grid_count, board_values, grid){
        element_index = -1
        for (let row_count=0; row_count<3; row_count++){
            for (let element_count=0; element_count<3; element_count++){
                element_index++
                element = board_values[Math.floor(grid_count/3)*3+row_count][grid_count%3*3+element_count]

                if (element == 0){ continue }
                else {
                    grid[element_index].value = String(element)
                    grid[element_index].setAttribute("disabled", null)
                }
            }
        }
    }

    function fillboard(board_values, board_template){
        for (let i=0; i < board_template.length; i++){
            fillgrid(i,board_values, board_template[i].children)
        }
    }

    //Solution checking and post request Code
    

    function post_req(name, time){
        var form = document.getElementById('post-req')
        form.children[2].value = name
        form.children[4].value = time
        form.submit()
    }

    function convert_board(board_template){
        rows = []
        for (let row_value = 0; row_value<9; row_value++){
            row = []
            for (let box_value = 0; box_value<3; box_value++){
                for(let element_value = 0; element_value<3; element_value++){
                    box = board_template[Math.floor(row_value/3)*3+box_value].children
                    element = box[row_value%3*3+element_value].value
                    row.push(parseInt(element))
                }
            }
            rows.push(row)
        }
        return rows
    }

    function compare_and_modify_board(board, correct_values){
        for (let row = 0; row<9; row++){
            for(let element = 0; element<9; element++){
                var value_to_check = board[row][element]

                if(value_to_check != correct_values[row][element]){
                   alert("Your solution is wrong!")
                   return false
                }

            }
        
        alert("Your answer is correct! Check the leaderboard to see if you are there.")
        return true
    }
}

    result_board = {{check_board}}
    console.log(result_board)
    function check_board_result(board_template){
        var board_rows = convert_board(board_template)
        return compare_and_modify_board(board_rows, result_board)
    }

</script>```