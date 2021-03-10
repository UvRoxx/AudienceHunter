
        const play = document.querySelector('button');

        const svgContainer = document.getElementById('svg');
        const animItem = bodymovin.loadAnimation({
            wrapper: svgContainer,
            animType: 'svg',
            loop: false,
            autoplay: false,
            path: 'https://assets2.lottiefiles.com/packages/lf20_u4yrau.json'
        });

        play.addEventListener('click', () => {
            svgContainer.classList.remove('hide');
            animItem.goToAndPlay(0,true);
        })

        animItem.addEventListener('complete', () => {
            svgContainer.classList.add('hide');
            
        })
        function myFunction() {
  var x = document.getElementById("container");
  var y = document.getElementById("loading");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  } else {
        x.style.display = "none";
        y.style.display = "block";

  }
}