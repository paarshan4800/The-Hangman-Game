var setWord = prompt("Enter the word you want your friend to guess");
var dashWord = prompt("Enter the word with blanks");
var lives = prompt("Enter the number of lives you wanna give to your friend");
var arr = [], tofill = 0;

    for(var i = 0;i<setWord.length;i++) {
        arr.push(dashWord.charAt(i));

        if(dashWord.charAt(i) == "_") {
            tofill++;
        }
    }

    Display();        
    
    function Display() {
        document.getElementById("wordwithblanks").innerHTML = arr;
        document.getElementById("numoflives").innerHTML = lives; 
        document.getElementById("numofblanks").innerHTML = tofill;
    }

    function Guess() {
        var flag = 0;
        if(lives > 0 && tofill > 0) {
            var guess = prompt("Guess a letter");
                    
            for(var i = 0;i<setWord.length;i++) {
                if(guess == setWord.charAt(i)) {
                    if(arr[i] == "_") {
                        arr[i] = guess;
                        tofill--;
                        flag = 1;
                        alert("Yay ! Correct Guess !");
                    }
                }
            }

            if(flag == 0) {
                alert("Ooops! Wrong guess !");
                lives--;
            }

            Display();
        }

        else {
            if(lives > 0) {
                alert("You guessed the word correctly");
            }
            else {
                alert("You guessed the word wrongly");
            }                        
        } 
    }  