// const BASE_URL = "localhost:5000"
const $gform = $("#guessform")
const $last = $("#lastguess")

$gform.on("submit", async function(e){
    e.preventDefault();
    const formData = new FormData($gform[0])
    const res = await axios({
        url: "/guess",
        method: "POST",
        data: formData
    });
    $last.text(res.data.result)
})