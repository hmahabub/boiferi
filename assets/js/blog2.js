function myFunction() {
  var dots = document.getElementsByClassName("dots");
  var moreText = document.getElementsByClassName("more");
  var btnText = document.getElementsByClassName("myBtn");

  if (dots[0].style.display === "none") {
    dots[0].style.display = "inline";
    btnText[0].innerHTML = "Read more";
    moreText[0].style.display = "none";
  } else {
    dots[0].style.display = "none";
    btnText[0].innerHTML = "Read less";
    moreText[0].style.display = "inline";
  }
}