// const BASE_URL = "localhost:5000"
const $gform = $("#guessform")
const $guess = $("#guess")
const $last = $("#lastguess")

$gform.on("submit", async function (e) {
    e.preventDefault();
    const res = await axios({
        url: "/guess",
        method: "GET",
        params: { "guess": $guess[0].value }
    });
    if (res.data.result === "ok") {
        $last.text("Nice!")
        if (!$last.hasClass("alert-success")) {
            $last.toggleClass("alert-success")
        }
        if ($last.hasClass("alert-danger")) {
            $last.toggleClass("alert-danger")
        }
    }
    else {
        if (res.data.result === "not-on-board") {
            $last.text("That's not on the board!")
        }
        else {
            $last.text("Not a real word!")
        }
            if ($last.hasClass("alert-success")) {
                $last.toggleClass("alert-success")
            }
            if (!$last.hasClass("alert-danger")) {
                $last.toggleClass("alert-danger")
            }
    }


})