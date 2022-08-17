const $gform = $("#guessform");
const $guess = $("#guess");
const $alert = $("#alert");
const $guessed = $("#guessed");
const scoreboard = document.getElementById("score");
const timer = document.getElementById("time");
const guessed = new Set();
let time = 60;
let currscore = 0;
const countdown = setInterval(async function () {
    time--;
    timer.innerText = time;
    if (time === 0) {
        clearInterval(countdown)
        $alert.removeClass("alert-success alert-danger");
        $alert.addClass("alert-primary")
        $alert.text("Game over!")
        const res = await axios({
            url: "/score",
            method: "POST",
            data: { "score": currscore }
        });
        $alert.text(res.data.newhighscore ? "New High Score!" : "Better Luck Next Time")
        console.log(res.data);
    }
}, 1000)

$gform.on("submit", async function (e) {
    e.preventDefault();
    if (time > 0) {
        if (!guessed.has($guess[0].value)) {
            const res = await axios({
                url: "/guess",
                method: "GET",
                params: { "guess": $guess[0].value }
            });
            if (res.data.result === "ok") {
                $alert.text("Nice!")
                if (!$alert.hasClass("alert-success")) $alert.toggleClass("alert-success")
                if ($alert.hasClass("alert-danger")) $alert.toggleClass("alert-danger")
                guessed.add($guess[0].value)
                $guessed.prepend(`<li>${$guess[0].value}</li>`)
                currscore += $guess[0].value.length
                scoreboard.innerText = currscore
            }
            else {
                if (res.data.result === "not-on-board") {
                    $alert.text("That's not on the board!")
                }
                else {
                    $alert.text("Not a real word!")
                }
                if ($alert.hasClass("alert-success")) $alert.toggleClass("alert-success")
                if (!$alert.hasClass("alert-danger")) $alert.toggleClass("alert-danger")
            }
            $guess[0].value = ""
        }
    }
})