const header = document.querySelector('#header');
function scrollFunc() {
    if (pageYOffset >= 90) {
        header.classList.add('on');
    } else {
        header.classList.remove('on');
    }
}
window.addEventListener('scroll', scrollFunc);