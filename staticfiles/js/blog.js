function myFunction(x) {
  var dots = document.getElementsByClassName("dots");
  var moreText = document.getElementsByClassName("more");
  var btnText = document.getElementsByClassName("myBtn");

  if (dots[x].style.display === "none") {
    dots[x].style.display = "inline";
    btnText[x].style.display = "none";
    moreText[x].style.display = "none";
  } else {
    dots[x].style.display = "none";
    btnText[x].style.display = "inline";
    moreText[x].style.display = "inline";
  }
}