for (i of document.getElementsByClassName("lista2")) {
    console.log(
        i.getElementsByClassName("lista")[1].getElementsByTagName("a")[0].getAttribute("onmouseover").match("(http.*?jpg)")[0],
        "https://rarbgprx.org" + i.getElementsByClassName("lista")[1].getElementsByTagName("a")[0].getAttribute("href")
    )
}
