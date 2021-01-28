```<!DOCTYPE HTML5>
{% load static %}

<html>
    <head>
        <title>
            Leaderboard
        </title>
        <link href="{% static 'mainapp/tailwind-output.css' %}" rel="stylesheet" type="text/css">
        <link rel="shortcut icon" href="{% static 'images/favicon.ico' %}" />
    </head>
    <body class="bg-gradient-to-b from-teal-300 to-blue-700">
        <div class="lg:mt-16 sm:mt-40 lg:mb-16 sm:mb-32">
            <h1 class="mainfont text-6xl text-center text-white bold select-none">LEADERBOARD</h1>
        </div>
        <div class="lg:flex sm:grid sm:colspan-1 lg:justify-center">
            <div class="bg-gray-200 rounded-xl shadow-lg sm:flex-col sm:justify-center lg:ml-40 sm:ml-48 mb-20 mt-10 lg:w-3/12 sm:w-3/5 lg:pb-2 sm:pb-8 subfont-ubmono">
                <h1 class="pl-8 lg:pr-32 sm:pr-8 lg:py-4 sm:py-8 text-gray-700 text-4xl lg:text-left sm:text-center">Top Scorers of ALL TIME!</h1>
                <div class="flex flex-col lg:pl-0 sm:pl-6">
                    <a href="home" class="lg:ml-8 lg:mr-8 sm:ml-48 w-20 py-1 w-40 text-center text-gray-700 text-2xl bg-opacity-0 border-4 border-green-500 rounded-full select-none hover:text-white hover:bg-green-500 hover:bg-opacity-100 shadow-lg active:bg-opacity-100 active:bg-green-600 transition duration-150 ease-in-out">Go Back</a>
                </div>
            </div>
            <div class="bg-white lg:mr-40 sm:mr-0 rounded-xl shadow-lg text-center grid grid-cols-3 justify-self-end lg:w-5/12 sm:w-4/5 lg:-ml-20 sm:ml-0 mb-10 sm:mr-24 lg:mt-0 sm:-mt-24" id="below">
                <div class="mx-8 mt-8 text-center flex-col col-span-3 border-gray-400" id="row">
                    <span class="hidden" id="data-get">{{ data }}</span>
                </div>
                <script>
                    var datalist = document.querySelector('#data-get')
                    var dataString = datalist.textContent
                    var data = eval(`[${dataString}]`);

                    var i = 0
                    while(i < 10) {
                        var entryDiv = document.createElement('div');
                        var index = document.createElement('h3');
                        var nameInput = document.createElement('h3');
                        var timeDisplay = document.createElement('h3');
                        var indexText = document.createTextNode(String(i+1) + '.');
                        var nameInputText = document.createTextNode(data[0][i][0]);
                        var time = data[0][i][1];
                        var hours = String(Math.floor(time / 60));

                        if(time % 60 < 10) {
                            seconds = '0' + String(time % 60)
                        }
                        else {
                            seconds = String(time % 60)
                        }

                        var timeDisplayText = document.createTextNode(hours + ':' + seconds);
                        
                        index.appendChild(indexText);
                        nameInput.appendChild(nameInputText);
                        timeDisplay.appendChild(timeDisplayText);

                        index.classList = ('flex-2 text-3xl lg:py-2 sm:py-6 mx-5 subfont-nomono');
                        nameInput.classList = ('flex-1 text-3xl lg:py-2 sm:py-6 mx-5');
                        timeDisplay.classList = ('flex-2 text-3xl lg:py-2 sm:py-6 mx-5 subfont-nomono');

                        entryDiv.appendChild(index);
                        entryDiv.appendChild(nameInput);
                        entryDiv.appendChild(timeDisplay);

                        entryDiv.classList = ('text-center flex col-span-3 border-b-2 border-gray-400 shadow-lg');

                        if(i % 2) {
                            entryDiv.classList.add('bg-gray-300')
                        }

                        if(i == 0) {
                            entryDiv.classList.add('rounded-t-lg')
                        }
                        else if(i == 9) {
                            entryDiv.classList.remove('border-b-2')
                            entryDiv.classList.add('rounded-b-lg')
                            entryDiv.classList.add('mb-8')
                        }
                        
                        var containedIn = document.getElementById("data-get").parentNode
                        var grab = document.getElementById("data-get")

                        containedIn.insertBefore(entryDiv, grab);
                        i++
                    }
                </script>
            </div>
        </div>
    </body>
</html>
```